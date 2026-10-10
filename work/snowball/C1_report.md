# C1 report: Standardised network analytics and data pipelines (snowball Phase 2)

Outputs: `work/SB_C1.jsonl` → `results/SB_C1_snowball_c1.csv`, `results/SB_C1_snowball_c1.bib`,
`results/SB_C1_unverified.csv` (empty). Judgement calls: `work/snowball/C1_decisions.md`.

## Counts (approximate where marked ~)
| Step | Count |
|---|---|
| Pool size (`pool_C1.csv`) | 517 |
| Screened by title | 517 (all rows) |
| Abstracts read (cache, plus Crossref/OpenAlex/S2 lookups for 6 with no cached abstract) | ~110 |
| Dropped: pre-2020 (71 rows; 1 kept as `seminal`) | 70 |
| Dropped: wrong type (no DOI/arXiv: spec refs, URLs, white papers, bio fragments; ~53; plus 1 retraction notice) | ~54 |
| Dropped: off-topic on title (generic FL/privacy/IoT/vehicular/RAN/mmWave/vision surveys) | ~300 |
| Dropped after abstract (off-topic, thin, duplicate, unreadable abstract, or other category) | ~90 |
| Selected | 15 |
| Verified (Crossref) | 15 (0 unverified) |

There were no title duplicates with `ALL_CANDIDATES.csv` (fuzzy match). One pool row turned out to be the conference version
of a seed (NOMS 2026 → Ardestani2026Closedloop) and was dropped. Two first-choice works (SCOPE-5G, AnomalyTrack) were already
selected by the C2/C3 agents and were replaced to avoid duplicates.

## Selected and verified (ranked by link_count, then relevance)
| id | title | year | L | rel | sub |
|---|---|---|---|---|---|
| Alawe2018Trafficforecast | Improving Traffic Forecasting for 5G Core Network Scalability: A Machine Learning Approach (IEEE Network) — `seminal` | 2018 | 5 | 3 | S8 |
| Tiwari2025Nwdafevolution | NWDAF in 5G: Architecture, Use Cases, and Evolution Across 3GPP Releases (NCC) — `survey` | 2025 | 5 | 3 | S1 |
| Jeon2024Hierarchicalnwdaf | Hierarchical Network Data Analytics Framework for 6G Network Automation (IEEE Internet Computing) | 2024 | 4 | 3 | S1 |
| Chen2024Nfppdataset | Comparative Analysis of Time Series Prediction Algorithms on Multiple Network Function Data of NWDAF (IJDSN) | 2024 | 4 | 3 | S1 |
| Oliveira2024Analyticsframework | Anomaly Detection Employing a 5G Core Data Analytics Framework (CloudNet) | 2024 | 4 | 3 | S1 |
| Chouman2024E2Etestbed | A Modular, End-to-End Next-Generation Network Testbed (TNSM) | 2024 | 3* | 3 | S1 |
| Saha2025Monarch | Monarch: Monitoring Architecture for 5G and Beyond Network Slices (TNSM) | 2025 | 3 | 2 | S1 |
| Hasan2026Ddosclosedloop | From Detection to Policy: Calibrated and Explainable Closed-Loop DDoS Management in 5G/B5G Networks (TNSM) | 2026 | 2 | 3 | S4 |
| BarrosoFernandez2026Aiaasnwdaf | AI as a Service for Intelligent Mobile Networks: Extending NWDAFs (IEEE ComStdMag) | 2026 | 2 | 3 | S1 |
| Yin2026Vflnwdaf | Intelligence Enhancement of NWDAF on Vertical Federated Learning towards Next Generation Core Network (IWCMC) | 2026 | 2 | 3 | S1 |
| Hossain2024Collaborativelearning | A Decentralized Collaborative Learning Approach in 5G+ Core Networks (IEEE Network) | 2024 | 2 | 3 | S1 |
| Zhu2022Disasterbackup | Failure-Aware and Automated Disaster Backup in the 5G Core Network (CECCC) | 2022 | 2 | 3 | S5 |
| Ameur2025Driftdetection | Dual Self-Attention is What You Need for Model Drift Detection in 6G Networks (IEEE TMLCN) | 2025 | 2 | 2 | S1 |
| Kuo2026Distributedmtlf | A Feasibility Study Toward Trustworthy 3GPP NWDAF Closed-Loop Analytics via Distributed MTLF with OpenDaisy (ICC Wkshps) | 2026 | 1 | 3 | S1 |
| Jeong2021Mobilityprediction | Mobility Prediction for 5G Core Networks (IEEE ComStdMag) | 2021 | 1 | 3 | S1 |

