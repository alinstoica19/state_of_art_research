# C2 report: network modelling and digital twins (snowball Phase 2)

## Counts
| Step | Count |
|---|---|
| Pool size (`pool_C2.csv`) | 185 |
| Screened by title | 185 (all) |
| Abstracts read | ~60. These are all plausibly relevant rows plus borderline ones, at 700-2200 characters each, with a few extra abstracts fetched from Semantic Scholar or OpenAlex (rows 73, 5G3E, COREX refs). |
| Dropped as off-topic | ~115, approximate (generic IoT/robotics/security/RAN DT, generic ML, simulators, unrelated fields) |
| Dropped as pre-2020 and not seminal | ~40, approximate (rows 138-177 overlap with the off-topic count) |
| Dropped as wrong type | ~12 (white paper, patent, press release, book or chapter, ISO standard, arXiv-only before 2025, duplicate arXiv version) |
| Deferred to C1 (C1-type works, also in pool_C1) | 3 (rows 0, 1, 3) + Chouman TNSM 2024 testbed (COREX backward-manual link) |
| Candidates added by hand from seed reference lists | 3 (COREX via Crossref refs: 5G3E dataset, Chouman testbed, Aykurt GNN plan); Costa and Zanzi references added nothing new |
| **Selected** | **14** |
| **Verified** (Crossref, `results/SB_C2_snowball_c2.csv`) | **14** (0 unverified) |

## Selected works (ranked by link_count, then relevance)
| id | title | year | link | rel |
|---|---|---|---|---|
| Nguyen2021Dt5Gbeyond | Digital Twin for 5G and Beyond (IEEE ComMag) | 2021 | 4 | 2 |
| SanzRodrigo2023Mndtmethodology | Digital Twins for 5G Networks: A Modeling and Deployment Methodology (IEEE Access) | 2023 | 2 | 3 |
| Araujo2026Scope5G | SCOPE-5G: standards-aligned synthetic AMF observability dataset (IEEE Access) | 2026 | 2 | 3 |
| Tran2025Ndt6Gsurvey | Network Digital Twin for 6G and Beyond: end-to-end multi-domain view (IEEE OJ-COMS) | 2025 | 2 | 3 |
| Dede2025Ai6Gcore | AI For Core Network in 6G (ISAS 2025) | 2025 | 2 | 3 |
| Mozo2022B5Geminijournal | B5GEMINI: AI-Driven Network Digital Twin (Sensors) | 2022 | 1 | 3 |
| Karamchandani2024B5Geminindt | Design of an AI-driven NDT for advanced 5G-6G network management (NOMS 2024) | 2024 | 1 | 3 |
| Petrik2025Dtdomaintransfer | DT for 5G and Beyond: domain transfer and behaviour classification (ELMAR 2025) | 2025 | 1 | 3 |
| Isah2026Kgfailureloc | Knowledge-graph propagation for failure localisation in 5G core networks (ICUFN 2026) | 2026 | 1 | 3 |
| VillotaJacome2022Coreslicingadmission | Admission Control for 5G Core Network Slicing based on DRL (IEEE Systems J.) | 2022 | 1 | 3 |
| Tao2025Dtonlinedrl | DT-accelerated online DRL for admission control in sliced networks (IEEE TCOM) | 2025 | 1 | 2 |
| Yu2023Dtselfhealing | DT-driven service self-healing with GNNs in 6G edge networks (IEEE JSAC) | 2023 | 1 | 2 |
| Nardini2024Simu5Gdt | Enabling simulation services for digital twins of 5G/B5G mobile networks (Computer Communications) | 2024 | 1 | 2 |
| Sengendo2024Ndtsync | Building Network Digital Twins Part I: State Synchronization (6GNet 2024) | 2024 | 1 | 2 |

## Runners-up (not selected, ranked)
1. Providing Heterogeneous Signaling and User Traffic for 5G Core Network Functional Testing (IEEE Access 2023), 10.1109/access.2022.3233412
2. An Open Dataset for Beyond-5G Data-driven Network Automation Experiments (5G3E) (6GNet 2022), 10.1109/6gnet54646.2022.9830292 (COREX backward-manual)
3. Centralized and Federated Learning for Predictive VNF Autoscaling in Multi-Domain 5G Networks and Beyond (TNSM 2021), 10.1109/tnsm.2021.3050955
4. 6G Digital Twin Networks: From Theory to Practice (IEEE ComMag 2023), 10.1109/mcom.001.2200830
5. Generative AI-Driven Digital Twin for Mobile Networks (IEEE Network 2024), 10.1109/mnet.2024.3420702
6. Lightweight Trace-Driven Burst Traffic Generation for 5G Network Digital Twins (NetSoft 2026), 10.1109/netsoft70012.2026.11603454
7. A Survey on Digital Twin Networks: Architecture, Technologies, Applications, and Open Issues (IEEE IoT-J 2025), 10.1109/jiot.2025.3565265
8. Real-Time Network Digital Twin: Experimental Setup for Proof of Concept (IEEE Wireless Commun. 2025), 10.1109/mwc.001.2400462
9. Towards Efficient Mobility Management in 5G-Advanced: A Predictive Model for Network Slice Availability (ACM SAC 2025), 10.1145/3672608.3707836
10. Digital Twin Network-Based 6G Self-Evolution (Sensors 2025), 10.3390/s25113543

