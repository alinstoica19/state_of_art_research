# SUMMARY — candidate literature for the survey

*AI-native automation of the 5G-Advanced and 6G core network: network analytics, digital twins and autonomous
decision loops. A critical review of the literature and of 3GPP Releases 18-21.*

Run date: 2026-10-10. Method: `PROTOCOL.md`. Judgement calls: `DECISIONS.md`. Per-subdomain gap notes:
`work/S<n>_report.md`. Search logs: `work/S<n>_decisions.md`.

**Bottom line.** There are **179 unique verified candidates**, all verified individually: 149 by DOI via Crossref,
8 by arXiv ID and 22 standards checked on the 3GPP portal, ETSI, IETF or ITU pages. No entry is `search-only`
and `unverified.csv` is empty. The target was about 130, so there is headroom to select 50-100. 157 of the 179
works (88%) date from 2022-2026, and 82 are relevance 3.

Files: `ALL_CANDIDATES.csv` (one row per work; surveys first), `references.bib` (179 entries, keys =
`id` column), `results/S<n>_*.csv/.bib` (per-subdomain files, before deduplication), `unverified.csv` (empty),
`grey_literature.csv` (1 vendor item).

## 1. Counts

Total rows in subdomain files: 189; unique works after deduplication: **179**; unverified: 0; grey: 1

| Subdomain | Primary | Incl. secondary | Relevance 3 | Surveys |
|---|---|---|---|---|
| S1 Network analytics (NWDAF/MDA) | 23 | 44 | 21 | 3 |
| S2 SBA and NF selection | 21 | 49 | 8 | 4 |
| S3 Network digital twins | 21 | 34 | 9 | 7 |
| S4 RCA and anomaly detection | 22 | 38 | 11 | 4 |
| S5 Resilience and failover | 24 | 33 | 8 | 3 |
| S6 Closed-loop / autonomous networks | 22 | 71 | 9 | 7 |
| S7 Energy efficiency | 24 | 30 | 10 | 5 |
| S8 AI/ML performance prediction | 22 | 57 | 6 | 4 |

| Year | Works |
|---|---|
| 2015 | 1 |
| 2016 | 1 |
| 2019 | 1 |
| 2020 | 4 |
| 2021 | 15 |
| 2022 | 31 |
| 2023 | 25 |
| 2024 | 34 |
| 2025 | 35 |
| 2026 | 32 |

| Venue type | Works |
|---|---|
| journal | 79 |
| conference | 70 |
| standard | 22 |
| preprint | 8 |

| Relevance | Works |
|---|---|
| 3 | 82 |
| 2 | 85 |
| 1 | 12 |

Top venues:

- IEEE Network (11)
- IEEE Transactions on Network and Service Management (9)
- IEEE Communications Surveys & Tutorials (8)
- arXiv preprint (8)
- IEEE Access (7)
- NOMS 2022-2022 IEEE/IFIP Network Operations and Management Symposium (5)
- Computer Communications (4)
- Computer Networks (4)
- IEEE Communications Magazine (3)
- ICC 2026 - IEEE International Conference on Communications (3)
- NOMS 2024-2024 IEEE Network Operations and Management Symposium (3)
- NOMS 2026-2026 IEEE Network Operations and Management Symposium (3)
- 2024 IEEE Conference on Network Function Virtualization and Software Defined Networks (NFV-SDN) (3)
- IEEE Internet of Things Journal (2)
- Journal of Network and Systems Management (2)

Citation counts come from OpenAlex. When OpenAlex reported fewer than 10 citations, the count was cross-checked
against Semantic Scholar and the higher value kept. The source and date are in `citations_date`. Counts for
2025-2026 works are naturally near zero.

Venue types per primary subdomain:

| Subdomain | Journal | Conference | Standard | Preprint |
|---|---|---|---|---|
| S1 | 8 | 11 | 3 | 1 |
| S2 | 9 | 8 | 3 | 1 |
| S3 | 12 | 4 | 4 | 1 |
| S4 | 6 | 15 | 0 | 1 |
| S5 | 10 | 10 | 3 | 1 |
| S6 | 12 | 5 | 4 | 1 |
| S7 | 11 | 8 | 4 | 1 |
| S8 | 11 | 9 | 1 | 1 |

