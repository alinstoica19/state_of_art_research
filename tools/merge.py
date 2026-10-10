#!/usr/bin/env python3
"""Phase 3: deduplicate results/S*_*.csv into ALL_CANDIDATES.csv, references.bib, unverified.csv,
grey_literature.csv, and print statistics (markdown) used in SUMMARY.md -> work/stats.md"""
import collections, csv, difflib, glob, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify import COLS, norm

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
PRIO = ["S3", "S1", "S5", "S8", "S6", "S4", "S2", "S7"]
NAMES = {"S1": "Network analytics (NWDAF/MDA)", "S2": "SBA and NF selection", "S3": "Network digital twins",
         "S4": "RCA and anomaly detection", "S5": "Resilience and failover", "S6": "Closed-loop / autonomous networks",
         "S7": "Energy efficiency", "S8": "AI/ML performance prediction"}


def parse_bib(path):
    out, cur, key = {}, [], None
    for line in open(path, encoding="utf-8"):
        m = re.match(r"@\w+\{([^,]+),", line)
        if m:
            key, cur = m.group(1), [line]
        elif key:
            cur.append(line)
            if line.startswith("}"):
                out[key] = "".join(cur); key = None
    return out


def wkey(r):
    if r["doi"]:
        return "doi:" + r["doi"].lower()
    if r["arxiv"]:
        return "arxiv:" + r["arxiv"]
    if r["venue_type"] == "standard":
        m = re.search(r"(TS|TR|GS|RFC|Y\.)\s*([0-9][0-9A-Za-z.\- ]*)", r["venue"])
        return "std:" + (re.sub(r"\s", "", m.group(0)) if m else norm(r["title"]))
    return "title:" + norm(r["title"])


rows, bibs = [], {}
for f in sorted(glob.glob("results/S*_*.csv")):
    if f.endswith("_unverified.csv"):
        continue
    sub = os.path.basename(f).split("_")[0]
    b = parse_bib(f[:-4] + ".bib") if os.path.exists(f[:-4] + ".bib") else {}
    for r in csv.DictReader(open(f, encoding="utf-8")):
        r["_bib"] = b.get(r["id"], "")
        rows.append(r)

groups = collections.OrderedDict()
for r in rows:
    groups.setdefault(wkey(r), []).append(r)

# fuzzy title pass: same work under different identifiers (e.g. arXiv vs DOI) -> merge; journal vs conf -> report
keys = list(groups)
fuzzy_pairs = []
for i, a in enumerate(keys):
    for b in keys[i + 1:]:
        if a in groups and b in groups:
            ta, tb = groups[a][0]["title"], groups[b][0]["title"]
            s = difflib.SequenceMatcher(None, norm(ta), norm(tb)).ratio()
            if s > 0.9:
                fuzzy_pairs.append((s, groups[a][0], groups[b][0]))

merged, used_keys = [], {}
for k, g in groups.items():
    g.sort(key=lambda r: (-int(r["relevance"] or 0), PRIO.index(r["subdomain"]) if r["subdomain"] in PRIO else 9))
    p = dict(g[0])
    subs = [r["subdomain"] for r in g]
    sec = []
    for r in g:
        sec += [s.strip() for s in re.split(r"[;,]", r["secondary_subdomains"]) if s.strip()]
    sec = [s for s in dict.fromkeys(subs[1:] + sec) if s != p["subdomain"] and re.match(r"S\d$", s)]
    p["secondary_subdomains"] = ";".join(sorted(sec))
    fl = []
    for r in g:
        fl += [x.strip() for x in r["flags"].split(";") if x.strip()]
    p["flags"] = ";".join(dict.fromkeys(fl))
    p["relevance"] = max(int(r["relevance"] or 0) for r in g)
    # global bib-key uniqueness
    key, bib = p["id"], p["_bib"]
    if key in used_keys and used_keys[key] != k:
        n = 1
        while key + "abcdefghij"[n - 1] in used_keys:
            n += 1
        new = key + "abcdefghij"[n - 1]
        bib = bib.replace("{" + key + ",", "{" + new + ",", 1)
        key = new
    used_keys[key] = k
    p["id"], p["_bib"] = key, bib
    p["_n_sub"] = len(subs)
    merged.append(p)

merged.sort(key=lambda o: ("survey" not in o["flags"], PRIO.index(o["subdomain"]) if o["subdomain"] in PRIO else 9,
                           -int(o["relevance"]), -int(o["year"] or 0)))
