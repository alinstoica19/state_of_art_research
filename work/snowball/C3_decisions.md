# C3 snowball: judgement calls

Category C3 (assurance: anomaly detection, RCA and resilience of the core). Pool `work/snowball/pool_C3.csv`, 246 rows.

## Seed recovered by hand

- **Leiter2022Upffailover** (doi:10.1109/noms54207.2022.9789799). Semantic Scholar lists 10 references but does not
  expose them. The Crossref record carries the full reference list (11 entries). All of them are product or
  project documentation: ONAP components (SDC, SO, CDS, Policy, A&AI, DMaaP, VES), Kubernetes, Helm, and one
  industry best-practice document on migrating from physical to virtual NFs. None is a peer-reviewed research
  work, so the backward-manual step added **no candidates**. Its 7 forward citations were already in the pool
  (rows from `Leiter2022Upffailover(forward)`) and were screened: two are relevant but were not selected
  (PDRS at IWCMC 2025 and the RAN fault-tolerance paper at NFV-SDN 2023, see the runners-up); the rest are
  generic cloud DR, test methods, an invited overview, and a non-English-venue router failover note.

## Borderline inclusions

- **Owen2025Sovereignfunctions** (IEEE Access, survey). It is about IP-level shared functions, not the 5GC, so it
  gets relevance 2. Kept because it links to three seeds and gives outage case studies for the motivation of the
  resilience section.
- **Tufeanu2026Residualartifacts** (TNSM 2026). It covers platform ageing (leftover Kubernetes objects) rather
  than NF faults. Kept with relevance 3 because it applies ML prediction to the stability of a cloud-native SBA
  core and links to three seeds.
- **Li2023Resilienceestimation** (TNSM 2023). A simulation model of service resilience to traffic surges. It is
  relevant as a model-based "what-if" resilience estimator (it touches G3/P2), but it does not model failures, so it
  gets relevance 2.
- **Sovitkar2024Capstateless** (CCNC 2024, 4-page short paper). Kept with relevance 3, as for its successor RECAP
  (the seed). It is the only pool work that measures the consistency/availability trade-off of shared 5GC state.
- **Kato2023Reconnectionstorm** (VTC 2023-Spring). VTC is not in the PROTOCOL §3 top list, but the paper is
  KDDI's on the UE reconnection storm after large failures, which is direct evidence for P3/P4. Kept.
- **Selvakumar2025Outlierdensity** (Globecom Workshops 2025). A workshop paper from Fraunhofer FOKUS (Corici), the
  group of the seed Chakraborty2021Failureforecast. It is kept as the current state of that line of work. Its
  companion FNWF 2025 paper (UE churn vs outlier density) is a runner-up.
- **Behnaminia2026Upfrecovery** (arXiv 2610.03245, October 2026). Preprint, allowed by the 2025-2026 rule. No
  published version was found on Crossref. It is flagged `preprint`.
- **Ahmad2022Cellclone** (CoNEXT 2022). Same group as Neutrino (already in ALL_CANDIDATES as the ToN journal
  version). CellClone is a different system (active replication with a quorum protocol), not a version of
  Neutrino, so it is not a duplicate.
- **AnomalyTrack** (ISCC 2025). ISCC is not in the top list, but it is a peer-reviewed IEEE symposium and the work
  uses one year of commercial-operator KPI data, which is rare in this category (gap 8).

## Exclusions worth noting

- **Neutrino, SIGCOMM 2020** ("A Low Latency and Consistent Cellular Control Plane"). This is the conference
  version of Ahmad2023Neutrino (ToN), which is already in ALL_CANDIDATES, so it was dropped as a duplicate.
- **CoreKube MobiCom 2023 demo** ("CoreKube - A Message Focused and Cloud Native Mobile Core System"). A companion
  demo of the seed Larrea2023Corekube, so it was dropped.
- **Warping the Edge** (arXiv 2024) and **Unraveling the Airalo Ecosystem** (arXiv 2024): preprints of published
  versions, and off-topic anyway.
- **"ML5G-PS-005: Network failure prediction on CNFs 5GC with Linux eBPF"** (ITU AI Challenge problem statement):
  not a peer-reviewed paper.
- **Procedure-based Functional Decomposition for 5G Core NFs** (repository record, 2022): an early short version
  of PP5GS (selected), so it was dropped.
- **Cyber resilience in next-generation networks** (Foundations and Trends in Networking 2026): a monograph-length
  work on generic cyber resilience, not core-specific. Dropped as background.
- **Alawe et al. 2018, "Improving Traffic Forecasting for 5G Core Network Scalability"** (IEEE Network, L=5, the
  most-linked row). It is about autoscaling (C4), not assurance, and it is pre-2020. It was not proposed as
  `seminal` from C3. It also appears in the C1 and C4+C5 pools, and the coordinator may take it as a seminal work
  from there.
- No `seminal` items are proposed from C3. StatelessNF (NSDI 2017) would be the natural candidate for state
  externalisation, but its pool row has no DOI and the topic is already covered by Kulkarni2021Statelesscost and
  the stateless-core papers in ALL_CANDIDATES.

## Venue notes

- IEEE Network (ForenSiX) is a peer-reviewed magazine, so it was kept as `journal`.
- PP5GS has a 2022 early-access DOI. Crossref gives the issue year as 2023 (vol. 20, no. 3), and the CSV uses 2023.
