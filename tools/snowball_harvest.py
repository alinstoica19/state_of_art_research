#!/usr/bin/env python3
"""Phase 1 of PROTOCOL_SNOWBALL.md: backward and forward citation harvest for the 37 seeds.

Sources (no keyword search, no e-mail or personal identifier sent):
  backward: OpenAlex `referenced_works` of the seed (single-work lookups /works/doi:..., /works/W...)
            + Semantic Scholar /paper/<id>/references
  forward:  Semantic Scholar /paper/<id>/citations (OpenAlex cited_by list queries are quota-blocked),
            kept only for 2022-2026

Writes
  work/snowball/pool_C<k>.csv      one row per candidate (no abstracts), with link_count and found_via
  <scratch>/abstracts.json         abstracts for screening (kept out of the repository: copyrighted text)
"""
import csv, json, os, re, sys, time, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify import get, norm, ROOT, CACHE  # same cache, no e-mail sent

SCRATCH = os.path.dirname(CACHE)
SEEDS = [l.split("|") for l in """C1|Abbas2022Sliceanalytics|10.1109/noms54207.2022.9789706
C1|Ameur2026Agenticnwdaf|10.1109/icc59461.2026.11587766
C1|Ardestani2026Closedloop|10.52953/svmm1934
C1|Bayleyegn2024Kpiprediction|10.1109/netsoft60951.2024.10588931
C1|Chouman2022Nwdaf|10.1109/iwcmc55113.2022.9824403
C1|Daniel2026Opennwdaf|arXiv:2601.01838
C1|GarciaMartin2024Nwdaf|10.1109/mnet.2023.3321524
C1|Jeon2022Distributednwdaf|10.1109/icce53296.2022.9730220
C1|Majumdar2026Ainative|10.1109/mcomstd.2025.3585376
C1|Manias2022Signaling|10.1109/globecom48099.2022.10000989
C1|Manias2023Modeldrift|10.1109/mcom.003.2200306
C1|Mekrache2023Abnormaltraffic|10.1109/globecom54140.2023.10436766
C1|Nadar2024Modelprovisioning|10.1109/medcomnet62012.2024.10578162
C1|Oliveira2025Aiaas|10.23919/cnsm67658.2025.11297508
C1|Romero2025Nwdafreview|10.14209/sbrt.2025.1571141712
C1|Sevgican2020Nwdaf|10.1109/jcn.2020.000019
C1|Zhang2025Fairfl|10.1109/tits.2024.3461679
C1|Zhang2025Sammf|10.1109/lnet.2025.3579358
C1|Zhou2023Federatednwdaf|10.1109/lnet.2023.3294497
C2|BenllochCaballero2026Corex|10.1109/tnsm.2026.3699692
C2|Costa2025Privatendt|arXiv:2510.12458
C2|Mozo2022B5Gemini|10.1109/noms54207.2022.9789810
C2|Tao2024Corecontrolplane|10.1109/tccn.2023.3324634
C2|Wang2024Sliceadmission|10.1016/j.future.2023.12.018
C2|Xie2026Signalingstorm|10.1145/3789240.3829205
C2|Zanzi2026Cloudnativendt|10.1109/icc59461.2026.11587512
C3|Basikolo2023Zerodowntime|10.52953/pyaf8065
C3|Chakraborty2021Failureforecast|10.1109/iccworkshops50388.2021.9473530
C3|Kawasaki2023Failureprediction|10.1109/vtc2023-spring57618.2023.10200028
C3|Larrea2023Corekube|10.1145/3570361.3592522
C3|Leiter2022Upffailover|10.1109/noms54207.2022.9789799
C3|Sovitkar2024Recap|10.1109/noms59830.2024.10575767
C3|Vittal2022Harness|10.1109/tnsm.2022.3157888
C3|Vittal2024Resilientcore|10.1109/tnsm.2023.3348137
C4|Kamran2025Energyexposure|10.1109/comsnets63942.2025.10885745
C5|Ameur2026Agenticsurvey|arXiv:2607.16066
C5|Coronado2022Zerotouch|10.1109/comst.2022.3212586""".split("\n")]
GROUP = {"C1": "C1", "C2": "C2", "C3": "C3", "C4": "C45", "C5": "C45"}
S2F = "title,year,externalIds,venue,publicationTypes,abstract,citationCount"


