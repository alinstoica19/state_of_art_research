# DECISIONS — snowballing run

Judgement calls made without asking the user (PROTOCOL_SNOWBALL.md §1).

## Setup

- **Privacy.** In the first run, `tools/verify.py` sent the user's e-mail to Crossref/OpenAlex (polite-pool `mailto` and
  User-Agent). §3 forbids this, so `MAILTO` was removed from every URL and from the User-Agent. The verification
  cache path now points to this session's scratchpad.
- **Harvest done centrally, screening done by parallel subagents.** §3 asks for one subagent per category for the
  harvest. The harvest itself is a deterministic API crawl, so one script (`tools/snowball_harvest.py`) runs it
  for all 37 seeds. This gives one cache, one rate limiter and one consistent link count across categories. The
  judgement-heavy part (abstract screening, selection, own-words characterisation, verification) is done by four
  parallel subagents (C1, C2, C3, C4+C5), plus one for the gap check.
- **Forward citations come from Semantic Scholar.** OpenAlex `cited_by` list queries return HTTP 429 (the shared
  anonymous daily budget is used up). Backward references use **both** OpenAlex `referenced_works` and Semantic
  Scholar `references`, because Semantic Scholar often lacks reference lists for IEEE papers.
- **Pools.** A candidate linked to seeds of several categories appears in the pool of each, and the
  cross-category merge removes duplicates. `link_count` = the number of distinct seeds it is linked to,
  backward or forward.
- **Abstracts** used for screening are kept in the scratchpad, not in the repository (copyrighted text).
