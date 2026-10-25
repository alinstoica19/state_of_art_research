# RUN_LOG_rest

- Start: 2026-10-25 (session time). Branch `claude/lectura-rest-2026-10-25` created from `claude/lectura-pdf-2026-10-25`
  (which already merges lectura-50, run2 and run3).
- Sources, in order: arXiv (ID or title, similarity > 0.9), Unpaywall (email alin.stoica@stud.etti.upb.ro), OpenAlex (OA locations),
  Semantic Scholar openAccessPdf (single attempt, no retry loop). Only URLs these services flag as open access are downloaded;
  PDFs are kept in a scratch directory outside the repository.
- 348 target entries (254 section C, 94 Securitate); 0 had an existing note at start.
