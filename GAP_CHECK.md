# GAP_CHECK — stress test of the gap and contribution claims

Phase 3 of `PROTOCOL_SNOWBALL.md` (§5). Run on **2026-10-10**.

## Method

For each claim I searched for prior work that would weaken it. I did not look for confirmation. The sources were:

- **Crossref.** About 95 bibliographic queries via `tools/verify.py search`, 20 hits each, screened by title.
- **arXiv API.** Nine queries. The API returns few hits per phrase query.
- **Semantic Scholar.** Single-paper lookups for abstracts only. Keyword search returned HTTP 429 throughout the session.
- **OpenAlex.** Single-work lookups for abstracts only. No keyword search was used.
- **Web search.** About 20 queries, mainly to find patents and grey literature.
- **Patent texts.** Front pages of US patents read on the USPTO image server (Google Patents throttled after the first page).
- **Standards text.** The 3GPP specifications themselves, read from the ETSI-published copies: ETSI TS 123 288 V19.8.0 (TS 23.288 Rel-19), ETSI TS 123 501 V19.9.0 (TS 23.501 Rel-19) and ETSI TS 123 527 V19.5.0 (TS 23.527 Rel-19), all dated 2026-10.
- **Snowball pools.** `work/snowball/pool_C1/C2/C3/C45.csv` grepped for gap vocabulary. `results/SNOWBALL.csv` (56 works) cross-checked.

**Search terms** (varied per claim; the full list is in the Search log at the end):

- **Telemetry and proxies:** service communication proxy, SCP, service mesh, sidecar, Envoy, Istio, HTTP/2 SBI anomaly.
- **Analytics and selection:** NWDAF NF load / abnormal behaviour analytics, NRF load-aware selection, UPF/SMF/AMF selection NWDAF, NF set reselection.
- **Resilience:** geo-redundant / multi-site / multi-cluster 5G core, UDR replication, UDSF, state database failover, disaster recovery, chaos engineering, fault injection.
- **Twins and what-if:** digital twin 5G core control plane / fidelity / what-if / synchronisation, counterfactual digital twin, pre-validation of changes, change verification, mitigation recommendation, safe action selection.
- **Procedures and storms:** registration procedure model, T3510, NAS retransmission / timer, Petri net, queueing, signalling / retry storm, metastable failure, MME pool / HSS outage (LTE/EPC predecessors).

**Rules followed:**

- Every reference below was verified: a DOI title-checked against Crossref, an arXiv ID through the arXiv API, a patent from its USPTO front page, or a 3GPP spec from the ETSI-published text.
- Items I could not verify, or whose content I could not read, are listed only in "Unverified leads".
- I describe a paper only from its abstract (or, for patents, the front-page abstract and figure).

**IDs used in this report:**

- IDs from `ALL_CANDIDATES.csv` are given as `[AC:<id>]`.
- IDs from the snowball run (`results/SNOWBALL.csv`) are given as `[SB:<id>]`.
- New works found here are given as `[GAP:<id>]`. They are written to `work/SB_GAP.jsonl` and `results/SB_GAP_gapcheck.csv`: **44 new verified works, 0 unverified**.

## Summary table

| Claim | Verdict | One-line reason |
|---|---|---|
| **G2** analytics not wired to standard actuators | **partially covered** | Rel-19 TS 23.288 §6.22 itself specifies NWDAF→SCP/NRF actions (redirect to another producer, NF-profile priority/capacity update); patents wire NWDAF/AI load or latency into NRF/SMF/SCP selection; a few papers wire analytics to other actuators. Still no peer-reviewed evaluation of analytics-driven NRF/SCP selection, TS 23.527 restoration or NF-set reselection. |
| **G3** core CP twins rare, fidelity unmeasured, no control-plane-speed action prediction | **partially covered** | "Rare" holds. "Fidelity not measured" is false as worded: several twins/generators report accuracy against real or emulated data. "No twin predicts a candidate action at control-plane speed" is weakened by a TNSM 2026 twin that pre-validates each handover for the AMF, and by a 6G-core feasibility-shield agent. |
| **G7** resilience disconnected from AI and geo-redundancy | **partially covered** | AI-for-resilience and multi-cluster/geo-distributed failover papers exist (mostly UPF/user plane, NFV-generic or single-site). Cross-site **subscriber-database** (UDR/UDSF) replication/primary failover and its effect on UE procedures: still not found. |
| **P1** SCP as telemetry source for analytics/AD/RCA | **partially covered** | Beyond 5G-RAD and US 12,155,534: Rel-19 TS 23.288 (Table 6.22.2-8) standardises SCP signalling information as NWDAF input; TS 23.501 lets the SCP expose load/delay/error-rate events; Oracle patent US 11,671,369 derives NF-set load at the SCP. Academic SBI-traffic anomaly detectors exist but sniff traffic. SCP telemetry for **RCA/remedy evaluation of non-security faults** remains unpublished. |
| **P2** testing whether a remedy can help before applying it | **partially covered** | Adjacent prior art: mitigation ranking by predicted impact (SWARM, datacenters), twin/sandbox pre-checks of candidate actions (GuardedAct; Chen 2026 feasibility shield in a 6G core; Çakır 2026 handover; Spillway). Nothing tests, for 5GC NF/database faults, whether rerouting can help when the shared back-end is the cause. |
| **P3** procedure-level models predicting UE-level outcomes (T3510, retries) under faults | **partially covered** | Closed-form NAS-timer models predicting registration attempts exist for NTN (AstroTimer, ICC 2026); Nakao (2025/2026) measures NAS-retry dynamics, registration-deadline violations and convergence in a real 5GC under registration storms; Markov storm models exist for 3G/4G RRC (2014). No validated model of the multi-NF registration chain under **NF/back-end faults** that predicts T3510 expiry/retry outcomes. |
| **P4** multi-action remedies in a multi-site core + transient cost of DB failover | **holds** | Only adjacent work: geo-distributed CP placement/routing for storms, intra- vs inter-cluster UPF restoration choice, cost-based backup selection, DRL/LLM recovery-action choice, SFC rerouting. None compares stay / reroute / DB failover or measures DB-failover transients on UE procedures. |

---

## G2 — Analytics are not wired to standard actuators

### (a) Evidence found

**The standards themselves (verified from ETSI-published text):**

