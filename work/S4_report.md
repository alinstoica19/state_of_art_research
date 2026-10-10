# S4 subagent final report (gaps and communities)
Gaps vs 3GPP Rel-18-21:
1. Almost no RCA/AD work is tied to standardised analytics: only one NOMS 2026 paper implements an MDAF; nothing exposes RCA as NWDAF Analytics IDs / MDA reports (TS 23.288 / TS 28.104) or feeds a closed loop.
2. 5GC anomaly detection is mostly security-flavoured, on free5GC/Open5GS/OAI with injected faults; one RCA work uses real operator traffic (5GC-Trace-RCA); no public 5GC fault benchmark comparable to TrainTicket/RCAEval.
3. No good-venue work on core-side signalling-storm/overload detection (storm work is RAN/O-RAN RRC).
4. Mature SE RCA (multimodal, causal, LLM agents) is barely tested on telecom; telecom LLM RCA still mostly preprints / RAN datasets.
5. Cross-domain partial observability, explainability and safe automated remediation are rarely studied; only one (2021, simulated NFV) uses a digital twin for RCA.
Communities (rel-3): Jiajia Liu / Yawen Tan / Jiadai Wang (Xidian); J. W.-K. Hong / S. Nam (POSTECH); Ericsson Ireland (Chawla, Bosneag); Gurusamy (NUS); Fajjari & Aitsaadi (Orange / Paris-Saclay); NTT; KDDI Research; Univ. Tokyo (Morikawa); China Unicom. Generic RCA: CUHK (Lyu), Microsoft, Alibaba, Hongyu Zhang.
