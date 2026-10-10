# C4+C5 snowball: judgement calls (Phase 2)

## Seeds recovered by hand
- **Ameur2026Agenticsurvey (arXiv:2607.16066).** The reference list was parsed from the arXiv HTML page
  (177 bibliography items, kept in the scratchpad only). Most items are generic LLM/agent papers, RAN/O-RAN agent
  papers, white papers or project web pages. These were dropped. The core-relevant items were screened:
  - selected: Li2025Agenticcore (Engineering), Tong2025Acore (ICC Workshops 2025), Manias2024Intentextraction
    (DRCN 2024; it was also in `pool_C1.csv` with 4 links, so its found_via merges the C1 pool row and the
    manual link, link_count = 5; the coordinator should dedupe against the C1 output);
  - runners-up: Gemayel & Mokh (ICC Workshops 2025), Yu et al. (IWCMC 2025), Rodriguez-Navas et al. (FNWF 2024);
  - noted but not added: ETSI GR ENI 055 V4.1.1 ("AI agents based core network"). This is a standards report
    that `verify.py` cannot check from a DOI, so it is left for the coordinator or the gap check to add as a
    `standard` row.
  - Other core-adjacent items were not added: Mekrache DMO-GPT/OSS-GPT (E2E/OSS rather than core), Kukliński
    "MLOps as a service" (NetSoft 2025), Ameur "When MLOps meets NWDAF" (C1 territory) and Quadrini 2023 NWDAF
    data collection (C1). These are flagged for the C1 agent.
- **Kamran2025Energyexposure (doi:10.1109/comsnets63942.2025.10885745).** Not recoverable. Semantic Scholar
  shows the publisher elided the 25 references. IEEE Xplore returns an error page to both WebFetch and curl.
  There is no arXiv version, and a web search found none. Only its 2 forward citations were usable. One of them,
  the NOMS 2026 EIF demo, was selected. The other is a green-RAN survey (RAN, dropped).

## Borderline inclusions
- **Chen2026Feasibilityshield (EuCNC/6G Summit 2026)** was **not found by snowballing**. It appeared in a Crossref
  title search run while resolving the DOI of the Ameur reference "A-Core". It is included because it is directly
  about an agentic self-healing 6G core that pre-validates candidate actions by lookahead simulation. That bears
  on gap claims P2 and G3. found_via says this honestly and link_count = 0. The coordinator may move it to the
  gap-check evidence instead.
- **Two seminal pre-2020 works (the cap):** Alawe2018Corescaling (IEEE Network, 5 links, ~236 citations) and
  Alawe2018Rnnscaling (GLOBECOM 2018, 3 links). Both are the origin of forecast-driven 5G-core scaling, which most
  C4 autoscaling papers cite. Alternatives not proposed: "On the scalability of 5G core network: the AMF case"
  (CCNC 2018, 1 link) and "An efficient and lightweight load forecasting for proactive scaling" (CSCN 2018, 1 link).
- **Subramanya2021Fedautoscaling (TNSM)** is MEC VNF autoscaling rather than 5GC NFs (relevance 2). It is kept for
  its 2 links (Coronado + Zanzi seeds), its operator dataset and its federated angle.
- **Sheoran2021Coreprovisioning (IEEE Internet Computing)** is a magazine-style but peer-reviewed article. It is
  recorded as a journal.
- **Hirayama2025Multiaiclosedloop (NOMS 2025, KDDI)** has an abstract with no numbers. It is kept as relevance 2
  because it links to the Kawasaki2023 seed and is an operator-lab closed loop over CNFs.
- **Kourtis2026Typesafeagents** is a 2026 arXiv preprint (allowed under PROTOCOL.md §3). It is kept because it is one
  of the very few works that measures wrong-action rates and decision latency of agentic 5G-core control.
- **Tufeanu2026Residualartifact (TNSM 2026)** was placed in S2 (cloud-native core platform automation) with
  S5/S4 secondary. It could equally sit in C3.

## Exclusions worth recording
- arXiv-only works older than 2025 were dropped: "Designing, Developing, and Validating Network Intelligence for
  Scaling in SBA based on DRL" (arXiv:2405.04441; no published version found on Crossref or arXiv journal_ref)
  and the 2023-2024 LLM-6G arXiv items.
- "LLM-Enabled NWDAF" (arXiv:2606.11877, 3 links) is left to the C1 agent, because it is also in the C1 pool and
  is primarily an NWDAF work.
- "Autonomous conflict handling in intent-based management" (Computer Networks 2025, Ericsson) and DETROIT
  (Computer Networks 2025) have no abstract in Crossref or S2, and ScienceDirect returned 403. Without an abstract
  they could not be characterised in my own words, so they are runners-up.
- "Intent-Based 6G Management with Generative AI" (NetSoft 2026, 3 links) is a PhD-symposium overview. It was
  dropped as low evidence despite its links.
- Most of the Coronado2022Zerotouch backward references (RAN slicing, MEC offloading, caching, SDN/WLAN programming,
  6G vision papers, security) and its forward citations (IoV, UAV, O-RAN xApps, security, SD-WAN, positioning)
  were dropped as not about the core.
- Venue doubt: several 2026 forward citations come from low-visibility venues (IJCESEN, "Iconic research and
  engineering", MENA conferences). All were dropped.
