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
| Gap check | pending |
| 4 Summary | pending |