- **TS 23.288 Rel-19 §6.22 (Signalling Storm Analytics).** Read in ETSI TS 123 288 V19.8.0. In this clause the NWDAF serves storm statistics and predictions to the SCP, NRF, AMF, SMF and others. Table 6.22.3-3 lists example consumer actions, among them:
  - the NRF updating NF-profile Priority/Capacity of the affected NFs;
  - the source NF reselecting or deprioritising NFs that show abnormal signalling;
  - the SCP redirecting requests to another service producer, or throttling them.

  The consumer may also chain NF-load and abnormal-behaviour analytics as triggers (procedure step 1). **The wiring from analytics to NRF/SCP selection is therefore standardised in Rel-19**, at least for the storm use case. The claim must be about evaluation, not about missing wiring. [AC:3GPP2026Nwdaf]
- **TS 23.501 Rel-19 §6.2.19 (SCP functionality).** Read in ETSI TS 123 501 V19.9.0. It lists optional interaction with the NWDAF for mitigating and preventing abnormal behaviour (signalling storms), and network protection based on NWDAF analytics, naming storm and NF-load analytics. It also says an SCP may use NWDAF storm analytics to select the next-hop SCP. The policy is left to implementation. [AC:3GPP2026Ts23501]
- **TS 23.527 Rel-19.** Read in ETSI TS 123 527 V19.5.0. The restoration procedures contain **no reference to NWDAF or analytics**. This part of the claim is consistent with the standard. [AC:3GPP2026Restoration]

**Patents (verified on USPTO front pages; not survey candidates):**

- **US 12,610,253 B2** (Ericsson; PCT filed 2020-07-31; granted 2026-04-21), "NF discovery and selection based on service response latency measurements":
  - consumer NFs report the service-response latency of producers to the NWDAF;
  - the NWDAF computes latency statistics and notifies the NRF for use in discovery and selection.

  This is analytics wired to NRF selection, in patent form.
- **US 12,489,712 B2** (Samsung; priority 2023-03-24; granted 2025-12-02), "Apparatus and method for selecting entity based on data". The SMF selects the serving UPF from AI-estimated UPF load values; the figure shows an NWDAF in the core. AI load prediction is wired to UPF selection.
- **US 12,041,120 B2** (Rakuten Mobile; granted 2024-07-16), "5G SBA communication based on machine learning". The NRF derives load-balance prioritisation from NF registration data and sends it to a service-mesh control plane or SCP, which balances load across NFs.
- **US 11,671,369 B2** (Oracle; filed 2021-07-14; granted 2023-06-06). The SCP derives NF-instance load-control information from producer responses and computes NF-set load information. It then sends this to consumers or uses it to select a producer within an NF set.

**Peer-reviewed papers that wire analytics to *some* actuator (none to NRF/SCP selection or TS 23.527):**

- **SMF consumes NWDAF analytics.** [AC:Ardestani2026Closedloop] (ITU J-FET 2026) and its conference version (Ardestani et al., NOMS 2026, doi:10.1109/noms69089.2026.11668240, verified) extend the SMF to consume NWDAF analytics. The loop is applied to security and QoS, not to NF selection.
- **[GAP:Chen2025Nwdafloadcontrol]** (Chen et al., free5GC World Forum 2025, doi:10.1145/3733814.3765498): NWDAF NF-load forecasts drive a URR threshold to avoid NF overload. This is **NF-load analytics wired to an actuator**, but the actuator is a charging parameter, not selection.
- **[GAP:Tran2026Abnormalbehaviour]** (Tran et al., ICACT 2026, doi:10.23919/icact68090.2026.11431420): NWDAF abnormal-behaviour analytics on operator data drive ping-pong handover prevention. The actuator is mobility, not core NF selection.
- **[GAP:Tran2025Nfloadanalytics]** (Tran et al., ICTC 2025, doi:10.1109/ictc66702.2025.11388576): an NF-load analytics implementation on operator MME data. No actuator is shown.
- **[SB:Zhu2022Disasterbackup]** (CECCC 2022): NWDAF detection of "all UDMs failed" triggers an HSS-as-UDM backup. This is analytics wired to a failover action, but a non-standard one, evaluated by fault-tree analysis only.
- **[AC:Vittal2024Resilientcore]**: an LSTM predicts NF-instance availability and feeds request scheduling in a closed loop. It does not go through the NRF/SCP or NF sets.
- **[GAP:Nguyen2021Cploadbalancing]** (Nguyen et al., EuCNC 2021, doi:10.1109/eucnc/6gsummit51104.2021.9482513): latency-, load- and queue-aware balancing across vMME instances. It uses live metrics, not standard analytics, in a 4G/NSA setting.
- **Adjacent relatives already in the list:** [AC:Chouman2023Amfscaling] (AMF-set load balancing), [AC:Yucebas2025Nrfbottleneck] (NRF as bottleneck), [SB:Sarkar2022Locomotive] (resilient CP load balancer).

### (b) What remains uncovered

- No peer-reviewed paper evaluates NWDAF NF-load, abnormal-behaviour or storm analytics driving **NRF/SCP producer selection or NF-set reselection**, measured on a core.
- No paper links failure analytics to **TS 23.527** restoration procedures (the spec contains no hook).
- The Rel-19 §6.22 actions (SCP redirect, NRF profile update) have **no academic evaluation**.

### (c) Verdict: **partially covered**

The claim holds for the peer-reviewed literature. It is wrong if read as "the wiring does not exist": Rel-19 specifies it for signalling storms, and several patents claim it.

### (d) Suggested rewording

> "Although Rel-19 (TS 23.288 §6.22) already lets NWDAF analytics steer SCP routing and NRF profile priorities, and several patents claim analytics-driven NF selection, we found no peer-reviewed evaluation of analytics-driven NF (re)selection through the NRF/SCP, and no work connecting failure analytics to TS 23.527 restoration or NF-set reselection; the few closed loops that exist act on SMF policy, charging thresholds or handover parameters."

---

## G3 — Core control-plane twins are rare, fidelity is not measured, no twin predicts action outcomes at control-plane speed

### (a) Evidence found

**Core or control-plane twins (confirms "rare", but the list is longer than SUMMARY §4 states):**

