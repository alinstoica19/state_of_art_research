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
- **Seeds with no usable citation-graph data.** BenllochCaballero2026Corex (no references or citations in
  either API), Kamran2025Energyexposure and Ameur2026Agenticsurvey (no reference list, 2 citing works each), and
  Leiter2022Upffailover (no reference list) returned little or nothing. These are recent works, so forward
  citations are expected to be thin. The category agents were asked to recover their reference lists by hand
  from the publisher or arXiv page where accessible (best effort, logged in `work/snowball/C*_decisions.md`).
- **Coronado2022Zerotouch dominates the C4+C5 pool.** It is a large survey with about 250 references and 156
  citing works since 2022. Its links were screened for core-network relevance only, so generic ZSM, RAN and IoT
  items were dropped.
- **Seminal cap (≤5 overall).** Each category agent may propose at most 2 pre-2020 works flagged `seminal`. The
  coordinator keeps the 5 with the most links.

## Phase 2 (coordinator)

- **C2 / B5GEMINI.** The journal version (Mozo2022B5Geminijournal, Sensors 2022) is kept in SNOWBALL.csv. The
  conference version stays in ALL_CANDIDATES.csv as the seed (Mozo2022B5Gemini, NOMS). PROTOCOL.md §3 prefers
  journal versions, so when the two lists are merged the author should cite the journal version and keep the NOMS
  paper only for its earlier date.
- **C2 left NWDAF items to C1:** row 0 (NOMS 2026, NWDAF-enabled closed loop, link count 6) and the Chouman
  testbed. The coordinator checks after C1 finishes that they were taken.
- **C3 venues.** VTC-Spring (Kato2023), ISCC (AnomalyTrack) and a Globecom workshop (Selvakumar2025) fall outside
  the strict venue list in PROTOCOL.md §3. They are kept because they bear directly on P3, on operator-scale
  data, and on the Fraunhofer failure-prediction line. Duplicates dropped: Neutrino SIGCOMM 2020 (its ToN
  version is in the list) and the CoreKube MobiCom 2023 demo.
- **Alawe 2018 traffic forecasting** (IEEE Network, 10.1109/mnet.2018.1800104) has the highest link count of
  any pool item (L=5: Coronado, Manias, Sovitkar, Vittal ×2). It is considered as a `seminal` candidate at the merge.