Deduplication: 189 subdomain rows collapsed into 179 works. The 10 works found by more than one subdomain keep one
primary subdomain, chosen by relevance and then by protocol priority; the others go in `secondary_subdomains`.
Overall, 141 works carry at least one secondary subdomain, which shows how strongly the topics overlap.

- Attaoui2023Cnfplacement (S2; also S7)
- Wang2024Sliceadmission (S3; also S6;S8)
- Ardestani2026Closedloop (S1; also S4;S6)
- Larrea2023Corekube (S5; also S2)
- Kawasaki2023Failureprediction (S5; also S4;S8)
- Saleem2025Tegra (S5; also S2)
- Jain2022Lowlatencycore (S5; also S2)
- Li2024Saferl (S8; also S3;S6)
- Kuranage2022Corescaling (S8; also S1;S2)
- Wang2022Slicedt (S8; also S3)

Conference/journal pairs of the same work were resolved by keeping the journal version, as listed in the
subagent decision logs. Examples: Shafiei Ardestani et al., where the ITU J-FET 2026 version was kept over NOMS
2026; Manias et al. on model drift, where IEEE Commun. Mag. 2023 was kept over MeditCom 2022; and the Bellin et
al. and Ziazet et al. journal versions over their NetSoft and FNWF 2023 papers.

### Standards in the list (22)

| Body | Document | Release / version | Topic |
|---|---|---|---|
| 3GPP SA2 | TS 23.288 | V19.8.0, Rel-19 | NWDAF architecture (analytics, MTLF/AnLF, DCCF/ADRF) |
| 3GPP SA2 | TR 23.700-84 | V19.0.0, Rel-19 | Study on core network enhanced support for AI/ML |
| 3GPP SA2 | TS 23.501 | V19.9.0, Rel-19 | 5GS architecture (SBA, NF sets, SCP) |
| 3GPP CT4 | TS 29.500 / TS 29.510 | V19.7.1 / V19.8.0, Rel-19 | SBA realisation, overload control / NRF services |
| 3GPP CT4 | TS 23.527 | V19.5.0, Rel-19 | Restoration procedures |
| 3GPP SA2 | TR 23.700-66 | V19.0.0, Rel-19 | Energy efficiency and energy saving (5GS) |
| 3GPP SA1 | TR 22.882 | V19.3.0, Rel-19 | Energy efficiency as a service criterion |
| 3GPP SA5 | TS 28.104 | V19.3.0, Rel-19 | Management Data Analytics (MDA) |
| 3GPP SA5 | TS 28.561 / TR 28.915 | V19.3.0 (Rel-20 in progress) / V19.0.0 | Management of network digital twins |
| 3GPP SA5 | TS 28.312 | V19.5.0, Rel-19 | Intent-driven management |
| 3GPP SA5 | TS 28.100 | V18.0.0, Rel-18 | Levels of autonomous network |
| 3GPP SA5 | TS 28.310 / TR 28.880 | V20.1.0, Rel-20 / V19.0.0 | Energy efficiency of 5G (management) |
| ETSI ZSM | GS ZSM 009-1 | V1.1.1 (2021) | Closed-loop automation enablers |
| ETSI NFV | GS NFV-REL 001 / 003 | 2015 / 2016 (`seminal`) | NFV resiliency and reliability models |
| IRTF NMRG | draft-irtf-nmrg-network-digital-twin-arch-13; RFC 9315 | 2026 / 2022 | NDT reference architecture; intent concepts |
| ITU-T | Y.3090; Y.3172 (`seminal`) | 2022; 2019 | Digital twin network; ML in future networks |

