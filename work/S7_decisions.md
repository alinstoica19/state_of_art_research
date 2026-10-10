# S7 Energy efficiency of the core: decisions

## Search queries run
Crossref (`verify.py search`): "energy efficient 5G core network function placement"; "energy-aware virtual network function placement survey";
"energy efficiency network function virtualization survey"; "green 6G survey energy efficiency"; "energy-aware VNF placement deep reinforcement learning";
"user plane function energy consumption measurement"; "energy consumption cloud-native 5G core measurement"; "VNF consolidation power consumption";
"energy efficient network slicing 5G core"; "AI models for green communications towards 6G"; "survey 5G radio access network energy efficiency ...";
"measurement-based approach power consumption softwarized 5G core"; "energy-aware network function selection 5G core"; "energy efficient UPF placement 5G";
"green network function virtualization survey energy"; "sustainable 6G networks survey energy"; "carbon-aware network management";
"power consumption model virtual network functions containers"; "energy consumption Kubernetes network functions Kepler";
"energy efficiency virtual network function placement survey taxonomy"; "energy-efficient network slicing survey"; "net zero 6G energy sustainability survey";
"energy-efficient service function chain placement reinforcement learning 5G"; "energy saving NWDAF analytics 5G core"; "energy-aware autoscaling 5G core network functions";
"green network slicing energy efficiency AI 6G"; "energy efficient 6G core network architecture"; "energy consumption open source 5G core Open5GS free5GC";
"sustainability 6G network management carbon footprint"; "Kamran Jha Chaporkar energy aware 5G"; "energy information exposure 5G system energy credit";
"energy as service criteria 5G subscription policy"; "renewable energy aware 5G core network"; "energy aware user plane path selection 5G";
"power consumption 5G core deployment containers virtual machines bare metal"; "energy efficient microservices placement 5G core service based architecture";
"carbon-aware routing software-defined networks carbon intensity"; "carbon-aware placement virtual network functions renewable";
"carbon emission aware edge network function placement 5G"; "energy efficient 5G core network sleep mode network functions";
"Kepler energy measurement cloud-native network functions 5G testbed"; "Bellin Granelli power consumption 5G core"; "digital twin energy saving 5G network optimization";
"intent-based energy saving network management 5G".
WebSearch: 5G core NF power measurement (UPF/AMF); green/energy-aware 6G surveys (COMST); 3GPP Rel-19 energy-as-service-criteria TR number;
energy-aware VNF placement surveys; energy-aware 5GC placement with RL; titles of individual papers to read abstracts.
Abstracts were read from OpenAlex, Semantic Scholar, arXiv and repository pages (riuma.uma.es for HADES).

