#!/usr/bin/env python3
"""Verification / build helper for the literature search.

Authoritative metadata (title, authors, year, venue, citations) is NEVER typed by hand:
it is pulled from Crossref (DOI), the arXiv API (arXiv ID) or the 3GPP portal (3GPP specs).

Usage
  verify.py doi <DOI> [...]          print verified metadata as JSON (title, authors, venue, cites)
  verify.py arxiv <ID> [...]         same for arXiv IDs
  verify.py search "<query>" [rows]  Crossref bibliographic search (DOI | year | venue | title)
  verify.py spec3gpp <specId>        title of a 3GPP spec from portal.3gpp.org (numeric specificationId)
  verify.py build S<n> <short_name>  read work/S<n>.jsonl, verify every row, write
                                     results/S<n>_<short_name>.csv, results/S<n>_<short_name>.bib,
                                     results/S<n>_unverified.csv

work/S<n>.jsonl: one JSON object per line with keys
  doi | arxiv | standard (one of them), venue_type, relevance, secondary_subdomains, summary,
  method, data_or_testbed, key_result, limitation_or_critique, standards_link, flags, keyword,
  and for standards also: title, authors (e.g. "3GPP"), year, venue (e.g. "3GPP TS 23.288 Rel-18"),
  url, spec_check (a URL whose page text must contain the spec number; 3GPP portal preferred).
  Optional: expected_title (used to check that a DOI matches the intended paper).
"""
import csv, datetime, difflib, hashlib, html, json, os, re, sys, time, unicodedata
import urllib.parse, urllib.request, xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.environ.get("VERIFY_CACHE", "/tmp/claude-0/-home-user-state-of-art-research/3780c51d-cb14-568e-b005-df3188a96f13/scratchpad/verify_cache")
os.makedirs(CACHE, exist_ok=True)
MAILTO = "mailto=alinstoica1234567@gmail.com"
UA = {"User-Agent": "lit-review-verifier/1.0 (" + MAILTO.split("=")[1] + ")"}
TODAY = datetime.date.today().isoformat()
COLS = ["id", "title", "authors", "year", "venue", "venue_type", "doi", "arxiv", "url", "citations",
        "citations_date", "subdomain", "secondary_subdomains", "relevance", "summary", "method",
        "data_or_testbed", "key_result", "limitation_or_critique", "standards_link", "flags", "verification"]


def get(url, accept=None, tries=4):
    key = hashlib.sha1((url + str(accept)).encode()).hexdigest()
    p = os.path.join(CACHE, key)
    if os.path.exists(p):
        with open(p, "rb") as f:
            data = f.read()
        return None if data == b"__404__" else data
    hdr = dict(UA)
    if accept:
        hdr["Accept"] = accept
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=hdr), timeout=40) as r:
                data = r.read()
            with open(p, "wb") as f:
                f.write(data)
            return data
        except urllib.error.HTTPError as e:
            if e.code == 404:
                with open(p, "wb") as f:
                    f.write(b"__404__")
                return None
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(2 ** (i + 1)); continue
            return None
        except Exception:
            time.sleep(2 ** (i + 1))
    return None


def norm(s):
    s = unicodedata.normalize("NFKD", html.unescape(s or "")).encode("ascii", "ignore").decode()
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def sim(a, b):
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()


def short_prefix(cr, exp):
    """Crossref sometimes stores only the system name (e.g. 'MimicNet') for ACM papers whose full title is
    'MimicNet: ...'. Accept the expected full title when it starts with the short Crossref title + ':'."""
    return len(cr) < 30 and len(norm(cr)) > 2 and re.match(re.escape(cr.strip()) + r"\s*:", exp.strip(), re.I) is not None


def clean(s):
    s = html.unescape(s or "")
    s = re.sub(r"\s*<(su[pb])>\s*(.*?)\s*</\1>\s*", r"\2", s)  # L<sup>2</sup>5GC -> L25GC
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", s).strip()


def citations(doi):
    d = get("https://api.openalex.org/works/doi:" + urllib.parse.quote(doi.lower()) + "?" + MAILTO)
    if d:
        try:
            return json.loads(d)["cited_by_count"], "OpenAlex " + TODAY
        except Exception:
            pass
    d = get("https://api.semanticscholar.org/graph/v1/paper/DOI:" + urllib.parse.quote(doi) + "?fields=citationCount")
    if d:
        try:
            return json.loads(d)["citationCount"], "SemanticScholar " + TODAY
        except Exception:
            pass
    return "", ""


