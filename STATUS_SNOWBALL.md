# STATUS — snowballing run (PROTOCOL_SNOWBALL.md)

Started 2026-10-10. Branch: `claude/5g-6g-literature-search-2lyo41` (the designated branch; pushes go there).

## API access (re-checked 2026-10-10)

| Service | Use | Outcome |
|---|---|---|
| OpenAlex single-work lookups (`/works/doi:…`, `/works/W…`) | seed `referenced_works` (backward) | **OK** |
| OpenAlex list/filter queries (`/works?filter=cites:…`) | forward citations | **Blocked** (HTTP 429, shared anonymous daily budget used up) → Semantic Scholar used for forward |
| Semantic Scholar Graph API (`/references`, `/citations`) | backward + forward | **OK** (1 req/s) |
| Crossref, arXiv API | verification | **OK** |

No e-mail address or personal identifier is sent to any API (`tools/verify.py` was changed accordingly).

## Progress

| Phase | Status |
|---|---|
| 1 Harvest | **done**: 1386 unique works linked to the seeds; 47 already in the list or seeds; pools C1 517, C2 185, C3 246, C4+C5 440 (overlapping) |
| 2 Select + verify C1 | **done**: 15 verified (+0 unverified) |
| 2 Select + verify C2 | **done**: 14 verified (+0 unverified) |
| 2 Select + verify C3 | **done**: 15 verified (+0 unverified) |
| 2 Select + verify C4+C5 | **done**: 15 verified (+0 unverified) |
| 3 Gap check | **done**: 44 verified (+0 unverified) |
| 4 Summary | **done**: `SNOWBALL_SUMMARY.md`; `results/SNOWBALL.csv` + `snowball.bib` = 100 new verified works (56 snowball + 44 gap check), 0 unverified |

## Outputs

- `results/SNOWBALL.csv`, `snowball.bib`, `unverified_snowball.csv` (empty)
- `GAP_CHECK.md`: verdicts G2/G3/G7/P1/P2/P3 **partially covered**, P4 **holds**, none **already done**
- `SNOWBALL_SUMMARY.md`
- Per-category working files: `work/SB_*.jsonl`, `results/SB_*`, `work/snowball/*`

All work is pushed to `claude/5g-6g-literature-search-2lyo41`.
