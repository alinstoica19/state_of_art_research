# Gap-check decisions (Phase 3, 2026-10-10)

These are the judgement calls behind `GAP_CHECK.md` and `work/SB_GAP.jsonl`.

## Sources and access

- **Semantic Scholar.** Keyword search returned HTTP 429 for the whole session; the snowball harvest was probably running in parallel. I used Semantic Scholar only for single-paper abstract lookups (`/paper/DOI:…`), which worked late in the session. The main discovery channels were Crossref bibliographic search, the arXiv API, web search and the snowball pools. Recall from Semantic Scholar's index is therefore missing; this is noted in GAP_CHECK.
- **arXiv API.** Phrase queries return very few hits (0–4). Recall is low, and I relied on web search to surface 2025–26 preprints. I then verified each one through the arXiv API.
- **3GPP specs.** The 3GPP FTP server returned 403, so I read the ETSI-published PDFs instead (TS 123 288 V19.8.0, TS 123 501 V19.9.0, TS 123 527 V19.5.0, all 2026-10). Reading the normative text was decisive for G2 and P1. Search-engine summaries of the specs were not used as evidence.
- **Patents.**
  - Google Patents blocked automated fetches after the first page, so I read US front pages from the USPTO image server (rendered to PNG and read visually).
  - WO publications could not be checked and went to "Unverified leads".
  - Patents are used as evidence in GAP_CHECK but are **not** survey candidates. PROTOCOL §3 has no patent venue type, so they are not in SB_GAP.

## Verdict calls

- **G2 → partially covered (not "already done").** Rel-19 TS 23.288 §6.22 defines NWDAF→SCP/NRF actions, and patents from Ericsson, Samsung, Rakuten and Oracle claim analytics- or load-driven selection. I still found no peer-reviewed evaluation of analytics-driven NRF/SCP selection. I judged that the survey's claim is about the literature, so it survives in reworded form. The restoration part holds: TS 23.527 Rel-19 contains no NWDAF hook, which I checked by grep.
- **G3 → partially covered.**
  - "Fidelity not measured" is literally false. Sequence F1 (Tao2024), KPI error (AbenAthar2025), sim-to-real accuracy drop (Petrik2025), the fidelity of control-plane traffic generators (SMM, CPT-GPT) and task-centric fidelity (Tao 2025 preprint) are all reported.
  - I kept the claim alive by distinguishing **observational** from **interventional** (action-conditioned) fidelity. No core twin reports the latter.
  - Çakır et al. (TNSM 2026) is the most damaging find. It does per-decision counterfactual pre-validation that the AMF consumes, but for handovers. I classified it as weakening G3's last sentence, not refuting it, because the actions are mobility rather than core remediation.
- **G7 → partially covered.** There is AI-for-resilience work, and geo- or multi-cluster failover exists for the UPF and for control-plane placement. The specific sub-claim, cross-site UDR/UDSF replication and DB primary failover measured on UE procedures, found no prior work. ECHO (MobiCom 2018) is the main older counter-example to "disconnected from geo-redundancy". It is pre-2020 and was added with the `seminal` flag; the coordinator should count it against the 5-seminal budget or drop it.
- **P1 → partially covered.**
  - The decisive find is TS 23.288 Rel-19 Table 6.22.2-8, which already standardises the SCP as an NWDAF data source with per-NF-instance request, failure, reselection and latency counters. The companion paper must not claim "first to use the SCP as a telemetry source".
  - SBI-traffic anomaly detectors (5GShield, GSAD, ADSeq, 5GCGuard, Granomaly) sniff traffic rather than use the SCP, and they target attacks. I counted them as near relatives, not as the same contribution.
- **P2 → partially covered.** SWARM (datacenter mitigation ranking by predicted connection-level impact) is the strongest prior art for the general principle. It is cited from its verified arXiv ID; the NSDI'25 venue is noted as unverified. It is not added to SB_GAP because the arXiv version is from 2023 and USENIX gives no DOI. GuardedAct, Chen2026Feasibilityshield and Spillway gate or validate actions, but none asks whether a reroute can help when the fault is in a shared dependency. I judged the specific formulation novel.
- **P3 → partially covered.**
  - The two Nakao papers (GC Workshops 2025, FiNE 2026) directly study NAS retries, T3510/T3346 and the UE registration deadline in a real 5GC, but under registration storms and as mechanisms, not predictive models.
  - AstroTimer (ICC 2026) and its 2026 follow-up are closed-form procedure/timer models that predict registration attempts, but for NTN propagation.
  - The claim survives only in narrow form: multi-NF chain, NF or back-end faults, validated prediction. If the companion paper's model is not validated on a running core, the remaining margin is thin.
