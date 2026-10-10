# C4+C5 snowball report (Phase 2: select and verify)

## Counts
| Step | Count |
|---|---|
| Pool `pool_C45.csv` | 440 |
| Screened by title | 440 (all rows) |
| Abstracts read (pool) | ~45 |
| Extra candidates screened from the hand-recovered Ameur2026Agenticsurvey reference list | 177 items by title, ~10 read in detail (abstracts via S2) |
| Dropped as pre-2020 (not seminal) | ~165 (approximate) |
| Dropped as wrong type (standards fragments, bios, product names, white papers, theses, arXiv-only before 2025) | ~40 (approximate) |
| Dropped as off-topic (RAN, MEC offloading, IoT/IoV/UAV, security, generic SDN/WLAN, 6G vision) | ~215 (approximate) |
| Already in `ALL_CANDIDATES.csv` (title re-check) | 0 in the pool; several Ameur references (e.g. Mekrache2024Llmintent, Manias2024Semanticrouting, Barbosa2026Agentxgcore) |
| **Selected** | **15** (C4: 6, C5: 9) |
| **Verified** | **15** (14 via Crossref DOI, 1 via the arXiv API); 0 unverified |

Output: `work/SB_C45.jsonl`, `results/SB_C45_snowball_c45.csv`, `.bib`; `results/SB_C45_unverified.csv` is empty.

## Selected works (ranked by link_count, then relevance)
| id | year | links | cat |
|---|---|---|---|
| Alawe2018Corescaling (seminal) | 2018 | 5 | C4 |
| Manias2024Intentextraction | 2024 | 5 | C5 |
| Alawe2018Rnnscaling (seminal) | 2018 | 3 | C4 |
| Tufeanu2026Residualartifact | 2026 | 3 | C4 |
| ElRajab2024Ztnsurvey (survey) | 2024 | 3 | C5 |
| Subramanya2021Fedautoscaling | 2021 | 2 | C4 |
| Hirayama2025Multiaiclosedloop | 2025 | 2 | C5 |
| Sheoran2021Coreprovisioning | 2021 | 1 | C4 |
| Tonini2026Eifenergy | 2026 | 1 | C4 (energy) |
| Li2025Agenticcore | 2025 | 1 (manual) | C5 |
| Tong2025Acore | 2025 | 1 (manual) | C5 |
| Ta2026Agenticgitops | 2026 | 1 | C5 |
| Kourtis2026Typesafeagents (preprint) | 2026 | 1 | C5 |
| Gharbaoui2026Intentconflictsurvey (survey) | 2026 | 1 | C5 |
| Chen2026Feasibilityshield | 2026 | 0 (incidental, not snowball) | C5 / gap evidence |

## Runners-up (not selected), ranked
1. Network Function Orchestration with LLM based Multi-Agent System (ICC Workshops 2025): 10.1109/iccworkshops67674.2025.11162489
2. NFVAgent: A Retrieval-Augmented LLM Agent for Resilient NFV Failure Recovery (CNSM 2025): 10.23919/cnsm67658.2025.11297536
3. Autonomous conflict handling in intent-based management (Computer Networks 2025): 10.1016/j.comnet.2025.111561 (no abstract retrievable)
4. AI Agent Based Autonomous Cognitive Architecture for 6G Core Network (IWCMC 2025): 10.1109/iwcmc65282.2025.11059600
5. Leveraging LLM for Evolving and Declarative Trace Analytics towards Next Generation Mobile Core Networks (FNWF 2024): 10.1109/fnwf63303.2024.11028833
6. Research on AI Agent for 6G Core Network: 3GPP Standardization Progress (Global 6G 2026): 10.1109/global6g69473.2026.11566946 (incidental)
7. Assured AI-Native Network Control Loops: State of the Art, Research Challenges and the Missing Runtime Assurance Layer (arXiv:2609.11996)
8. DETROIT: Decomposition techniques for a hierarchy of 6G network intent management functions (Computer Networks 2025): 10.1016/j.comnet.2025.111657
9. AI For Core Network in 6G (ISAS 2025): 10.1109/isas66241.2025.11101846
10. LLM-Enabled NWDAF: A Step Toward AI-Native 6G Network Intelligence (arXiv:2606.11877, 3 links; left to C1)

Standard noted for the coordinator: ETSI GR ENI 055 V4.1.1, *Use cases and requirements for AI agents based core
network* (cited by Ameur2026Agenticsurvey).