- **Already in the list:** [AC:Tao2024Corecontrolplane], [AC:Xie2026Signalingstorm] (Spillway), [AC:Zanzi2026Cloudnativendt], [AC:BenllochCaballero2026Corex], [AC:Mozo2022B5Gemini], [AC:Wang2024Sliceadmission].
- **From the snowball:** [SB:SanzRodrigo2023Mndtmethodology], [SB:Karamchandani2024B5Geminindt], [SB:Petrik2025Dtdomaintransfer], [SB:Chen2026Feasibilityshield].
- **New here:**
  - [GAP:Zheng2022Dtselfrecovery] (Zheng et al., *Digital Twin* journal 2022, doi:10.12688/digitaltwin.17692.1): a 5GC twin used for fault-propagation reasoning, disaster-recovery analysis and closed-loop self-recovery. It reports detection within 1 min, delimitation within 20 min and recovery within 5 min. This is minute-scale, and twin fidelity is not quantified.
  - [GAP:Cakir2026Emulationdt] (Çakır et al., ICC Workshops 2026, doi:10.1109/iccworkshops63917.2026.11586630): an emulation twin of the 5G control plane for automated what-if security experiments.
  - [GAP:RodriguesDS2025Opensourcedt] (ICTON 2025, doi:10.1109/icton67126.2025.11125422) and [GAP:Vasalos2025Ndtframework] (DCOSS-IoT 2025, doi:10.1109/dcoss-iot65416.2025.00139): open-source and testbed-synchronised 5G twins. Neither reports fidelity numbers in its abstract.

**Fidelity *is* measured in several works, in different senses:**

- [AC:Tao2024Corecontrolplane] reports message-sequence F1 above 99.999% against a tester-driven core. This is fidelity of signalling sequences, not of timing or load.
- [AC:AbenAthar2025Whatif] reports twin latency-prediction error against its (emulated) network.
- [SB:Petrik2025Dtdomaintransfer] (ELMAR 2025) shows the accuracy of a 5G-core twin classifier drops significantly on real traffic. This is an explicit sim-to-real gap measurement.
- **Control-plane traffic generators validated against operator traces:**
  - [GAP:Meng2023Smm] (IMC 2023, doi:10.1145/3618257.3624808): a state-machine model of UE control-plane events;
  - [GAP:Kong2024Cptgpt] (IMC 2024, doi:10.1145/3646547.3688422): reduces stateful-semantics violations by two orders of magnitude versus a GAN.
- [GAP:Ntassah2026Llmdtfidelity] (ICC 2026, doi:10.1109/icc59461.2026.11586822) reports twin repeatability and surrogate-to-twin R² of about 0.99. That is not twin-to-reality fidelity.
- [GAP:Tao2025Trustworthydt] (arXiv:2511.19961, 2025; same first author as Tao2024): proposes task-centric twin-fidelity evaluation based on the agent's MDP and applies it on a real wireless testbed.
- [GAP:Tao2024Dtmeasurement] (CloudNet 2024, doi:10.1109/cloudnet62863.2024.10815817): measures how measurement itself perturbs the network and hence twin accuracy.
- [SB:Sengendo2024Ndtsync]: twin synchronisation delay.

**Prediction of a candidate action's outcome before execution:**

- **[GAP:Cakir2026Dthandover]** (Çakır et al., IEEE TNSM 2026, doi:10.1109/tnsm.2026.3690572). A generative twin produces counterfactual short-horizon trajectories for each candidate handover, and **the AMF approves or rejects it via standard signalling before execution**. This is per-decision, control-plane-timescale what-if validation. The action is mobility, not core remediation.
- **[SB:Chen2026Feasibilityshield]** (EuCNC/6G Summit 2026): LLM-proposed remediation in a simulated 6G core passes a feasibility shield and a short-horizon lookahead simulation before execution. The faults are link failures, in simulation only.
- **[AC:Xie2026Signalingstorm]** (Spillway): what-if validation of overload-control configurations at operator scale. It runs in minutes, not per control-plane decision.
- **[AC:Li2024Saferl]** (DT-LNS): pre-checks slicing actions in a twin. [SB:Nardini2024Simu5Gdt]: lockstep and branching what-if analysis (RAN-oriented).

### (b) What remains uncovered

- No core twin reports **interventional (action-conditioned) fidelity**, i.e. how well it predicts the effect of a remediation (reroute, failover) against the real core under a fault.
- No twin covers **NF failover or state/database replication**.
- No twin is exposed via the TS 28.561 management services.
- No core twin predicts **UE-procedure outcomes** of a remediation within control-plane timescales.

### (c) Verdict: **partially covered**

The "rare" part holds. The "fidelity is not measured" and "no twin predicts the outcome of a candidate action at control-plane speed" parts are too strong as worded.

### (d) Suggested rewording

> "Twins of the 5G core control plane remain rare and mostly reproduce message sequences or resource KPIs; where fidelity is reported it is observational (sequence F1, KPI or traffic-distribution error), not interventional. Per-decision what-if validation now exists for mobility actions (AMF-side handover pre-validation) and for link-failure remediation in a simulated 6G core, but no twin predicts, and reports the accuracy of, the outcome of core remediation actions such as NF rerouting or database failover on UE procedures."

---

## G7 — Resilience is disconnected from AI and from geo-redundancy

### (a) Evidence found

**AI or learning for core and NFV resilience (weakens "disconnected from AI"):**

- **Already in the list:** [AC:Vittal2024Resilientcore], [AC:Kawasaki2023Failureprediction], [AC:Basikolo2023Zerodowntime], [AC:Chakraborty2021Failureforecast], [AC:Nam2026Mdaf].
- [GAP:Shaghaghi2022Ztpfr] (IEEE TNSM 2022, doi:10.1109/tnsm.2021.3113054): DRL-based proactive failure recovery of stateful VNFs (simulation).
- [GAP:Woo2025Nfvagent] (CNSM 2025, doi:10.23919/cnsm67658.2025.11297536): a RAG-LLM agent choosing NFV recovery actions (accuracy against labelled events).
- [GAP:Chilukuri2023Sentinel] (COMSNETS 2023, doi:10.1109/comsnets56262.2023.10041318): AI-based self-protection keeping the 5GC CP available under DDoS.
- [GAP:Santos2025Predictivedr] (IWCMC 2025, doi:10.1109/iwcmc65282.2025.11059520): ML-predicted disaster plus selection of the backup instance by migration cost, for 5G O&M systems rather than core NFs.
- [SB:Zhu2022Disasterbackup]: NWDAF-triggered UDM→HSS backup, analytical only.

