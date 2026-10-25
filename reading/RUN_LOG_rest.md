# RUN_LOG_rest

- Start: 2026-10-25 (session time). Branch `claude/lectura-rest-2026-10-25` created from `claude/lectura-pdf-2026-10-25`
  (which already merges lectura-50, run2 and run3).
- Sources, in order: arXiv (ID or title, similarity > 0.9), Unpaywall (email alin.stoica@stud.etti.upb.ro), OpenAlex (OA locations),
  Semantic Scholar openAccessPdf (single attempt, no retry loop). Only URLs these services flag as open access are downloaded;
  PDFs are kept in a scratch directory outside the repository.
- 348 target entries (254 section C, 94 Securitate); 0 had an existing note at start.

## Oprire la cererea utilizatorului (2026-10-25)
- Rularea a fost oprita de utilizator dupa 81 din 348 de intrari incercate (toate din sectiunea C; sectiunea SEC nu a fost inceputa).
- Contoare: [x] text integral 50, [a] doar rezumat 29, [p] doar titlu 2.
- Urmatoarea intrare de incercat: linia 82 din lista tinta, `Albuquerque2026Powerprediction` (apoi Correia2025Corepower, DeAraujo2025Aicarbon, Sahraoui2024Vnffg, BenSalah2024Coreconsolidation...). Aceste cinci au fost descarcate sau cautate, dar nu au fost inca inregistrate, deci trebuie reluate.
- Probleme intalnite:
  - bot check Cloudflare la ACM DL si Wiley; HTTP 403 la ScienceDirect, chiar si pentru lucrari open access;
  - Semantic Scholar raspunde frecvent cu 429 (nu s-a reincercat in bucla);
  - HAL si mediaTUM au fost intermitent indisponibile (anti-bot sau timeout). La reincercare au mers, iar 4 note scrise initial din rezumat au fost rescrise din textul integral: Raza2025Ndtsurvey, Goshi2023Pp5Gs, Goshi2021Internf, plus Li2022Petrinet citit la a doua incercare;
  - unele texte integrale legale au fost gasite pe site-urile autorilor sau institutiilor, prin cautare web: ECHO (Microsoft Research), De Sousa 2022 (INTRIG Unicamp).
- Niciun PDF nu a fost adaugat in repository; PDF-urile au ramas in directorul de lucru temporar.
