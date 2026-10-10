# DECISIONS

Judgement calls made while executing `PROTOCOL.md` (autonomous run, no questions asked).

## Process / infrastructure

- **Git branch.** The protocol says push to `main`; this cloud session is configured to develop and push only on
  `claude/5g-6g-literature-search-2lyo41`, and pushing elsewhere requires separate permission. All commits are
  pushed to that branch; merge it into `main` (or open a PR) when you are happy with the results.
- **No `PILOT_REPORT.md`.** The protocol requires it only if the APIs are blocked. They are not (see `STATUS.md`),
  so every main-list entry is verified individually and none is `search-only`.
- **Metadata is machine-filled.** `tools/verify.py build` fills title, authors, year, venue, DOI/URL and citation
  counts from Crossref / arXiv / 3GPP portal. Subagents write only the identifiers and the analytical fields
  (summary, method, critique ...) into `work/S<n>.jsonl`. This makes typos or invented metadata impossible in the
  main lists; any identifier that fails to resolve or whose title does not match the intended paper goes to
  `results/S<n>_unverified.csv` (merged into `unverified.csv` in Phase 3).
- **arXiv over HTTPS.** `http://export.arxiv.org` redirects (301); `https://export.arxiv.org` is used.
- **OpenAlex search budget exhausted** for the shared IP; literature discovery uses web search + Crossref
  bibliographic search instead. OpenAlex is used only for per-DOI citation counts (still working).
- **Citation counts** are OpenAlex `cited_by_count` (fallback: Semantic Scholar) on the retrieval date given in
  `citations_date`; they differ from Google Scholar and IEEE Xplore counts.
- **BibTeX keys** are `FirstAuthorSurname + Year + Keyword` (ASCII), suffixed a/b/... on collision.
- **Venue type** for a DOI defaults to Crossref's type (journal-article → journal, proceedings-article →
  conference) unless the subagent overrides it.
- **Phase 2 parallelism.** 8 subagents run in parallel; to avoid git conflicts only the orchestrator commits and
  pushes, immediately after each subagent finishes.

## Subdomain-level decisions

(appended by each subdomain run; see the sections below)

### S8 (subagent decisions)

# S8 — AI/ML models for network performance prediction: decisions

## Search queries run
Crossref (`verify.py search`): "RouteNet graph neural network network modeling"; "Graph neural networks for communication
networks context use cases opportunities"; "graph-based deep learning for communication networks survey"; "deep learning
mobile traffic forecasting survey"; "cellular traffic prediction machine learning survey"; "MimicNet fast performance
estimates data center networks machine learning"; "DeepQueueNet"; "m3 accurate flow-level performance estimation machine
learning"; "network digital twin graph neural network 5G"; "graph neural network 6G network digital twin"; "building a
digital twin for network optimization using graph neural networks"; "TwinNet digital twin graph neural network queuing";
"data-driven network modeling digital twin graph neural network survey"; "safe reinforcement learning network slicing";
"constrained reinforcement learning network slicing"; "OnSlicing online end-to-end network slicing reinforcement learning";
"Atlas automate online service configuration network slicing"; "digital twin assisted safe reinforcement learning network";
"safe deep reinforcement learning 5G core resource"; "transformer 5G traffic prediction"; "mobile traffic forecasting
transformer IEEE Transactions"; "spatio-temporal graph neural network cellular traffic prediction"; "deep transfer learning
cellular traffic prediction cross-domain"; "mobile network traffic prediction large language model"; "network traffic
foundation model"; "Global-scale mobile traffic foundation model"; "NetLLM adapting large language models for networking";
"large language models for networking survey"; "VNF resource prediction graph neural network"; "graph neural network SFC VNF
placement latency prediction"; "5G core network function resource prediction machine learning"; "5G core UPF performance
prediction machine learning"; "5G core network KPI forecasting deep learning"; "AMF load prediction 5G core autoscaling";
"ML-based 5G core network load forecasting with metrics from performance measurement"; "LLM network traffic prediction 5G
core"; "generalization graph neural network network performance unseen topologies"; "RouteNet generalization 5G";
"network calculus graph neural network delay"; "machine learning network performance modeling survey".
WebSearch: "graph neural network 5G core network digital twin performance prediction 2024 IEEE"; "foundation model mobile
network traffic forecasting 2025 large language model cellular traffic prediction"; "safe reinforcement learning network
management survey IEEE Communications Surveys Tutorials constrained"; "machine learning performance modeling 5G core network
functions UPF AMF resource prediction TNSM 2024 OR 2025". Abstracts were read via OpenAlex abstract index, arXiv abstract
pages (WebFetch) and search snippets.

## Judgement calls
- Query evolution: generic GNN/RouteNet queries return mostly wired/SDN/data-center work; 5G-core-specific ML prediction
  had to be found with NF-level terms (AMF, UPF, Kubernetes scaling, PM metrics). No GNN-based performance model of the 5G
  core control plane (SBA signalling) in a strong venue was found — recorded as a gap.
- RouteNet (JSAC 2020) kept and flagged `seminal` as allowed by the task. RouteNet-Erlang (INFOCOM 2022,
  10.1109/infocom48880.2022.9796944) dropped in favour of its journal successor RouteNet-Fermi (ToN 2023).
- MimicNet, DeepQueueNet, OnSlicing (and Atlas) have Crossref titles that contain only the system name; expected_title was set to
  that short name so the guard passes. The full titles are "MimicNet: Fast Performance Estimates for Data Center Networks with
  Machine Learning", "DeepQueueNet: Towards Scalable and Generalized Network Performance Estimation with Packet-Level
  Visibility" and "OnSlicing: Online End-to-End Network Slicing with Reinforcement Learning" — the orchestrator may wish to
  restore them in the merged CSV/BibTeX.
- Data-center learned simulators (MimicNet, DeepQueueNet, m3) are relevance 2: methods transferable to core-network digital
  twins, but evaluated only on data-center topologies.
- "Digital Twin for Networking: A Data-Driven Performance Modeling Perspective" (IEEE Network 2023) flagged `survey`
  (it reviews and compares data-driven performance models); possible overlap with S3.