Not added (to avoid duplicates across subdomains), but a reviewer will expect the paper to cite them: TS 28.105
(AI/ML management), TS 29.520 (Nnwdaf services), TS 23.502, ETSI GS ZSM 002, and the Rel-20/21 6G study items
(SA1/SA2 6G studies). The article should cite these directly; the protocol's verification steps for standards
apply to them too.

## 2. Existing surveys (position the article against these)

| id | Year | Title | Venue | Subdomain | Cites |
|---|---|---|---|---|---|
| Manalastas2025Simulatorsdt | 2025 | From Simulators to Digital Twins for Enabling Emerging Cellular Networks: A Tutorial and Survey | IEEE Communications Surveys & Tutorials | S3 | 25 |
| Raza2025Ndtsurvey | 2025 | A comprehensive survey of Network Digital Twin architecture, capabilities, challenges, and requirements for Edge–Cloud Continuum | Computer Communications | S3 | 22 |
| Almasan2022Ndt | 2022 | Network Digital Twin: Context, Enabling Technologies, and Opportunities | IEEE Communications Magazine | S3 | 181 |
| Khan2022Digitaltwin6G | 2022 | Digital-Twin-Enabled 6G: Vision, Architectural Trends, and Future Directions | IEEE Communications Magazine | S3 | 552 |
| Kuruvatti2022Digitaltwin6G | 2022 | Empowering 6G Communication Systems With Digital Twin Technology: A Comprehensive Survey | IEEE Access | S3 | 164 |
| Mihai2022Digitaltwins | 2022 | Digital Twins: A Survey on Enabling Technologies, Challenges, Trends and Future Prospects | IEEE Communications Surveys & Tutorials | S3 | 1048 |
| Wu2021Dtnsurvey | 2021 | Digital Twin Networks: A Survey | IEEE Internet of Things Journal | S3 | 835 |
| Romero2025Nwdafreview | 2025 | Towards Network Data Analytics in 5G Systems and Beyond | Anais do XLIII Simpósio Brasileiro de Telecomunicações e Processamento de Sinais | S1 | 3 |
| GarciaMartin2024Nwdaf | 2024 | Network Automation and Data Analytics in 3GPP 5G Systems | IEEE Network | S1 | 22 |
| Niu2022Nwdafmanagement | 2022 | A Survey of 3GPP Release 18 on Network Data Analytics Function Management | 2022 IEEE/CIC International Conference on Communications in China (ICCC Workshops) | S1 | 6 |
| Mauro2026Availabilitysurvey | 2026 | Reliability and Availability in Virtualized Networks: A Survey on Standards, Modeling Approaches, and Research Challenges | IEEE Communications Surveys & Tutorials | S5 | 11 |
| Shahab2025Sfcfaulttolerance | 2025 | Fault Tolerance in Service Function Chains: A Taxonomy, Survey and Future Directions | Journal of Network and Systems Management | S5 | 5 |
| Khaloopour2024Resiliencebydesign | 2024 | Resilience-by-Design in 6G Networks: Literature Review and Novel Enabling Concepts | IEEE Access | S5 | 40 |
| SuarezVarela2023Gnnnetworks | 2023 | Graph Neural Networks for Communication Networks: Context, Use Cases and Opportunities | IEEE Network | S8 | 115 |
| Hui2023Dtperfmodel | 2023 | Digital Twin for Networking: A Data-Driven Performance Modeling Perspective | IEEE Network | S8 | 106 |
| Jiang2022Graphdl | 2022 | Graph-based deep learning for communication networks: A survey | Computer Communications | S8 | 284 |
| Jiang2022Trafficprediction | 2022 | Cellular traffic prediction with machine learning: A survey | Expert Systems with Applications | S8 | 175 |
| Ameur2026Agenticsurvey | 2026 | LLM-Powered Agentic AI for 5G/6G Networks: A Tutorial and Survey on Architectures, Protocols, and Standardization | arXiv preprint | S6 |  |
| Coronado2022Zerotouch | 2022 | Zero Touch Management: A Survey of Network Automation Solutions for 5G and 6G Networks | IEEE Communications Surveys & Tutorials | S6 | 183 |
| Zhou2025Llmtelecom | 2025 | Large Language Model (LLM) for Telecommunications: A Comprehensive Survey on Principles, Key Techniques, and Opportunities | IEEE Communications Surveys & Tutorials | S6 | 241 |
| Hong2025Llmnetmgmt | 2025 | A Comprehensive Survey on LLM‐Based Network Management and Operations | International Journal of Network Management | S6 | 19 |
| Leivadeas2023Intentsurvey | 2023 | A Survey on Intent-Based Networking | IEEE Communications Surveys & Tutorials | S6 | 318 |
| Mehmood2023Intentcellular | 2023 | Intent-driven autonomous network and service management in future cellular networks: A structured literature review | Computer Networks | S6 | 79 |
| Liyanage2022Zsm | 2022 | A survey on Zero touch network and Service Management (ZSM) for 5G and beyond networks | Journal of Network and Computer Applications | S6 | 151 |
| Zhang2025Llmaiops | 2025 | A Survey of AIOps in the Era of Large Language Models | ACM Computing Surveys | S4 | 45 |
| Murphy2024Faultprediction | 2024 | Fault Prediction for Heterogeneous Telecommunication Networks Using Machine Learning: A Survey | IEEE Transactions on Network and Service Management | S4 | 29 |
| Soldani2022Rcasurvey | 2022 | Anomaly Detection and Failure Root Cause Analysis in (Micro) Service-Based Cloud Applications: A Survey | ACM Computing Surveys | S4 | 252 |
| Notaro2021Aiops | 2021 | A Survey of AIOps Methods for Failure Management | ACM Transactions on Intelligent Systems and Technology | S4 | 135 |
| Atalay2026Cloudsurvey | 2026 | A Survey on Cloud-Based 6G Deployments: Current Solutions, Future Directions and Open Challenges | arXiv preprint | S2 |  |
| Attaoui2023Cnfplacement | 2023 | VNF and CNF Placement in 5G: Recent Advances and Future Trends | IEEE Transactions on Network and Service Management | S2 | 106 |
| Aldas2023Servicemesh | 2023 | Cloud-Native Service Mesh Readiness for 5G and Beyond | IEEE Access | S2 | 23 |
| Robitzsch2023Microservices | 2023 | Prospects on the adoption of a microservice-based architecture in 5G systems and beyond | Computer Networks | S2 | 5 |
| Kamran2025Energyexposure | 2025 | A Review of Energy Information Collection and Exposure in 3GPP Mobile Networks | 2025 17th International Conference on COMmunication Systems and NETworks (COMSNETS) | S7 | 2 |
| Setiawan2025Softwarized | 2025 | Energy-Efficient Softwarized Networks: A Survey | IEEE Transactions on Network and Service Management | S7 | 11 |
| Kamran2025Energyaware6G | 2025 | Energy-Aware 6G Network Design: A Survey | arXiv preprint | S7 |  |
| Mao2022Greenai | 2022 | AI Models for Green Communications Towards 6G | IEEE Communications Surveys & Tutorials | S7 | 301 |
| LopezPerez2022Ranenergy | 2022 | A Survey on 5G Radio Access Network Energy Efficiency: Massive MIMO, Lean Carrier Design, Sleep Modes, and Machine Learning | IEEE Communications Surveys & Tutorials | S7 | 282 |

