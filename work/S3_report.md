# S3 subagent final report (gaps and communities)
Gaps vs 3GPP Rel-18-21:
1. TS 28.561 / TR 28.915 standardise NDT management (lifecycle, MnS, link to automation), not fidelity; no paper measures twin fidelity against the TS 28.561 information model or exposes a twin through its MnS.
2. Few core/control-plane twins (Tao TCCN 2024 signalling model; Spillway SIGCOMM 2026 signalling storms; Zanzi ICC 2026 commercial core on K8s; COREX TNSM 2026; a 2025 lab preprint); none twins NF failover or state replication (S5 use case).
3. What-if validation thin: TR 28.915 key use case of verifying changes pre-deployment; only operator-scale evidence is Spillway (proprietary, single operator); others on transport/radio, DT-LNS only in simulation.
4. No link of twins to NWDAF/MDA, ETSI ZSM closed loops or intent-driven management; DT-in-the-loop / GenAI closed-loop papers mostly magazine visions.
5. No shared open datasets or fidelity metrics for core-network twins.
Communities (rel-3): China Mobile, Huawei, Telefonica, Orange (IRTF NDT draft editors; China Mobile TR 28.915 rapporteur); Hongtao Xie group (Spillway); NEC Labs Europe (Zanzi, Li, Liebsch); Xidian (J. Wang, J. Liu); Tsinghua/SJTU (Zhenyu Tao, Guanghui He); UPM (Mozo, B5GEMINI); UWS (Qi Wang, COREX); Trento (Granelli).