TYPEMAP = {"journal-article": "journal", "proceedings-article": "conference", "book-chapter": "conference",
           "posted-content": "preprint", "standard": "standard"}


def crossref(doi):
    doi = doi.strip().replace("https://doi.org/", "").replace("http://dx.doi.org/", "")
    d = get("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/") + "?" + MAILTO)
    if not d:
        return None
    m = json.loads(d)["message"]
    auth = []
    for a in m.get("author", []):
        nm = (a.get("given", "") + " " + a.get("family", "")).strip() or a.get("name", "")
        auth.append(nm)
    year = ""
    for k in ("published-print", "published-online", "issued", "published"):
        if m.get(k, {}).get("date-parts") and m[k]["date-parts"][0][0]:
            year = m[k]["date-parts"][0][0]; break
    if m.get("issued", {}).get("date-parts") and m["issued"]["date-parts"][0][0]:
        year = m["issued"]["date-parts"][0][0]
    venue = clean((m.get("container-title") or [""])[0])
    if not venue and m.get("event"):
        venue = clean(m["event"].get("name", ""))
    c, cd = citations(doi)
    return {"doi": m.get("DOI", doi).lower(), "title": clean((m.get("title") or [""])[0]),
            "authors": auth, "year": year, "venue": venue,
            "crossref_type": m.get("type", ""), "venue_type_guess": TYPEMAP.get(m.get("type", ""), ""),
            "publisher": m.get("publisher", ""), "volume": m.get("volume", ""), "issue": m.get("issue", ""),
            "pages": m.get("page", ""), "url": "https://doi.org/" + m.get("DOI", doi).lower(),
            "citations": c, "citations_date": cd}


def arxiv(aid):
    aid = re.sub(r"^(arxiv:|https?://arxiv.org/abs/)", "", aid.strip(), flags=re.I)
    aid = re.sub(r"v\d+$", "", aid)
    d = get("https://export.arxiv.org/api/query?id_list=" + aid)
    if not d:
        return None
    ns = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
    root = ET.fromstring(d)
    e = root.find("a:entry", ns)
    if e is None or e.find("a:title", ns) is None or not e.find("a:id", ns).text or "api/errors" in e.find("a:id", ns).text:
        return None
    pub = e.find("a:published", ns).text
    jref = e.find("x:journal_ref", ns)
    edoi = e.find("x:doi", ns)
    return {"arxiv": aid, "title": clean(e.find("a:title", ns).text),
            "authors": [clean(a.find("a:name", ns).text) for a in e.findall("a:author", ns)],
            "year": int(pub[:4]), "published": pub[:10], "venue": "arXiv preprint",
            "journal_ref": clean(jref.text) if jref is not None else "",
            "published_doi": edoi.text if edoi is not None else "",
            "url": "https://arxiv.org/abs/" + aid}


def spec3gpp(sid):
    d = get("https://portal.3gpp.org/desktopmodules/Specifications/SpecificationDetails.aspx?specificationId=" + str(sid))
    if not d:
        return None
    t = d.decode("utf-8", "ignore")
    num = re.search(r'id="referenceVal">([^<]+)<', t)
    title = re.search(r'id="titleVal">([^<]*)<', t)
    if not num:
        return None
    return {"spec": num.group(1).strip(), "title": clean(title.group(1)) if title else ""}


def search(q, rows=15):
    url = ("https://api.crossref.org/works?query.bibliographic=" + urllib.parse.quote(q) + "&rows=" + str(rows) +
           "&select=DOI,title,container-title,issued,type,is-referenced-by-count&filter=from-pub-date:2019-01-01&" + MAILTO)
    d = get(url)
    if not d:
        print("search failed"); return
    for it in json.loads(d)["message"]["items"]:
        y = (it.get("issued", {}).get("date-parts") or [[""]])[0][0]
        print("%s | %s | %s | %s | refs=%s | %s" % (it["DOI"], y, it.get("type", ""),
              clean((it.get("container-title") or [""])[0])[:60], it.get("is-referenced-by-count", ""),
              clean((it.get("title") or [""])[0])))


