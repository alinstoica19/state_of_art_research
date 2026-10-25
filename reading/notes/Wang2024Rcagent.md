# RCAgent: Cloud Root Cause Analysis by Autonomous Agents with Tool-Augmented Large Language Models (2024)
Cheie: Wang2024Rcagent . DOI/link: https://doi.org/10.1145/3627673.3680016 . Sursa textului: integral: arXiv 2310.16340v3 (2 august 2024; versiunea CIKM '24)
Sectiunea din plan: C . Tema: anomalii/RCA / agenti LLM
Autori: Zefan Wang, Zichuan Liu, Yingying Zhang, Aoxiao Zhong, Jihong Wang, Fengbin Yin, Lunting Fan, Lingfei Wu, Qingsong Wen (Alibaba Group si universitati partenere). CIKM 2024, Boise; 9 pagini.

## Problema (cum o formuleaza autorii)
- Metodele LLM existente pentru RCA in cloud depind de workflow-uri configurate manual (fine-tuning, RAG few-shot: RCACopilot, PACE-LM, Xpert). Se bazeaza pe modele GPT externe, ceea ce ridica probleme de confidentialitate a datelor, si nu folosesc capacitatile autonome ale LLM-urilor (1).
- Trei provocari pentru agentii LLM in RCA cloud (2):
  - confidentialitate: modelul trebuie gazduit intern, deci este mai slab;
  - lungimea contextului: loguri, cod si rezultate de interogari sunt foarte mari;
  - validitatea actiunilor: modelele mai slab aliniate genereaza actiuni invalide.

## Ce propun (metoda, pe scurt)
- **RCAgent**, agent autonom de tip ReAct (gand-actiune-observatie), cu un controller agent, rulat pe un model local (3, Fig. 1):
  - **OBSK (Observation Snapshot Key):** controller-ul vede doar inceputul observatiei si o cheie hash; observatia completa este intr-un key-value store si poate fi interogata (3.1);
  - **unelte de colectare** semantic minimaliste, care primesc doar ID-uri de entitati, nu SQL sau API-uri de log; deduplicare si excluderea mesajelor sub nivelul WARNING (3.2.1);
  - **unelte analitice ("expert agents")** (3.2.2):
    - analiza de cod, recursiva: citeste clasa si recomanda alte clase de analizat;
    - analiza de log: linii -> graf de similaritate ponderat cu distanta in document -> clustering Louvain -> RAG pe fiecare chunk; analizele ale caror dovezi nu se potrivesc cu textul logului sunt eliminate (Algoritmul 1);
  - **stabilizare** (3.3): JSON repairing ("JsonRegen") si mesaje de eroare pentru actiuni problematice (apeluri duplicate, intrari triviale, finalizare prematura);
  - **Self-Consistency** (3.4): vot pe embedding-uri sau agregare cu LLM; Trajectory-level SC (TSC), care esantioneaza doar dupa pasii preliminari greedy.
- Iesiri: cauza, solutia, dovezile si responsabilitatea (platforma vs. utilizator).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Real-time Compute Platform for Apache Flink, Alibaba Cloud (pana la 100 de milioane de inregistrari pe secunda la varf) (4).
- Model: Vicuna-13B-V1.5-16K cu vLLM pe un A100 80 GB; embedding GTE-LARGE; decodare greedy implicit; 10 esantioane pentru SC (4.1).
- **Dataset offline** (4.2):
  - 15.616 joburi anormale dintr-o luna (esec nerecuperabil sau pornire esuata in 6 minute);
  - filtrate la aproximativ 5.000 de joburi netriviale;
  - etichetate cu baza de reguli Flink Advisor (cunostintele SRE);
  - reduse la 161 de joburi, cu cel mult doua joburi per cauza identica.
- Metrici semantice: METEOR, NUBIA, BLEURT, BARTScore, EmbScore. Metrici LLM: GPT-4 (gpt-4-0613) ca evaluator, G-Correctness si G-Helpfulness pe scala 0-10.
- **Evaluare online:** joburi out-of-distribution (in afara regulilor existente) din primele doua saptamani de deployment, etichetate de SRE, cu scor uman H-Helpfulness 0-5 (6).

## Experimente si metrici
- Predictia cauzei (Tabelul 1), a solutiei (Tabelul 2) si a dovezilor (Tabelul 3); ablatie: fara expert agents, fara JsonRegen, fara OBSK.
- Statistici de traiectorie: Pass Rate in 15 pasi, lungime, Invalid Rate (Tabelul 4).
- SC la diferite scari (Fig. 4); evaluare online pe OoD (Tabelul 5); performanta si resurse in functie de volumul de date (Fig. 5).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- **Tabelul 1** (cauza, METEOR / BLEURT): ReAct 6,44 / 25,17; RCAgent 15,15 / 31,57; fara expert agents 9,60 / 27,77; cu TSC (LLM) 16,49 ± 0,09 / 34,43 ± 0,59.
- Fata de ReAct, RCAgent castiga +8,71 METEOR la cauza si +6,52 la solutie. TSC adauga +3,51 METEOR, +4,50 BLEURT si +2,28% G-Helpfulness la solutie (5.1).
- **Tabelul 4:**

| Varianta | Pass Rate | Lungime traiectorie | Invalid Rate |
|---|---|---|---|
| ReAct | 86,33 | 7,48 | 22,82 |
| RCAgent | 99,38 | 6,78 | 7,93 |
| fara JsonRegen | 85,71 | 7,91 | 18,75 |
| cu sampling | 70,19 | 10,66 | 44,80 |
| cu unelte SQL | 65,84 | 10,55 | 70,94 |

- **Tabelul 5** (joburi OoD online):
  - precizia responsabilitatii: XGBoost 77,65, T5 fine-tuned 77,85, LLM Summary 77,21, ReAct 73,53, RCAgent 80,74, RCAgent + TSC 82,06 ± 0,42;
  - H-Helpfulness: ReAct 1,36, RCAgent 2,47, RCAgent + TSC 2,92 (Tukey HSD p = 0,001 fata de ReAct).

## Limitari declarate de autori
- Scorul uman de 2,92 este interpretat de autori ca "moderate support" pentru RCA (6).
- Modelul local este mai slab decat modelele externe, compromis acceptat pentru confidentialitate (2).
- Etichetele offline provin din regulile Flink Advisor, rezumate de LLM (4.2).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - platforma Flink din Alibaba Cloud (4).
- UE reale sau emulate?: nu se aplica - joburi reale de productie (4.2).
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu.
- executa actiuni automat (bucla inchisa)?: nu - agentul colecteaza si analizeaza date autonom, dar rezultatele (cauza, solutie, responsabilitate) sunt predate echipei SRE (6).
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: partial - evaluarea pe joburi OoD din primele doua saptamani de deployment, etichetate ulterior de SRE (6).
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu - metrici semantice, LLM si umane de utilitate.
- observa traficul la SCP / proxy?: nu.