## Judgement calls
- **The RAN dominates the energy literature.** Most "5G energy efficiency" hits are about sleep modes, massive MIMO, or O-RAN DU/RU energy. RAN-only papers are kept out. The one exception is the López-Pérez et al. COMST 2022 survey, kept as the reference energy survey with relevance 1.
- **Core-specific energy work is thin and recent (2023-2026).** It comes from a few groups and is almost all UPF-centric: measurement (Bellin/Granelli/Munaretto, Trento), UPF selection (DRL), UPF switching (LSTM), and UPF placement (DeMPUP, Goshi et al., Ziazet/Jaumard). No peer-reviewed paper was found on energy-aware *control-plane* NF (AMF/SMF/NRF) consolidation or selection.
- **Relevance 3** goes to works on 5GC NFs (mainly UPF) with optimisation or AI, the 5GC power-measurement journal paper, and the 3GPP-energy-exposure review. Generic VNF/CNF energy placement and cloud autoscaling get **relevance 2** (transferable methods).
- **Bellin et al. measurement work exists twice.** The Computer Networks 2024 journal version (10.1016/j.comnet.2024.110312) is kept. The NetSoft 2023 "A Preliminary Study on the Power Consumption of Virtualized Edge 5G Core Networks" (10.1109/netsoft57336.2023.10175489) is dropped as its preliminary conference version. arXiv 2502.13879 is the same paper and resolves to the journal DOI.
- **Ziazet & Jaumard.** The TNSM 2026 journal paper is kept. The FNWF 2023 "Placement of Logical Functionalities in 5G/B5G Networks" (10.1109/fnwf58287.2023.10520419) is the earlier conference version and is not included. The CCECE 2026 follow-up was not included either (no abstract available).
- **Correia et al. (WCNPS 2025)** is a small workshop venue. It is kept at relevance 2 because 5GC power measurements are rare.
- **Energy-Aware 6G Network Design: A Survey** (arXiv 2509.11289, 2025) is kept as a `preprint`. No published version was found.
- **Kamran/Jha/Chaporkar group (IIT Bombay).** The COMSNETS 2025 review of 3GPP energy information collection and exposure is kept (rel. 3, survey). Their COMSNETS 2024 "Green 6G: Energy Awareness in Design" (10.1109/comsnets59351.2024.10427334) was left out as overlapping; it can be added if more standards-oriented coverage is wanted.
- **6GNet 2025 demo** (energy/carbon of a DRL agent) is kept and flagged `demo`. It is the only peer-reviewed item found on the energy cost of the AI control loop itself, which matters for an AI-native core.
- **Rejected:**
  - NOMS 2026 "Network Management and Configuration Models for Reducing the Internet's Carbon Footprint": a PhD-symposium summary (thesis-like).
  - JNCA 2026 "Intelligent Load-Aware gNB Optimization for Energy Saving in 5G via NWDAF-Orchestrated Agent Framework" (10.1016/j.jnca.2026.104482): highly relevant title (NWDAF plus energy), but the abstract could not be read anywhere (ScienceDirect 403, no OpenAlex/S2 abstract). Worth adding manually after reading.
  - Computing 2025 "Energy-efficient and SLA-aware VNF placement using predictive auto-scaling": no abstract readable.
  - FGCS 2021 Mai et al.: no abstract readable.
  - IEEE Access 2019 "Optimized Energy Aware 5G NFV": pre-2020, not seminal enough.
  - Renewable & Sustainable Energy Reviews 2022 "energy use implications of 5G": whole-network LCA review, background only. Can be added as rel-1 context.
  - arXiv 2107.05991 (2021 preprint, outside the 2025-2026 preprint rule).
  - arXiv 2608.24841 (O-RAN CU-UP placement, RAN).
  - TechRxiv, SSRN and Preprints.org posted-content items.
  - IFIP Networking 2021 Mu et al. and WCNC 2024 Sasan et al.: valid but generic; dropped to keep the list focused. Both are easy re-adds.
- **Carbon-aware network management.** Almost nothing peer-reviewed on 5G/6G cores was found. This is recorded as a gap, not filled with off-topic items.
- **Standards (4).** The 3GPP portal IDs were found by probing `verify.py spec3gpp`. The version and Release of each were read from the 3GPP FTP archive listings.

  | Spec | Portal id | Version cited |
  |---|---|---|
  | TS 28.310 | 3550 | V20.1.0, Rel-20, 2026-09 (Rel-19 V19.3.0 also exists, 2026-01) |
  | TR 23.700-66 | 4208 | V19.0.0, Rel-19, 2024-09; SA2 study behind the EnergySys WI |
  | TR 28.880 | 4259 | V19.0.0, Rel-19, 2025-01 |
  | TR 22.882 | 4096 | V19.3.0, Rel-19, 2024-04 |

  Other related specs seen but not included:

  | Spec | Portal id | Title |
  |---|---|---|
  | TR 22.883 | 4308 | Energy efficiency as service criteria phase 2 |
  | TR 28.813 | 3743 | Rel-17 SA5 EE study |
  | TR 33.766 | 4297 | Security aspects of energy saving |

  ETSI ES 203 228 / NFV-EVE were not added, to keep within about 4 standards. The TR 23.700-66 summary of KI#2 scoping comes from third-party mirrors and should be checked against the TR text.
- **AGORA (IEEE Access 2026, 10.1109/access.2026.3672699)** was added at the orchestrator's suggestion (found by S6). I verified it and read its abstract via OpenAlex/S2. It is relevance 3 with secondary S6, since an LLM agent steers the UPF for energy saving. It is the only agentic-AI or intent-driven energy work on the core found. Its arXiv version is 2602.13290.
- (orchestrator) AGORA was handed over by S6 and added by the S7 agent; a duplicate row added by the orchestrator was removed.