- Wang et al. GNN-based DT for slicing (TII) has Crossref year 2022 (issue year), online 2020 — kept as 2022.
- Safe/constrained RL: kept OnSlicing (CoNEXT 2021, real OAI testbed incl. core domain), DT-LNS (IoT-J 2024) and the FGCS 2024
  5G-core slice admission work. Rejected: Liu et al. ICNP 2020 constrained RL slicing (simulation, superseded by OnSlicing
  line), Atlas (CoNEXT 2022, 10.1145/3555050.3569115 — same group as OnSlicing; dropped to stay within ~22 items, a good
  backup), VTC 2023 safe RL slicing (weaker venue), several SSRN/TechRxiv/Research Square posted-content items (not peer-reviewed).
- Transfer learning: Zhang et al. JSAC 2019 "Deep Transfer Learning for Intelligent Cellular Traffic Prediction Based on
  Cross-Domain Big Data" (10.1109/jsac.2019.2904363, ~376 cites) is a strong seminal backup but pre-2020; generalisation is
  covered instead by RouteNet-Fermi, TwinNet and Farreras et al. (NOMS 2022). QT-RouteNet (ITU J-FET 2022) not included.
- Foundation models: NetLLM (SIGCOMM 2024) and MobiGPT (arXiv 2509.18166, Sept 2025, flagged `preprint`, no DOI version
  found). Other LLM traffic-prediction papers (FDALLM+ IoT-J 2025, MobileLLM TMC 2026, Shokouhi & Wong GLOBECOM 2024) were
  seen but not included; GNNet 2024 workshop "Towards a Graph-based Foundation Model for Network Traffic Analysis" not
  included (workshop).
- ICC Workshops 2025 "Network Digital Twin for Route Optimization in 5G/B5G Transport Slicing with What-If Analysis"
  (10.1109/iccworkshops67674.2025.11162404) verified but dropped (workshop paper, transport domain) — backup candidate.
- Standard: ITU-T Y.3172 (06/2019) included as the single allowed standard (relevance 1, flagged seminal+standard);
  verified by WebFetch of https://www.itu.int/rec/T-REC-Y.3172 (title confirmed, version 06/19 in force).
- Tool note: `tools/verify.py build` crashes in `bibentry()` because `year` from Crossref is an int
  (`v.startswith`). I did NOT edit the shared tool; I ran the build through a wrapper that casts year to str before
  calling `bibentry` (scratchpad `s8/run_build.py`). The orchestrator should fix line ~219 (use `str(v)`).
- (orchestrator) `tools/verify.py` now accepts a full expected title when Crossref stores only the system-name prefix
  (`<Name>:` pattern, ACM records); MimicNet, DeepQueueNet and OnSlicing now carry their full published titles.

### S4 (subagent decisions)

# S4 — Root-cause analysis and anomaly detection: decisions

## Queries run
Crossref (`verify.py search`): "AIOps survey failure management"; "root cause analysis microservices survey";
"anomaly detection 5G core network"; "root cause analysis 5G core network functions"; "fault diagnosis network
function virtualization machine learning"; "alarm correlation telecommunication network root cause"; "MicroRCA root
cause localization microservices"; "Eadro multi-source data troubleshooting microservices"; "Nezha interpretable
fine-grained root causes"; "large language models root cause analysis cloud incidents"; "RCAgent autonomous agent
root cause analysis cloud"; "PDiagnose BARO multi-source root cause"; "CIRCA causal inference root cause analysis";
"graph neural network root cause localization microservice"; "KPI anomaly detection cellular network"; "log anomaly
detection deep learning survey"; "anomaly detection network function virtualization VNF failure prediction";
"signaling storm detection 5G"; "AIOps survey cloud intelligence"; "anomaly detection mobile network survey machine
learning"; "anomaly detection and failure root cause analysis microservice-based cloud applications survey"; "survey
AIOps large language models"; "fault localization microservices survey"; "self-healing cellular networks survey fault
management"; "machine learning network fault management survey"; "root cause analysis telecom network machine learning
knowledge graph"; "fault detection 5G network function virtualized core deep learning"; "anomaly detection cloud-native
network functions Kubernetes"; "network slice anomaly detection 5G"; "digital twin root cause analysis 5G";
"explainable AI anomaly detection 5G network"; "large language model telecom fault diagnosis"; "failure prediction
virtual network functions logs"; "Causal Inference-Based Root Cause Analysis for Online Service Systems with
Intervention Recognition"; "Reasoning Language Models for Root Cause Analysis in 5G Wireless Networks"; "TN-AutoRCA
alarm root cause telecom benchmark"; "anomaly detection 5G core control plane graph neural network transactions";
"root cause analysis cloud-native 5G core observability tracing"; "failure prediction 5G core ... ITU journal";
"reasoning language models root cause analysis 5G TeleLogs"; "eBPF 5G core tracing anomaly localization".
WebSearch: RCA 5G core TNSM 2024-2025 cloud-native; 5G core anomaly dataset Open5GS/free5GC fault injection;
LLM RCA telecom 2025; exact-title searches for 5GC-Trace-RCA, the GLOBECOM 2025 optimal-transport paper, the NOMS 2026
MDAF paper, APGNN and the Big Data Research VNF-log paper.
Abstracts were read through OpenAlex/Crossref/Semantic Scholar APIs and arXiv (IEEE Xplore and ScienceDirect block
direct fetching).

## How the queries changed
- Generic "root cause analysis microservices" queries in Crossref return many low-quality posted-content items
  (SSRN, TechRxiv, Preprints.org, Research Square) and predatory-looking journals; switched to exact-title queries
  for known high-impact works (ICSE/FSE/EuroSys/CIKM/KDD/ASE) and to "5G core" specific phrasing.
- "Signalling storm" queries only returned RAN/O-RAN RRC storm work (ISCC 2025, NOMS 2026 RAID) and minor venues —
  nothing on core-side signalling-storm detection in a good venue; not included (gap).

## Inclusions / judgement calls
- 23 rows, all verified: 4 surveys, 13 relevance-3 5G-core works (incl. 1 preprint), 6 relevance-2 works
  (2 telecom, 5 generic cloud/microservice; MicroRCA counted as relevance 2).
- Surveys: Soldani & Brogi (ACM CSUR 2022), Notaro et al. (ACM TIST 2021), Zhang et al. LLM4AIOps (ACM CSUR 2025),
  Murphy et al. (IEEE TNSM 2024). Landauer et al. "Deep learning for anomaly detection in log data: A survey" (MLWA
  2023, 10.1016/j.mlwa.2023.100470) was dropped to keep the list focused; it is a good backup survey for log AD.
