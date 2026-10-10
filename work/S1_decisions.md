# S1 — Network analytics in the 5G core: decisions

## Search queries run
Crossref (`verify.py search`): "network data analytics function NWDAF"; "NWDAF survey 5G network analytics";
"network data analytics function machine learning 5G core"; "NWDAF federated learning"; "management data analytics MDA 3GPP";
"NWDAF anomaly detection"; "NWDAF load prediction network function"; "5G core network analytics survey AI";
"NWDAF open source testbed free5GC"; "analytics function 6G network intelligence NWDAF"; "survey network data analytics 5G 6G closed loop NWDAF MDA";
"management data analytics function 5G network automation"; "NWDAF QoS sustainability prediction"; "NWDAF network slice analytics machine learning";
"MTLF AnLF model training NWDAF"; "NWDAF explainable AI"; "data collection coordination function DCCF analytics"; "NWDAF user equipment mobility prediction";
"network analytics 5G core open5GS machine learning"; "model drift detection adaptation 5G core networks"; "model drift in dynamic networks";
"NWDAF implementation open-source 5G core MLflow"; "open-source NWDAF event-driven analytics"; "network data analytics 5G systems beyond survey";
"Mekrache Ksentini NWDAF"; "NWDAF large language model"; "NWDAF digital twin"; "privacy preserving analytics 5G core federated NWDAF vertical";
"artificial intelligence 3GPP 5G-Advanced survey"; "network analytics 5G core Kubernetes autoscaling prediction NWDAF"; "NWDAF network slicing load analytics deep learning";
"analytics driven network slice management 5G machine learning admission"; "zero-touch network slicing analytics NWDAF closed loop"; "NWDAF abnormal behaviour UE analytics";
"distributed analytics 5G core hierarchical NWDAF edge"; "UE communication analytics NWDAF traffic classification"; "AI as a service NWDAF 6G"; "NWDAF security analytics";
"MDAF management data analytics function"; "management data analytics service 3GPP"; "NWDAF MDA network automation 6G AI native architecture"; "intent LLM agent NWDAF";
"NWDAF graph neural network"; "NWDAF reinforcement learning core network function"; "NWDAF QoS prediction vehicle V2X".
WebSearch: NWDAF surveys in IEEE Access/COMST; NWDAF journal articles 2024-2025; Manias/Chouman/Shami NWDAF drift; MDA TS 28.104 papers; 3GPP spec IDs for
TS 28.104 and TR 23.700-84; Agentic-NWDAF abstract; PreQoS (Barmpounakis) NWDAF link. Abstracts read via OpenAlex abstract index / arXiv / EURECOM listings.

## Judgement calls
- **No journal-grade NWDAF survey exists.** Searches of IEEE Access / COMST / Computer Networks returned none. Surveys kept: García-Martín et al. (IEEE Network 2024,
  standards tutorial), Romero & Suyama (SBrT 2025, 70+ article review; arXiv 2506.04860 resolved to its published DOI), Niu et al. (ICCC Workshops 2022, Rel-18 NWDAF
  management). This absence is itself a gap the survey article can fill.
- **Rejected surveys:** "NWDAF in 3GPP 5G Advanced: A Survey" (EIECS 2023, 10.1109/eiecs59936.2023.10435433) and "NWDAF in 5G: Architecture, Use Cases, and
  Evolution Across 3GPP Releases" (NCC 2025, 10.1109/ncc63735.2025.10983338) — minor venues overlapping the IEEE Network tutorial; listed here as optional extras.
  "Machine Learning in FCAPS" (COMST 2024, Mekrache/Ksentini) is about machine reasoning in FCAPS rather than core analytics — left to S6.
- **Sevgican et al. JCN 2020** kept (in range, 134 cites) and flagged `seminal;tutorial` because it is the de facto reference for ML inside NWDAF, despite synthetic data.
- **Majumdar et al. (IEEE Commun. Standards Mag. 2026)** kept as relevance 3 (AI-overlay vs native AI in 6G core); not flagged survey (position/vision piece).
- **Conference vs journal duplicates:**
  - Shafiei Ardestani/Saha/Limam/Boutaba: NOMS 2026 "Towards NWDAF-enabled Analytics and Closed-Loop Automation in 5G Networks" (10.1109/NOMS69089.2026.11668240,
    also arXiv 2505.06789) vs ITU J-FET 2026 "Towards zero-touch network orchestration..." (10.52953/svmm1934). Kept the journal version.
  - Manias/Chouman/Shami: MeditCom 2022 "A Model Drift Detection and Adaptation Framework for 5G Core Networks" vs IEEE Commun. Mag. 2023 "Model Drift in Dynamic
    Networks". Kept the magazine/journal version; MeditCom mentioned in critique.
- **Preprint:** arXiv 2601.01838 (Daniel et al., open-source free5GC NWDAF, Jan 2026) kept as `preprint`; web search hinted an IFIP venue but no DOI was found.
- **Standards:** TS 23.288 cited as V19.8.0 (2026-09, Rel-19; portal id 3579); TS 28.104 as V19.3.0 (2025-09, Rel-19; id 3877); TR 23.700-84 V19.0.0 (2024-12;
  id 4252, portal title confirmed with `verify.py spec3gpp 4252`). TS 29.520 (id 3355) verified but not included to keep standards ≤ 3-4.
- **TR 23.700-84 lands in unverified only because of a tool bug:** `build` strips non-[0-9.] characters from the spec number ("23.700-84" -> "23.70084") so it
  never matches the portal's "23.700-84". The portal page (specificationId=4252) does show the right number and title. Fix: keep '-' in the regex at
  tools/verify.py line ~277 (`[^0-9.\-]`), then rebuild.
- **Excluded borderline items:** many 2023-2026 NWDAF papers in minor venues (ICTC, ISNCC, ICASI, ICCT, CITS, ICACT, APNOMS 2021/2022, free5GC World Forum, ICCCN 2026,
  IWCMC 2026 VFL, TrustCom 2025) — low citation and/or very short; Ben Saad (Security & Privacy 2024, D-NWDAF poisoning/XAI) — niche; IntAgent (ICC 2026) — overlaps
  Agentic-NWDAF (kept Agentic-NWDAF, both are LLM+MCP over NWDAF; IntAgent 10.1109/icc59461.2026.11587323 is a good alternate); OpenDaisy distributed MTLF (ICC Wkshps
  2026) — no abstract available to characterise; Barmpounakis PreQoS (Computer Networks 2022) — V2X predictive QoS but NWDAF link not confirmed; ResearchSquare /
  TechRxiv / SSRN items (e.g., "LLM-Enabled NWDAF") excluded as non-peer-reviewed posted content; retracted INCOFT 2022 paper excluded.
- **MDA (TS 28.104) has almost no academic literature**: Crossref/web searches found only one Springer CCIS chapter on MDAF slice scalability (2022) — not included.
- Fair-FL TITS 2025 paper kept despite non-networking venue because it is one of the few journal-level NWDAF-FL works (32 cites).
