# S5 subagent final report (gaps and communities)
Gaps vs 3GPP Rel-18-21:
1. No survey on 5GC resilience: existing surveys cover NFV/SFC generally or 6G resilience conceptually; none maps TS 23.527 restoration, NF sets, binding indications onto research results.
2. Geo-redundancy almost absent from peer-reviewed work (patents/vendor only); nearest: island-ready/decentralised core, ONAP inter-cluster UPF failover (NOMS 2022); no quantification of UDR/UDSF cross-site replication consistency vs availability (RECAP 5GC tests CAP only on 2 nodes).
3. ML failure prediction (LSTM, SVR, eBPF features) stops at prediction; nothing feeds NWDAF analytics into TS 23.527 procedures or NF-set reselection; LLM-assisted recovery only in a workshop paper.
4. Availability modelling (Salerno group on Open5GS, rejuvenation; Mandal TSC 2025) is offline stochastic; not used as runtime DT or in closed loops.
5. Stateless designs (CoreKube, ML-SLD, procedure-aware statelessness, cost of stateless NFs) measure latency/overhead, rarely failover time/session continuity; no chaos-engineering at scale; Rel-18-20 restoration enhancements unevaluated.
Communities (rel-3): IIT Hyderabad (Vittal, Franklin) x3; Fraunhofer FOKUS (Corici, Magedanz, Chakraborty); KDDI Research (Kawasaki, Otani); Edinburgh (Marina). Rel-2: Salerno (Di Mauro, Postiglione, Longo), TUM (Kellerer).