- Zhou et al. (IEEE Wireless Communications 2026) is half review, half framework; flagged `magazine`, not `survey`.
- LNEE chapter "A Method of Alarm Correlation and RCA in 5G Core Network" (Signal and Information Processing,
  Networking and Computers proceedings) kept as `conference`: it is the only alarm-correlation work specific to the
  5G core we found, but we could not read the abstract (Springer redirects to login); summary is based on a search
  snippet (expert rule base + GNN) and the critique says so.
- arXiv 2508.09152 (5G core fault detection + GenAI, accepted at CoaCoNS 2025, no DOI yet) kept as `preprint`.
- MDAF NOMS 2026 paper links to TS 28.104 only in standards_link (S1 owns the standard row).
- ICC 2021 digital-twin assisted RCA in NFV: relevance 2 (VM/server faults, simulation) with S3 secondary.
- Two NOMS 2026 papers (5GC-Trace-RCA, MDAF) and GLOBECOM 2025 have 0 citations — included for recency and because
  they are the most directly core-focused RCA works.

## Rejected / not included
- APGNN (Computer Networks 2023, 10.1016/j.comnet.2022.109485) and "Anomaly detection based on system text logs of
  virtual network functions" (Big Data Research 2024, 10.1016/j.bdr.2024.100485): verified DOIs but no abstract
  reachable (ScienceDirect 403, APIs return none) — not characterised; backups.
- arXiv 2512.19697 (LLM fault detection in a Kubernetes 5G core, fine-tuned GPT-4.1 nano): weak evaluation; dropped.
- arXiv 2507.21974 (Sana et al., TeleLogs reasoning LLM RCA, Huawei): RAN-oriented preprint; covered indirectly via
  Zhou et al. 2026 which uses TeleLogs. Backup if a wireless LLM-RCA item is wanted.
- arXiv 2602.03596 SAGE-5GC (ITASEC 2026): security/adversarial evaluation of 5GC anomaly detectors — more S-security
  than RCA; backup.
- ICPADS 2023 "Unsupervised Graph-Sequence AD for 5GC control plane traffic" (10.1109/icpads60453.2023.00230):
  overlaps with ADSeq-5GCN line; dropped.
- NOMS 2025 "Enabling Cloud-Native Observability for White-Box Performance Analysis of the 5G Core"
  (10.1109/noms57970.2025.11073613): observability/performance testing, more S1/S2; backup.
- ICC Workshops 2024 MALEAF "ML Driven RCA in Telco Microservices Continuum" (10.1109/iccworkshops59551.2024.10615702):
  evaluated on an IoT testbed only; dropped.
- Nezha (FSE 2023), BARO (FSE 2024), CIRCA (KDD 2022), ICSE 2023 LLM incident RCA (10.1109/icse48619.2023.00149),
  IEEE TCC 2024 "RCA for Cloud-Native Applications": strong generic works dropped to keep the generic share small;
  all verified via Crossref and usable as backups.
- All SSRN/TechRxiv/Preprints.org/Research Square hits and low-tier journals (e.g., Technium, GJAETS, IJERET)
  rejected per protocol.
- No standards added (TS 28.104 owned by S1; no ETSI ENI GS directly on RCA was worth adding).

### S2 (subagent decisions)

# S2 — Service-based architecture and NF selection: decisions

## Queries run
Crossref (`verify.py search`): "service communication proxy 5G core"; "NF discovery selection NRF 5G core"; "load balancing 5G core network functions reinforcement learning"; "AMF load balancing 5G"; "service mesh 5G core Istio"; "cloud-native 5G core Kubernetes autoscaling"; "open-source 5G core comparison free5GC Open5GS performance"; "5G core control plane scalability microservices"; "CoreKube autoscaling resilient mobile core"; "L25GC low latency 5G core"; "Neutrino fast consistent edge-based cellular control plane"; "survey cloud-native 5G core network functions"; "service mesh 5G core network performance"; "HTTP/2 service based interface 5G core QUIC"; "proactive autoscaling 5G core network functions deep reinforcement learning"; "AMF scaling machine learning traffic forecasting 5G core"; "6G core network service-based architecture design"; "network function placement 5G core control plane latency"; "VNF and CNF placement in 5G recent advances future trends"; "survey resource management cloud native network functions"; "survey 5G core network architecture service based"; "survey autoscaling network functions virtualization machine learning"; "6G core network survey architecture"; "survey microservices telecommunication network functions container orchestration"; "service communication proxy performance evaluation indirect communication"; "Cloud-native service mesh readiness for 5G and beyond"; "microservice 5G core network functions decomposition Robitzsch"; "Smart scaling of the 5G core network RNN"; "Improving traffic forecasting for 5G core network scalability machine learning"; "graph neural network autoscaling 5G core microservices"; "eBPF 5G service based architecture"; "5G core signaling storm control plane overload"; "Kubernetes 5G core network function placement scheduling"; "horizontal scaling 5G core network functions Kubernetes machine learning journal"; "NWDAF load analytics network function selection"; "intelligent load balancing service based architecture 5G core"; "scalable 5G core control plane design stateless network functions"; "cloud-native 5G core performance HTTP/2 SBI latency evaluation"; "AMF autoscaling LSTM 5G core"; "service-based architecture 6G core AI-native"; "5G core network function deployment latency-aware placement edge cloud control plane"; "multi-agent reinforcement learning 5G core network functions resource"; "proactive scaling 5G core network functions online learning concept drift"; "AI-driven autoscaling cloud-native network functions 5G core 2024"; "free5GC Kubernetes horizontal pod autoscaler control plane evaluation"; "NRF bottleneck 5G core scaling service discovery"; "Performance and viability analysis of deploying cloud-native 5G autoscaling platforms"; "deep reinforcement learning UPF scaling Kubernetes 5G core".
WebSearch: survey cloud-native 5G core SBA (IEEE COMST); survey open-source 5G cores; auto-scaling VNF survey ML 5G core; "service communication proxy" SCP load balancing NF selection; NRF NF discovery/selection ML; cloud-native 5G core survey IEEE Access/Computer Networks; 5G SBI HTTP/2 vs QUIC; RL NF selection NRF/SCP 2024-2025; L25GC DOI; arXiv 2025 autoscaling RL Open5GS/free5GC; arXiv 2025-2026 SCP/service mesh SBA.
Abstracts were read via OpenAlex abstract index, the arXiv API and Zenodo (Robitzsch et al.; ScienceDirect returned 403).