## Taxonomy categories strengthened
- **C4:**
  - forecast-driven core scaling: the two seminal Alawe papers, Sheoran and Subramanya;
  - cloud-native core platform automation: Tufeanu;
  - the first 3GPP-aligned EIF energy-exposure prototype: Tonini.
- **C5:**
  - the industrial agentic-core architectures (Huawei: Li2025Agenticcore, Tong2025Acore), which are the
    reference designs the survey must position against;
  - intent extraction for the 5GC (Manias);
  - agentic actuation through GitOps/MCP (Ta);
  - safety and guard-rail evidence (Kourtis, Chen);
  - loop and intent conflict assurance (Gharbaoui);
  - a ZSM survey (El Rajab).

## Evidence touching the gap claims (SUMMARY.md §4)
- **G5 (agentic operations lack safety evidence): partially weakened.**
  - Kourtis2026Typesafeagents (preprint) measures wrong-action rates under changed questions and the latency
    cost (11-29 times slower) of typed agent decisions on an Open5GS policy loop, with an act/escalate/abstain gate.
  - Chen2026Feasibilityshield adds a deterministic feasibility shield (a guard-rail).
  - Ta2026Agenticgitops reports a 78% success rate.
  - Suggested rewording: "few works quantify..." rather than "no work quantifies...".
- **P2 (testing whether a remedy can help before applying it): partially covered.**
  - Chen2026Feasibilityshield validates LLM-proposed remediation actions by short-horizon lookahead simulation
    in a 3GPP-compliant 6G core simulator before execution.
  - Its faults are link failures with a no-action baseline. It does not address the case where rerouting cannot
    help because a shared back-end is degraded, and it has no NF or database failover.
  - The gap-check agent should cite it.
- **G3 (control-plane twins; predicting action outcomes):** Chen2026's "cognitive digital twin" is a core-level
  lookahead model, but twin fidelity is not measured and it is simulator-only. G3 still mostly holds.
- **G6 (energy exposure unimplemented): partially weakened.** Tonini2026Eifenergy implements the Rel-19 EIF on
  OAI and exposes per-UE energy to an AF. It does not cover control-plane NF energy or energy-aware NF selection,
  so that part of G6 holds.
- **G4 (loop conflicts):** Gharbaoui2026 is a survey of IBN assurance and conflict detection. The Ericsson
  Computer Networks 2025 runner-up handles intent conflicts autonomously. Neither addresses agent-driven core
  loops, so G4 holds for agentic loops.
- **G2 (analytics wired to NRF/SCP or TS 23.527 restoration), G7 (geo-redundancy, UDR/UDSF failover), P1 (SCP
  telemetry), P3 (procedure-level UE models under faults), P4 (multi-site multi-action remedies):** nothing found
  in this pool. Hirayama2025 (KDDI) runs closed loops reacting to predicted CNF failures, but without standard
  restoration or NRF/SCP actuation.

## Research groups not listed in SUMMARY.md §5
- **Huawei (Wen Tong, Xu Li, Chenghui Peng):** the Agentic-AI Core and A-Core.
- **NCSR Demokritos (Kourtis, Xilouris):** typed agentic 5G control.
- **University of Bologna / CNIT (Cerroni, Tonini, Borsatti) with Huawei Munich (Trivisonno, Poe):** EIF energy
  exposure.
- **Soongsil University (Younghan Kim):** Agentic GitOps for cloud-native 5G.
- **CNIT / Scuola Superiore Sant'Anna Pisa (Martini, Castoldi, Gharbaoui):** intent assurance and conflicts.
- **University Politehnica of Bucharest (Vochin, Tufeanu) with University of Agder (Frank Y. Li):** Kubernetes
  SBA hygiene.
- **NTUST Taiwan (Jenq-Shiou Leu):** feasibility-shielded self-healing core.
- **Purdue / HPE (Fahmy, Sheoran, Sharma):** AI-driven core provisioning.
- **KDDI (Kawasaki, Hirayama):** already known via the Kawasaki2023 seed; NOMS 2025 closed loop.
- **Orange Labs / Ksentini (Alawe, Bertin):** the 2018 scaling origin, an early EURECOM link.
- **Ericsson Research (Orlic, D'Angelo, Kattepur):** intent conflicts and decomposition (runners-up).