**Multi-cluster, geo-distributed or cloud-scale failover (weakens "disconnected from geo-redundancy"):**

- [GAP:Nguyen2018Echo] (Nguyen et al., MobiCom 2018, doi:10.1145/3241539.3241564; flagged `seminal`): a reliable distributed core for public clouds with low component availability.
- [GAP:Kurata2024Geostorm] (Kurata et al., NetSoft 2024, doi:10.1109/netsoft60951.2024.10588904): geo-distributed placement and per-UE routing of CP NF instances, aimed at inter-site signalling storms. This is the same KDDI group as [AC:Kurata2025Softguarantee].
- [AC:Leiter2022Upffailover]: ONAP inter-cluster UPF failover.
- [GAP:NguyenTrung2025Upffailover] (Electronics 2025, doi:10.3390/electronics14152991): UPF restoration in the same or another cluster, chosen by resource availability and health.
- [GAP:Wernet2024Upfredirection] (NFV-SDN 2024, doi:10.1109/nfv-sdn61811.2024.10807476): proactive UPF session mirroring and redirection.
- **Snowball works:** [SB:Behnaminia2026Upfrecovery] (UPF restoration plus history-aware selection); [SB:Paul2025Faulttolerantk8S] (fault-tolerant cloud-native core variants, single cluster); [SB:Ahmad2022Cellclone] (CellClone, quorum-replicated CP clones).
- [AC:Ahmad2023Neutrino] and [AC:Janzen2026Islandready].

**State consistency for core data (the closest to UDR/UDSF):**

- [AC:Sovitkar2024Recap] (AMF–UDSF, two nodes) and [SB:Sovitkar2024Capstateless] (CAP trade-off of a stateless core under partition, single site).
- [AC:Larrea2023Corekube] (shared state database).
- [AC:Kurata2025Softguarantee]: keeps procedures running during data-tier outages.
- 3GPP TS 23.527 Rel-19 includes "Restoration of Profiles related to UDR" and UDR restoration during subscriber data migration (verified in ETSI TS 123 527 V19.5.0). These are data-loss and resynchronisation procedures, not replication or failover design.

### (b) What remains uncovered

- No peer-reviewed work quantifies **cross-site UDR/UDSF replication** (synchronous vs asynchronous, primary failover) or the **transient effect of database primary failover on UE procedures** (registration, PDU session) in a 3GPP-compliant core.
- Geo-redundancy studies concern the user plane (UPF), CP placement for storms, or non-standard control-plane redesigns.
- AI resilience work stays at prediction or generic NFV recovery and is not combined with multi-site failover of core NFs plus databases.
- No chaos-style failure campaign on a multi-site 5GC was found.

### (c) Verdict: **partially covered**

The broad claim is too strong. The narrow claim about cross-site subscriber-database failover and UE-procedure impact holds.

### (d) Suggested rewording

> "Learning-based resilience work for the core exists but stops at failure prediction or generic NFV recovery-action choice, and geo-distributed failover studies concern mostly the user plane (UPF), control-plane placement for signalling storms, or non-3GPP control-plane redesigns. None quantifies cross-site replication and primary failover of the subscriber databases (UDR/UDSF) or their transient effect on UE procedures, and none runs failure campaigns on a multi-site 3GPP core."

---

## P1 — The SCP as a telemetry source for analytics, anomaly detection or RCA

### (a) Evidence found (beyond the already-cited 5G-RAD, doi:10.1109/infocomwkshps57453.2023.10226155, and US 12,155,534 B1)

**Standards (verified from ETSI-published text). This is the main new finding for P1:**

- **TS 23.288 Rel-19, Table 6.22.2-8 "SCP Signalling Information"** (ETSI TS 123 288 V19.8.0) defines SCP-sourced NWDAF input data, per NF instance:
  - number of requests sent to an NF service instance, and by an NF instance;
  - successful and failed responses per NF service, with the reasons for failures;
  - failure responses generated by the SCP itself, with reasons;
  - the number of times and the reasons the SCP reselected an NF instance;
  - connection status;
  - average request-to-response time.

  These are collected through Nnf_EventExposure (procedure step 2) for signalling storm analytics. **SCP telemetry as an NWDAF data source is therefore standardised in Rel-19**, though only for the signalling-storm analytics ID.
- **TS 23.501 Rel-19 §6.2.19** (ETSI TS 123 501 V19.9.0): the SCP may optionally expose events on load, delay, error rate and message counts, and the NWDAF can use them.

**Patents (USPTO front pages):**

- **US 11,671,369 B2** (Oracle, 2023): the SCP computes per-instance and NF-set load-control information from producer responses and uses it for producer selection. This uses the SCP as a load-telemetry point.
- **US 11,864,093 B2** (Oracle, 2024): SCPs pass delegated-discovery results so that a downstream SCP can reroute to an alternate producer (also across sites and NF sets) after a routing or processing failure. This is SCP-level failure handling, not analytics.
- **US 11,856,426 B2** (EXFO, 2023): a probe NF subscribes to NWDAF analytics and correlates them with control- and user-plane probe data to identify anomalies. This is RCA-style correlation from probes, not from the SCP.

**Academic: SBI-traffic anomaly detection.** The traffic is sniffed or captured, not taken at an SCP. This is the closest non-SCP relative:

- [GAP:Wehbe2023Http2Anomaly] (5GShield, IFIP Networking 2023, doi:10.23919/ifipnetworking57963.2023.10186410): autoencoder on HTTP/2 SBI features.
- [GAP:Wang2023Graphsequence] (GSAD, ICPADS 2023, doi:10.1109/icpads60453.2023.00230).
- Already in the list: [AC:Tian2023Adseq], [AC:Tan20255Gcguard], [AC:Fritz2025Granomaly].

All of these detect attacks or misbehaviour. None localises a performance fault or evaluates a remedy.

**Academic: tracing, meshes and observability of the 5GC:**