## How the queries changed
- Searches for SCP / NRF / "NF selection" with ML found almost no peer-reviewed papers (only patents, vendor docs such as Oracle/Nexign SCP guides, and 3GPP text). This is a real gap (see below), so I moved to the neighbouring topics where most of the work sits: autoscaling/load balancing of 5GC NFs, service-mesh realisations of the SBA, stateless/cloud-native core designs and open-source core benchmarks.
- No dedicated IEEE COMST survey on cloud-native 5GC / SBA was found. Used as surveys: Attaoui et al. (TNSM 2023, VNF/CNF placement), Aldas & Babakian (IEEE Access 2023, service-mesh readiness, review + design), Robitzsch et al. (Computer Networks, microservice prospects, position/review), and Atalay et al. (arXiv 2026, cloud-based 6G deployments survey, preprint).

## Inclusion / borderline calls
- **L25GC (SIGCOMM 2022):** Crossref stores the title as "L<sup>2</sup>5GC", which the build renders as "L 2 5GC". Following the orchestrator note, I set expected_title to "L 2 5GC: A Low Latency 5G Core Network based on High-Performance NFV Platforms", so the CSV shows that form; the official name is L²5GC/L25GC. The follow-up L25GC+ (IEEE CloudNet 2023) was not added.
- **CoreKube (MobiCom 2023):** I chose the MobiCom paper over the GetMobile 2024 digest (10.1145/3665112.3665118) and the MobiCom demo (10.1145/3570361.3614075). It is rated relevance 3 because autoscaling and self-healing are the core contribution, even though the scaling uses Kubernetes defaults rather than learning.
- **Robitzsch et al.:** Crossref gives the year as 2023 (online first); the issue is Computer Networks vol. 337 (2024). It has few citations but it is the main peer-reviewed argument for decomposing 5GC NFs into microservices. An SSRN preprint version (10.2139/ssrn.4485374) exists and was excluded.
- **Yucebas et al. (1st free5GC World Forum 2025, ACM, 4 pages):** The venue is new and workshop-like. I kept it because it is the only peer-reviewed result I found that names the **NRF** as the autoscaling bottleneck in a free5GC Helm deployment.
- **Barbosa et al. (ICOIN 2025):** A mid-tier venue, kept as a recent open-source core comparison with 18 citations. The arXiv version 2412.21162 is superseded by the DOI.
- **TEGRA (arXiv 2509.07410, 2025):** Preprint kept as a recent SBA-native design that compares against CoreKube, free5GC, Open5GS and Aether. An Aether wiki gives smaller speed-ups than the arXiv abstract; the CSV uses the arXiv abstract figures.
- **Cognitive Service Architecture for 6G Core (TII 2021):** A visionary paper with limited validation. I rated it relevance 3 as AI-native core design, and it is the most-cited 6G-core SBA item found.
- **Moreira et al. (IJNM 2020):** Kept as the only peer-reviewed SBI protocol (HTTP/2 vs HTTP/3/QUIC) evaluation found. It relates to TR 29.893.
- Relevance 2 was given to non-AI architecture and benchmark works (L25GC, service mesh, benchmarks); relevance 3 to works that automate scaling or load balancing of core NFs.

## Rejected / not included (and why)
- Buyakar et al., "Prototyping and Load Balancing the SBA of 5G Core Using NFV" (NetSoft 2019, 10.1109/netsoft.2019.8806648): it is foundational for SBA load balancing (look-aside load balancer, gRPC), but it is pre-2020 with only about 20 citations, so it is not "highly cited". It could be added as `seminal` if the author wants an SBA load-balancing anchor.
- Neutrino (IEEE/ACM ToN 2023, 10.1109/tnet.2022.3202496): relevant edge control-plane design, dropped only to keep within budget. **Good reserve.**
- The Cost of Stateless NFs in 5G (ANCS 2021, 10.1145/3493425.3502749) and ML-SLD (DCN 2023, 10.1016/j.dcan.2022.04.026): stateless-core designs, reserve candidates.
- Hirai et al., ML performance prediction for cloud-native 5GC (WCNC 2022, 10.1109/wcnc51071.2022.9771942): fits S8 better, reserve.
- Toka et al. (TNSM 2021, ML scaling for Kubernetes edge clusters, 173 citations) and GRAF (ToN 2024, GNN autoscaling for microservices): generic microservice autoscaling with transferable methods (relevance 2), dropped for budget. Toka et al. is a strong reserve if generic Kubernetes ML scaling is wanted.
- Kaur et al., latency-aware placement for cloud-native 5G/6G (CCNC 2022), Shared NF placement for cloud-native 5GC (NoF 2023), and Corici et al., Organic 6G core (ICIN 2022) / 6G service-based RAN-core interface (EuCNC 2025): reserves.
- Nakao, "Come Back Later": LLM-assisted mitigation of AMF signalling storms (GC Workshops 2025, 10.1109/gcwkshps68340.2025.11590969): interesting LLM angle but no abstract was accessible, so I could not characterise it honestly. **Possible S6 candidate.**
- Holistic-Service-Based Architecture for Open-Source 6G Core Networks (IEEE Network 2026, 10.1109/mnet.2026.3708223): no abstract accessible. **Check later.**
- Gadouh & Koubaa NFV resource-allocation survey (IJNM 2025): generic NFV and cloud, only 1 citation.
- Excluded on venue grounds: SSRN, TechRxiv and Research Square items (e.g. SuPhRL UPF autoscaling, a TechRxiv HPA paper), and the low-tier journals WJAETS and IJSR.
- Not added because they belong to other subdomains: the 5GC control-plane digital twin (TCCN 2024, S3) and 5GC anomaly-detection works (S4).

## Standards
- TS 23.501 V19.9.0 (Rel-19, 2026-09), TS 29.500 V19.7.1 (Rel-19, 2026-09) and TS 29.510 V19.8.0 (Rel-19, 2026-09). The version numbers come from the 3GPP FTP archive listing, read with WebFetch on 2026-10-10. Rel-20 drafts (23501-k30, 29510-k10, 29500-k00) also exist; Rel-19 was cited as the latest frozen release. Spec IDs 3144, 3338 and 3345 were checked with `verify.py spec3gpp`.
- TS 23.502 was not added (optional; procedures are better covered by other subdomains).

### S1 (subagent decisions)

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

### S5 (subagent decisions)

# S5 - Resilience, geo-redundancy and failover of the 5G core: decisions