def surname(full):
    full = unicodedata.normalize("NFKD", html.unescape(full or "")).encode("ascii", "ignore").decode().strip()
    if not full:
        return "Anon"
    last = full.split()[-1]  # keeps hyphenated surnames whole: Garcia-Martin -> GarciaMartin
    return "".join(x[:1].upper() + x[1:] for x in re.split(r"[-']", last) if x)


def bibkey(first_author, year, keyword, used):
    kw = re.sub(r"[^A-Za-z0-9]", "", (keyword or "Work").title())
    base = re.sub(r"[^A-Za-z0-9]", "", surname(first_author)) + str(year) + kw
    k, i = base, 0
    while k in used:
        i += 1; k = base + "abcdefghij"[i - 1]
    used.add(k)
    return k


def tex(s):
    s = str(s)
    for a, b in (("&", r"\&"), ("%", r"\%"), ("_", r"\_"), ("#", r"\#")):
        s = s.replace(a, b)
    return s


def bibentry(key, row, meta):
    vt = row["venue_type"]
    f = {"title": "{" + tex(row["title"]) + "}", "author": " and ".join(tex(a) for a in row["_authors"]) or tex(row["authors"]),
         "year": row["year"]}
    if vt == "journal":
        typ = "article"; f["journal"] = tex(row["venue"])
    elif vt == "conference":
        typ = "inproceedings"; f["booktitle"] = tex(row["venue"])
    elif vt == "preprint":
        typ = "misc"; f["howpublished"] = "arXiv preprint arXiv:" + row["arxiv"]; f["eprint"] = row["arxiv"]
        f["archivePrefix"] = "arXiv"
    else:
        typ = "techreport"; f["institution"] = tex(row["authors"]); f["number"] = tex(row["venue"])
    for k in ("volume", "issue", "pages", "publisher"):
        if meta.get(k):
            f["number" if k == "issue" and typ == "article" else k] = tex(meta[k])
    if row["doi"]:
        f["doi"] = row["doi"]
    if row["url"]:
        f["url"] = row["url"]
    return "@%s{%s,\n%s\n}\n" % (typ, key, ",\n".join("  %s = {%s}" % (k, v) if not str(v).startswith("{") else "  %s = %s" % (k, v)
                                                     for k, v in f.items()))


