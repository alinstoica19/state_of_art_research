# S7 subagent final report (gaps and communities)
Gaps vs 3GPP Rel-18-21:
1. Only the user plane is studied: core-specific energy papers all deal with the UPF (measurement, DRL selection, LSTM switching, placement); no peer-reviewed energy-aware placement/consolidation/selection of control-plane NFs (AMF, SMF, NRF, SCP). TS 28.310 itself measures core EE only as N3 data volume per energy.
2. Rel-19/20 energy-awareness features (TR 23.700-66, TR 22.882: NF energy data collection/exposure, NWDAF energy analytics, energy as service criterion in policy control) are unimplemented in academia beyond IIT Bombay standards reviews.
3. Measurement immature: few testbeds report core power (Bellin et al.; one 8-UE workshop study); no per-NF power model validated against TS 28.310 VNF energy estimation; Kepler-style container telemetry not tied to 3GPP metrics.
4. Carbon/renewable awareness and the energy cost of AI itself almost absent (one 6GNet 2025 demo; AGORA measures LLM agent footprint), although TR 28.880 includes renewable use cases.
5. Generic NFV energy methods (transformer DRL placement, NUMA consolidation, HADES/OSM, energy-aware K8s autoscaling) use abstract SFCs, no 3GPP EE metrics, no NWDAF/MDA-driven loops, no digital twins.
Communities (rel-3): Trento (Bellin, Granelli, Munaretto); IIT Bombay (Kamran, Jha, Chaporkar); Concordia (Ziazet, Jaumard); Sorbonne (Christakis, Makris, Fdida); Goshi et al.; UFU Brazil (Moreira, De Oliveira Silva — AGORA).
Note: JNCA 2026 gNB energy saving via NWDAF (10.1016/j.jnca.2026.104482) not included — abstract unreadable; worth a manual check.