## Queries run
Crossref (`verify.py search`): "5G core resilience survey"; "availability model 5G core network stochastic Petri net";
"high availability 5G core network functions"; "stateless network functions 5G core state externalization";
"geo-redundancy 5G core"; "AMF failure recovery 5G"; "fault tolerance cloud-native network functions Kubernetes 5G";
"reliability availability 5G service-based architecture"; "resilience by design 6G networks literature review";
"survey reliability network function virtualization fault tolerance"; "CoreKube ..."; "L25GC ..."; "Neutrino ...";
"availability modeling containerized 5G core network"; "performability assessment 5G core network";
"self-healing 5G core network machine learning"; "chaos engineering 5G core"; "failure prediction virtual network
functions machine learning"; "NFV-MANO availability model software rejuvenation"; "UPF failure redundancy 5G user plane";
"Island-Ready 5G ..."; "TEGRA ..."; "NF migration containerized 5G core CRIU"; "software rejuvenation 5G network
performability queueing"; "stateless 5G core state management function availability"; "Revamping resilience ...";
"resilient 5G core network function failure detection recovery"; "UDSF unstructured data storage function 5G";
"session state replication 5G core consistency"; "Kubernetes failover 5G core network function recovery time";
"high availability 5G control plane replication"; "reliability aware placement 5G core network functions";
"proactive failure management cloud-native 5G core deep learning"; "digital twin resilience 5G core failure";
"redundancy 5G core network slice availability optimization"; "Markov availability model virtualized network function 5G";
"network function set restoration 3GPP"; "disaster resilient mobile core network"; "control plane failure mobile core
recovery"; "reinforcement learning failure recovery 5G core"; "fault injection 5G core resilience testing"; "SMF failure
session continuity 5G"; "5G core outage signaling storm resilience"; "service availability 5G core network slicing Markov".
WebSearch: Di Mauro/Longo SRN 5G core availability; survey resilience 5G core restoration; L25GC resiliency; stateful
failover SMF/AMF Kubernetes; geo-redundant 5G core multi-cluster; NFV reliability surveys; stateless 5GC surveys;
3GPP TS 23.527 versions; ETSI NFV-REL 001/003; Corici group failure prediction; Nakao "Come Back Later".

## Judgement calls
- Query evolution: generic "geo-redundancy 5G core" and "chaos engineering 5G core" return only book chapters / nothing
  peer-reviewed. Geo-redundancy is almost absent from the academic literature (only patents and vendor material);
  the closest peer-reviewed items are the island-ready/decentralised core work (Janzen & Hollick) and the ONAP
  inter-cluster UPF failover. Chaos engineering appears only indirectly (ML-SLD uses Chaosblade fault injection).
- Relevance rule used: 3 = 5GC-specific AND autonomous/AI-driven recovery or failure prediction (closed loop, SON,
  LSTM/SVR, Kubernetes self-healing as core design); 2 = 5GC-specific resilience/state design or availability
  modelling without AI, and NFV-generic surveys; 1 = pure standards background (ETSI NFV-REL).
- Surveys: no dedicated survey on 5G *core* resilience exists. Included the closest: COMST 2026 (Di Mauro et al.,
  NFV reliability/availability modelling; arXiv 2503.22034 version superseded by the DOI), IEEE Access 2024
  resilience-by-design 6G, JNSM 2025 SFC fault-tolerance survey (abstract read from its Research Square preprint
  10.21203/rs.3.rs-4913807, the JNSM DOI is used). Janzen & Hollick (Comput. Commun. 2026) is a vision/analysis
  paper flagged `vision`, not `survey`.
- Vittal / Franklin (IIT Hyderabad) group has many related papers: kept TNSM 2024 (Revamping), TNSM 2022 (HARNESS) and
  NOMS 2024 (RECAP 5GC). Not included (overlap): CNSM 2022 LOCOMOTIVE (10.23919/cnsm55787.2022.9964553, LB-based HA,
  conceptually precursor of the TNSM 2024 work), CCNC 2024 "Evaluating CAP Theorem on a Stateless 5G Core"
  (10.1109/ccnc51664.2024.10454811, precursor of RECAP), NetSoft 2024 UDM/UDSF sharding (10.1109/netsoft60951.2024.10588906,
  short paper; good candidate if more database-replication coverage is wanted).
- Di Mauro / Postiglione / Longo (Salerno) group: kept NetSoft 2025 Open5GS performability with rejuvenation. Alternatives
  not added: RNDM 2024 multi-tenant 5G performability (10.1109/rndm64105.2024.10820438), NetSoft 2026 transient-aware
  non-exponential performability (10.1109/netsoft70012.2026.11603483, no abstract available to me), TDSC 2022 IMS
  performability (10.1109/tdsc.2021.3082626, IMS not 5GC), Tola et al. TNSM 2021 NFV-MANO availability (10.1109/tnsm.2021.3090208).
- CoreKube: MobiCom 2023 paper kept; the GetMobile 2024 magazine reprint (10.1145/3665112.3665118) is not a separate work.
- Neutrino: the IEEE/ACM ToN 2023 journal version is used (conference version CoNEXT 2020 not added).
- L25GC (SIGCOMM 2022): Crossref stores the title as "L<sup>2</sup>5GC" (now cleaned to "L25GC"); expected_title set to
  "L25GC: A Low Latency 5G Core Network based on High-Performance NFV Platforms" so the short-prefix rule accepts it.
  The author should render it as L²5GC / L25GC. Follow-up L25GC+ (CloudNet 2023, 10.1109/cloudnet59005.2023.10490024) is
  latency-focused and not added.
- Failure prediction: Chakraborty/Corici/Magedanz ICC Wkshps 2021 kept (17 cites). Later work by the same Fraunhofer
  FOKUS group (FNWF 2025, 10.1109/fnwf66845.2025.11317174; Globecom Wkshps 2025, 10.1109/gcwkshps68340.2025.11591148)
  not added: the Globecom one had no readable abstract, FNWF is incremental.
- Rejected for lack of a readable abstract: Nakao, "Come Back Later": LLM-assisted mitigation of AMF signaling storms
  (Globecom Wkshps 2025, 10.1109/gcwkshps68340.2025.11590969) - interesting AI+resilience item, worth checking manually;
  Anand/Gundall/Schotten NF migration in containerized 6G core (Globecom Wkshps 2025, 10.1109/gcwkshps68340.2025.11591208).
- Rejected as not peer-reviewed / wrong type: SSRN "Failure Prediction with ML for Reliable Cloud Native Core NFs"
  (10.2139/ssrn.5256232), TechRxiv placement preprints, IJAMR "Operational reliability engineering framework" (low-quality
  venue), USPTO patents on geo-redundant hybrid-cloud cores (patents are not in scope), Spirent/Keysight resiliency
  white papers (vendor).