**Positioning.** No survey above covers the *core network* with *AI-driven automation across analytics, digital
twins and decision loops*, mapped to Rel-18-21:
- The closest are García-Martín et al. (IEEE Network 2024, a magazine tutorial on 3GPP NWDAF/MDA automation) and
  Niu et al. (ICCC-W 2022, Rel-18 NWDAF management). Both are short and descriptive, with no systematic method.
- The ZSM, IBN and autonomous-network surveys (Coronado COMST 2022, Liyanage JNCA 2022, Leivadeas COMST 2023,
  Mehmood ComNet 2023) predate the Rel-19 intent and NDT specs and LLM agents, and treat the core only as one
  domain among many.
- The digital-twin surveys (Wu IoT-J 2021, Mihai COMST 2022, Khan COMMAG 2022, Manalastas COMST 2025) focus on
  general, RAN or simulator concerns and do not cover twins of the core control plane.
- The LLM/agentic surveys (Zhou COMST 2025, Hong IJNM 2025, the Ameur 2026 preprint) are broad and not
  core-specific.
- The resilience and energy surveys (Di Mauro COMST 2026, Setiawan TNSM 2025) cover NFV generically, not 3GPP
  core procedures.

There is no COMST-grade survey dedicated to the cloud-native 5GC/SBA, NWDAF, or 5GC resilience; the S1, S2 and S5
subagents each confirmed this independently. That is the article's opening.

