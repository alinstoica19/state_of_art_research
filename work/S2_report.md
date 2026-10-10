# S2 subagent final report (gaps and communities)
Gaps vs 3GPP Rel-18-21:
1. TS 29.510/29.500 define NF profile load/capacity/priority and SCP load/overload control but leave the selection policy open; no peer-reviewed AI/RL NF selection via NRF/SCP/delegated discovery found (only patents, vendor manuals).
2. AI work autoscales single NFs (AMF, UPF, Magma) with DRL/safe RL/forecasting, ignoring interplay with discovery/selection; Goshi (CNSM 2021) and Yucebas (free5GC World Forum 2025, NRF bottleneck) show it matters.
3. No paper feeds NWDAF NF-load analytics (TS 23.288) into NF selection or SCP routing, although supported since Rel-17.
4. Performance work (L25GC, CoreKube, TEGRA) gains by bypassing standard HTTP/2 SBI or per-NF split; no learned control, no standardisation path.
5. Toy testbeds (free5GC/Open5GS/OAI/Magma, synthetic load); no operator traces, multi-site or 6G scale; 6G core design papers still conceptual.
Communities (rel-3): Orange/Magma (Fraysse, Matsuo, Singh, Long); Nguyen / Van Do / Rotter; Nhu & Park; IMT Atlantique (Kuranage, Nuaymi, Bouabdallah); Western Univ. (Chouman, Manias, Shami); Taleb / Bagaa; Aitsaadi; Edinburgh (Larrea, Ferguson, Marina). Also Stavrou/Atalay (Virginia Tech).
No CST survey dedicated to cloud-native 5GC/SBA found.
