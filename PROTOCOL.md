# PROTOCOL: systematic literature search for a state-of-the-art article



You are running autonomously in a cloud session. The repository is empty. First save this whole
message as `PROTOCOL.md` in the repository root, then execute it **from start to end without
stopping**. **Do not ask the user questions:** make reasonable choices, write them to
`DECISIONS.md`, and continue. Commit and push to `main` after every finished subdomain and at the
end of each phase.

## 1. Goal and context

A PhD candidate in telecommunications (Politehnica University of Bucharest; research on
AI-based automation and management of 5G/6G core networks) is preparing a **state-of-the-art
survey article**. Working title:

> *AI-native automation of the 5G-Advanced and 6G core network: network analytics, digital twins
> and autonomous decision loops. A critical review of the literature and of 3GPP Releases 18-21.*

The model articles are systematic reviews: search and selection method → a taxonomy of ~4
categories → per-paper comparison tables (method, metrics, tools or testbed, pros/cons) →
discussion → challenges and future directions, with 100+ references.

Your job is **only to identify, verify and characterise the candidate literature**. You do not
write the article. Target: about **130 verified candidates** after deduplication, from which the
author will select 50-100.

## 2. Subdomains (search each one)

| # | Subdomain | Example search terms (combine, vary) |
|---|---|---|
| S1 | Network analytics in the 5G core | NWDAF, network data analytics function, MDA management data analytics, 3GPP analytics, 5G core analytics machine learning |
| S2 | Service-based architecture and NF selection | 5G SBA, service communication proxy, SCP, NF discovery and selection, NRF, load balancing 5G core, service mesh 5G core, cloud-native 5G core |
| S3 | Network digital twins (mobile / core) | network digital twin, NDT 5G core, digital twin control plane, what-if analysis network, digital twin network validation, TS 28.561 |
| S4 | Root-cause analysis and anomaly detection | 5G core anomaly detection, root cause analysis 5G, AIOps telecom, microservice root cause localization, fault diagnosis cloud-native network functions |
| S5 | Resilience, geo-redundancy and failover | 5G core resilience, geo-redundancy, NF failure restoration, high availability 5G core, database replication telecom, failover network functions, TS 23.527 |
| S6 | Closed-loop and autonomous networks | zero-touch network and service management, ETSI ZSM, intent-based networking, closed loop automation 5G, autonomous networks, LLM agents network operations, agentic AI telecom |
| S7 | Energy efficiency of the core | energy-aware network function placement, energy efficient 5G core, NF consolidation energy, green 5G core, energy-aware NF selection, Rel-20 energy |
| S8 | AI/ML models for network performance prediction | graph neural network network modeling, RouteNet, GNN digital twin, LSTM transformer 5G traffic prediction, MLP latency prediction, learned network simulator, safe reinforcement learning network control |

## 3. Inclusion and exclusion

- **Years:** 2020-2026, with priority on **2022-2026**. A pre-2020 work is allowed only if it is
  foundational and highly cited; flag it `seminal`.
- **Venue types:**
  1. peer-reviewed **journals**: priority to IEEE, ACM, Elsevier, Springer, Wiley transactions and journals;
  2. top **conferences**: IEEE/IFIP NOMS, CNSM, IM, IEEE INFOCOM, ACM SIGCOMM, IEEE ICC, GLOBECOM, NetSoft, EuCNC/6G Summit;
  3. **standards**: 3GPP TS/TR (give the number and Release), ETSI ZSM/ENI GS, IETF/IRTF NMRG drafts, O-RAN where relevant;
  4. **arXiv preprints** only from 2025-2026, flagged `preprint`.
- **Exclude:** non-English works, theses, blogs, white papers without peer review (vendor white
  papers go in a separate optional list `grey_literature.csv`), duplicates (keep the journal
  version over the conference version and record both).
- **Do not guess journal quartiles.** Record the venue name exactly; quartiles will be checked in
  JCR by the author.

## 4. Verification (mandatory, no exceptions)

- **Never invent a reference.** Every entry must be verified against an authoritative record:
  - a DOI resolved via `https://api.crossref.org/works/<DOI>` (or `https://doi.org/<DOI>`), with
    the title matching; or
  - an arXiv ID via `http://export.arxiv.org/api/query?id_list=<ID>`; or
  - for standards, the official 3GPP/ETSI page or spec number.
- If available, add the citation count from OpenAlex (`https://api.openalex.org/works/doi:<DOI>`)
  or Semantic Scholar, with the date of retrieval.
- If an item cannot be verified, put it in `unverified.csv` with the reason, **never** in the main
  list.
- If network access to these APIs is blocked in this environment, say so at the top of
  `PILOT_REPORT.md` and mark every entry `verification: search-only`.

## 5. Output format

- `results/S<n>_<short_name>.csv`, one per subdomain. Columns, in this order:
  `id, title, authors, year, venue, venue_type(journal|conference|standard|preprint), doi, arxiv, url, citations, citations_date, subdomain, secondary_subdomains, relevance(1-3), summary, method, data_or_testbed, key_result, limitation_or_critique, standards_link, flags(seminal|preprint|survey|...), verification(doi|arxiv|standard|search-only)`
- `summary`, `key_result` and `limitation_or_critique`: **one sentence each, in your own words**.
  No copied abstract text, and no quotation longer than 10 words.
- `relevance`:
  - **3:** directly about the 5G/6G core, with AI/automation or digital twins;
  - **2:** adjacent (RAN, IP networks, or generic cloud with transferable methods);
  - **1:** background.
- `references.bib`: BibTeX for every verified entry, keyed `FirstAuthorYearKeyword`.
- Mark existing **surveys/reviews** with the flag `survey`, and list them first in each file. The
  new article must position itself against them.

## 6. Phases

### Phase 1: check access (a few minutes)

- Test one Crossref, one arXiv and one OpenAlex request.
- Write the outcome at the top of `STATUS.md`. If an API is blocked, continue with
  `verification: search-only` and say so.

### Phase 2: all 8 subdomains in parallel (start immediately, no pilot)

- Launch **8 parallel subagents, one per subdomain** (S1-S8), each following sections 3-5.
- Target 15-20 verified entries per subdomain.
- **Budget safety:** the credit budget is limited and its exhaustion must not lose work.
  - As soon as a subdomain finishes, commit and push its `results/S<n>_*.csv` and BibTeX
    entries, and update `STATUS.md` (which subdomains are done, how many entries).
  - Priority if you must sequence: S3, S1, S5, S8, S6, S4, S2, S7.

### Phase 3: merge (right after Phase 2, no need to wait for the user)

- Deduplicate across subdomains: one row per work, with the other subdomains in
  `secondary_subdomains`.
- Produce `ALL_CANDIDATES.csv` and the merged `references.bib`.
- Produce `SUMMARY.md` containing:
  - counts per subdomain, year and venue type;
  - the list of existing surveys;
  - a draft **taxonomy proposal** of 4-5 categories that covers the candidates;
  - **gaps**: what the standards (3GPP Rel-18-21) require that the literature does not cover;
  - the **most frequent authors and groups** in the relevance-3 works (the research community
    the article must engage with).
- Commit and push.

## 7. General rules

- Do not reproduce copyrighted text; summaries must be short and in your own words.
- Prefer quality over quantity: a smaller verified list beats a long unverified one.
- Keep `DECISIONS.md` updated with every judgement call (borderline inclusions, venue doubts, query changes).