## 3. Draft taxonomy (5 categories)

The taxonomy follows the life cycle of an autonomous core decision: *observe → model/predict → diagnose →
decide/act → govern*. Each candidate falls in at least one category. The counts below use the primary subdomain
and are approximate; secondary subdomains add cross-links.

| # | Category | What it contains | Main subdomains | Works (rel-3) |
|---|---|---|---|---|
| **C1** | **Standardised network analytics and data pipelines** | NWDAF/MDA implementations, analytics IDs, data collection (DCCF/ADRF), federated learning across NWDAFs, model drift and accuracy monitoring, KPI and traffic forecasting that feeds analytics | S1, part of S8 | ~23 (21) |
| **C2** | **Network modelling and digital twins** | GNN/learned performance models (RouteNet family, m3, DeepQueueNet), twins of the core and control plane, what-if validation, twin-assisted safe RL, NDT management standards | S3, S8 | ~43 (15) |
| **C3** | **Assurance: anomaly detection, RCA and resilience** | 5GC control-plane anomaly detection, trace/log/metric RCA (classic, causal, LLM-based), failure prediction, availability modelling, stateless and geo-redundant designs, restoration | S4, S5 | ~46 (19) |
| **C4** | **Autonomous resource and service decisions in the core** | DRL/forecast-driven autoscaling (AMF, UPF, CNFs), NF placement and selection, load balancing via NRF/SCP/service mesh, energy-aware placement/selection/consolidation | S2, S7 | ~45 (18) |
| **C5** | **Closed-loop governance: zero-touch, intent and agentic AI** | ZSM and closed-loop frameworks, intent translation and assurance, autonomy levels, LLM/agentic operations of the core, conflicts between loops | S6 | ~22 (9) |

A 4-category alternative merges C4 and C5 into "decision loops" (*act* and *govern*). This keeps the three nouns
of the title (analytics, digital twins, autonomous decision loops), with assurance as the fourth category. In that
variant, energy (S7) works best as a **cross-cutting objective** rather than a category; the comparison tables can
mark it with an "objective" column (latency / availability / energy / cost).

Suggested comparison-table columns per category: method family (supervised / DRL / safe-RL / GNN / LLM-agent),
data (synthetic / testbed / operator traces), testbed (free5GC / Open5GS / OAI / Magma / commercial),
standards anchor (spec + clause), closed-loop (yes/no; actuator), evaluation metrics, open artefacts.

## 4. Gaps: what Rel-18-21 calls for that the literature does not deliver

These are synthesised from the eight subdomain reports (`work/S<n>_report.md`).

1. **The standard analytics life cycle is almost unused (Rel-17/18/19, TS 23.288, TS 28.104, TR 23.700-84).**
   - Papers build ad-hoc NWDAF-like modules. Few use the MTLF/AnLF split, DCCF/ADRF/MFAF data collection, model
     sharing, or accuracy and drift monitoring.
   - The Rel-19 AI/ML topics, such as vertical FL between AF and NWDAF and NWDAF-assisted signalling-storm
     analytics, have almost no academic evaluation.
   - MDA (TS 28.104) has nearly no evaluation at all.