- [AC:Zhao2026Tracerca]: RCA from distributed traces of 5GC procedures on real traffic. This is the nearest RCA relative.
- [AC:Atalay2024Meshoverhead]: a sidecar mesh with OpenTelemetry/Jaeger, used to measure overhead only.
- [AC:Aldas2023Servicemesh]: SCP-like indirect communication mapped onto Envoy.
- [GAP:Atalay2025Servicemesh5Gc] (5G-STREAM, DSN 2025, doi:10.1109/dsn64029.2025.00025): a 5GC-tailored mesh for lower NRF signalling, not used for telemetry.
- [GAP:Raffeck2026Signallingobservability] (NetSoft 2026, doi:10.1109/netsoft70012.2026.11603420): per-UE, per-NF signalling observability inside Open5GS NFs.
- [GAP:Issa2026Telegan] (IEEE Access 2026, doi:10.1109/access.2026.3699648): anomaly detection on production 5GC NF and interface counters.
- [SB:Araujo2026Scope5G]: a synthetic AMF dataset with no SBI or SCP traces.

### (b) What remains uncovered

- No peer-reviewed work uses SCP-observed per-producer request outcomes and latencies for **root-cause localisation of non-security faults** (e.g. a degraded shared back-end such as UDR), or for **deciding whether rerouting at the SCP would help**.
- No evaluation of the Rel-19 SCP signalling-information input exists.

### (c) Verdict: **partially covered**

The *idea* of the SCP as an analytics data source is now standard (Rel-19) and patented in several variants. Its use for RCA and remedy evaluation is unpublished.

### (d) Suggested rewording for the companion paper

> "Rel-19 already lists SCP signalling information (per-producer request counts, failures, reselections and response times) as NWDAF input for signalling-storm analytics (TS 23.288, Table 6.22.2-8), and prior work used the SCP to validate message sequences against attacks (5G-RAD) or to export topology and load information (patents). To our knowledge we are the first to use SCP-observed per-producer outcomes to localise non-security faults and to decide whether SCP-level rerouting can help."

Avoid "first to use the SCP as a telemetry source".

---

## P2 — Testing whether a remedy can help before applying it

### (a) Evidence found

**Ranking or validating candidate mitigations by predicted effect (closest prior art, outside the 5GC):**

- **SWARM** (Namyar et al., arXiv:2305.13792, verified; published at NSDI 2025 according to the USENIX programme found by web search). For each datacenter-network failure it estimates the connection-level performance impact of every candidate mitigation and picks the best. This is the strongest prior art for "check whether the action helps before applying it", in datacenter networks. It is not a survey candidate: the arXiv version is from 2023 and USENIX papers have no DOI.
- [GAP:Cai2026Guardedact] (GuardedAct, arXiv:2609.11264, 2026): a digital-twin sandbox estimates the blast radius of each LLM-proposed remediation and auto-executes only low-risk ones. It is evaluated on microservices. It models **risk of harm, not whether the action removes the cause**.
- [SB:Chen2026Feasibilityshield]: a short-horizon lookahead simulation before executing LLM remediation in a simulated 6G core (link failures).
- [GAP:Cakir2026Dthandover]: counterfactual twin pre-validation of each handover decision at the AMF.
- [AC:Xie2026Signalingstorm] (Spillway): simulation of candidate overload-control configurations before deployment, at operator scale.
- [AC:Li2024Saferl] (DT-LNS): twin pre-check of slicing actions.
- [SB:Nardini2024Simu5Gdt]: branching what-if analysis.
- [SB:Yu2023Dtselfhealing] (JSAC 2023): a GNN twin evaluates service redeployment.
- Gao et al. (arXiv:2608.15016, 2026, verified) validate recovery commands for enterprise-network security incidents in an emulated twin. Mentioned only; not added.

**Mitigation recommendation and change verification (operators and clouds):**

- [GAP:Ahmed2023Mitigationllm] (ICSE 2023, doi:10.1109/icse48619.2023.00149): LLM-recommended root causes and mitigations for more than 40k Microsoft incidents, with no effectiveness check before application.
- [GAP:Li2025Panacea] (AIOps 2025, doi:10.1109/aiops66738.2025.00008): orchestrated "safe" cross-layer mitigation of gray failures in production.
- [GAP:Mahimkar2021Cornet] (SIGCOMM 2021, doi:10.1145/3452296.3472901): operator change management with change-impact verification on 4G/5G. Verification happens after deployment.
- Mahimkar et al.'s Auric (SIGCOMM 2021, doi:10.1145/3452296.3472906) and Aurora (IMC 2022, doi:10.1145/3517745.3561455): configuration recommendation, not remediation.
- [GAP:Woo2025Nfvagent]: recovery-action choice scored against labels.
- [AC:Chen2024Rcacopilot] and [AC:Wang2024Rcagent]: LLM RCA.

### (b) What remains uncovered

- No work, in the 5GC or elsewhere in telecom, tests **before acting** whether a candidate remedy can address the actual cause. The motivating case is rerouting among NF instances that share a degraded back-end (UDR/UDSF), where rerouting cannot help.
- Existing pre-checks estimate collateral risk (GuardedAct), aggregate performance (SWARM, Spillway) or mobility outcomes (Çakır). They do not reason about shared-dependency causality in the SBA.

### (c) Verdict: **partially covered**

