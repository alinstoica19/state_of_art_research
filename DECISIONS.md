# DECISIONS

Judgement calls made while executing `PROTOCOL.md` (autonomous run, no questions asked).

## Process / infrastructure

- **Git branch.** The protocol says push to `main`; this cloud session is configured to develop and push only on
  `claude/5g-6g-literature-search-2lyo41`, and pushing elsewhere requires separate permission. All commits are
  pushed to that branch; merge it into `main` (or open a PR) when you are happy with the results.
- **No `PILOT_REPORT.md`.** The protocol requires it only if the APIs are blocked. They are not (see `STATUS.md`),
  so every main-list entry is verified individually and none is `search-only`.
- **Metadata is machine-filled.** `tools/verify.py build` fills title, authors, year, venue, DOI/URL and citation
  counts from Crossref / arXiv / 3GPP portal. Subagents write only the identifiers and the analytical fields
  (summary, method, critique ...) into `work/S<n>.jsonl`. This makes typos or invented metadata impossible in the
  main lists; any identifier that fails to resolve or whose title does not match the intended paper goes to
  `results/S<n>_unverified.csv` (merged into `unverified.csv` in Phase 3).
- **arXiv over HTTPS.** `http://export.arxiv.org` redirects (301); `https://export.arxiv.org` is used.
- **OpenAlex search budget exhausted** for the shared IP; literature discovery uses web search + Crossref
  bibliographic search instead. OpenAlex is used only for per-DOI citation counts (still working).
- **Citation counts** are OpenAlex `cited_by_count` (fallback: Semantic Scholar) on the retrieval date given in
  `citations_date`; they differ from Google Scholar and IEEE Xplore counts.
- **BibTeX keys** are `FirstAuthorSurname + Year + Keyword` (ASCII), suffixed a/b/... on collision.
- **Venue type** for a DOI defaults to Crossref's type (journal-article → journal, proceedings-article →
  conference) unless the subagent overrides it.
- **Phase 2 parallelism.** 8 subagents run in parallel; to avoid git conflicts only the orchestrator commits and
  pushes, immediately after each subagent finishes.

## Subdomain-level decisions

(appended by each subdomain run; see the sections below)