\* 2 harvested links plus 1 manual backward link from BenllochCaballero2026Corex (found by the C2 agent).

## Runners-up (not selected), ranked
1. Rajabzadeh et al., *Reliable feedback-driven federated learning for distributed NWDAFs at the edge*, Computer Networks 2026, 10.1016/j.comnet.2025.111972. Journal version of the HPSR 2024 FDFL paper. No abstract was accessible, so **check by hand**; it is a strong candidate.
2. Habibi et al., *Unlocking O-RAN Potential: How Management Data Analytics Enhances SMO Capabilities?*, OJCOMS 2024, 10.1109/ojcoms.2024.3431286. One of the rare MDA (TS 28.104) works, but conceptual.
3. Rajabzadeh & Outtagarts, *Federated Learning for Distributed NWDAF Architecture*, ICIN 2023, 10.1109/icin56760.2023.10073493 (L=4, demo paper).
4. Mestoukirdi & Khanfouci, *Reliable Vertical Federated Learning in 5G Core Network Architecture*, arXiv 2505.15244 (2025 preprint; Rel-19 VFL with NWDAF reliability).
5. *A Machine Learning-Driven NWDAF Architecture For Intelligent 5G Core Networks*, free5GC@CCS 2025, 10.1145/3733814.3765498. Decoupled MTLF on free5GC, with NF-load forecasts driving the URR threshold, i.e. an analytics → SMF/UPF actuator.
6. *Leveraging NWDAF and Machine Learning for Data Collection, Resource Optimization, Security and Privacy in 6G Networks*, IEEE Access 2024, 10.1109/access.2024.3359992 (L=4, survey-style).
7. *Network Data Analytics Function for IBN-based Network Slice Lifecycle Management*, APNOMS 2021, 10.23919/apnoms52696.2021.9562662 (L=4).
8. Garg, Bag & Mitschele-Thiel, *Decentralized ML based Network Data Analytics for Cognitive Management of Mobile Communication Networks*, NOMS 2022, 10.1109/noms54207.2022.9789936.
9. *A machine learning approach to forecast 5G metrics in a commercial and operational 5G platform*, Computer Communications 2024, 10.1016/j.comcom.2024.107974 (L=3, commercial 5G data; journal version of the WONS 2024 paper).
10. *Securing FL-Enabled NWDAF in Private 5G Networks Against Hybrid Attacks*, IEEE TGCN 2026, 10.1109/tgcn.2026.3735240.

Also adjacent: *Cobra-5G* NWDAF session anomaly detection on Open5GS (ICCNS 2024, 10.1109/iccns62192.2024.10776531), and the
UC3M-independent *Beyond NWDAF Services* (CITS 2025, 10.1109/cits65975.2025.11099169).

## Taxonomy categories strengthened
- **C1** (main): the NWDAF architecture variants (hierarchical/leaf-root, distributed FL/split learning, VFL management,
  distributed MTLF under drift, AIaaS on NWDAF workers), data pipelines (Monarch), datasets (NWDAF-NFPP) and drift (DSA-AE).
- **C3**: Hasan2026 (calibrated NWDAF DDoS mitigation), Oliveira2024 (anomaly detection use case), Zhu2022 (NWDAF-triggered UDM
  failover).
- **C4**: Alawe2018 (forecast-driven core scaling, seminal).
- **C5**: Kuo2026 and Hasan2026 (closed-loop operation and action gating).
- **C2** (weakly): Chouman2024 testbed as an experimentation substrate.

## Evidence on the gap claims (SUMMARY.md §4 and PROTOCOL_SNOWBALL §5)
- **Gap 1 (standard analytics life cycle almost unused).** This is **weakened slightly but holds in substance**.
  - The MTLF/AnLF split is evaluated under drift with distributed training (Kuo2026). Earlier, Jeon2024 does the same with a hierarchical root/leaf split.
  - Rel-19 VFL among NWDAFs has a design-only paper (Yin2026) and a preprint (runner-up 4).
  - MDA has one conceptual SMO paper (Habibi2024) with no numbers.
  - DCCF/ADRF data collection is still absent; Monarch builds a non-3GPP pipeline.
  - Suggested rewording: "a handful of 2024-26 workshop/short papers touch MTLF/AnLF, FL and VFL; none evaluates DCCF/ADRF/MFAF or MDA quantitatively".