- **P4 → holds.** Only adjacent decisions were found: intra- vs inter-cluster UPF restore, cost-based backup selection, geo-distributed CP routing for storms, generic DRL/LLM recovery choice and SFC rerouting. No work measures DB-failover transients on UE procedures.

## Inclusion calls for SB_GAP (44 works, all verified)

- **Deduplication.** All 44 were checked against `ALL_CANDIDATES.csv` and `results/SNOWBALL.csv` by DOI or arXiv ID and by normalised title. Works already found by the snowball (Zhu2022Disasterbackup, Paul2025Faulttolerantk8S, Kato2023Reconnectionstorm, Chen2026Feasibilityshield, Araujo2026Scope5G, Petrik2025Dtdomaintransfer and others) are cited in GAP_CHECK by their `SB:` id and **not** duplicated.
- **Relevance 3** went to works on the 5G core with an AI or automated decision or a twin: Chen2025, Tran2025, Tran2026, 5GShield, GSAD, TeleGAN-Core, SENTINEL, Kurata2024, NguyenTrung2025, Çakır ×2, Zheng2022, the two Nakao papers and Gopikrishnan2023. Kurata2024 and NguyenTrung2025 have no ML, but they automate core decisions; under PROTOCOL §5, "AI/automation" was read to include them.
- **Relevance 2** went to adjacent or transferable works: generic NFV/cloud, RAN/NTN, measurement-only studies and generic metastable-failure models.
- **Zheng2022Dtselfrecovery.** The *Digital Twin* journal (10.12688) uses open post-publication peer review (F1000 model), so the work is flagged `open-peer-review`. I kept it because it is one of the very few operator 5GC-twin recovery reports.
- **Two 2023–24 cloud/AIOps works** were included as relevance 2 because the coordinator's brief explicitly counts Microsoft/Alibaba-style mitigation work as partial prior art for P2: Ahmed2023 (ICSE) and Li2025 Panacea (AIOps workshop). CORNET (SIGCOMM 2021) was included because it is operator 4G/5G change-impact verification.
- **Preprints.** Only 2025–26 arXiv items were included (Tao 2025, GuardedAct 2026, Liu 2026).
- **Mentioned in GAP_CHECK but not added** (adjacent, pre-2020, weak, or no DOI):
  - Storms in mobile networks (2014); SWARM (arXiv 2023); Shang et al. TCC 2021; Bronson HotOS 2021.
  - Di Mauro & Peluso CNSM 2025 (an M/G/k model of 5G SFCs, already represented by DeSimone2025 from the same group); the coordinator may add it.
  - Auric/Aurora; Colosseum; Gao 2026 (arXiv:2608.15016); Nha & Nakao GC Workshops 2025.
  - The ICOIN 2023 Cilium-mesh 5GC design: qualitative only.
- **Bibkey glitch.** `S2025Open5Gsperf` takes the Crossref family name "S" (the author is "Sooraj Subramanian M S"). The key is valid but odd; the coordinator may rename it `Subramanian2025Open5Gsperf` at merge.
- **Year oddities.** MSF-Model has Crossref year 2024 (SRDS 2024), while Semantic Scholar says 2023; Crossref was kept. Shaghaghi2022Ztpfr is TNSM, online in 2021 with issue year 2022, as Crossref reports.

## Notes for SUMMARY §4 (do not edit here; for the coordinator)

- **Gap 1** ("NWDAF-assisted signalling-storm analytics have almost no academic evaluation") is consistent with what I found. The Nakao papers address storms without NWDAF.
- **Gap 2** should cite TS 23.288 §6.22 Table 6.22.3-3 as the standard actuator list and say that the gap is evaluation.
- **Gap 3** should drop "No paper measures twin fidelity" in favour of "no paper measures interventional fidelity of core twins".