- arXiv: TEGRA (2509.07410, 2025) kept as `preprint`. NetMon hybrid monitoring (2609.12649, Ericsson AMF clusters) is
  closer to S4 (fault detection) and was left out.
- Rejected as too generic: Huang et al. ToN 2026 reliability-aware VNF placement with MADRL (10.1109/ton.2025.3631076);
  IEEE IoT-J 2024 NFV fault diagnosis survey (10.1109/jiot.2024.3362991; belongs to S4 if anywhere).
- Standards: 3GPP TS 23.527 (specificationId 3349, confirmed with `verify.py spec3gpp`), cited as V19.5.0 (2026-01,
  Rel-19); V20.0.0 (2026-06, Rel-20) also exists in the 3GPP archive. ETSI GS NFV-REL 001 V1.1.1 (2015-01) and
  NFV-REL 003 V1.1.2 (2016-07): PDFs fetched via WebFetch and cover pages checked with pdftotext (ETSI blocks curl),
  hence `verified_by_webfetch`. Pre-2020, flagged `seminal`. TS 23.501 / TS 29.500 intentionally left to S2.

## Orchestrator fixes during Phase 2

- `tools/verify.py` was fixed four times while the subagents ran: BibTeX writer crash on integer years; full titles
  kept when Crossref stores only the system name (MimicNet, DeepQueueNet, OnSlicing); `<sup>` markup in titles
  (L25GC); hyphenated spec numbers (TR 23.700-84). BibTeX keys now use the Crossref *family* name, so hyphens and
  particles survive (GarciaMartin, DeSimone). One exception: Crossref records Di Mauro's family name as "Mauro"
  (given name "Mario Di"), so that key reads `Mauro2026...`. The key follows the authoritative record and was not hand-edited.
  All finished subdomains were rebuilt after each fix.

### S3 (subagent decisions)

# S3 — Network digital twins (mobile / core): decisions

## Queries run
Crossref (`verify.py search`): "digital twin networks survey"; "network digital twin context enabling technologies opportunities";
"digital twin enabled 6G vision architectural trends"; "digital twins survey enabling technologies challenges trends future prospects";
"network digital twin 5G core"; "digital twin network slicing"; "digital twin network what-if analysis";
"digital twin network configuration validation"; "digital twin closed loop network automation"; "emulation-based network digital twin";
"digital twin 6G networks survey"; "network digital twin survey 2024"; "digital twin control plane 5G"; "digital twin network intent-based";
"network digital twin standardization"; "digital twin network architecture key technologies"; "digital twin 5G core network function";
"digital twin assisted network slicing core reinforcement learning"; "digital twin network graph neural network what-if";
"digital twin network management NFV orchestration"; "digital twin open5gs"; "digital twin free5gc"; "network digital twin generative AI";
"digital twin in-the-loop reinforcement learning network"; "network digital twin fidelity synchronization";
"digital twin 6G network management large language model"; "digital twin zero-touch network service management";
"network digital twin IETF architecture"; "digital twin core network signaling storm"; "intent-based digital twin network slicing 5G core testbed";
"digital twin network data analytics 5G core NWDAF"; "network digital twin anomaly detection 5G core"; "digital twin 5G network emulation Kubernetes core what-if";
"digital twin network lifecycle management autonomous network"; "network digital twin 6G O-RAN survey"; "digital twin assisted network function placement";
"digital twin enabled closed loop 5G network slicing orchestration testbed"; plus exact-title searches for the hinted surveys.
WebSearch: "network digital twin 5G core control plane what-if analysis paper IEEE 2024"; "3GPP TS 28.561 network digital twin management Rel-19";
"draft-irtf-nmrg-network-digital-twin-arch datatracker"; "3GPP TR 28.915 study on management aspects of network digital twin";
"ITU-T Y.3090 digital twin network requirements and architecture"; "survey network digital twin mobile networks IEEE COMST 2024 OR 2025";
"digital twin 5G core network validation configuration change emulation testbed 2025"; "arxiv 2025 network digital twin 5G core open5gs what-if".
Abstracts were read from OpenAlex (abstract index), Semantic Scholar API (ICC 2026 paper), arXiv abs page and web snippets (FGCS 2024).
Query evolution: generic "digital twin" queries were swamped by manufacturing/healthcare/construction; adding "core", "control plane",
"signaling", "slice admission", "what-if" and "NWDAF" surfaced the core-specific works; the 2026 items (SIGCOMM, ICC, TNSM) only appeared via Crossref.

## Hint checks
- Wu et al. "Digital Twin Networks: A Survey" — confirmed IEEE IoT J 8(18) 2021.
- Almasan et al. — confirmed IEEE Commun. Mag. 2022 (10.1109/mcom.001.2200012). OpenAlex gives only 6 citations, which looks like an
  OpenAlex mis-attribution (the arXiv version is widely cited); left as retrieved, flagged in the critique.
- Khan et al. "Digital-Twin-Enabled 6G" — the hint said IEEE Wireless Commun.; it is actually **IEEE Communications Magazine** 2022 (10.1109/mcom.001.21143).
- Mihai et al. — confirmed IEEE COMST 2022.
- "Kuruvatti/others": used Kuruvatti et al. "Empowering 6G Communication Systems With Digital Twin Technology: A Comprehensive Survey", IEEE Access 2022.
- Added two newer surveys: Manalastas et al. COMST 2025 (simulators -> DTs for cellular) and Raza/Minerva/Crespi, Computer Communications 2025 (NDT specs, edge-cloud).

## Standards
- 3GPP TS 28.561 exists (portal specificationId 4384, found by scanning portal IDs with `verify.py spec3gpp`); archive shows Rel-19 V19.3.0
  (2026-07) and Rel-20 V20.2.0 (2026-09). Cited V19.3.0, year 2026; Rel-20 "NDT phase 2" (incl. NTN) noted.
- 3GPP TR 28.915 exists (specificationId 4263), V19.0.0 placed in archive Dec 2024/Jan 2025; cited year 2024.
- IRTF draft-irtf-nmrg-network-digital-twin-arch-13 (1 July 2026), state "Waiting for IRTF Chair", Informational. Editors/authors: C. Zhou,
  H. Yang, X. Duan (China Mobile), D. Lopez, A. Pastor (Telefonica), Q. Wu (Huawei), M. Boucadair, C. Jacquenet (Orange). Authors field set to
  "IRTF NMRG" to get a clean BibTeX key; page confirmed via WebFetch and datatracker API (`verified_by_webfetch`).