2. **Analytics are not wired to standard actuators.**
   - NF-load analytics are not used for NF selection through the NRF or SCP (TS 29.510/29.500 leave the selection
     policy open).
   - Failure analytics are not linked to TS 23.527 restoration or NF-set reselection.
   - Energy analytics are not used in PCF policy (TR 23.700-66).
   - Analytics-triggered core loops (NWDAF → SMF/PCF) appear only in 2026 papers.
3. **Twins of the core control plane are rare, and fidelity is unaddressed.**
   - TS 28.561 and TR 28.915 standardise NDT *management* only.
   - No paper measures twin fidelity, exposes a twin through the NDT management services, or twins NF
     failover/state replication.
   - What-if validation before change deployment is a headline TR 28.915 use case, yet it has a single
     operator-scale proof (Spillway, SIGCOMM 2026), on a proprietary simulator.
   - GNN performance models remain IP/data-centre-centric.
4. **Intent and autonomy levels are not operationalised (TS 28.312, TS 28.100).**
   - LLM intent work outputs YAML, NSDs or vendor configs, not the 3GPP intent information model, intent reports
     or feasibility checks.
   - No system reports its TS 28.100 autonomy level.
   - Conflicts between multiple loops (ZSM 009) are unaddressed for agent-driven loops.
5. **Agentic and LLM operations lack safety evidence.**
   - The 2025-26 agentic-core papers are prototypes with one or two use cases.
   - No work quantifies hallucination, rollback or guard-rails, or decision latency against core timing budgets,
     while SA5, TM Forum and ETSI are already standardising agentic management.
6. **Energy is studied only for the user plane.**
   - No peer-reviewed work on energy-aware placement or selection of control-plane NFs (AMF/SMF/NRF/SCP).
   - The Rel-19/20 energy exposure and energy-as-service-criterion features (TR 23.700-66, TR 22.882,
     TS 28.310 Rel-20) are unimplemented.
   - The carbon footprint and energy cost of the AI itself are almost absent.
7. **Resilience research is disconnected from AI and from geo-redundancy.**
   - Availability models are offline and stochastic.
   - Stateless designs report latency, not failover time.
   - Cross-site UDR/UDSF replication trade-offs and chaos-style failure campaigns are absent from peer-reviewed
     work.
8. **The evidence base is weak.**
   - Evaluations mostly use small free5GC/Open5GS/OAI labs with synthetic load.
   - There are no public 5GC fault or performance benchmarks (nothing like TrainTicket/RCAEval for
     microservices), and operator traces are rare.
   - Generalisation under drift and across operators is untested.
9. **6G readiness (Rel-20 studies → Rel-21 normative).** 6G core design papers are conceptual. None evaluates
   AI-native core functions (e.g. analytics or agents as native NFs) against the emerging 6G architecture studies.

## 5. Research community (relevance-3 works)

Most frequent authors among relevance-3 works (Crossref author lists):

