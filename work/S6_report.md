# S6 subagent final report (gaps and communities)
Gaps vs 3GPP Rel-18-21:
1. LLM intent work translates NL to NSDs/YAML/vendor configs; none implements the TS 28.312 intent information model, intent reports, negotiation or feasibility checks.
2. No system is evaluated against TS 28.100 autonomy levels; "Level 4/5" claims are not comparable.
3. Concrete core loops with 3GPP analytics triggers (NWDAF -> SMF/PCF) only in 2026 (Waterloo group, IntAgent); most loops act on slicing/RAN and stop at MANO/transport.
4. Conflicts between multiple closed loops (ZSM 009; Gomes 2021) essentially unaddressed for agent/LLM-driven loops.
5. Agentic papers 2025-26 (AgentxGCore, AICOM, AGILE-6G, autogenic) are prototypes with 1-2 use cases; no quantification of hallucination, rollback, safety guards, decision latency in the core; standards (TM Forum, SA5, ETSI) ahead of evidence.
Communities (rel-3): EURECOM (Ksentini, Mekrache); Waterloo (Boutaba, Limam, Shafiei Ardestani); Western (Manias, Chouman, Shami); Orange / Paris-Saclay (Aitsaadi, Fajjari); Qatar Univ. (Erbad, Mohamed); UFPE (Barbosa, Dias); Patras (Brodimas, Birbas); i2CAT (Coronado, Costa-Pérez).
