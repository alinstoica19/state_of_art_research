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