Deferred to C1 (strong, and the coordinator should make sure at least one is selected): *Towards NWDAF-enabled Analytics and Closed-Loop
Automation in 5G Networks* (NOMS 2026, 10.1109/noms69089.2026.11668240, link 6); *NWDAF in 5G: Architecture, Use
Cases, and Evolution Across 3GPP Releases* (NCC 2025, link 5); *Data Collection Using NWDAF ... with Real Traffic*
(ISNCC 2023, link 3); Chouman et al. TNSM 2024 testbed (link 2 in pool_C1, 3 with the COREX manual link).

## Taxonomy categories strengthened
- **C2 (main):** 5G-core twins (B5GEMINI journal and NOMS 2024 papers, the MNDT methodology, the Open5GS twin with domain transfer), what-if
  simulation services (Simu5G branching analysis), twin synchronisation, twin-assisted RL (DT-accelerated online
  DRL), a GNN-twin self-healing loop, and two surveys (OJ-COMS NDT, ComMag DT for 5G).
- **C3:** SCOPE-5G (benchmark dataset for AMF anomaly detection) and knowledge-graph failure localisation on real 5GC telemetry.
- **C4:** 5G core slice admission control with RL (the baseline lineage of the Wang2024 seed).
- **Positioning:** two more surveys/reviews to position against (Tran2025 NDT survey; Dede2025 AI for the 6G core).

## Evidence on the gap claims (SUMMARY.md §4)
- **G3 (control-plane twins and fidelity):** the claim **largely holds**, with nuances.
  - *Petrik2025* reports a large accuracy loss when models trained on an Open5GS twin meet real traffic. This is empirical sim-to-real evidence, but it measures ML transfer, not the fidelity of the twin itself.
  - *Sengendo2024* treats synchronisation delay as a twin-quality concern, which is a proxy for fidelity.
  - *Araujo2026 (SCOPE-5G)* validates synthetic AMF data statistically against public references. This is the closest thing to a fidelity metric, but it applies to a dataset generator, not to a live twin.
  - None of these predicts the outcome of a candidate action at control-plane speed.
- **What-if / pre-validating remediation (P2):** two works come close.
  - *Nardini2024* defines lockstep and branching what-if analysis in a simulation-based twin to anticipate faults and reconfigurations, but it is RAN-oriented.
  - *Yu2023* uses a GNN twin to evaluate service redeployment away from abnormal nodes. This is pre-validation of a remediation, but at the edge or IP level, not for core NFs.
  - Together they show the *idea* exists outside the core. The P2 claim should be worded as "not done for core control-plane remedies".
- **Twin-assisted safe RL:** *Tao2025* uses a twin to give online DRL a safe starting policy (from the same group as the Tao2024 seed). It adds to Li2024Saferl.
- **G2 (analytics wired to NRF/SCP or TS 23.527), G7 / P4 (geo-redundancy, UDR/UDSF failover, multi-site multi-action remedies), P1 (SCP telemetry), P3 (procedure-level UE models under faults):**
  **no evidence found** in the C2 pool.
  - SCOPE-5G models AMF *procedures* as aggregate counters at 15-minute granularity, not UE-level timer outcomes. It therefore does not weaken P3.
  - The COREX and Zanzi reference lists contain nothing on failover or SCP.
- **Gap 8 (no public 5GC benchmarks):** this claim is **slightly weakened**.
  - SCOPE-5G (2026) releases an open, TS 28.552-aligned synthetic AMF dataset with labelled anomalies.
  - 5G3E (2022, runner-up) releases emulation time series that include core NF metrics.
  - The claim should become "no public *operator-grade* 5GC fault benchmarks".

## Research groups not in SUMMARY.md §5
- **UPM / Telefónica (Madrid)**: Mozo, Moreno, Sanz, Karamchandani, Pastor, D. R. López. B5GEMINI 5G-core NDT (3 works).
- **Southeast University (Nanjing)**: Zhenyu Tao, Wei Xu, Xiaohu You. 5GC control-plane modelling (seed) and twin-accelerated DRL.
- **University of Pisa**: Nardini, Stea. Simu5G as a twin with what-if services.
- **Middlesex University London**: H. X. Nguyen, R. Trestian. Early DT-for-5G vision (422 citations).
- **UNICAMP / UFABC (Brazil)**: Villota-Jacome, Caicedo, da Fonseca (core slicing admission); Kamienski, Bianchi (SCOPE-5G).
- **BUPT**: Peng Yu, Wenjing Li, Lei Feng. GNN twin for self-healing.
- **Chonnam National University**: Jinsul Kim's group. 5GC failure localisation.
- **University of the West of Scotland**: Alcaraz-Calero, Salva-Garcia, Qi Wang (COREX seed). 5G/6G emulation twins and cyber ranges.
- **STU / Comenius, Bratislava**: Petrík, Ries. Open5GS twin with domain transfer.