def jget(url):
    for i in range(6):
        d = get(url, tries=3)
        if d is None:
            return None
        try:
            return json.loads(d)
        except Exception:
            return None
    return None


def s2(path):
    url = "https://api.semanticscholar.org/graph/v1/paper/" + path
    time.sleep(1.1)  # stay under the anonymous S2 rate limit
    return jget(url)


def oa_abstract(inv):
    if not inv:
        return ""
    pos = sorted((p, w) for w, ps in inv.items() for p in ps)
    return " ".join(w for _, w in pos)


def s2_id(ident):
    return ("ARXIV:" + ident[6:]) if ident.startswith("arXiv:") else "DOI:" + ident


def oa_id(ident):
    return ("doi:10.48550/arxiv." + ident[6:]) if ident.startswith("arXiv:") else "doi:" + ident


def from_s2(p):
    ex = p.get("externalIds") or {}
    return {"title": p.get("title") or "", "year": p.get("year") or "", "venue": p.get("venue") or "",
            "doi": (ex.get("DOI") or "").lower(), "arxiv": ex.get("ArXiv") or "",
            "types": ";".join(p.get("publicationTypes") or []), "abstract": p.get("abstract") or "",
            "cites": p.get("citationCount") or ""}


def from_oa(w):
    doi = (w.get("doi") or "").replace("https://doi.org/", "").lower()
    arx = ""
    for loc in w.get("locations") or []:
        u = (loc.get("landing_page_url") or "")
        m = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", u)
        if m:
            arx = m.group(1)
    m = re.match(r"10\.48550/arxiv\.(.+)", doi)
    if m:
        arx, doi = m.group(1), ""
    venue = ((w.get("primary_location") or {}).get("source") or {}).get("display_name") or ""
    return {"title": w.get("title") or "", "year": w.get("publication_year") or "", "venue": venue,
            "doi": doi, "arxiv": arx, "types": w.get("type") or "",
            "abstract": oa_abstract(w.get("abstract_inverted_index")), "cites": w.get("cited_by_count") or ""}


