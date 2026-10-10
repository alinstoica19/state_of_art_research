# C2 decisions (Network modelling and digital twins): snowball Phase 2

Judgement calls made without asking (PROTOCOL_SNOWBALL.md §1).

## Seeds recovered by hand
- **BenllochCaballero2026Corex** (TNSM 2026, doi:10.1109/tnsm.2026.3699692). OpenAlex and Semantic Scholar returned nothing,
  but the **Crossref record carries the full reference list (41 refs)**. I resolved the 15 refs that have DOIs and read the
  unstructured ones. Most are UWS group self-citations on 5G security emulation, DDoS self-protection and cyber ranges
  (off-topic for the core-automation survey), or 2008-2011 emulator papers. The candidates worth noting:
  - Chouman et al., *A Modular, End-to-End Next-Generation Network Testbed* (TNSM 2024, 10.1109/tnsm.2024.3416031). This
    is already in pool_C1 with link_count 2. COREX also cites it, so its link_count should be **3** with
    `BenllochCaballero2026Corex(backward-manual)` added. It belongs to C1 (Western University NWDAF testbed), so I left
    the selection to the C1 agent and the coordinator. Flagging it here so that the extra link is not lost.
  - Phung et al., *An Open Dataset for Beyond-5G Data-driven Network Automation Experiments (5G3E)* (6GNet 2022,
    10.1109/6gnet54646.2022.9830292). Relevance 2: a dataset with core NF metrics and operator-trace-driven traffic.
    Listed as a runner-up.
  - Aykurt & Kellerer, *Autonomous Network Management in Multi-Domain 6G Networks based on GNNs* (NetSoft 2023,
    10.1109/netsoft57336.2023.10175480). This is a research-plan paper, so it was dropped as too thin.
- **Costa2025Privatendt** (arXiv 2510.12458). I parsed the reference list from the arXiv HTML. All 14 references are
  already in the pool (DT standards, ISO 23247, synchronisation, Sengendo & Granelli) or are tools and URLs. The two IETF/IRTF
  drafts it cites (NDT reference architecture; *data generation and optimization for NDT performance modelling*) are
  not peer-reviewed. The first is already in ALL_CANDIDATES as IRTFNMRG2026Ndtarch. The second is left to the
  coordinator as a possible standards/grey item. Nothing new was added.
- **Zanzi2026Cloudnativendt** (ICC 2026). Crossref holds its 10 references. All of them are already in the pool
  (rows 7, 8, 48, 49, 50, 89), in ALL_CANDIDATES (Basikolo2023Zerodowntime, Costa2025Privatendt), or are one
  ACM UCC 2023 paper on microservice autoscaling (pool row 90). Nothing new was added. No arXiv version was found.

## Inclusions (borderline)
- **Dede2025Ai6Gcore** (ISAS 2025, a niche symposium). It is a thin, qualitative review, but it is one of the few works
  whose topic is exactly *AI in the 6G core*, so the survey should position itself against it. Flagged `survey`, with a critical
  limitation.
- **Petrik2025Dtdomaintransfer** (ELMAR 2025, a regional venue). Included because it is rare empirical evidence of a
  **twin-fidelity (sim-to-real) gap** on an Open5GS twin, which bears on gap G3.
- **Isah2026Kgfailureloc** (ICUFN 2026). This is a C3-type paper (5GC RCA on real telemetry), but it appears only in the C2 pool (via
  Tao2024Corecontrolplane forward). Included because few 5GC failure-localisation works use real core telemetry.
- **Araujo2026Scope5G** (IEEE Access 2026). Primary subdomain S4. It is in C2 because it cites the Tao control-plane model.
  Included because it touches gap 8 (no public 5GC benchmarks).
- **Mozo2022B5Geminijournal** (Sensors 2022) is the journal companion of the seed Mozo2022B5Gemini (NOMS 2022).
  PROTOCOL.md §3 says to keep the journal version over the conference version and to record both. Both are now present. The coordinator
  may decide whether to keep both or to cite the journal one only.
- **Tao2025Dtonlinedrl** (TCOMM). The pool lists it as 2023 (arXiv). The verified version is TCOMM, Crossref year 2025.
  Its arXiv twin (pool row 81, arXiv 2310.09299) was dropped as a duplicate.
- **VillotaJacome2022Coreslicingadmission**: core-slicing admission with RL. It has no twin, but it is the core-specific
  baseline that the C2 seed Wang2024Sliceadmission builds on. Relevance 3 because the work is explicitly about the 5G core with AI.

## Exclusions (borderline)
- Pool rows 0, 1, 3 (NOMS 2026 NWDAF closed loop, link 6; NCC 2025 NWDAF review, link 5; ISNCC 2023 NWDAF data
  collection, link 3) are relevant but are **C1 works**, and they appear identically in pool_C1. They were left to the C1 agent to avoid
  duplicate characterisation. If C1 does not select them, the coordinator should take at least row 0.
- Row 77 (*Heterogeneous signalling and user traffic for 5GC functional testing*, IEEE Access 2023) is a core testing tool
  with no AI or twin modelling. It is listed as a runner-up.
- Row 8 (*predictive VNF autoscaling*, TNSM 2021) is a C4 topic, not in the core and not a twin. Runner-up.
- Row 97 (Ericsson Technology Review), rows 126, 131 and 132 (patent, press release, roadmap) and row 99 (white paper) were dropped as
  not peer-reviewed. Row 88 (Springer book chapter) was dropped as a book.
- Many forward citers of Wang2024Sliceadmission and Mozo2022B5Gemini are generic IoT, robotics, security or RAN-slicing DT papers
  in low-visibility venues (rows 10-12, 16-25, 27, 30, 33-38, 40-41, 43, 45-47, 52-53, 57-59). They were dropped as off-topic for the core.
- Pre-2020 rows (138-177) are generic ML (Adam, LSTM, BERT, Transformer) or old RAN and M2M work. No `seminal` item was proposed:
  none is a foundational network-twin or core-modelling work that is missing from ALL_CANDIDATES.
- arXiv-only rows from before 2025 (61 DTRAN, 81, 136 HEBO) were dropped by rule.

## Venue notes
- ISAS 2025: Crossref names the venue "9th International Symposium on Innovative Approaches in Smart Technologies"
  (the pool said "International Service Availability Symposium"). The Crossref name is recorded.
- Nardini2024Simu5Gdt: OpenAlex gives 2023 (online first), Crossref gives 2024 (issue). The Crossref year is kept.
