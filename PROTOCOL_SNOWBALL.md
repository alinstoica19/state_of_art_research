# PROTOCOL 2: citation snowballing and gap check

<!-- Pentru Alin: copiază TOT fișierul ca prim mesaj într-o sesiune cloud nouă, pe repo state_of_art_research,
     ramura claude/5g-6g-literature-search-2lyo41 (acolo e ALL_CANDIDATES.csv de la prima căutare). -->

You are running autonomously in a cloud session. First save this message as `PROTOCOL_SNOWBALL.md`,
then execute it **from start to end without stopping**. **Do not ask the user questions:** write
judgement calls to `DECISIONS_SNOWBALL.md` and continue. Commit and push after every finished batch.
If you can only push to a session branch, say so in `STATUS_SNOWBALL.md`.

## 1. Context

A first systematic search (this repository: `PROTOCOL.md`, `ALL_CANDIDATES.csv`, `SUMMARY.md`) produced 179
verified works for a survey:

> *AI-native automation of the 5G-Advanced and 6G core network: network analytics, digital twins and autonomous
> decision loops. A critical review of the literature and of 3GPP Releases 18-21.*

Keyword search misses works that use other vocabulary. This run applies standard **citation snowballing**
(backward and forward) to the 37 most central works, the seeds, and then **stress-tests the gap claims**.
The same rules apply as in `PROTOCOL.md` §3-§5: verification, own-words summaries, no guessed quartiles,
and the same CSV columns.

## 2. Seeds (37; category = draft taxonomy in `SUMMARY.md` §3)

| Cat | Key | Identifier | Year |
|---|---|---|---|
| C1 | Abbas2022Sliceanalytics | doi:10.1109/noms54207.2022.9789706 | 2022 |
| C1 | Ameur2026Agenticnwdaf | doi:10.1109/icc59461.2026.11587766 | 2026 |
| C1 | Ardestani2026Closedloop | doi:10.52953/svmm1934 | 2026 |
| C1 | Bayleyegn2024Kpiprediction | doi:10.1109/netsoft60951.2024.10588931 | 2024 |
| C1 | Chouman2022Nwdaf | doi:10.1109/iwcmc55113.2022.9824403 | 2022 |
| C1 | Daniel2026Opennwdaf | arXiv:2601.01838 | 2026 |
| C1 | GarciaMartin2024Nwdaf | doi:10.1109/mnet.2023.3321524 | 2024 |
| C1 | Jeon2022Distributednwdaf | doi:10.1109/icce53296.2022.9730220 | 2022 |
| C1 | Majumdar2026Ainative | doi:10.1109/mcomstd.2025.3585376 | 2026 |
| C1 | Manias2022Signaling | doi:10.1109/globecom48099.2022.10000989 | 2022 |
| C1 | Manias2023Modeldrift | doi:10.1109/mcom.003.2200306 | 2023 |
| C1 | Mekrache2023Abnormaltraffic | doi:10.1109/globecom54140.2023.10436766 | 2023 |
| C1 | Nadar2024Modelprovisioning | doi:10.1109/medcomnet62012.2024.10578162 | 2024 |
| C1 | Oliveira2025Aiaas | doi:10.23919/cnsm67658.2025.11297508 | 2025 |
| C1 | Romero2025Nwdafreview | doi:10.14209/sbrt.2025.1571141712 | 2025 |
| C1 | Sevgican2020Nwdaf | doi:10.1109/jcn.2020.000019 | 2020 |
| C1 | Zhang2025Fairfl | doi:10.1109/tits.2024.3461679 | 2025 |
| C1 | Zhang2025Sammf | doi:10.1109/lnet.2025.3579358 | 2025 |
| C1 | Zhou2023Federatednwdaf | doi:10.1109/lnet.2023.3294497 | 2023 |
| C2 | BenllochCaballero2026Corex | doi:10.1109/tnsm.2026.3699692 | 2026 |
| C2 | Costa2025Privatendt | arXiv:2510.12458 | 2025 |
| C2 | Mozo2022B5Gemini | doi:10.1109/noms54207.2022.9789810 | 2022 |
| C2 | Tao2024Corecontrolplane | doi:10.1109/tccn.2023.3324634 | 2024 |
| C2 | Wang2024Sliceadmission | doi:10.1016/j.future.2023.12.018 | 2024 |
| C2 | Xie2026Signalingstorm | doi:10.1145/3789240.3829205 | 2026 |
| C2 | Zanzi2026Cloudnativendt | doi:10.1109/icc59461.2026.11587512 | 2026 |
| C3 | Basikolo2023Zerodowntime | doi:10.52953/pyaf8065 | 2023 |
| C3 | Chakraborty2021Failureforecast | doi:10.1109/iccworkshops50388.2021.9473530 | 2021 |
| C3 | Kawasaki2023Failureprediction | doi:10.1109/vtc2023-spring57618.2023.10200028 | 2023 |
| C3 | Larrea2023Corekube | doi:10.1145/3570361.3592522 | 2023 |
| C3 | Leiter2022Upffailover | doi:10.1109/noms54207.2022.9789799 | 2022 |
| C3 | Sovitkar2024Recap | doi:10.1109/noms59830.2024.10575767 | 2024 |
| C3 | Vittal2022Harness | doi:10.1109/tnsm.2022.3157888 | 2022 |
| C3 | Vittal2024Resilientcore | doi:10.1109/tnsm.2023.3348137 | 2024 |
| C4 | Kamran2025Energyexposure | doi:10.1109/comsnets63942.2025.10885745 | 2025 |
| C5 | Ameur2026Agenticsurvey | arXiv:2607.16066 | 2026 |
| C5 | Coronado2022Zerotouch | doi:10.1109/comst.2022.3212586 | 2022 |

