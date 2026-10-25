# RUN_LOG

- Start: Sun Oct 25 08:10:08 UTC 2026
- End: Sun Oct 25 08:26:03 UTC 2026
- Attempted: 144 (all papers of the target list; limit 150 not reached). [x] full text read: 24. [a] abstract only: 120. Target of 50 [x] NOT reached.
- Reason: for 120 papers no legally accessible full text was found (Unpaywall: none or paywalled; no arXiv copy by exact/fuzzy title search; Semantic Scholar API rate-limited, 429, only partial coverage).
- Access problems (no bypass attempted): bot-check/403/418 on HAL (Anubis), TechRxiv, MDPI, Hindawi/DOAJ, ACM, Napier, Aalto, Zenodo, IEEE Xplore (Access papers). See NEEDS_PDF.md.
- 24 abstracts could not be retrieved (OpenAlex/Crossref/arXiv); those notes contain only the title and "nedeclarat".
- Method: texts downloaded to scratch (not stored in repo); notes drafted by subagents from the texts/abstracts. Tran2025Ndt6Gsurvey and Coronado2022Zerotouch (very long surveys) were read via headings, intro and relevant sections.
- Commits: single commit at the end (not every 10 papers).

## Run 2
- Start: Sun Oct 25 11:53:52 UTC 2026
- End: Sun Oct 25 12:00:58 UTC 2026
- Attempted: 106/106 (81 B, 22 STD, 3 D). Branch: claude/lectura-run2-2026-10-25.
- Section B: [x] 10, [a] 62, [p] 9 (nu s-a putut obtine nici rezumatul).
- Section STD: [x] 4 (IRTF NMRG NDT draft-13, RFC 9315, ITU-T Y.3090, ITU-T Y.3172), [a] 0, [p] 18 (3GPP/ETSI inaccesibile; note minimale "TEXT NEACCESIBIL").
- Section D: [x] 1 (LopezPerez2022Ranenergy; citit integral doar rezumat, introducere, Sec. II, IX-X, restul doar structura), [a] 2.
- Problems: www.3gpp.org/ftp, etsi.org/deliver, docbox.etsi.org si 3gpp DynaReport returneaza 403 Cloudflare (nu am ocolit); portal.3gpp.org da doar metadate. IEEE Xplore 418/bot-check (si pentru BD-137, open access); ACM 403 (BD-52); ScienceDirect redirect/403; Semantic Scholar 429 pe tot parcursul; arXiv fara potriviri pentru majoritatea; conexiune resetata de proxy pentru BD-308 (sol.sbc.org.br, OA) si Mihai2022 (copii deschise blocate). reading/pdf_inbox nu exista. BD-169: cifrele din Table I nu au putut fi extrase din PDF.
- Commits: intermediare dupa terminarea fiecarui grup de agenti (nu strict la 10 intrari) si commit final.
