# SNOWBALL_SUMMARY — citation snowballing and gap check

Run date: 2026-10-10. Method: `PROTOCOL_SNOWBALL.md`. Judgement calls: `DECISIONS_SNOWBALL.md`. Per-category
reports, with runners-up: `work/snowball/C{1,2,3,45}_report.md`. Gap check: `GAP_CHECK.md`.

**Bottom line.**
- **100 new verified works** are added on top of the 179 in `ALL_CANDIDATES.csv`, none of them duplicates:
  - **56** come from backward and forward snowballing of the 37 seeds;
  - **44** come from the targeted gap-check searches.
- Verification: 95 by DOI via Crossref, 5 by arXiv ID (2025-2026 preprints). `unverified_snowball.csv` is empty.
- The gap check found **no claim already done**. **Six of seven claims are partially covered and must be
  reworded.** Only P4 holds as written.

Files:
- `results/SNOWBALL.csv`: the `ALL_CANDIDATES.csv` columns plus `found_via`, `link_count` and `category`. Filter on
  `category = gap-check` to separate the targeted-search works.
- `snowball.bib`: 100 entries; keys equal the `id` column and do not clash with `references.bib`.
- `unverified_snowball.csv` (empty) and `work/snowball/pool_*.csv` (the full harvested pools).

## 1. Counts

| Stage | Count |
|---|---|
| Seeds | 37 (C1 19, C2 7, C3 8, C4 1, C5 2) |
| Unique works linked to the seeds (backward + forward 2022-2026) | 1386 |
| … already in `ALL_CANDIDATES.csv` or a seed | 47 |
| Pool rows screened (pools overlap across categories) | C1 517, C2 185, C3 246, C4+C5 440 (+177 references of Ameur2026Agenticsurvey recovered by hand) = 1388 + 177 |
| Abstracts read (approx.) | C1 ~110, C2 ~60, C3 ~90, C4+C5 ~55 |
| Dropped as pre-2020 (approx.) | C1 70, C2 ~40, C3 97, C4+C5 ~165 |
| Dropped as wrong type (approx.: white papers, patents, spec fragments, theses, arXiv before 2025, duplicates) | C1 ~54, C2 ~12, C3 ~8, C4+C5 ~40 |
| Dropped as off-topic (approx.) | C1 ~390, C2 ~115, C3 ~110, C4+C5 ~215 |
| Selected and verified by category agents | C1 15, C2 14, C3 15, C4+C5 15 = 59 |
| … after cross-category merge (3 works selected twice) | **56** |
| Gap-check targeted search, verified new works | **44** |
| **Total new verified works** | **100** (relevance 3: 57; relevance 2: 43) |
| Unverified | 0 |
| `seminal` (pre-2020) | 3 of 5 allowed: Alawe2018Trafficforecast, Alawe2018Rnnscaling, Nguyen2018Echo |

