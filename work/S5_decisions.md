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