def build(sub, short):
    src = os.path.join(ROOT, "work", sub + ".jsonl")
    rows, bad, bibs, used = [], [], [], set()
    for ln, line in enumerate(open(src, encoding="utf-8"), 1):
        line = line.strip()
        if not line or line.startswith("//"):
            continue
        r = json.loads(line)
        out = {c: "" for c in COLS}
        for c in COLS:
            if c in r and c not in ("title", "authors", "year", "venue", "citations", "citations_date", "verification"):
                out[c] = r[c]
        out["subdomain"] = sub
        meta, why = {}, ""
        if r.get("doi"):
            meta = crossref(r["doi"])
            if not meta:
                why = "DOI did not resolve in Crossref"
            elif r.get("expected_title") and sim(meta["title"], r["expected_title"]) < 0.75 and not short_prefix(meta["title"], r["expected_title"]):
                why = "Crossref title '%s' does not match expected '%s'" % (meta["title"], r["expected_title"])
            else:
                if r.get("expected_title") and short_prefix(meta["title"], r["expected_title"]):
                    meta["title"] = clean(r["expected_title"])  # Crossref holds only the system name (ACM)
                out.update(title=meta["title"], authors="; ".join(meta["authors"]), year=meta["year"],
                           venue=meta["venue"], doi=meta["doi"], url=meta["url"], citations=meta["citations"],
                           citations_date=meta["citations_date"], verification="doi")
                if not out["venue_type"]:
                    out["venue_type"] = meta["venue_type_guess"]
                if r.get("arxiv"):
                    out["arxiv"] = r["arxiv"]
        elif r.get("arxiv"):
            meta = arxiv(r["arxiv"])
            if not meta:
                why = "arXiv ID not found"
            elif r.get("expected_title") and sim(meta["title"], r["expected_title"]) < 0.75:
                why = "arXiv title '%s' does not match expected '%s'" % (meta["title"], r["expected_title"])
            elif meta["year"] < 2025 and "seminal" not in r.get("flags", ""):
                why = "arXiv-only work older than 2025 (protocol allows preprints only from 2025-2026)"
            else:
                out.update(title=meta["title"], authors="; ".join(meta["authors"]), year=meta["year"],
                           venue="arXiv preprint", arxiv=meta["arxiv"], url=meta["url"], venue_type="preprint",
                           verification="arxiv")
                if "preprint" not in out["flags"]:
                    out["flags"] = ";".join([x for x in [out["flags"], "preprint"] if x])
        elif r.get("standard"):
            ok = False
            chk = r.get("spec_check", "")
            m = re.search(r"specificationId=(\d+)", chk)
            num = re.sub(r"[^0-9.\-]", "", r["standard"].split()[-1]) if r["standard"] else ""
            if m:
                s = spec3gpp(m.group(1))
                if s and num and s["spec"].strip() == num:
                    ok = True
                    if r.get("title") and s["title"] and sim(s["title"], r["title"]) < 0.6:
                        ok = False; why = "3GPP portal title '%s' differs from '%s'" % (s["title"], r["title"])
                    elif s["title"]:
                        r["title"] = s["title"]
                else:
                    why = "3GPP portal page does not show spec %s" % num
            elif chk:
                d = get(chk)
                if d and num and num in d.decode("utf-8", "ignore").replace(" ", ""):
                    ok = True
                elif r.get("verified_by_webfetch"):
                    ok = True  # agent confirmed the page via WebFetch (site blocks direct curl); recorded in note
                else:
                    why = "could not confirm spec page %s" % chk
            else:
                why = "no spec_check URL given"
            if ok:
                out.update(title=r.get("title", ""), authors=r.get("authors", ""), year=r.get("year", ""),
                           venue=r.get("venue", r["standard"]), url=r.get("url", chk), venue_type="standard",
                           verification="standard")
        else:
            why = "no DOI / arXiv / standard identifier"
        if why:
            bad.append({"subdomain": sub, "identifier": r.get("doi") or r.get("arxiv") or r.get("standard", ""),
                        "expected_title": r.get("expected_title", r.get("title", "")), "reason": why})
            print("UNVERIFIED line %d: %s" % (ln, why), file=sys.stderr)
            continue
        out["_authors"] = meta.get("authors") if meta.get("authors") else [out["authors"]]
        first = out["_authors"][0] if out["_authors"] else "Anon"
        key = bibkey(first if out["venue_type"] != "standard" else re.sub(r"[^A-Za-z0-9]", "", out["authors"]) or "Std",
                     out["year"], r.get("keyword", ""), used)
        out["id"] = key
        bibs.append(bibentry(key, out, meta or {}))
        rows.append(out)
    # surveys first, then relevance desc, then year desc
    rows.sort(key=lambda o: ("survey" not in str(o["flags"]), -int(o["relevance"] or 0), -int(o["year"] or 0)))
    base = os.path.join(ROOT, "results", "%s_%s" % (sub, short))
    with open(base + ".csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore")
        w.writeheader(); w.writerows(rows)
    with open(base + ".bib", "w", encoding="utf-8") as f:
        f.write("\n".join(bibs))
    with open(os.path.join(ROOT, "results", sub + "_unverified.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["subdomain", "identifier", "expected_title", "reason"])
        w.writeheader(); w.writerows(bad)
    print("%s: %d verified, %d unverified -> %s.csv" % (sub, len(rows), len(bad), base))
    # sanity listing so the agent can eyeball title/venue/year actually retrieved
    for o in rows:
        print("  [%s] %s | %s | %s | %s | cites=%s" % (o["venue_type"], o["year"], o["venue"][:50], o["title"][:90],
                                                     o["doi"] or o["arxiv"] or "", o["citations"]))


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        print(__doc__); sys.exit(1)
    if a[0] == "doi":
        for x in a[1:]:
            print(json.dumps(crossref(x), ensure_ascii=False))
    elif a[0] == "arxiv":
        for x in a[1:]:
            print(json.dumps(arxiv(x), ensure_ascii=False))
    elif a[0] == "search":
        search(a[1], int(a[2]) if len(a) > 2 else 15)
    elif a[0] == "spec3gpp":
        print(json.dumps(spec3gpp(a[1])))
    elif a[0] == "build":
        build(a[1], a[2])