def main():
    existing_doi, existing_t = set(), set()
    for r in csv.DictReader(open(os.path.join(ROOT, "ALL_CANDIDATES.csv"), encoding="utf-8")):
        if r["doi"]:
            existing_doi.add(r["doi"].lower())
        if r["arxiv"]:
            existing_doi.add("arxiv:" + r["arxiv"].lower())
        existing_t.add(norm(r["title"]))
    pool = {}  # key -> record
    log = []
    sel = "id,doi,title,publication_year,primary_location,locations,type,abstract_inverted_index,cited_by_count"
    for cat, key, ident in SEEDS:
        grp = GROUP[cat]
        found = []
        # backward via OpenAlex
        w = jget("https://api.openalex.org/works/" + urllib.parse.quote(oa_id(ident), safe=":/") + "?select=id,referenced_works")
        nb_oa = 0
        if w:
            for ref in w.get("referenced_works") or []:
                rw = jget("https://api.openalex.org/works/" + ref.rsplit("/", 1)[-1] + "?select=" + sel)
                if rw:
                    found.append(("backward", from_oa(rw))); nb_oa += 1
        # backward via Semantic Scholar
        r = s2(urllib.parse.quote(s2_id(ident), safe=":") + "/references?fields=" + S2F + "&limit=1000")
        nb_s2 = 0
        for it in (r or {}).get("data") or []:
            p = it.get("citedPaper") or {}
            if p.get("title"):
                found.append(("backward", from_s2(p))); nb_s2 += 1
        # forward via Semantic Scholar (paged)
        nf, off = 0, 0
        while off is not None and off < 5000:
            r = s2(urllib.parse.quote(s2_id(ident), safe=":") + "/citations?fields=" + S2F + "&limit=500&offset=%d" % off)
            if not r:
                break
            for it in r.get("data") or []:
                p = it.get("citingPaper") or {}
                if p.get("title") and (p.get("year") or 0) >= 2022:
                    found.append(("forward", from_s2(p))); nf += 1
            off = r.get("next")
        log.append({"seed": key, "cat": cat, "oa_refs": nb_oa, "s2_refs": nb_s2, "forward_2022plus": nf,
                    "oa_found": bool(w)})
        print(log[-1], file=sys.stderr)
        for direction, rec in found:
            t = norm(rec["title"])
            if not t:
                continue
            k = rec["doi"] or ("arxiv:" + rec["arxiv"].lower() if rec["arxiv"] else "t:" + t)
            # merge records that share a title but were keyed differently
            alt = "t:" + t
            ent = pool.get(k) or pool.get(alt)
            if ent is None:
                for kk, ee in pool.items():
                    if ee["ntitle"] == t:
                        ent = ee; break
            if ent is None:
                ent = pool[k] = dict(rec, ntitle=t, links={}, groups=set())
            for f in ("doi", "arxiv", "venue", "abstract", "year", "cites"):
                if not ent.get(f) and rec.get(f):
                    ent[f] = rec[f]
            ent["links"].setdefault(key, set()).add(direction)
            ent["groups"].add(grp)
    seeds_doi = {s[2].lower() for s in SEEDS}
    seeds_doi |= {"arxiv:" + s[2][6:].lower() for s in SEEDS if s[2].startswith("arXiv:")}
    abstracts, out = {}, {g: [] for g in ("C1", "C2", "C3", "C45")}
    n_total = n_exist = 0
    for k, e in pool.items():
        n_total += 1
        ids = {e["doi"]} | ({"arxiv:" + e["arxiv"].lower()} if e["arxiv"] else set())
        if ids & seeds_doi or ids & existing_doi or e["ntitle"] in existing_t:
            n_exist += 1; continue
        lc = len(e["links"])
        via = "; ".join("%s(%s)" % (s, "+".join(sorted(d))) for s, d in sorted(e["links"].items()))
        row = {"key": k, "title": e["title"], "year": e["year"], "venue": e["venue"], "doi": e["doi"],
               "arxiv": e["arxiv"], "types": e["types"], "cites": e["cites"], "link_count": lc,
               "found_via": via, "groups": ";".join(sorted(e["groups"])), "has_abstract": bool(e["abstract"])}
        abstracts[k] = e["abstract"]
        # a candidate goes to the pool of every category whose seeds it is linked to
        for g in e["groups"]:
            out[g].append(row)
    os.makedirs(os.path.join(ROOT, "work", "snowball"), exist_ok=True)
    cols = ["key", "title", "year", "venue", "doi", "arxiv", "types", "cites", "link_count", "found_via", "groups",
            "has_abstract"]
    for g, rows in out.items():
        rows.sort(key=lambda r: (-r["link_count"], -(int(r["year"]) if str(r["year"]).isdigit() else 0)))
        with open(os.path.join(ROOT, "work", "snowball", "pool_%s.csv" % g), "w", newline="", encoding="utf-8") as f:
            wr = csv.DictWriter(f, fieldnames=cols); wr.writeheader(); wr.writerows(rows)
    json.dump(abstracts, open(os.path.join(SCRATCH, "abstracts.json"), "w"))
    with open(os.path.join(ROOT, "work", "snowball", "harvest_log.json"), "w") as f:
        json.dump({"seeds": log, "unique_harvested": n_total, "already_in_list_or_seed": n_exist,
                   "per_group": {g: len(r) for g, r in out.items()}}, f, indent=1)
    print("harvested %d unique, %d already listed; pools: %s" % (n_total, n_exist,
          {g: len(r) for g, r in out.items()}))


if __name__ == "__main__":
    main()
