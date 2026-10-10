# C3 snowball report: assurance (anomaly detection, RCA, resilience of the core)

## Counts

| Step | Count |
|---|---|
| Pool size (`pool_C3.csv`) | 246 |
| Screened by title | 246 (all rows) |
| Abstracts read | about 90 (every plausibly relevant row from 2020 on, plus a few borderline pre-2020 rows) |
| Dropped: pre-2020 or undated | 97 (includes about 15 news items, blogs and other non-papers, from Basikolo2023Zerodowntime's reference list) |
| Dropped: wrong type or duplicate | about 8 (conference/demo/preprint versions of works already listed, one ITU challenge statement, one monograph, one repository short version) |
| Dropped: off-topic or too far from the core (from 2020 on) | about 110, approximate (RAN/IoT/V2X forecasting, generic cloud, security surveys, slicing resource allocation, scheduling theory, measurement studies with no assurance angle) |
| Relevant but not selected | about 15 (see runners-up) |
| **Selected** | **15** |
| **Verified** (Crossref for 14 DOIs, arXiv API for 1 ID) | **15** (0 unverified) |

Leiter2022Upffailover: its reference list was recovered from Crossref (11 entries). All are ONAP, Kubernetes or
Helm documentation, plus one industry best-practice document, so no peer-reviewed candidates came from it. See
`C3_decisions.md`.

## Selected and verified works (ranked by link_count, then relevance)

| id | title | year | L | rel | sub |
|---|---|---|---|---|---|
| DaSilva2025Anomalytrack | AnomalyTrack: Scalable and Self-Adaptive Anomaly Detection in Large-Scale 5G Networks (ISCC) | 2025 | 3 | 3 | S4 |
| Tufeanu2026Residualartifacts | Residual Artifact Governance With ML-Enabled Garbage Collection Prediction in Kubernetes-Based 5G/6G SBA (TNSM) | 2026 | 3 | 3 | S5 |
| Owen2025Sovereignfunctions | Failures and Resilience in the IP Era ... The Sovereign Functions (IEEE Access, survey) | 2025 | 3 | 2 | S5 |
| Sovitkar2024Capstateless | Evaluating CAP Theorem on a Stateless 5G Core (CCNC) | 2024 | 2 | 3 | S5 |
| Sarkar2022Locomotive | LOCOMOTIVE 5G Core for 6G ready Resilient and Highly Available Network Slices and SFCs (CNSM) | 2022 | 2 | 3 | S5 |
| Khichane20245Gcanalyser | 5GC-Analyser: Demistifying the 5G Core Network Through Statistical Analysis (ICC) | 2024 | 2 | 3 | S4 |
| Hirayama2025Multiaiclosedloop | Autonomic Closed-Loop Service Management based on Interworking Multiple AI Models (NOMS) | 2025 | 2 | 3 | S6 |
| Goshi2023Pp5Gs | PP5GS: An Efficient Procedure-Based and Stateless Architecture for Next-Generation Core Networks (TNSM) | 2023 | 2 | 2 | S2 |
| Li2023Resilienceestimation | Estimating 5G Network Service Resilience Against Short Timescale Traffic Variation (TNSM) | 2023 | 2 | 2 | S5 |
| Paul2025Faulttolerantk8S | A Scalable and Fault-Tolerant 5G Core on Kubernetes (COMSNETS) | 2025 | 1 | 3 | S5 |
| Huang2025Forensix | ForenSiX: Automated Network Forensics and Diagnostics for B5G and 6G Networks Using LLMs (IEEE Network) | 2025 | 1 | 3 | S4 |
| Kato2023Reconnectionstorm | Congestion Control by Mobile Core and RAN Coordination in 5G Mobile Network (VTC-Spring) | 2023 | 1 | 3 | S5 |
| Selvakumar2025Outlierdensity | Proactive 5G Core Network Failure Prediction using Nonlinear Dynamical Analysis and Statistical Outlier Detection (GC Wkshps) | 2025 | 1 | 3 | S4 |
| Behnaminia2026Upfrecovery | A Dynamic UPF Fault Recovery Mechanism for Enhanced Resilience in 5G Core Networks (arXiv 2610.03245) | 2026 | 1 | 3 | S5 |
| Ahmad2022Cellclone | Enabling emerging edge applications through a 5G control plane intervention, i.e. CellClone (CoNEXT) | 2022 | 1 | 2 | S5 |

Files: `work/SB_C3.jsonl`, `results/SB_C3_snowball_c3.csv`, `results/SB_C3_snowball_c3.bib`,
`results/SB_C3_unverified.csv` (empty).

## Runners-up, ranked (not selected)

1. Predictive Disaster Recovery for Multi-Redundant Operations and Maintenance 5G Network Systems (IWCMC 2025):
   doi:10.1109/iwcmc65282.2025.11059520. ML-predicted proactive failover to the best of several redundant backups,
   applied to O&M systems rather than core NFs.
2. 5G-STREAM: Service Mesh Tailored for Reliable, Efficient and Authorized Microservices in the Cloud (DSN 2025):
   doi:10.1109/dsn64029.2025.00025.
3. Characterizing 5G Core Stability under Dynamic UE Conditions via Outlier Density Analysis (FNWF 2025):
   doi:10.1109/fnwf66845.2025.11317174.
4. Signaling Storm Mitigation by Geographically Distributed C-plane NF Placement and Routing (NetSoft 2024):
   doi:10.1109/netsoft60951.2024.10588904.
5. Anomaly Detection using a Semi-Supervised Deep Learning Model on Open 5G Core Metrics during User-Equipment
   Registration (CSCN 2023): doi:10.1109/cscn60443.2023.10453203.
6. Automated Fault Detection in 5G Core Networks Using Large Language Models (arXiv 2512.19697, 2025).
7. Measuring What Matters: Increasing the Observability of Signalling Traffic in the 5G Core (NetSoft 2026):
   doi:10.1109/netsoft70012.2026.11603420.
8. High-Fidelity Cellular Network Control-Plane Traffic Generation without Domain Knowledge (IMC 2024):
   doi:10.1145/3646547.3688422. More relevant to C2/G3 (fidelity of generated control-plane traffic).
9. Monitoring 5G Core Networks Vulnerabilities With eBPF (IEEE Networking Letters 2025): doi:10.1109/lnet.2025.3577184.
10. Resource-Aware Service Prioritization in a Slice-Supportive 5G Core Control Plane for Improved Resilience and
    Sustenance (CCNC 2024): doi:10.1109/ccnc51664.2024.10454708.
11. Organic 6G Networks: Towards a Dependable, Flexible Control Plane (NetSoft 2026): doi:10.1109/netsoft70012.2026.11603534.
12. Fault-Tolerance in Future RAN: Enabling Redundancy for Efficient Recovery of RAN Network Functions (NFV-SDN 2023):
    doi:10.1109/nfv-sdn59219.2023.10329718.

## Taxonomy categories strengthened

- **C3, resilience (S5):** 9 works. They add measured evidence on stateless and replicated control planes (CAP
  trade-off, Kubernetes failover design choices, active replication with quorum consistency, LB redundancy versus
  hot standby), UPF failure recovery, and recovery from post-failure reconnection storms.
- **C3, anomaly detection and RCA (S4):** 4 works. These are operator-scale KPI anomaly detection, statistical
  causality among 5GC NF metrics, control-plane failure prediction (the Fraunhofer line), and LLM-assisted
  cross-NF forensics.
- **C5 (S6):** 1 work (a closed loop of interworking AI models acting on predicted failures).
- **C4 (S2):** 1 work (PP5GS, stateless procedure-based core).

## Evidence on the gap claims (SUMMARY.md §4)

- **G2 (analytics wired to NRF/SCP selection or TS 23.527 restoration).** The claim mostly holds. The nearest work
  is Behnaminia2026Upfrecovery, which feeds UPF failure history into UPF selection. This partly weakens the claim
  for *UPF* selection, but the work is a preprint, it does not use NWDAF, and it is not compared with TS 23.527
  PFCP restoration. Hirayama2025Multiaiclosedloop acts on predicted failures without using 3GPP actuators. The
  NetSoft 2024 signaling-storm runner-up routes UEs to C-plane NF instances by load and context count, but it is
  algorithmic, not analytics-driven.
- **G3 (control-plane twins, twin fidelity).** No core control-plane twin in this pool. Li2023Resilienceestimation
  is a model-based estimator of service resilience under traffic surges: an offline what-if model, not a twin, and
  not validated for fidelity. The IMC 2024 control-plane traffic generator (runner-up 8) explicitly evaluates
  *fidelity* of synthetic control-plane traces. It is the closest thing to a fidelity metric and is worth citing in
  the G3 discussion.
- **G7 (geo-redundancy, UDR/UDSF failover, effect on UE procedures).** Partly weakened for single-site failover.
  Paul2025Faulttolerantk8S measures fault tolerance of 3GPP-compliant core variants on Kubernetes,
  Sovitkar2024Capstateless measures the CAP trade-off of shared NF state, CellClone measures replicated control
  planes under node failure, and LOCOMOTIVE measures LB failure. The claim still **holds for cross-site
  geo-redundancy**: no work in the pool measures UDR/UDSF replication across sites, database primary failover, or
  their effect on UE procedures. The PDRS runner-up does multi-redundant predictive failover, but for O&M systems.
  Suggested rewording: "stateless and replicated designs now report single-site failover behaviour, but
  cross-site subscriber-database failover and its UE-procedure cost remain unmeasured."
- **P1 (SCP as telemetry source).** Nothing new. 5G-STREAM (service mesh for the core) and the eBPF SBI-monitoring
  letter observe SBI traffic, but for signalling efficiency and for security, not for analytics or RCA through an
  SCP.
- **P2 (testing whether a remedy can help before applying it).** Nothing direct. Li2023 compares auto-scaling and
  isolation strategies in an offline model. No work checks online whether rerouting can help when a shared back
  end is degraded.
- **P3 (procedure-level UE models under faults).** Holds. The nearest works are Kato2023Reconnectionstorm (an
  aggregate model of the UE reconnection storm after large failures, with no NAS timers), the Fraunhofer UE-churn
  study (runner-up 3), anomaly detection during UE registration (runner-up 5) and per-UE signalling observability
  (runner-up 7). None predicts UE-level outcomes such as T3510 expiry or retries.
- **P4 (multi-action remedies in a multi-site core; transient cost of DB failover).** Holds. The works compare
  single mechanisms (hot standby vs active LB, CP vs AP mode, Kubernetes failover variants). No work evaluates
  stay / reroute / DB-failover alternatives across sites.

## Research groups not listed in SUMMARY.md §5

Affiliations are inferred from author lists and known group membership. Confirm them before citing.

- **IIT Bombay** (Mythili Vutukuru): fault-tolerant 3GPP-compliant core on Kubernetes.
- **LUMS, Pakistan** (Zafar Ayyub Qazi, with Muhammad Taqi Raza): CellClone. This is the same team as Neutrino
  (already listed as a work, but the group is not named in §5).
- **TU Munich and Nokia** (Wolfgang Kellerer, Endri Goshi; Rastin Pries, Hasanin Harkous): procedure-based
  stateless core (PP5GS).
- **USTC** (Kaiping Xue): LLM-based forensics and RCA for B5G/6G (ForenSiX).
- **CentraleSupélec / Paris-Saclay with Orange** (Zhiguo Zeng, Anne Barros, Bertrand Decocq): 5G service
  resilience estimation.
- **KDDI Research with NEC** (Takuya Miyasaka, Junichi Kawasaki, Takayuki Kuroda): closed-loop CNF management
  and reconnection-storm congestion control. This extends the "KDDI Research" entry in §5.
- **Politehnica Bucharest and University of Agder** (Marius-Constantin Vochin, Frank Y. Li): residual-artifact
  governance in Kubernetes SBA.
- **Brazil** (Michel Santos Da Silva, Lourenço Alves Pereira): operator-scale anomaly detection (AnomalyTrack).
- **UTS Sydney** (Mehran Abolhasan): telecom failure survey.
- **IIT Hyderabad** (Vittal, Franklin, with Sarkar and Sovitkar): already listed. Two of the new works
  (LOCOMOTIVE, the CAP evaluation) are theirs.