The general principle (predict or validate an action's effect before applying it) has clear prior art. The specific 5GC formulation does not.

### (d) Suggested rewording

> "Prior work ranks or sandbox-checks candidate mitigations by predicted impact or blast radius (e.g. SWARM for datacenter networks, twin-gated LLM remediation for microservices and simulated 6G cores, Spillway for overload configurations). We address a question these do not: whether a 5G-core remedy such as SCP/NRF rerouting can help at all when the fault lies in a dependency shared by all candidate producers, and we test this before acting."

---

## P3 — Procedure-level models of UE procedures under faults that predict UE-level outcomes (T3510 expiry, retries)

### (a) Evidence found

**The closest prior art:**

- **[GAP:Nakao2025Comebacklater]** (Nakao, IEEE Globecom Workshops 2025, doi:10.1109/gcwkshps68340.2025.11590969). It frames AMF signalling storms as causing widespread registration failures and notes that static NAS retry timers (T3510, T3346) are ineffective under load. It adds a "come back later" SCTP signal that tells UEs when to retry. With 500 UEs, registration time drops from 35.7 s to 11.6 s on free5GC.
- **[GAP:Nakao2026Admissionpacing]** (Nakao, FiNE 2026, doi:10.1109/fine71157.2026.00029). An AMF admission gate with an LLM agent tuning the threshold and retry interval in a real 5GC. Against uncoordinated NAS retries it measures convergence speed, gNB drop churn and tail non-convergence. It also identifies that a retry interval can exceed the **UE registration deadline** while telemetry looks quiet.

  This is experimental, UE-outcome-level evidence for overload storms. It is not a predictive model, and it does not cover NF or back-end faults.
- **[GAP:Hezaveh2026Astrotimer]** (Rezaie Hezaveh & Hu, ICC 2026, doi:10.1109/icc59461.2026.11587804): a **closed-form model** for sizing NAS watchdog and back-off timers for 5G registration over LEO satellites from link variability, processing delays and NF placement. In simulation it reduces registration time, retry frequency and UE energy.
- [GAP:Liu2026Nastimer] (arXiv:2607.21947, 2026): extends AstroTimer to per-UE timers, with AMF queueing exposure as an input; it predicts registration attempts.

  These are **procedure-level timer models predicting UE-level attempts and latency**, but the stressor is propagation delay in NTN, not core faults.

**Older and adjacent models:**

- Gorbil et al., "Storms in mobile networks" (Q2SWinet 2014, doi:10.1145/2642687.2642688, verified; pre-2020): a mathematical (Markov) model plus simulation of RRC signalling storms in 3G/4G. Not added: pre-2020.
- [SB:Kato2023Reconnectionstorm] (VTC 2023): the reconnection storm after large failures, with an aggregate UE model.
- [GAP:Meng2023Smm] and [GAP:Kong2024Cptgpt]: models of UE control-plane event sequences under normal operation.
- [GAP:Goshi2025Mmtcmodel] (IEEE TNSM 2025, doi:10.1109/tnsm.2024.3481240): an analytical arrival model at the core.
- [GAP:Li2022Petrinet] (ICIN 2022, doi:10.1109/icin53892.2022.9758134): a Petri-net availability model of NFV 5G.
- [AC:DeSimone2025Performability] and the CNSM 2025 M/G/k queueing model of 5G SFCs (Di Mauro & Peluso, doi:10.23919/cnsm67658.2025.11297502, verified; same group). Both model latency and availability, not UE timers.
- **Generic retry-collapse (metastable failure) models:**
  - [GAP:Habibi2024Metastablemodel] (MSF-Model, SRDS 2024, doi:10.1109/srds64841.2024.00013): a queueing model predicting metastable failures;
  - [GAP:Isaacs2025Metastableanalysis] (HotOS 2025, doi:10.1145/3713082.3730380): queueing models, DES and emulation to predict vulnerability;
  - Bronson et al. (HotOS 2021, doi:10.1145/3458336.3465286, verified): the problem framing.

  These are transferable methods for retry storms after failover, but they are not telecom.

**Measurements and detection of registration under stress:**

- [GAP:Chen2024Registrationperf] (APWCS 2024, doi:10.1109/apwcs61586.2024.10679317): duplicate registration requests at the AMF.
- [GAP:S2025Open5Gsperf] (COMSNETS 2025, doi:10.1109/comsnets63942.2025.10885600): more than 50k emulated UEs, with public traces.
- [GAP:Raffeck2026Signallingobservability]: attach performance and AMF stability under load.
- [GAP:Gopikrishnan2023Registrationad] (CSCN 2023, doi:10.1109/cscn60443.2023.10453203): anomaly detection on NF metrics during registration.
- [GAP:Hayashi2025Retrydetection] (NOMS 2025, doi:10.1109/noms57970.2025.11073597): detects operator failures from surges of user reconnection signalling. Retries are used as a symptom, not predicted.
- **Patent US 12,641,481 B2** (Boost SubscriberCo, 2026; USPTO front page): a RIC monitors registration messages, detects a storm and alters RAN treatment of registrations.

### (b) What remains uncovered

- No model of the **multi-NF 5G registration chain** (AMF–AUSF–UDM–UDR via SCP) under **NF or back-end faults** (degradation, failover) that predicts UE-visible outcomes: T3510 expiries, retry counts and amplification, registration success within the deadline.
- No such model validated against a running 3GPP core.
- The existing timer models target NTN propagation. The existing storm work is either experimental (Nakao) or aggregate (Kato, Gorbil).

### (c) Verdict: **partially covered**

The claim holds only in its narrow form: core faults, multi-NF procedure chain, validated prediction.

### (d) Suggested rewording

> "Prior work models NAS timers and registration attempts for satellite access (AstroTimer), measures NAS-retry dynamics under AMF registration storms (Nakao, 2025-2026), and models RRC or reconnection storms at aggregate level. To our knowledge no model predicts UE-level registration outcomes (T3510 expiry, retry amplification, completion within the registration deadline) from the multi-NF SBA call chain under NF or back-end faults, validated against a running 3GPP core."

---

## P4 — Multi-action remedies in a multi-site core and the transient cost of database failover

### (a) Evidence found (adjacent only)

- [GAP:Kurata2024Geostorm] (NetSoft 2024): joint geo-distributed placement and per-UE routing of CP NF instances, aimed at storms. Simulation only, with no failure-triggered choice between actions.
- [GAP:NguyenTrung2025Upffailover] (Electronics 2025): chooses intra- versus inter-cluster UPF restoration by resources and health. This is a two-option decision for the user plane, measured on redeployment time and cost.
- [GAP:Santos2025Predictivedr] (IWCMC 2025): chooses a backup among redundant candidates using migration cost (O&M systems).
- [GAP:Shaghaghi2022Ztpfr] and [GAP:Woo2025Nfvagent]: learned recovery-action choice for generic NFV.
- Shang et al., "Rerouting Strategies for Highly Available Virtual Network Functions" (IEEE TCC 2021, doi:10.1109/tcc.2019.2925110, verified): local and supplementary rerouting of SFCs around failed points of presence. Not added: generic SFC.
- **Patent US 11,864,093 B2** (Oracle): SCP alternate routing across sites and NF sets after failure.
- [AC:Sovitkar2024Recap] and [SB:Sovitkar2024Capstateless]: consistency/availability trade-off of the state store at a single site. [AC:Kurata2025Softguarantee]: keeps procedures alive during data-tier outages.
- Grey literature: a vendor press item (ZTE NetTwinGuard) claims twin simulation of resource-pool disaster-recovery switchover; see Unverified leads.

### (b) What remains uncovered

- No study compares **stay / reroute NFs / fail over the database** as alternative remedies in a multi-site 3GPP core.
- No study measures the **transient cost of database (UDR/UDSF) primary failover** on UE procedures: registration and session failures, retries, timer expiries during promotion and resynchronisation.

### (c) Verdict: **holds**

Cite the adjacent works above to show awareness.

### (d) Suggested wording (minor tightening)

> "To our knowledge this is the first evaluation of alternative remedies (stay, reroute NFs, fail over the subscriber database) in a multi-site 3GPP core that also quantifies the transient cost of database primary failover on UE procedures; prior work chooses between restoration locations for the user plane, places control-plane NFs geographically against storms, or selects generic NFV recovery actions."

---

## Unverified leads (not used as evidence)

| Lead | Why unverified / not used |
|---|---|
| WO 2025/216683 A1, "Network data analytics function assisted detection and mitigation of network function anomaly" (Google Patents result) | Google Patents throttled my requests and the USPTO image server has no WO publications. The title suggests NWDAF→NF anomaly mitigation (G2), which would be relevant. |
| US 12,349,050 B2 (prioritised alternate NF instances in NF profiles), US 12,095,628 B2 (ML prediction of network abnormalities; SCP only in background), US 2021/0367854 A1 (SCP relaying NWDAF data collection), US 11,259,196 B2 / US 12,219,377 B2 (AT&T, assessing the impact of cellular network changes) | Seen only in web-search snippets; front pages not read. |
| ZTE "NetTwinGuard" (vendor news: core-network storm defence; simulation of resource-pool disaster-recovery switchover; reported accuracy above 95%) | Vendor marketing, not peer-reviewed. Relevant to G3/P4 as grey literature only. |
| TDCommons defensive publication on twin-validated remediation (web-search snippet) | Not peer-reviewed; content not read. |
| "5G Control Plane Congestion Mitigation by Pre-slice Priority Control and AMF Delay Analysis" (Nha & Nakao, IEICE technical report) | Technical report (not peer-reviewed); not read. The related GC Workshops 2025 paper (doi:10.1109/gcwkshps68340.2025.11590958) was found but not added. |
| "Mitigating Signalling Storms in 5G" (University of Waterloo, UWSpace) | Thesis (excluded by PROTOCOL §3). |
| CNSM 2023 paper at dl.ifip.org (`1570935488.pdf`), linked from the storm search | The PDF did not download; title unknown. |
| SWARM venue (NSDI 2025) | The arXiv ID is verified; the NSDI publication is from the USENIX programme page seen in web search and has no DOI. |
| Colosseum (Polese et al., OJCOMS 2024, doi:10.1109/ojcoms.2024.3447472, verified) as evidence of measured twin fidelity | DOI verified, but the abstract describes twinning pipelines without stating a fidelity measurement, so it is not used for G3. |
| MicroRCA [AC:Wu2020Microrca] as service-mesh-telemetry RCA prior art | I recall it uses service-mesh metrics, but the stored summary and the abstract I saw do not say so; not used for P1. |
| 3GPP TR 23.791 (Rel-16 NWDAF study: SMF requests UPF load from NWDAF for UPF selection), TR 23.700-84 statement that SCP as an input source is left to normative work | Seen only via third-party spec mirrors in web search; not read from 3GPP/ETSI. The normative Rel-19 text I did read (TS 23.288 §6.22) already supports the point. |
| Semantic Scholar keyword search | HTTP 429 for the whole session; only single-paper lookups worked. Recall from that index is therefore missing. |

## Search log

Hits are the number of records returned and screened by title. Abstracts were then read, through OpenAlex/Crossref/Semantic Scholar single lookups or the arXiv API, for about 110 candidates.

| Claim | Source | Query | Hits |
|---|---|---|---|
| P1 | Crossref | service communication proxy | 20 |
| P1 | Crossref | service communication proxy 5G core monitoring analytics | 20 |
| P1 | Crossref | service communication proxy performance evaluation 5G | 20 |
| P1 | Crossref | indirect communication 5G core SCP | 20 |
| P1 | Crossref | SCP load balancing 5G core evaluation | 20 |
| P1 | Crossref | service mesh 5G core telemetry anomaly | 20 |
| P1 | Crossref | service mesh root cause localization microservices | 20 |
| P1 | Crossref | Istio metrics anomaly detection microservices | 20 |
| P1 | Crossref | 5G core network function interaction anomaly detection | 20 |
| P1 | Crossref | HTTP/2 service based interface 5G core traffic analysis | 20 |
| P1 | Crossref | signalling storm 5G core detection | 20 |
| P1 | arXiv | abs:"service communication proxy" | 1 |
| P1 | arXiv | abs:"service mesh" AND abs:"5G core" | 0 |
| P1 | arXiv | all:"service mesh" AND all:5G | 2 |
| P1 | arXiv | all:SCP AND all:5G AND all:core | 2 |
| P1 | arXiv | abs:"5G core" AND abs:"root cause" / all:5G AND all:core AND all:"root cause" | 2 / 4 |
| P1 | arXiv | abs:"5G core" AND abs:telemetry AND abs:anomaly | 1 |
| P1 | arXiv | abs:"service-based interface" AND abs:anomaly; abs:"5G core" AND abs:"distributed tracing" | 0; 0 |
| P1 | Semantic Scholar | 7 queries (service communication proxy anomaly / monitoring; service mesh telemetry; Istio; sidecar; Envoy; SBI HTTP/2) | failed (HTTP 429) |
| P1 | Web | "service communication proxy" anomaly detection telemetry; patent SCP NWDAF data collection root cause; service mesh Istio Envoy 5G core fault localization; patent SCP detect anomaly ML; Google Patents SCP RCA; NWDAF signalling storm analytics SCP evaluation | ~9 results each |
| G2 | Crossref | NWDAF network function load analytics selection | 20 |
| G2 | Crossref | NF selection NRF load aware 5G core | 20 |
| G2 | Crossref | UPF selection NWDAF analytics | 20 |
| G2 | Crossref | SMF selection NWDAF load | 20 |
| G2 | Crossref | AMF selection load balancing NWDAF | 20 |
| G2 | Crossref | NWDAF abnormal behaviour analytics mitigation | 20 |
| G2 | Crossref | network function discovery selection machine learning 5G | 20 |
| G2 | Crossref | NWDAF closed loop AMF overload | 20 |
| G2 | Crossref | 5G core overload control NWDAF | 20 |
| G2 | Crossref | NF set reselection 5G core failure | 20 |
| G2 | Crossref | AMF set failure UE re-registration | 20 |
| G2 | Crossref | MME pool failure impact signaling | 20 |
| G2 | Crossref | HSS outage impact mobile network subscribers | 20 |
| G2 | Crossref | cellular core network outage measurement study | 20 |
| G2 | Web | NWDAF "NF load" NF selection NRF SCP testbed; load-aware NF selection NRF RL; Oracle SCP overload alternate routing NWDAF patent; NWDAF analytics-assisted UPF/SMF/AMF selection free5GC Open5GS | ~9 results each |
| G2 | Standards | ETSI TS 123 288 V19.8.0, TS 123 501 V19.9.0, TS 123 527 V19.5.0 full-text grep (NF load analytics, SCP, NWDAF, selection, UDR, geo) | n/a |
| G3 | Crossref | digital twin 5G core control plane | 20 |
| G3 | Crossref | digital twin 5G core network fidelity | 20 |
| G3 | Crossref | network digital twin fidelity measurement | 20 |
| G3 | Crossref | digital twin what-if analysis 5G core | 20 |
| G3 | Crossref | digital twin validation network configuration change before deployment | 20 |
| G3 | Crossref | network digital twin accuracy synchronization evaluation | 20 |
| G3 | Crossref | 3 title look-ups (Colosseum; DCOSS NDT framework; OTA testbed twin) | 20 each |
| G3 | Web | LLM-guided DT fidelity (title); NDT fidelity metric twin vs physical 5G testbed; "digital twin" "5G core" failover what-if recovery | ~9 results each |
| G7 | Crossref | geo-redundant 5G core | 20 |
| G7 | Crossref | geographic redundancy mobile core network failover | 20 |
| G7 | Crossref | UDR replication 5G core | 20 |
| G7 | Crossref | unstructured data storage function UDSF 5G | 20 |
| G7 | Crossref | 5G core state database failover | 20 |
| G7 | Crossref | subscriber database replication HSS geo-redundancy | 20 |
| G7 | Crossref | multi-site 5G core disaster recovery | 20 |
| G7 | Crossref | 5G core network function failure recovery time measurement | 20 |
| G7 | Crossref | AMF failure UE context recovery | 20 |
| G7 | Crossref | chaos engineering 5G core | 20 |
| G7 | Crossref | fault injection 5G core resilience | 20 |
| G7 | Crossref | multi-cluster 5G core failover Kubernetes | 20 |
| G7 | Crossref | multi-cloud 5G core deployment resilience | 20 |
| G7 | Crossref | distributed 5G core edge cloud failure resilience session continuity | 20 |
| G7 | Crossref | 5G core control plane failure impact user equipment registration | 20 |
| G7 | Crossref | ECHO reliable distributed cellular core (2 variants) + filtered Crossref query | 20 + 5 |
| G7 | Web | fault-tolerant cellular core state replication geo-distributed (ECHO, Neutrino); Vutukuru fault-tolerant 5G core state replication | ~9 results each |
| P2 | Crossref | mitigation recommendation cloud incidents | 20 |
| P2 | Crossref | incident mitigation large-scale cloud systems automatic | 20 |
| P2 | Crossref | counterfactual network digital twin | 20 |
| P2 | Crossref | what-if analysis remediation action network | 20 |
| P2 | Crossref | pre-validation network change digital twin safe action | 20 |
| P2 | Crossref | safe action selection network management digital twin reinforcement learning | 20 |
| P2 | Crossref | change verification cellular network operator | 20 |
| P2 | Crossref | action effect prediction network self-healing | 20 |
| P2 | Crossref | 3 title look-ups (DT handover; SWARM; NetPilot) | 20 each |
| P2 | Web | SWARM mitigation ranking; evaluate remediation before applying (5G core / telecom); Mahimkar AT&T change management (Auric, CORNET); DT validate remediation LLM sandbox | ~9 results each |
| P3 | Crossref | 5G registration procedure model queueing | 20 |
| P3 | Crossref | registration procedure latency model 5G core analytical | 20 |
| P3 | Crossref | attach procedure Markov model MME failure | 20 |
| P3 | Crossref | T3510 timer | 20 |
| P3 | Crossref | NAS retransmission timer 5G registration failure | 20 |
| P3 | Crossref | signaling storm model mobile core analytical | 20 |
| P3 | Crossref | AMF overload model queueing | 20 |
| P3 | Crossref | Petri net model 5G registration procedure | 20 |
| P3 | Crossref | retry storm cellular network signaling | 20 |
| P3 | Crossref | MME overload control model LTE attach | 20 |
| P3 | Crossref | NAS timer non-terrestrial network registration | 20 |
| P3 | Crossref | NAS timer optimization 5G satellite registration | 20 |
| P3 | Crossref | registration burst LEO satellite AMF 5G core | 20 |
| P3 | Crossref | 5G registration procedure satellite non-terrestrial core network delay timer | 20 |
| P3 | Crossref | metastable failures distributed systems retry; metastable failure modeling retry storm | 20; 20 |
| P3 | Crossref | 3 title look-ups (AstroTimer; Storms in mobile networks ×2; SMM) | 20 each |
| P3 | Web | "Come Back Later" Nakao; model of UE registration retries T3510 T3511 storm; Peng Hu NAS timer closed-form model | ~9 results each |
| P4 | Crossref | NFV failure recovery action selection reinforcement learning | 20 |
| P4 | Crossref | remediation action selection network function failure 5G | 20 |
| P4 | Crossref | proactive failure recovery stateful NFV | 20 |
| P4 | Crossref | joint failover rerouting decision virtual network functions | 20 |
| P4 | Crossref | VNF state migration failover cost transient | 20 |
| all | Snowball pools | regex over titles of pool_C1/C2/C3/C45 (SCP, mesh, geo, replication, failover, registration, NAS, timer, retry, storm, what-if, mitigation, fidelity, NRF, chaos, MME, …) | 64 matching titles screened |
| all | Patents (USPTO front pages read) | US 12,155,534 (via Google Patents); 12,041,120; 12,489,712; 12,610,253; 11,671,369; 11,864,093; 11,856,426; 12,641,481 | 8 verified |
