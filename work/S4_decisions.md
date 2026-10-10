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
