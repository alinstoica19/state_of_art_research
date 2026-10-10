# S6 — Closed-loop and autonomous networks: decisions

## Search queries run
Crossref bibliographic search (`verify.py search`): "zero-touch network and service management survey"; "intent-based networking survey";
"intent-based management 5G"; "closed loop automation 5G network slicing"; "autonomous networks survey"; "large language models
telecommunications survey"; "LLM intent-based networking configuration"; "agentic AI 6G network management"; "large language models for
telecom survey"; "large language model enabled 6G network"; "generative AI for 6G network management"; "LLM agents network operations
troubleshooting"; "self-driving networks"; "knowledge-defined networking"; "MAPE-K autonomic network management 5G"; "intent-driven network
slicing closed loop"; "AI-native 6G network management autonomous"; "zero-touch 5G core closed-loop"; title look-ups for known works (Coronado
ZTM survey, Zhou LLM-telecom survey, Maatouk, Huang LLM-networking, NetLLM, Mekrache LLM-centric IBN, NetConfEval, KDN, intent-driven closed
loops, GenAI network management); "autonomous network levels intent 3GPP TM Forum"; "large language model agents autonomous network
operation"; "LLM multi-agent 5G core network"; "intent-based network slicing zero-touch closed loop reinforcement learning"; "intent assurance
closed loop 5G"; "generative AI agents autonomous networks survey"; "self-healing 5G core closed loop"; "zero-touch network slicing management
closed-loop machine learning 5G"; "From zero-touch to intent-based networking ..."; "Ksentini large language model network slicing intent";
"LLM agents 6G network management survey".
WebSearch: "arXiv 2025 LLM agent 5G core network autonomous closed-loop"; "agentic AI autonomous networks survey 2025 telecom IEEE";
3GPP spec-id look-ups for TS 28.312 / TS 28.100; ETSI ZSM 009-1 / ZSM 002 PDFs; AICOM and JNSM 2022 abstracts.
Abstracts were read via OpenAlex (abstract_inverted_index), arXiv API, or search snippets (AICOM, JNSM 2022).

## Judgement calls
- **Query drift.** Generic "autonomous networks survey" and "self-driving networks" returned mostly vehicle/UAV papers; "knowledge-defined
  networking" returned only weak venues (MDPI Telecom, Array) — no KDN item kept. Discovery was redirected to ZSM/IBN/LLM/agentic terms.
- **Standards (4).** ETSI GS ZSM 009-1 V1.1.1 (2021-06) confirmed via WebFetch of the ETSI PDF (title page extracted locally; curl gets 403),
  hence `verified_by_webfetch`. ETSI GS ZSM 002 V1.1.1 (2019-08) was also confirmed but left out to respect the ~4-standards cap (ZSM 009-1
  builds on it; cite it in the article as architecture background). 3GPP TS 28.312: portal specificationId 3554, cited at V19.5.0 (Rel-19),
  version confirmed from the ETSI TS 128 312 V19.5.0 (2026-04) title page; draft Rel-20 versions (V20.0.x/V20.1.0) exist on the 3GPP FTP but
  were not cited. 3GPP TS 28.100 (levels of autonomous network): specificationId 3756 (found by scanning portal IDs), cited at V18.0.0 (Rel-18),
  confirmed from ETSI TS 128 100 V18.0.0 (2024-05); a Rel-19 V19.0.0 is reported by third-party indexes only, so not cited. TS 28.105 (AI/ML
  management) left to S1/S8. RFC 9315 entered as a standard row (datatracker URL; DOI 10.17487/rfc9315 exists) so the BibTeX key is clean.
