# S8 subagent final report (gaps and communities)
Gaps vs 3GPP Rel-18-21:
1. Strong GNN / learned-simulator models target IP or data-centre queueing; no strong-venue GNN/DT performance model of the 5GC control plane (SBA signalling AMF/SMF/UPF).
2. 5GC-specific prediction papers are small free5GC/Kubernetes testbed studies (NOMS/NetSoft/WCNC); none consumes/produces NWDAF analytics (TS 23.288) or follows the AI/ML lifecycle of TS 28.105 (training, testing, drift/accuracy monitoring).
3. Generalisation shown for unseen topologies, not under operational drift or across operators; no counterpart to Rel-18/19 ML model performance monitoring.
4. Safe RL depends on digital twins whose fidelity/uncertainty is assumed, not validated; evaluations mostly simulation-only (link to Y.3172 sandbox and Rel-19/20 NDT).
5. Foundation/LLM models (NetLLM, MobiGPT) target application/RAN tasks; none addresses core KPIs or inference latency within near-real-time core loops.
Communities: rel-3 dispersed (IMT Atlantique: Kuranage/Nuaymi/Bouabdallah; NTT; NYCU; Q. Liu / T. Han + Nokia Bell Labs; Xidian: J. Wang / J. Liu; BUPT; Exeter: H. Wang / Y. Wu / G. Min). Dominant overall: UPC / Barcelona Neural Networking Center (Cabellos-Aparicio, Barlet-Ros, Suárez-Varela, Ferriol-Galmés, Rusek).