- Dimitrios Michael Manias (5): Manias2023Modeldrift, Chouman2022Nwdaf, Manias2022Signaling, Manias2024Semanticrouting, Chouman2023Amfscaling
- Ali Chouman (5): Manias2023Modeldrift, Chouman2022Nwdaf, Manias2022Signaling, Manias2024Semanticrouting, Chouman2023Amfscaling
- Abdallah Shami (5): Manias2023Modeldrift, Chouman2022Nwdaf, Manias2022Signaling, Manias2024Semanticrouting, Chouman2023Amfscaling
- Adlen Ksentini (4): Ameur2026Agenticsurvey, Ameur2026Agenticnwdaf, Mekrache2023Abnormaltraffic, Mekrache2024Llmintent
- Fabrizio Granelli (4): Costa2025Privatendt, Bayleyegn2024Kpiprediction, Bellin2024Powermeasurement, Bellin2024Upfselection
- Abdelkader Mekrache (3): Ameur2026Agenticsurvey, Mekrache2023Abnormaltraffic, Mekrache2024Llmintent
- Jiadai Wang (3): Wang2024Sliceadmission, Tan20255Gcguard, Tan2023Loganomaly
- Jiajia Liu (3): Wang2024Sliceadmission, Tan20255Gcguard, Tan2023Loganomaly
- Shwetha Vittal (3): Vittal2024Resilientcore, Sovitkar2024Recap, Vittal2022Harness
- Ilhem Fajjari (3): Veronese2026Aicom, Zhao2026Tracerca, Khichane2022Cnforchestration
- Nadjib Aitsaadi (3): Veronese2026Aicom, Zhao2026Tracerca, Khichane2022Cnforchestration
- Mazene Ameur (2): Ameur2026Agenticsurvey, Ameur2026Agenticnwdaf
- Bouziane Brik (2): Ameur2026Agenticsurvey, Ameur2026Agenticnwdaf
- Raouf Boutaba (2): Ardestani2026Closedloop, Boutaba2021Closedloop
- A. Antony Franklin (2): Vittal2024Resilientcore, Vittal2022Harness
- Yawen Tan (2): Tan20255Gcguard, Tan2023Loganomaly
- Yuanhao Li (2): Tan20255Gcguard, Tan2023Loganomaly
- Guillaume Fraysse (2): Long2024Saferl, Singh2023Drlautoscaling
- Arturo Bellin (2): Bellin2024Powermeasurement, Bellin2024Upfselection
- Daniele Munaretto (2): Bellin2024Powermeasurement, Bellin2024Upfselection

The main groups the article must engage with:
- **Western University** (Shami, Manias, Chouman): NWDAF, drift, intent and LLMs, AMF scaling.
- **EURECOM** (Ksentini, Mekrache, Brik, Ameur): NWDAF, LLM intent, agentic survey.
- **University of Waterloo** (Boutaba, Limam, Shafiei Ardestani): standards-compliant closed loops.
- **University of Trento** (Granelli, Bellin): NWDAF KPI prediction, core power, NDT.
- **Xidian University** (Jiajia Liu, Jiadai Wang, Yawen Tan): 5GC anomaly detection, DT slice admission.
- **IIT Hyderabad** (Vittal, Franklin): 5GC resilience and high availability.
- **Orange / Paris-Saclay** (Aitsaadi, Fajjari): 5GC RCA, CNF orchestration, LLM configuration management.
- **Orange / Magma autoscaling** (Fraysse et al.).
- **IMT Atlantique** (Kuranage, Nuaymi, Bouabdallah): 5GC resource forecasting.
- **Edinburgh** (Marina): CoreKube.
- **Fraunhofer FOKUS** (Corici, Magedanz): failure prediction.
- **KDDI Research** and **NTT**: operator-lab failure prediction and RCA.
- **NEC Labs Europe**: cloud-native core twin.

The dominant adjacent (relevance-2) group in modelling is **UPC / Barcelona Neural Networking Center**
(Cabellos-Aparicio, Barlet-Ros, Suárez-Varela, Ferriol-Galmés: RouteNet, NDT).
Standards editors of note: China Mobile, Huawei, Telefónica and Orange (IRTF NDT draft; China Mobile also holds
the TR 28.915 rapporteurship).

## 6. Items to check by hand

- JNCA 2026, gNB energy saving orchestrated via NWDAF (10.1016/j.jnca.2026.104482). This looks highly relevant
  but was not included, because its abstract could not be read.
- AICOM (IFIP Networking 2026) and the LNEE 2024 alarm-correlation chapter. Their summaries are based on search
  snippets only; the critique fields say so.
- TR 23.700-66: which key issues were scoped out was taken from third-party mirrors; check the TR text.
- Venues to check in JCR or CORE: SBrT 2025 (Romero & Suyama), free5GC World Forum 2025, LNEE chapter, ICOIN,
  COMSNETS, WCNPS. These were kept because the works are on-topic, but they are weaker venues.
- Quartiles were deliberately **not** recorded (protocol §3).

## 7. Fuzzy-title near-duplicate check

None found (title similarity > 0.9 across different identifiers).
