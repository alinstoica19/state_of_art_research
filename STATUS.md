# STATUS

## Phase 1 — API access check (2026-10-10)

| Service | Test | Outcome |
|---|---|---|
| Crossref REST API (`api.crossref.org/works/<DOI>`) | DOI 10.1109/COMST.2022.3202047 | **OK** (200, title matched). Bibliographic search endpoint also OK. |
| doi.org content negotiation (BibTeX) | same DOI | **OK** |
| arXiv API | `id_list=2201.04839` | **OK over HTTPS** (`http://` returns 301 → use `https://export.arxiv.org`) |
| OpenAlex single work (`/works/doi:<DOI>`) | same DOI | **OK** (citation count returned) |
| OpenAlex search (`/works?search=`) | keyword query | **Blocked** — shared anonymous daily budget exhausted (HTTP 429); not needed for verification |
| Semantic Scholar Graph API | DOI lookup | **Intermittent** (429 rate limit, then 200) — used only as citation fallback |
| 3GPP portal (`portal.3gpp.org/.../SpecificationDetails.aspx`) | spec 23.288 | **OK** (spec number + title readable) |
| 3GPP FTP / www.3gpp.org | archive folder | Blocked for curl (403); portal used instead |
| ETSI (`www.etsi.org/deliver/...`) | ZSM 002 | Blocked for curl (403), **reachable via WebFetch tool** |
| IETF Datatracker | NMRG draft page | **OK** |

**Conclusion:** full verification is possible. Entries are verified by DOI (Crossref), arXiv ID (arXiv API)
or standard (3GPP portal / ETSI / IETF page). `verification: search-only` is **not** needed.
Citation counts come from OpenAlex (fallback Semantic Scholar), dated at retrieval.

## Phase 2 — subdomains

| # | Subdomain | Status | Verified entries |
|---|---|---|---|
| S3 | Network digital twins | running | – |
| S1 | Network analytics (NWDAF/MDA) | running | – |
| S5 | Resilience / geo-redundancy | running | – |
| S8 | AI/ML performance prediction | **done** | 23 (+0 unverified) |
| S6 | Closed-loop / autonomous networks | running | – |
| S4 | RCA / anomaly detection | **done** | 23 (+0 unverified) |
| S2 | SBA / NF selection | **done** | 25 (+0 unverified) |
| S7 | Energy efficiency | running | – |

## Phase 3 — merge

pending