- **Conference vs journal duplicates.** Shafiei Ardestani/Limam/Boutaba: kept ITU J-FET 2026 journal version (10.52953/svmm1934) over NOMS 2026
  (10.1109/noms69089.2026.11668240); note both are also in S1 (dedup in Phase 3). Sousa/Rothenberg: kept JNSM 2022 over CLARA (NFV-SDN 2021,
  10.1109/nfv-sdn53031.2021.9665048). Mekrache/Ksentini: kept IEEE Network 2024 over NetSoft 2024 (10.1109/netsoft60951.2024.10588881).
  Manias/Chouman/Shami: kept GLOBECOM 2024 (semantic routing, dataset) over DRCN 2024 (10.1109/drcn60692.2024.10539172, LLM intent extraction
  in 5GC, 54 cites) — both are relevance-3; author may add DRCN. Brodimas et al.: kept ICNC 2025 (5G core deployment) over EuCNC/6G Summit 2024
  (10.1109/eucnc/6gsummit60053.2024.10597022).
- **Preprints.** AgentxGCore (arXiv 2606.00417) and AGORA (arXiv 2602.13290) have published DOIs; AgentxGCore entered with its IEEE Network
  DOI. AGORA (IEEE Access 2026, 10.1109/ACCESS.2026.3672699, LLM agent steering UPF for energy) is a good candidate for S7 and not included
  here to stay within ~22. Only one pure preprint kept: Ameur/Mekrache/Brik/Ksentini 2026 agentic tutorial-survey (under review).
- **Relevance.** Coronado survey and the agentic 5G/6G survey rated 3 because they explicitly cover the core network; generic IBN/LLM surveys
  rated 2. 3GPP TS 28.312/28.100 and ETSI ZSM 009-1 rated 2 (directly define closed-loop/intent/autonomy concepts for mobile management);
  RFC 9315 rated 1 (IP-oriented terminology).
- **Venue doubts.** Journal of ICT Standardization (River Publishers) is peer-reviewed but low-profile; kept for its ZSM/intent closed-loop
  coordination content (Ericsson authors). Boutaba et al. 2021 is an ACM FlexNets workshop (SIGCOMM 2021) vision paper — kept as the conceptual
  MAPE-loop anchor of the Waterloo group. ITU J-FET is peer-reviewed (ITU journal).
- **AICOM (IFIP Networking 2026).** OpenAlex abstract was empty and the IFIP PDF returned 503; summary is based on search snippets of the PDF
  (Orange Innovation / Paris-Saclay; GitOps + Kubernetes + LLM agents; OAI 5GC with Gemini/Qwen/Llama). Critique worded cautiously.

## Rejected / not included (and why)
- Gallego-Madrid et al., ML-based ZSM survey (DCN 2022, 10.1016/j.dcan.2021.09.001): overlaps with Coronado and Liyanage surveys; optional add.
- Benzaid & Taleb, AI-driven ZSM (IEEE Network 2020, 10.1109/mnet.001.1900252, ~315 cites): position paper on AI risks in ZSM; strong
  optional add if the author wants a highly-cited ZSM+AI anchor.
- Maatouk et al. LLMs for Telecom (IEEE ComMag 2025), Huang et al. LLMs for Networking (IEEE Network 2025), NetLLM (SIGCOMM 2024): general
  LLM-for-networking pieces without closed-loop/core focus; covered by the Zhou and Hong surveys.
- Maestro (IEEE Netw. Lett. 2024, LLM agents negotiating in O-RAN), INTA (ICNP 2025, config translation), IJNM 2024 intent-based config with
  LLMs, CNSM 2024 config generation: relevance 2 at best, RAN/IP focus.
- Vittal et al. CNSM 2021 zero-touch 5GC slicing (demo, 10.23919/cnsm52442.2021.9615531) and Abbas et al. IEEE Access 2021 IBN slice
  lifecycle (10.1109/access.2021.3084834): older 5G slicing loops, dropped for space; good optional additions for a 5GC testbed angle.
- ICT 2026 "Closed Loop Intent Based Agent for Resilient Multi-UPF 5G Networks", Computer Communications 2026 "IBN using LLM-driven agentic RL",
  TNSM 2026 PCLANSA proactive slice assurance: no abstract could be read; not included (could be checked by the author; PCLANSA abstract seen,
  relevant to S5/S6).
- Excluded as non-peer-reviewed/weak venues: SSRN, TechRxiv, Research Square, IJSR, IJCA, Technium, MDPI-like KDN surveys.