The drop counts are approximate (agents' own estimates), and a row can be dropped for more than one reason.

| Primary subdomain | Snowball | Gap check | Total |
|---|---|---|---|
| S1 Analytics (NWDAF/MDA) | 12 | 3 | 15 |
| S2 SBA and NF selection | 6 | 6 | 12 |
| S3 Digital twins | 10 | 8 | 18 |
| S4 RCA and anomaly detection | 7 | 8 | 15 |
| S5 Resilience and failover | 10 | 9 | 19 |
| S6 Closed loop / intent / agentic | 9 | 3 | 12 |
| S7 Energy | 1 | 0 | 1 |
| S8 AI performance models | 1 | 7 | 8 |

| Year | 2018 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|
| Works | 3 | 6 | 8 | 11 | 19 | 30 | 23 |

Venue types: 35 journal, 60 conference, 5 preprint. New surveys (position the article against them):
Tiwari2025Nwdafevolution, Tran2025Ndt6Gsurvey, Dede2025Ai6Gcore, Owen2025Sovereignfunctions,
ElRajab2024Ztnsurvey, Gharbaoui2026Intentconflictsurvey.

**Seed coverage.**
- **No usable citation data:** BenllochCaballero2026Corex, Kamran2025Energyexposure and Ameur2026Agenticsurvey
  had no references or citations in OpenAlex or Semantic Scholar, and Leiter2022Upffailover had no reference
  list.
- **Recovered by hand:** the agents rebuilt these reference lists from Crossref and arXiv HTML (Corex 41 refs,
  Leiter 11 refs, Ameur 177 refs). Kamran's list could not be recovered, because the publisher withholds it.
- **Coronado2022Zerotouch** contributed the largest share of the C4+C5 pool: about 250 references and 156
  citing works.

## 2. The 10 most important new works

| # | id | Venue | Why it matters |
|---|---|---|---|
| 1 | Cakir2026Dthandover | IEEE TNSM 2026 | A generative twin produces counterfactual outcomes so the AMF can approve or reject each handover before execution. This is the closest prior art to per-decision what-if validation in the core (G3, P2). |
| 2 | Chen2026Feasibilityshield | EuCNC/6G Summit 2026 | LLM-proposed remediation actions in a 6G core pass a feasibility shield and a lookahead simulation before they run. This is direct prior art for P2, though only for link failures. |
| 3 | Nakao2025Comebacklater | GC Workshops 2025 | Measures NAS-retry behaviour and registration time under AMF registration storms in a real 5G core, and adds an overload back-off signal. This is the nearest work to P3. |
| 4 | Zhu2022Disasterbackup | CECCC 2022 | NWDAF-detected loss of all UDMs triggers fallback to the 4G HSS. This is analytics driving a restoration-like action on the subscriber database (G2, G7), evaluated only by fault-tree analysis. |
| 5 | Kong2024Cptgpt | ACM IMC 2024 | A transformer generator of per-UE control-plane traffic with measured fidelity. It shows that fidelity *is* measured for control-plane traffic models (G3). |
| 6 | Kuo2026Distributedmtlf | ICC Workshops 2026 | Implements the NWDAF MTLF/AnLF split as hierarchical federated learning and stresses it under drift. It is one of the few evaluations of the standard analytics life cycle (gap 1). |
| 7 | Manias2024Intentextraction | DRCN 2024 | A domain-tuned LLM from the Western University group extracts operator intents for 5G core management (L=5, 54 citations). It is a core reference for C5. |
| 8 | Alawe2018Trafficforecast | IEEE Network 2018 (`seminal`) | LSTM/DNN forecasting drives proactive 5GC scaling (236 citations). It has the highest link count in the harvest (L=5) and is the origin of forecast-driven core scaling. |
| 9 | Tiwari2025Nwdafevolution | NCC 2025 (`survey`) | An NWDAF overview across Releases 16/17 (L=5). The article must position itself against it. |
| 10 | Tonini2026Eifenergy | NOMS 2026 (demo) | A first implementation of the Rel-19 Energy Information Function exposing per-UE energy to an AF. It partly weakens gap 6. |

Close runners-up:
- Sovitkar2024Capstateless: CAP trade-offs of a stateless core (G7).
- Nguyen2021Dt5Gbeyond: the most-cited new digital-twin work, 422 citations.
- Kourtis2026Typesafeagents: wrong-action rates and decision latency of agentic 5G control (gap 5).
- Tran2025Nfloadanalytics: an NWDAF NF-load analytics implementation (G2).
- Kurata2024Geostorm: geographically distributed control-plane NF placement against signalling storms (G7, P4).

## 3. Which taxonomy categories are strengthened

The mapping follows `SUMMARY.md` §3 (S1 → C1; S3, S8 → C2; S4, S5 → C3; S2, S7 → C4; S6 → C5).

| Category | New works | What is strengthened |
|---|---|---|
| **C1** Analytics and data pipelines | 15 | NWDAF implementations and frameworks: Jeon2024 hierarchical NWDAF, Oliveira2024, Tran2025/2026, Chen2025 NWDAF load control, BarrosoFernandez2026 AIaaS. Federated, VFL and MTLF learning: Hossain2024, Yin2026, Kuo2026. Drift: Ameur2025. Datasets: Chen2024 NFPP. |
| **C2** Modelling and twins | 26 | Clearly the biggest gain. Core-twin platforms: the B5GEMINI line (journal and NOMS 2024), Vasalos2025, RodriguesDS2025, Petrik2025. Twin fidelity and synchronisation: Sengendo2024, Ntassah2026, Tao2024, Kong2024, Meng2023. Twin-gated decisions: Cakir2026, Tao2025 online DRL, Yu2023 self-healing. Control-plane traffic and mMTC models: Goshi2025. |
| **C3** Assurance and resilience | 34 | Resilience of stateless and cloud-native cores: Sovitkar2024 CAP, Goshi2023 PP5GS, Paul2025, Sarkar2022 LOCOMOTIVE, CellClone, ECHO. UPF failover and redirection: NguyenTrung2025, Wernet2024, Behnaminia2026. Storms and metastable failures: Kato2023, Kurata2024, Habibi2024, Isaacs2025. SBI/HTTP2 and control-plane anomaly detection: 5GShield, Wang2023, TeleGAN-Core, AnomalyTrack. LLM forensics: ForenSiX. |
| **C4** Resource and service decisions | 13 | Core scaling origins (Alawe 2018 ×2), core provisioning (Sheoran2021), federated VNF autoscaling (Subramanya2021), slicing admission (VillotaJacome2022), control-plane load balancing (Nguyen2021), service prioritisation (Kumari2024), service mesh for the 5GC (5G-STREAM). Energy gains only one work (Tonini2026). |
| **C5** Closed-loop governance | 12 | Agentic core architectures: Li2025 Agentic-AI Core and Tong2025 A-Core (both Huawei). Agent safety and guard-rails: Kourtis2026, Chen2026, Ta2026 Agentic GitOps. Intent: Manias2024 and the Gharbaoui2026 intent-conflict survey. ZTN survey: ElRajab2024. |

The added literature fills C2 and C3 most. C4/energy remains the thinnest area; the S7 gap from the first run
stands.

## 4. Do the new works change the gaps in `SUMMARY.md` §4?

Full evidence and exact suggested wording are in `GAP_CHECK.md`.

| Gap (SUMMARY §4) | Effect | Note |
|---|---|---|
| 1 Analytics life cycle unused | **Slightly weakened** | Kuo2026 (MTLF/AnLF under drift), Yin2026 (VFL in NWDAF, design only), Ameur2025 (drift). DCCF/ADRF/MFAF and MDA evaluations are still absent. |
| 2 Analytics not wired to standard actuators (= G2) | **Partially covered** | Rel-19 TS 23.288 §6.22 itself specifies NWDAF signalling-storm analytics consumed by the SCP and NRF, with reselection and deprioritisation actions. Patents wire analytics into NRF/SMF/SCP selection (Ericsson US 12,610,253; Samsung US 12,489,712; Rakuten US 12,041,120; Oracle US 11,671,369). Zhu2022 wires analytics to UDM→HSS fallback. Still missing: peer-reviewed evaluation of analytics-driven NRF/SCP (re)selection, and any link to TS 23.527 restoration. The claim must be about **evaluation**, not about missing wiring. |
| 3 Control-plane twins rare; fidelity unaddressed (= G3) | **Partially covered** | "Rare" holds. "Fidelity not measured" is false as worded: Kong2024, Meng2023, Ntassah2026 and Petrik2025 report it. Per-decision what-if now exists for handover (Cakir2026) and simulated link-failure remediation (Chen2026). Still open: **interventional** fidelity for core remediation actions (rerouting, DB failover). |
| 4 Intent and autonomy levels not operationalised | **Mostly unchanged** | Manias2024 and Ta2026 add LLM intent work, but not against the TS 28.312 model. Gharbaoui2026 surveys intent conflict detection, so "loop conflicts unaddressed" should be narrowed to agent-driven core loops. |
| 5 Agentic/LLM operations lack safety evidence | **Partially weakened** | Kourtis2026 measures wrong-action rates and decision latency; Chen2026 and GuardedAct (Cai2026) add guard-rails and blast-radius checks. The evidence is still small-scale and partly preprint. |
| 6 Energy only for the user plane | **Slightly weakened** | Tonini2026 implements the Rel-19 EIF (per-UE exposure). Energy-aware placement or selection of control-plane NFs is still absent. |
| 7 Resilience disconnected from AI and geo-redundancy (= G7) | **Partially covered** | Single-site and user-plane failover are measured (Sovitkar2024, Paul2025, NguyenTrung2025, Wernet2024, CellClone, ECHO), as are geo-distributed control-plane placement against storms (Kurata2024) and AI recovery-action choice (NFVAgent, Shaghaghi2022). Still absent: cross-site UDR/UDSF replication and DB primary failover measured on UE procedures. |
| 8 Weak evidence base | **Slightly weakened** | There are now open datasets: SCOPE-5G (synthetic, TS 28.552-aligned AMF observability) and the NWDAF-NFPP operator-lab dataset (Chen2024). Reword to "no public **operator-grade 5GC fault** benchmark". |
| 9 6G readiness | **Unchanged** | Li2025, Tong2025 and Dede2025 are conceptual or architectural. |

**Companion-paper contributions (P1-P4).**
- **P1 (SCP telemetry):** partially covered. TS 23.288 Rel-19 already lists SCP signalling information as an
  NWDAF input. Oracle US 11,671,369 derives NF-set load at the SCP. **Do not claim "first to use the SCP as a
  telemetry source".** Claim instead SCP-observed per-producer outcomes for localising *non-security* faults and
  deciding whether rerouting can help.
- **P2 (test a remedy before applying it):** partially covered. Prior art: SWARM, GuardedAct, Chen2026,
  Cakir2026, Spillway. The novel part is the **shared-dependency case**: whether rerouting can help at all when
  every candidate producer depends on the degraded back-end.
- **P3 (procedure-level UE outcome models):** partially covered.
  - AstroTimer (ICC 2026) models NAS timers and registration attempts, but for satellite delay.
  - Nakao 2025/2026 measures NAS retries under AMF storms.
  - The novel part is a validated model of the **multi-NF SBA registration chain under NF or back-end faults**
    that predicts T3510 expiry and retries.
- **P4 (multi-action remedies, DB-failover transient):** **holds**, with a minor tightening of the wording.

## 5. Research groups not seen in the first run

Affiliations are inferred from author lists by the agents. Confirm them before naming groups in the article.

- **Analytics (C1)**
  - China Telecom Research Institute: NWDAF-NFPP dataset, NWDAF VFL, UDM disaster backup.
  - Korea University (Sangheon Pack): distributed and hierarchical NWDAF.
  - Nokia Bell Labs Paris-Saclay with Univ. Rennes / Saint-Étienne: federated learning across NWDAFs (runner-up).
  - NJIT (Ansari) with Futurewei.
  - UC3M Madrid (de la Oliva, Bernardos): AIaaS NWDAF.
  - UFMG (Brazil).
  - NYCU Taiwan: OpenDaisy distributed MTLF.
  - KFUPM.
  - Ericsson (Jeong, Roeland).
  - RPTU Kaiserslautern with NEC Labs Europe: MDA (runner-up).
- **Twins (C2)**
  - UPM / Telefónica (Mozo, Pastor, López): B5GEMINI.
  - Southeast University Nanjing (Tao, Xu, You).
  - University of Pisa (Nardini, Stea): Simu5G twin.
  - Middlesex University (Nguyen, Trestian).
  - UNICAMP / UFABC: core slicing, SCOPE-5G.
  - BUPT: GNN self-healing twin.
  - University of the West of Scotland (Alcaraz-Calero, Qi Wang): COREX.
  - STU / Comenius Bratislava.
- **Assurance and resilience (C3)**
  - IIT Bombay (Vutukuru): fault-tolerant 5GC on Kubernetes.
  - LUMS (Qazi) with M. T. Raza: CellClone, Neutrino.
  - TU Munich with Nokia (Kellerer, Goshi): PP5GS, mMTC core models.
  - USTC (Xue): ForenSiX.
  - CentraleSupélec with Orange: service resilience estimation.
  - KDDI Research with NEC: closed-loop CNF management, reconnection storms.
  - The University of Tokyo (Nakao): AMF registration storms.
- **Agents and energy (C4+C5)**
  - Huawei (Wen Tong et al.): Agentic-AI Core, A-Core.
  - NCSR Demokritos: typed agentic control.
  - University of Bologna / CNIT with Huawei Munich: EIF energy exposure.
  - Soongsil University: Agentic GitOps.
  - Sant'Anna Pisa / CNIT: intent conflicts.
  - NTUST Taiwan: feasibility-shielded self-healing core.
  - Purdue / HPE: AI core provisioning.
- **Local link:** **University Politehnica of Bucharest (Vochin, Tufeanu) with University of Agder (Frank Y. Li)**
  wrote Tufeanu2026Residualartifacts (IEEE TNSM 2026, ML-based cleanup prediction in a Kubernetes 5G/6G SBA). It
  is a natural local collaborator or citation for the author.

## 6. To check by hand

- **ETSI GR ENI 055** (AI agents based core network) is cited by Ameur2026Agenticsurvey. It was not added because
  `verify.py` cannot verify ETSI GRs automatically; add it as a standard after checking the ETSI page.
- **Elsevier works with no retrievable abstract**, kept as runners-up only:
  - "Reliable feedback-driven federated learning for distributed NWDAFs at the edge" (Computer Networks 2026,
    10.1016/j.comnet.2025.111972);
  - the Ericsson intent-conflict paper and DETROIT (Computer Networks 2025).
- **Gap-check unverified leads** (see `GAP_CHECK.md`): WO 2025/216683 (NWDAF-assisted NF anomaly mitigation)
  and the venue of SWARM (NSDI 2025; arXiv ID verified).
- **Exact Rel-19 table numbers** cited in `GAP_CHECK.md`: TS 23.288 Tables 6.22.2-8 and 6.22.3-3 were read from
  the ETSI copy V19.8.0. Re-check them against the final 3GPP text before quoting.
- **Version pair:** Mozo2022B5Geminijournal (Sensors) is the journal version of the seed Mozo2022B5Gemini (NOMS).
  Cite the journal version.
- **Venues outside the PROTOCOL §3 list** were kept for content: VTC-Spring, ISCC, GC Workshops, CECCC, ELMAR,
  ISAS, ICACT, ICTC. Drop them if venue quality is a selection criterion.
