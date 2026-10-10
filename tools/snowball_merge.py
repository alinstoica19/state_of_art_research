#!/usr/bin/env python3
"""Phase 2 merge of PROTOCOL_SNOWBALL.md.

Reads results/SB_{C1,C2,C3,C45,GAP}_*.csv (built by verify.py from work/SB_*.jsonl) and writes
  results/SNOWBALL.csv       one row per new work: ALL_CANDIDATES.csv columns + found_via, link_count, category
  snowball.bib               BibTeX for every row (keys = id column)
  unverified_snowball.csv    union of results/SB_*_unverified.csv
Drops anything already in ALL_CANDIDATES.csv (DOI, arXiv ID or normalised title) and keeps at most 5 `seminal`
works (most links first).
"""
import csv, glob, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify import ROOT, COLS, norm

GROUPS = ["C1", "C2", "C3", "C45", "GAP"]
OUT_COLS = COLS + ["found_via", "link_count", "category"]


def bib_blocks(path):
    txt = open(path, encoding="utf-8").read()
    return {m.group(1): m.group(0) for m in re.finditer(r"@\w+\{([^,]+),.*?\n\}\n", txt, re.S)}


def main():
    have_doi, have_t, have_ids = set(), set(), set()
    for r in csv.DictReader(open(os.path.join(ROOT, "ALL_CANDIDATES.csv"), encoding="utf-8")):
        have_ids.add(r["id"])
        for x in (r["doi"], r["arxiv"]):
            if x:
                have_doi.add(x.lower())
        have_t.add(norm(r["title"]))
    rows, bibs, dropped = {}, {}, []
    for g in GROUPS:
        for p in glob.glob(os.path.join(ROOT, "results", "SB_%s_*.csv" % g)):
            if p.endswith("_unverified.csv"):
                continue
            bp = p[:-4] + ".bib"
            blocks = bib_blocks(bp) if os.path.exists(bp) else {}
            for r in csv.DictReader(open(p, encoding="utf-8")):
                ids = {x.lower() for x in (r["doi"], r["arxiv"]) if x}
                t = norm(r["title"])
                if ids & have_doi or t in have_t:
                    dropped.append((r["id"], "already in ALL_CANDIDATES.csv")); continue
                k = next((kk for kk, e in rows.items()
                          if ({x.lower() for x in (e["doi"], e["arxiv"]) if x} & ids) or norm(e["title"]) == t), None)
                lab = "C4+C5" if g == "C45" else ("gap-check" if g == "GAP" else g)
                if k is None:
                    old, i = r["id"], 0
                    while r["id"] in rows or r["id"] in have_ids:  # key clash with another work: suffix it
                        i += 1; r["id"] = old + "abcdefghij"[i - 1]
                    if old in blocks:
                        blocks[r["id"]] = blocks[old].replace("{" + old + ",", "{" + r["id"] + ",", 1)
                    r["category"] = lab
                    r["link_count"] = r.get("link_count") or "0"
                    rows[r["id"]] = r
                    if r["id"] in blocks:
                        bibs[r["id"]] = blocks[r["id"]]
                else:  # same work selected by two agents: merge provenance
                    e = rows[k]
                    vias = [v.strip() for v in (e["found_via"] + ";" + r.get("found_via", "")).split(";") if v.strip()]
                    e["found_via"] = "; ".join(dict.fromkeys(vias))
                    e["link_count"] = str(max(int(e["link_count"] or 0), int(r.get("link_count") or 0)))
                    if lab not in e["category"].split(";"):
                        e["category"] += ";" + lab
                    sec = {s for s in (e["secondary_subdomains"] + ";" + r["secondary_subdomains"] + ";" + r["subdomain"]).split(";")
                           if s.strip() and s.strip() != e["subdomain"]}
                    e["secondary_subdomains"] = ";".join(sorted(sec))
                    e["relevance"] = str(max(int(e["relevance"] or 0), int(r["relevance"] or 0)))
                    dropped.append((r["id"], "duplicate of %s (merged)" % k))
    # seminal cap: keep the 5 with the most links
    sem = sorted([r for r in rows.values() if "seminal" in r["flags"]], key=lambda r: -int(r["link_count"] or 0))
    for r in sem[5:]:
        dropped.append((r["id"], "seminal cap (>5)")); del rows[r["id"]]
    out = sorted(rows.values(), key=lambda o: ("survey" not in o["flags"], -int(o["relevance"] or 0),
                                               -int(o["link_count"] or 0), -int(o["year"] or 0)))
    with open(os.path.join(ROOT, "results", "SNOWBALL.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=OUT_COLS, extrasaction="ignore"); w.writeheader(); w.writerows(out)
    with open(os.path.join(ROOT, "snowball.bib"), "w", encoding="utf-8") as f:
        f.write("\n".join(bibs[o["id"]] for o in out if o["id"] in bibs))
    unv = []
    for p in sorted(glob.glob(os.path.join(ROOT, "results", "SB_*_unverified.csv"))):
        unv += list(csv.DictReader(open(p, encoding="utf-8")))
    with open(os.path.join(ROOT, "unverified_snowball.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["subdomain", "identifier", "expected_title", "reason"]); w.writeheader(); w.writerows(unv)
    missing = [o["id"] for o in out if o["id"] not in bibs]
    print("SNOWBALL.csv: %d works; unverified: %d; dropped: %d; missing bib: %s" % (len(out), len(unv), len(dropped), missing))
    for d in dropped:
        print("  dropped", *d)
    from collections import Counter
    print("  per category:", dict(Counter(o["category"] for o in out)))


if __name__ == "__main__":
    main()