with open("ALL_CANDIDATES.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore"); w.writeheader(); w.writerows(merged)
with open("references.bib", "w", encoding="utf-8") as f:
    f.write("% Merged BibTeX for ALL_CANDIDATES.csv (metadata from Crossref / arXiv / 3GPP portal)\n\n")
    f.write("\n".join(p["_bib"] for p in merged if p["_bib"]))

# unverified + grey
unv = []
for f in sorted(glob.glob("results/S*_unverified.csv")):
    unv += list(csv.DictReader(open(f, encoding="utf-8")))
with open("unverified.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["subdomain", "identifier", "expected_title", "reason"]); w.writeheader(); w.writerows(unv)
grey = []
for f in sorted(glob.glob("work/S*_grey.csv")):
    sub = os.path.basename(f).split("_")[0]
    for r in csv.DictReader(open(f, encoding="utf-8")):
        r["subdomain"] = sub; grey.append(r)
if grey:
    with open("grey_literature.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["subdomain", "title", "organisation", "year", "url", "note"], extrasaction="ignore")
        w.writeheader(); w.writerows(grey)

# stats
L = []
L.append("Total rows in subdomain files: %d; unique works after deduplication: **%d**; unverified: %d; grey: %d\n"
         % (len(rows), len(merged), len(unv), len(grey)))
L.append("| Subdomain | Primary | Incl. secondary | Relevance 3 | Surveys |\n|---|---|---|---|---|")
for s in sorted(NAMES):
    prim = [p for p in merged if p["subdomain"] == s]
    tot = [p for p in merged if p["subdomain"] == s or s in p["secondary_subdomains"].split(";")]
    L.append("| %s %s | %d | %d | %d | %d |" % (s, NAMES[s], len(prim), len(tot),
             sum(1 for p in prim if int(p["relevance"]) == 3), sum(1 for p in prim if "survey" in p["flags"])))
yc = collections.Counter(str(p["year"]) for p in merged)
L.append("\n| Year | Works |\n|---|---|")
for y in sorted(yc):
    L.append("| %s | %d |" % (y, yc[y]))
vc = collections.Counter(p["venue_type"] for p in merged)
L.append("\n| Venue type | Works |\n|---|---|")
for v, c in vc.most_common():
    L.append("| %s | %d |" % (v, c))
rc = collections.Counter(int(p["relevance"]) for p in merged)
L.append("\n| Relevance | Works |\n|---|---|")
for v in (3, 2, 1):
    L.append("| %d | %d |" % (v, rc[v]))
venc = collections.Counter(p["venue"] for p in merged if p["venue_type"] != "standard")
L.append("\nTop venues:\n")
for v, c in venc.most_common(15):
    L.append("- %s (%d)" % (v, c))
L.append("\n## Surveys\n")
L.append("| id | Year | Title | Venue | Subdomain | Cites |\n|---|---|---|---|---|---|")
for p in merged:
    if "survey" in p["flags"]:
        L.append("| %s | %s | %s | %s | %s | %s |" % (p["id"], p["year"], p["title"], p["venue"], p["subdomain"], p["citations"]))
ac = collections.Counter()
for p in merged:
    if int(p["relevance"]) == 3 and p["venue_type"] != "standard":
        for a in p["authors"].split("; "):
            if a.strip():
                ac[a.strip()] += 1
L.append("\n## Most frequent authors in relevance-3 works\n")
for a, c in ac.most_common(40):
    if c < 2:
        break
    ws = [p["id"] for p in merged if int(p["relevance"]) == 3 and a in p["authors"].split("; ")]
    L.append("- %s (%d): %s" % (a, c, ", ".join(ws)))
L.append("\n## Fuzzy-title near duplicates (review)\n")
for s, a, b in fuzzy_pairs:
    L.append("- %.2f: %s [%s, %s] <-> %s [%s, %s]" % (s, a["id"], a["venue"], a["year"], b["id"], b["venue"], b["year"]))
L.append("\n## Works appearing in more than one subdomain file\n")
for p in merged:
    if p["_n_sub"] > 1:
        L.append("- %s (%s; also %s)" % (p["id"], p["subdomain"], p["secondary_subdomains"]))
open("work/stats.md", "w").write("\n".join(L) + "\n")
print("\n".join(L))
