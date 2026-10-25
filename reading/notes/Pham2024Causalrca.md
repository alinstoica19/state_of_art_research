# Root Cause Analysis for Microservice System based on Causal Inference: How Far Are We? (2024)
Cheie: Pham2024Causalrca . DOI/link: https://doi.org/10.1145/3691620.3695065 . Sursa textului: integral: arXiv 2408.13729v2 (versiunea ASE '24)
Sectiunea din plan: C . Tema: anomalii/RCA / inferenta cauzala microservicii
Autori: Luan Pham, Huong Ha, Hongyu Zhang. IEEE/ACM ASE 2024, Sacramento; 13 pagini. Cadrul de evaluare RCAEval este open-source (GitHub, Zenodo).

## Problema (cum o formuleaza autorii)
- Identificarea cauzei unui defect intr-un sistem de microservicii este dificila: zeci pana la sute de servicii, multe metrici per serviciu si propagarea defectelor. Fara unelte automate, poate dura ore (I).
- Metodele RCA bazate pe inferenta cauzala construiesc un graf cauzal din metrici si apoi aplica o metoda de scoring. Evaluarile existente sunt limitate: nu evalueaza constructia grafului, nu includ metode recente (RCD, CIRCA, CausalRCA, RUN) si nu studiaza hiperparametrii sau lungimea datelor (I, 6).

## Ce propun (metoda, pe scurt)
- Studiu empiric al:
  - 9 metode de causal discovery: PC, PCMCI, FCI, Granger, LiNGAM, GES/fGES, NOTEARS-Low-Rank etc.;
  - 21 de metode RCA: variante PC/FCI/Granger/LiNGAM/fGES/NTLR cu PageRank sau random walk, CausalRCA, MicroCause, CIRCA, RCD, NSigma, epsilon-Diagnosis, BARO, CausalAI, RUN;
  - plus o baseline Dummy (alegere aleatoare), pe care autorii spun ca o folosesc primii (4.2).
- Patru intrebari de cercetare (3):
  - RQ1: eficacitatea constructiei grafului;
  - RQ2: eficacitatea localizarii cauzei;
  - RQ3: eficienta (timp de rulare);
  - RQ4: efectul lungimii datelor de intrare.
- Variante cu momentul defectului exact (t_delta = 0) si decalat cu 60 s (t_delta = 60) (4.2).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- **Date sintetice** (3.1.1, Tabelul 1), din generatoarele CIRCA (VAR, continuu), RCD (pyAgrum, discret) si CausIL; grafuri de 10 si 50 de noduri; 200 de cazuri pentru CIRCA si RCD si 10 pentru CausIL.
- **Benchmark-uri de microservicii** (3.1.2, Tabelul 2): Sock Shop, Online Boutique si Train Ticket, pe un cluster Kubernetes de 4 noduri in AWS; monitorizare cu Istio, Prometheus si cAdvisor; 100-200 de utilizatori concurenti generati cu load generator-ele sistemelor.
- Cinci defecte injectate (CPU hog, memory leak, disk IO stress, network delay, packet loss) in cinci servicii per sistem.

| Dataset | metrici | servicii | servicii tinta | tipuri defect | cazuri |
|---|---|---|---|---|---|
| Sock Shop 1 (din [28]) | 38 | 13 | 5 | 2 | 50 |
| Sock Shop 2 | 46 | 15 | 5 | 5 | 125 |
| Online Boutique | 49 | 12 | 5 | 5 | 125 |
| Train Ticket | 212 | 64 | 5 | 5 | 125 |

- Fiecare experiment este repetat de 10 ori. Masini Linux cu 8 CPU si 16 GB RAM; limita de 2 ore per caz (4.3).

## Experimente si metrici
- Graful cauzal: F1, F1-S (pe schelet) si SHD, cu hiperparametri impliciti (Tabelul 3) si tunati prin BIC (Tabelul 4).
- RCA: Avg@5 pe opt seturi de date, pe tipuri de defect (Tabelul 5).
- Timp de rulare (Tabelul 6, Tabelul S1 in materialul suplimentar).
- Performanta in functie de lungimea datelor de intrare (Fig. 4).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- **Causal discovery** (4.1):
  - PC si FCI sunt cele mai bune: PC in 7 din 18 cazuri, FCI in 9;
  - toate metodele estimeaza prost directia muchiilor (F1 sub F1-S);
  - F1 este intre 0,1 si 0,54;
  - performanta scade mult cu marimea grafului;
  - tuning-ul ajuta pe grafuri mici, dar pe CIRCA50 PC si FCI tunate scad cu 23% si 10% fata de setarile implicite.
- **RCA** (4.2, Tabelul 5):
  - CausalRCA, RCD, CIRCA, NSigma si BARO sunt in general cele mai bune;
  - variantele PC/FCI/Granger/LiNGAM/fGES/NTLR cu PageRank sau random walk, CausalAI, RUN si MicroCause sunt apropiate de Dummy;
  - CIRCA si NSigma sunt sensibile la decalarea momentului defectului, mai ales pe Train Ticket; RCD, epsilon-Diagnosis si BARO sunt mai robuste;
  - performanta pe datele sintetice nu reflecta performanta pe sistemele reale.
- **Eficienta** (4.3):
  - de la 10 la 50 de noduri, causal discovery devine de 7 pana la mii de ori mai lent;
  - PC cu testul KCI depaseste in medie o ora per caz pe grafuri de 10 noduri;
  - NSigma si BARO sunt cele mai rapide, urmate de RCD; CausalRCA, MicroCause, RUN si NTLR sunt cele mai lente.
- **Lungimea datelor** (4.4, Fig. 4):
  - pe Online Boutique, Avg@5 pentru RCD (t_delta = 0) creste de la 0,13 la 0,79 cand datele cresc de la 60 la 600 de puncte;
  - pe Sock Shop 1, Avg@5 pentru CausalRCA creste de la 0,62 la 0,93 cand datele cresc de la 120 la 600 de puncte.

## Limitari declarate de autori
- Amenintari la validitate (5.3): hiperparametrii (impliciti din lucrarile originale, cu tuning doar pentru causal discovery); cod reutilizat din lucrarile publicate; sisteme si defecte posibil nereprezentative pentru alte aplicatii; cinci tipuri de defect.
- Directii (5.2): sisteme mari (performanta buna sub 50 de metrici, slaba peste 200), eficienta, sensibilitatea la momentul defectului, seturi de date diverse, generare mai buna de date sintetice, tuning sistematic, pipeline end-to-end detectie + RCA.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - benchmark-uri de microservicii web (Sock Shop, Online Boutique, Train Ticket) (3.1.2).
- UE reale sau emulate?: nu se aplica - utilizatori web emulati de load generator-ele benchmark-urilor (100-200 concurenti) (3.1.2).
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu.
- executa actiuni automat (bucla inchisa)?: nu - RCA offline.
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu - metricile sunt de RCA (Avg@5) si de graf (F1, SHD).
- observa traficul la SCP / proxy?: partial - metricile de nivel serviciu sunt colectate prin service mesh-ul Istio (proxy-uri side-car); nu este SCP 3GPP (3.1.2).
