#!/usr/bin/env python3
"""Show snowball pool candidates with their abstracts for screening (abstracts stay in the scratchpad).

Usage
  snowball_view.py C1 [--min-links N] [--from-year Y] [--grep REGEX] [--start I] [--count K] [--chars C]
Prints: index | link_count | year | venue | doi/arxiv | title | found_via, then the abstract (first C chars).
"""
import argparse, csv, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify import ROOT, CACHE

ap = argparse.ArgumentParser()
ap.add_argument("group")
ap.add_argument("--min-links", type=int, default=1)
ap.add_argument("--from-year", type=int, default=0)
ap.add_argument("--grep", default="")
ap.add_argument("--start", type=int, default=0)
ap.add_argument("--count", type=int, default=60)
ap.add_argument("--chars", type=int, default=600)
a = ap.parse_args()
abstracts = json.load(open(os.path.join(os.path.dirname(CACHE), "abstracts.json")))
rows = list(csv.DictReader(open(os.path.join(ROOT, "work", "snowball", "pool_%s.csv" % a.group), encoding="utf-8")))
sel = []
for i, r in enumerate(rows):
    y = int(r["year"]) if str(r["year"]).isdigit() else 0
    if int(r["link_count"]) < a.min_links or y < a.from_year:
        continue
    ab = abstracts.get(r["key"], "")
    if a.grep and not re.search(a.grep, r["title"] + " " + ab + " " + r["venue"], re.I):
        continue
    sel.append((i, r, ab))
print("%d matching of %d in pool %s" % (len(sel), len(rows), a.group))
for i, r, ab in sel[a.start:a.start + a.count]:
    print("#%d | L=%s | %s | %s | %s | %s\n   via: %s" % (i, r["link_count"], r["year"], r["venue"][:45],
          r["doi"] or ("arXiv:" + r["arxiv"] if r["arxiv"] else "-"), r["title"], r["found_via"]))
    if ab and a.chars:
        print("   ABS: " + ab[:a.chars].replace("\n", " "))