- ITU-T Y.3090 (02/2022) verified against itu.int page (curl works).

## Inclusion judgement calls
- Xie et al., SIGCOMM 2026 (Spillway): included at relevance 3; it is the strongest at-scale evidence of DT-based what-if validation of core
  configuration (production 5G SA core), even though it has 0 citations yet.
- Zanzi et al., ICC 2026 (NEC): abstract only via Semantic Scholar; included, relevance 3 (commercial 5G core NDT on Kubernetes/AWS).
- COREX (TNSM 2026): included, emulation-based DT spanning core; relevance 3.
- Costa/Zhou/Granelli arXiv 2510.12458 (Oct 2025) — preprint allowed (2025); no published DOI found.
- Aben-Athar et al. ICC Workshops 2025 — workshop paper (not main track); kept for being explicitly about what-if analysis; arXiv version 2505.04879 superseded by the DOI.
- Tao et al. TCCN 2024: arXiv 2302.06980 version superseded by journal DOI.
- Wang (H.) et al. TII 2022 GNN DT for slicing: Crossref year 2022 (online 2020). Possible overlap with S8 (GNN DT) — secondary S8 set.

## Rejected / not included
- Ferriol-Galmes et al. "Building a Digital Twin for network optimization using GNNs" (Computer Networks 2022) and RouteNet (JSAC 2020):
  left to S8 to avoid duplication.
- Hakiri et al. Computer Networks 2024 survey: no abstract accessible; generic IoT scope; dropped (could be added if author wants a 7th survey).
- Tang et al. "Survey on Digital Twin Edge Networks (DITEN)" OJCOMS 2022: edge/MEC focus, not core; dropped.
- Rodrigues et al. ICTON 2025 "Open-Source 5G Digital Twin: Virtualizing Core and RAN": very relevant topic but abstract describes planned
  work ("will evaluate"), optical-conference venue; dropped. Mentioned here as a pointer.
- Vila/Sallent/Perez-Romero Sensors 2023 (RAN NDT for O-RAN RL training): RAN-only, dropped for space (relevance 2 candidate).
- Ak et al. IWCMC 2024 what-if framework (NS-3 wireless): dropped in favour of transport/core what-if works.
- Yaqoob et al. IEEE Internet Computing 2024, Wu et al. IEEE Network 2026 (AI-native NDT), Chai et al. IEEE Network 2024 (GAI DT), Yang et al.
  IEEE Network 2025 (LGM DT): magazine visions overlapping with the included Huang et al. 2025; dropped to keep list ~22.
- DTN-Core (CNSM 2024): generic DT-of-DTs model checking, not mobile networks.
- MITO (TNSM 2026): no abstract retrievable; not judged.
- Polverini et al. NOMS 2023 (BGP what-if): IP-only.
- All SSRN / TechRxiv / Research Square / F1000 "Digital Twin" journal versioned items ignored.

### S6 (subagent decisions)

# S6 — Closed-loop and autonomous networks: decisions

## Search queries run
Crossref bibliographic search (`verify.py search`): "zero-touch network and service management survey"; "intent-based networking survey";
"intent-based management 5G"; "closed loop automation 5G network slicing"; "autonomous networks survey"; "large language models
telecommunications survey"; "LLM intent-based networking configuration"; "agentic AI 6G network management"; "large language models for
telecom survey"; "large language model enabled 6G network"; "generative AI for 6G network management"; "LLM agents network operations
troubleshooting"; "self-driving networks"; "knowledge-defined networking"; "MAPE-K autonomic network management 5G"; "intent-driven network
slicing closed loop"; "AI-native 6G network management autonomous"; "zero-touch 5G core closed-loop"; title look-ups for known works (Coronado
ZTM survey, Zhou LLM-telecom survey, Maatouk, Huang LLM-networking, NetLLM, Mekrache LLM-centric IBN, NetConfEval, KDN, intent-driven closed
loops, GenAI network management); "autonomous network levels intent 3GPP TM Forum"; "large language model agents autonomous network
operation"; "LLM multi-agent 5G core network"; "intent-based network slicing zero-touch closed loop reinforcement learning"; "intent assurance
closed loop 5G"; "generative AI agents autonomous networks survey"; "self-healing 5G core closed loop"; "zero-touch network slicing management
closed-loop machine learning 5G"; "From zero-touch to intent-based networking ..."; "Ksentini large language model network slicing intent";
"LLM agents 6G network management survey".
WebSearch: "arXiv 2025 LLM agent 5G core network autonomous closed-loop"; "agentic AI autonomous networks survey 2025 telecom IEEE";
3GPP spec-id look-ups for TS 28.312 / TS 28.100; ETSI ZSM 009-1 / ZSM 002 PDFs; AICOM and JNSM 2022 abstracts.
Abstracts were read via OpenAlex (abstract_inverted_index), arXiv API, or search snippets (AICOM, JNSM 2022).

## Judgement calls
- **Query drift.** Generic "autonomous networks survey" and "self-driving networks" returned mostly vehicle/UAV papers; "knowledge-defined
  networking" returned only weak venues (MDPI Telecom, Array) — no KDN item kept. Discovery was redirected to ZSM/IBN/LLM/agentic terms.
- **Standards (4).** ETSI GS ZSM 009-1 V1.1.1 (2021-06) confirmed via WebFetch of the ETSI PDF (title page extracted locally; curl gets 403),
  hence `verified_by_webfetch`. ETSI GS ZSM 002 V1.1.1 (2019-08) was also confirmed but left out to respect the ~4-standards cap (ZSM 009-1
  builds on it; cite it in the article as architecture background). 3GPP TS 28.312: portal specificationId 3554, cited at V19.5.0 (Rel-19),
  version confirmed from the ETSI TS 128 312 V19.5.0 (2026-04) title page; draft Rel-20 versions (V20.0.x/V20.1.0) exist on the 3GPP FTP but
  were not cited. 3GPP TS 28.100 (levels of autonomous network): specificationId 3756 (found by scanning portal IDs), cited at V18.0.0 (Rel-18),
  confirmed from ETSI TS 128 100 V18.0.0 (2024-05); a Rel-19 V19.0.0 is reported by third-party indexes only, so not cited. TS 28.105 (AI/ML
  management) left to S1/S8. RFC 9315 entered as a standard row (datatracker URL; DOI 10.17487/rfc9315 exists) so the BibTeX key is clean.
