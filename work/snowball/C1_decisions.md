# C1 decisions (Standardised network analytics and data pipelines): snowball Phase 2

Judgement calls made without asking (PROTOCOL_SNOWBALL.md §1).

## Seeds with thin citation data, and manual recovery
- **Jeon2022Distributednwdaf** (ICCE 2022, 2 refs in OpenAlex, 0 in S2), **GarciaMartin2024Nwdaf** (IEEE Network, 4 refs) and
  **Nadar2024Modelprovisioning** (MedComNet 2024, 4 refs) had the thinnest reference lists. Forward data is fine for all
  three (26, 24 and 13 citing works).
  - Nadar2024: I read the full reference list from the open HAL copy (hal-04639577). It has only **6 references**: TS 23.288,
    Manias2022Signaling, Nadar's own VTC 2024 AIaaS paper (pool row 268), Mekrache2023Abnormaltraffic, an ontology URL and the
    Milan dataset (pool row 85). All of them are seeds, already in the pool, or off-topic, so nothing new was added.
  - GarciaMartin2024: no arXiv version was found (arXiv title search). IEEE Xplore reference lists cannot be reached from here,
    so the 4 OpenAlex refs stand. Best effort only.
  - Jeon2022: a 4-page ICCE paper, so 2 refs is plausibly close to the real count. Not pursued further.
- **C2 cross-link adopted:** the C2 agent found, in the Crossref reference list of BenllochCaballero2026Corex, a citation of
  Chouman et al. TNSM 2024 (pool row 45). It is selected here as `Chouman2024E2Etestbed`, with found_via
  `BenllochCaballero2026Corex(backward-manual)` added and link_count raised from 2 to **3**.

## Exclusions (non-obvious)
- **"Towards NWDAF-enabled Analytics and Closed-Loop Automation in 5G Networks"** (NOMS 2026, 10.1109/noms69089.2026.11668240,
  arXiv 2505.06789; top of the pool, link_count 6). This is the **conference version of seed Ardestani2026Closedloop**
  (ITU J-FET 2026), and ALL_CANDIDATES already records it in that seed's critique field. It is dropped under the
  journal-over-conference rule. Its 6 links do show that the Waterloo NWDAF work is central.
- **SCOPE-5G** (IEEE Access 2026, 10.1109/access.2026.3727225) and **AnomalyTrack** (ISCC 2025, 10.1109/iscc65549.2025.11326411)
  were in my first selection, but the C2 and C3 agents had already selected them (same keys `Araujo2026Scope5G`,
  `DaSilva2025Anomalytrack`). I replaced them here so that the slots are not spent on duplicates. Both remain
  relevant to C1 (AMF observability dataset; operator KPI anomaly detection), and the coordinator may add `S1` as a secondary
  subdomain.
- **Reliable feedback-driven FL for distributed NWDAFs at the edge** (Computer Networks 2026, 10.1016/j.comnet.2025.111972,
  Nokia Bell Labs + Univ. Rennes). This is the journal version of the HPSR 2024 FDFL paper (pool row 49). Neither Crossref,
  OpenAlex, S2 nor HAL has its abstract, and ScienceDirect returns 403. Rather than summarise a journal paper from its conference
  abstract, I left it as runner-up #1. **Check by hand.**
- **GEN-DRIFT** (Computer Networks 2025): no abstract accessible, and related work by the same group (Sant'Anna Pisa / IIT
  Hyderabad) is O-RAN-focused, so it was dropped as adjacent and unreadable.
- **Habibi et al., MDA for O-RAN SMO** (OJCOMS 2024). This is one of the very few works on 3GPP MDA (TS 28.104), which is
  relevant to gap 1. It was swapped out for the Chouman TNSM testbed because it is conceptual and RAN/SMO-centred (relevance 2,
  link_count 1). It stays as a runner-up, and the gap check should cite it as the "MDA has no evaluation" exception that still
  has no numbers.
- **Generic items:** generic FL/privacy, homomorphic encryption, IoT/IIoT, vehicular, UAV, healthcare, concept-drift theory,
  O-RAN xApp, handover and mmWave works, and the many 2014-2019 5G/6G vision surveys (e.g. *What Will 5G Be?*, COMST 5G
  surveys), were dropped as off-topic or background. About 53 rows with no DOI/arXiv are 3GPP/ETSI spec references,
  white papers, software URLs or author-bio fragments mis-parsed as references, and were dropped as the wrong type.
- **Retracted:** pool row 384 (INCOFT 2022, retraction notice) was dropped.
- **Off-category but notable (left to other agents or the coordinator):** LLM intent extraction for the 5G core (DRCN 2024,
  Western) → C5; SBA-Route domain-based routing for distributed NRFs (IWQoS 2026) → C4; AI-native E2E slicing with a core
  abstraction (TCCN 2025) → C4.

## Inclusions (borderline)
- **Alawe2018Trafficforecast** (IEEE Network 2018, 236 citations, link_count 5): the **only `seminal`** proposed by C1. It is
  the foundational forecast-driven 5GC scaling paper (Ksentini and Hadjadj-Aoul are co-authors), cited by 5 seeds across
  C1, C3 and C5.
- **Jeong2021Mobilityprediction** (IEEE ComStdMag 2021, Ericsson, link_count 1): kept despite the single link, because it is an
  operator-vendor work on 5G core analytics evaluated on live-network data (adaptive paging, up to 75% less signalling).
- **Zhu2022Disasterbackup** (CECCC 2022, China Telecom): a **weak venue**, analytical evaluation only. It is kept because it is
  direct prior art for gaps G2/G7: NWDAF-detected UDM failure triggering an HSS fallback. It is flagged `gap-evidence`.
- **Tiwari2025Nwdafevolution** (NCC 2025, C-DOT India): a modest venue, but link_count 5 and a survey the article should
  position itself against. Flagged `survey`.
- **Yin2026Vflnwdaf** (IWCMC 2026, China Telecom Research Institute): design-only, no numbers in the abstract. It is kept
  because the Rel-19 NWDAF VFL topic has almost no academic coverage (gap 1).
- **Kuo2026Distributedmtlf** (ICC 2026 Workshops, NYCU): a workshop paper, but it is the only snowballed work that explicitly
  evaluates the **MTLF/AnLF split under drift** with distributed (federated) training (gap 1).
- **Ameur2025Driftdetection** (TMLCN 2025, EURECOM): drift detection for 6G telecom data, not core-specific, so relevance 2.
- **Venue types:** IEEE Network, IEEE Internet Computing and IEEE ComStdMag are recorded as `journal` (peer-reviewed
  magazines), as in the first run. IJDSN (Hindawi/SAGE) is a journal. Quartiles were not recorded.