## 3. Phase 1: harvest (parallel subagents, one per category C1, C2, C3, C4+C5)

For each seed:
- **Backward:** its reference list, from OpenAlex `referenced_works`
  (`https://api.openalex.org/works/doi:<DOI>`) or the Semantic Scholar `references` endpoint.
- **Forward:** the works citing it, from the OpenAlex `cited_by_api_url` (filtered to 2022-2026) or Semantic
  Scholar `citations`.
- Single-work lookups and `cited_by` pages are cheap. Avoid OpenAlex keyword search (its free daily quota ran
  out in the first run). On HTTP 429, back off and fall back to Semantic Scholar.
- **Do not send any e-mail address or personal identifier to these APIs.**

Pool the candidates per category and drop:
- works already in `ALL_CANDIDATES.csv` (match by DOI, else by normalised title);
- pre-2020 works, unless foundational: flag `seminal`, at most 5 in total;
- off-topic works, after reading the abstract.

Rank the remaining candidates by **link count** (how many seeds cite them or are cited by them), then by
relevance to the 5G/6G core.

## 4. Phase 2: select and verify

- From each category, keep the best **8-15 new works** that clearly belong in the survey. Overall target:
  **30-50 new works.**
- Verify each exactly as in `PROTOCOL.md` §4. Never invent; unverifiable items go to `unverified_snowball.csv`.
- Output `results/SNOWBALL.csv` with the same columns as `ALL_CANDIDATES.csv` plus:
  - `found_via`: seed keys and `backward`/`forward`;
  - `link_count`.
- Output `snowball.bib`.
- **Budget safety:** commit and push each category as soon as it is done, and update `STATUS_SNOWBALL.md`.

## 5. Phase 3: gap check (the most important part)

The survey will claim the gaps in `SUMMARY.md` §4. A later companion paper will claim specific contributions.
Search **specifically for prior work that would weaken these claims**: snowball, plus targeted searches on
Crossref, Semantic Scholar and arXiv. For each claim, report what you find, with verified references, and give
a verdict: **holds**, **partially covered**, or **already done**.

| # | Claim to stress-test |
|---|---|
| G2 | Analytics (e.g. NWDAF NF-load or abnormal-behaviour analytics) are **not** wired to standard actuators: NF selection or reselection via NRF/SCP, TS 23.527 restoration, or NF-set reselection. |
| G3 | Digital twins of the **5G core control plane** are rare, and **twin fidelity is not measured**. No twin predicts the outcome of a candidate action at control-plane speed. |
| G7 | Resilience work is disconnected from AI and from **geo-redundancy**: cross-site failover of core NFs and of the subscriber database (UDR/UDSF replication, DB primary failover) and its effect on UE procedures. |
| P1 | Using the **SCP** (Service Communication Proxy) as a telemetry source for analytics, anomaly detection or root-cause analysis. Known prior art, already cited: 5G-RAD (INFOCOM 2023) and the T-Mobile patent US 12,155,534. Find anything else. |
| P2 | **Testing whether a remedy can help before applying it** in the core: rerouting cannot help when a shared back-end is degraded; checking whether the action helps. |
| P3 | **Procedure-level models** of 5G registration or other UE procedures under faults that predict **UE-level outcomes**, such as NAS timer (T3510) expiry or retries. |
| P4 | Evaluating **multi-action remedies** in a multi-site core (stay / reroute NFs / database failover) and the **transient cost of database failover** on UE procedures. |

Write `GAP_CHECK.md`: one section per claim, with the evidence found, a verdict, and how the claim should be
reworded if it is weakened.

## 6. Phase 4: summary

Write `SNOWBALL_SUMMARY.md` containing:
- counts: harvested, filtered, verified, and per category;
- the 10 most important new works, with one line each;
- which taxonomy categories they strengthen;
- whether the new works change any gap in `SUMMARY.md` §4;
- additional research groups not seen in the first run.

Then commit and push.

## 7. Rules

- No copyrighted text: one-sentence summaries in your own words, and no quotation longer than 10 words.
- A smaller verified list beats a long unverified one.
- Keep `DECISIONS_SNOWBALL.md` updated.
