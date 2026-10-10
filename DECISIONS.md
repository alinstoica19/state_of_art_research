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