- **G2 (analytics not wired to standard actuators).** **Partially covered, but not on NRF/SCP.**
  - Zhu2022 wires NWDAF failure detection to an automated UDM → HSS fallback, a restoration-like action, though not TS 23.527 and with analytical evaluation only.
  - Hasan2026 maps NWDAF-style analytics to graded actions (terminate/throttle/monitor), but not through PCF/SMF.
  - The NOMS 2026 conference version of Ardestani2026 has the SMF consuming NWDAF analytics (already known).
  - Runner-up 5 uses NF-load forecasts to tune SMF URR thresholds.
  - **No work in the C1 pool uses NF-load analytics for NRF/SCP NF selection or NF-set reselection.**
- **G3 (control-plane twins, fidelity).** No C1 evidence. The pool has only RAN-centred DT items: DT for RL training in 6G
  (ICC Wkshps 2026) and an NDT for traffic anomaly detection (Comput. Networks 2026, abstract unavailable).
- **G7 / P4 (geo-redundancy, UDR/UDSF failover, DB failover cost).** Zhu2022 is the closest item: subscriber-database
  (UDM) disaster backup triggered by analytics. It is evaluated only by fault-tree analysis, with no cross-site replication
  and no transient UE-procedure cost, so **G7/P4 hold**, but Zhu2022 should be cited as partial prior art.
- **P1 (SCP as telemetry source).** Nothing found in the C1 pool.
- **P2 (pre-validating remedies).** Nothing direct. Hasan2026 gates actions on calibrated confidence and severity, which
  checks whether to act but not whether the action will help.
- **P3 (procedure-level UE models under faults).** Nothing direct.
  - SCOPE-5G (selected by C2) models 21 AMF procedures with queueing and anomaly injection, but at aggregate PM level, without UE outcomes or NAS timers.
  - Chouman2024 emulates full registration sequences on a testbed, but without faults.
- **Gap 8 (evidence base).** Slightly weakened.
  - NWDAF-NFPP (Chen2024) is an operator-lab NF performance dataset.
  - SCOPE-5G (C2) is an open, labelled synthetic AMF anomaly dataset.
  - AnomalyTrack (C3) and Jeong2021 use live operator data.
  - There is still no public multi-NF 5GC *fault* benchmark from real systems.

## Research groups not listed in SUMMARY.md §5
- **China Telecom Research Institute** (Chen, Song; Yin, Li; Zhu, Li): NWDAF-NFPP dataset, NWDAF VFL management, UDM disaster backup.
- **Korea University** (Sangheon Pack, Youbin Jeon): distributed and hierarchical NWDAF (H-NDAF; also seed Jeon2022).
- **Nokia Bell Labs Paris-Saclay + Univ. Rennes/Saint-Étienne** (Rajabzadeh, Outtagarts, Hadjadj-Aoul): FL for distributed NWDAFs.
- **NJIT** (Nirwan Ansari) with **Futurewei**: decentralised FL/split learning in the 5G+ core.
- **UC3M Madrid** (de la Oliva, Bernardos): AIaaS extending the NWDAF on SLICES-Madrid.
- **UFMG, Brazil** (Oliveira, Macedo, Nogueira; also seed Oliveira2025Aiaas): 5GC analytics frameworks and AIaaS.
- **NYCU, Taiwan** (Kuo, Chang, Wang): distributed MTLF (OpenDaisy).
- **KFUPM** (Sheltami, Mahmoud): calibrated NWDAF DDoS loops.
- **Ericsson** (Jeong, Roeland): mobility prediction for the 5GC.
- **C-DOT India**: NWDAF overview.
- **RPTU Kaiserslautern / NEC Labs Europe** (Habibi, Schotten, Costa-Pérez): MDA in the O-RAN SMO (runner-up).
- Waterloo's **Monarch** (Saha, Limam, Boutaba) extends a group already listed.

## Problems
- Elsevier abstracts were not retrievable (Crossref/OpenAlex/S2 empty, ScienceDirect 403). Affected: FDFL ComNet 2026,
  GEN-DRIFT, *Service-based Analytics for 5G open experimentation platforms* (ComNet 2022), SIM+ (ComNet 2024) and *Network load
  prediction and anomaly detection* (ComComm 2022). None was selected, and runner-up 1 needs a manual check.
- For Yin2026, Hossain2024 and BarrosoFernandez2026 the abstracts give no numbers, so `key_result` is qualitative.