- **Conference vs journal duplicates.** Shafiei Ardestani/Limam/Boutaba: kept ITU J-FET 2026 journal version (10.52953/svmm1934) over NOMS 2026
  (10.1109/noms69089.2026.11668240); note both are also in S1 (dedup in Phase 3). Sousa/Rothenberg: kept JNSM 2022 over CLARA (NFV-SDN 2021,
  10.1109/nfv-sdn53031.2021.9665048). Mekrache/Ksentini: kept IEEE Network 2024 over NetSoft 2024 (10.1109/netsoft60951.2024.10588881).
  Manias/Chouman/Shami: kept GLOBECOM 2024 (semantic routing, dataset) over DRCN 2024 (10.1109/drcn60692.2024.10539172, LLM intent extraction
  in 5GC, 54 cites) — both are relevance-3; author may add DRCN. Brodimas et al.: kept ICNC 2025 (5G core deployment) over EuCNC/6G Summit 2024
  (10.1109/eucnc/6gsummit60053.2024.10597022).
- **Preprints.** AgentxGCore (arXiv 2606.00417) and AGORA (arXiv 2602.13290) have published DOIs; AgentxGCore entered with its IEEE Network
  DOI. AGORA (IEEE Access 2026, 10.1109/ACCESS.2026.3672699, LLM agent steering UPF for energy) is a good candidate for S7 and not included
  here to stay within ~22. Only one pure preprint kept: Ameur/Mekrache/Brik/Ksentini 2026 agentic tutorial-survey (under review).
- **Relevance.** Coronado survey and the agentic 5G/6G survey rated 3 because they explicitly cover the core network; generic IBN/LLM surveys
  rated 2. 3GPP TS 28.312/28.100 and ETSI ZSM 009-1 rated 2 (directly define closed-loop/intent/autonomy concepts for mobile management);
  RFC 9315 rated 1 (IP-oriented terminology).
- **Venue doubts.** Journal of ICT Standardization (River Publishers) is peer-reviewed but low-profile; kept for its ZSM/intent closed-loop
  coordination content (Ericsson authors). Boutaba et al. 2021 is an ACM FlexNets workshop (SIGCOMM 2021) vision paper — kept as the conceptual
  MAPE-loop anchor of the Waterloo group. ITU J-FET is peer-reviewed (ITU journal).
- **AICOM (IFIP Networking 2026).** OpenAlex abstract was empty and the IFIP PDF returned 503; summary is based on search snippets of the PDF
  (Orange Innovation / Paris-Saclay; GitOps + Kubernetes + LLM agents; OAI 5GC with Gemini/Qwen/Llama). Critique worded cautiously.

## Rejected / not included (and why)
- Gallego-Madrid et al., ML-based ZSM survey (DCN 2022, 10.1016/j.dcan.2021.09.001): overlaps with Coronado and Liyanage surveys; optional add.
- Benzaid & Taleb, AI-driven ZSM (IEEE Network 2020, 10.1109/mnet.001.1900252, ~315 cites): position paper on AI risks in ZSM; strong
  optional add if the author wants a highly-cited ZSM+AI anchor.
- Maatouk et al. LLMs for Telecom (IEEE ComMag 2025), Huang et al. LLMs for Networking (IEEE Network 2025), NetLLM (SIGCOMM 2024): general
  LLM-for-networking pieces without closed-loop/core focus; covered by the Zhou and Hong surveys.
- Maestro (IEEE Netw. Lett. 2024, LLM agents negotiating in O-RAN), INTA (ICNP 2025, config translation), IJNM 2024 intent-based config with
  LLMs, CNSM 2024 config generation: relevance 2 at best, RAN/IP focus.
- Vittal et al. CNSM 2021 zero-touch 5GC slicing (demo, 10.23919/cnsm52442.2021.9615531) and Abbas et al. IEEE Access 2021 IBN slice
  lifecycle (10.1109/access.2021.3084834): older 5G slicing loops, dropped for space; good optional additions for a 5GC testbed angle.
- ICT 2026 "Closed Loop Intent Based Agent for Resilient Multi-UPF 5G Networks", Computer Communications 2026 "IBN using LLM-driven agentic RL",
  TNSM 2026 PCLANSA proactive slice assurance: no abstract could be read; not included (could be checked by the author; PCLANSA abstract seen,
  relevant to S5/S6).
- Excluded as non-peer-reviewed/weak venues: SSRN, TechRxiv, Research Square, IJSR, IJCA, Technium, MDPI-like KDN surveys.

### S7 (subagent decisions)

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
- (orchestrator) Added AGORA (IEEE Access 2026, 10.1109/ACCESS.2026.3672699; preprint arXiv 2602.13290), handed over by
  S6 as an energy candidate. Its summary is written from the arXiv abstract, since Crossref has none. Relevance 3,
  secondary S6.

## Phase 3 (merge)

- **Deduplication key:** the DOI, else the arXiv ID, else the standard number, else the normalised title; plus a
  fuzzy title check (>0.9 similarity), which found nothing further. The primary subdomain is the row with the
  highest relevance, ties broken by the protocol priority order (S3, S1, S5, S8, S6, S4, S2, S7). The other
  subdomains are merged into `secondary_subdomains`, and flags are unioned.
- **179 works were kept, against a target of about 130.** Every row is verified and characterised, so cutting
  50 rows would only remove choices the author is meant to make. Relevance and the surveys-first ordering make the
  cut easy.
- **Order of `ALL_CANDIDATES.csv`:** surveys first, then by primary subdomain in protocol priority order, then
  relevance descending, then year descending.
- **Taxonomy:** five categories (C1 analytics, C2 modelling/digital twins, C3 assurance, C4 decisions, C5
  governance), with a 4-category variant in `SUMMARY.md`. Category counts are approximated from the primary
  subdomain; no per-row taxonomy column was added because the protocol fixes the CSV columns.
- **Weaker venues kept** because they are on-topic and peer-reviewed: SBrT 2025, free5GC World Forum 2025,
  ICOIN, COMSNETS, WCNPS, and an LNEE chapter. They are listed in SUMMARY §6 for a JCR/CORE check.
- **Standards versions:** subagents cited the latest version on the 3GPP archive at retrieval time (mostly
  Rel-19, with TS 28.310 at Rel-20). In the article, cite the Release you discuss.
