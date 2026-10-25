# Eadro: An End-to-End Troubleshooting Framework for Microservices on Multi-source Data (2023)
Cheie: Lee2023Eadro . DOI/link: https://doi.org/10.1109/icse48619.2023.00150 . Sursa textului: integral: arXiv 2302.05092v1 (10 februarie 2023)
Sectiunea din plan: C . Tema: anomalii/RCA / microservicii multi-sursa
Autori: Cheryl Lee, Tianyi Yang, Zhuangbin Chen, Yuxin Su, Michael R. Lyu (The Chinese University of Hong Kong; Sun Yat-sen University). ICSE 2023. Datele si codul sunt publicate.

## Problema (cum o formuleaza autorii)
Doua limitari ale abordarilor existente pentru troubleshooting-ul microserviciilor (I):
- **Folosirea insuficienta a datelor de monitorizare:** majoritatea metodelor folosesc doar trace-uri, care nu reflecta toate anomaliile. De exemplu, epuizarea CPU apare in KPI si loguri, dar nu neaparat ca latenta in trace-uri.
- **Separarea fazelor:** detectia anomaliilor si localizarea cauzei sunt tratate independent, desi au intrari si cunostinte comune. Localizatoarele folosesc detectoare simplificate (de exemplu N-sigma), iar etichetele zgomotoase ale acestora degradeaza localizarea.

## Ce propun (metoda, pe scurt)
- **Eadro**, cadru end-to-end care integreaza detectia anomaliilor si localizarea cauzei pe date multi-sursa (IV):
  1. **Invatare per modalitate:**
     - loguri: parsate in evenimente, modelate cu proces Hawkes si un strat FC;
     - KPI: dilated causal convolution (DCC);
     - trace-uri: DCC pe seriile de latenta;
  2. **Invatarea starii tinand cont de dependente:** fuziune cu gated concatenation, apoi GAT pe un graf de dependente construit din invocarile istorice;
  3. **Detectie si localizare comune:** multi-task learning, cu reprezentari si obiectiv partajate; da probabilitatea unei anomalii si probabilitatea ca fiecare microserviciu sa fie vinovatul.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Doua benchmark-uri desfasurate intr-un testbed distribuit, in containere Docker (V.A):
  - TrainTicket (TT): 41 de microservicii, 27 legate de business;
  - SocialNetwork (SN): 21 de microservicii, 14 legate de business, comunicare prin Thrift RPC.
- Colectare: trace-uri cu Jaeger; KPI per secunda (CPU, memorie, rx/tx bytes) cu cAdvisor, Prometheus si InfluxDB; loguri cu Elasticsearch, Fluentd si Kibana.
- Defecte injectate cu Chaosblade: CPU exhaustion, network delay, packet loss.
- Cereri: 0,2-0,5 pe secunda pentru TT si 2-3 pe secunda pentru SN. Date normale: 7 ore (TT) si 1,2 ore (SN). Durata defectelor: 10 minute (TT) si 2 minute (SN). 162 de injectari pe TT si 72 pe SN.
- Datele rezultate: 48.296 de trace-uri (TT) si 126.384 (SN); impartire 60% antrenare / 40% test.
- Implementare: GTX 1080, Python 3.7; Adam, lr 0,001, batch 256, 50 de epoci (V.C).

## Experimente si metrici
- Detectie: F1, recall, precizie (Tabelul II).
- Localizare: HR@1/3/5 si NDCG@3/5 (Tabelul III).
- Baseline-uri:
  - detectie: TraceAnomaly, MultimodalTrace;
  - localizare: TBAC, NetMedic, MonitorRank, CloudRanger, DyCause;
  - metode multi-sursa derivate de autori: MS-RF, MS-SVM, MS-LSTM, MS-DCC (V.B).
- Ablatie: fara loguri (L), fara KPI (M), fara trace-uri (T), fara GAT (G); vizualizare t-SNE (Fig. 7).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- **Tabelul II** (F1): TraceAnomaly 0,486 (TT) / 0,539 (SN); MultimodalTrace 0,608 / 0,676; MS-LSTM 0,967 / 0,948; Eadro 0,989 / 0,986.
- **Tabelul III** (HR@1): DyCause 0,231 (TT) / 0,273 (SN); MS-DCC 0,767 / 0,789; Eadro 0,990 / 0,974. NDCG@5 pentru Eadro: 0,994 (TT) / 0,983 (SN).
- Din introducere: F1 cu 53,82%-92,68% mai mare decat abordarile comparate; HR@1 cu 290%-5068% mai mare decat cele cinci baseline-uri; in medie +43,06% HR@1 fata de metodele derivate.
- Ablatie: logurile contribuie cel mai putin (Eadro fara L este a doua cea mai buna varianta); fara KPI sau fara trace-uri performanta scade mult, mai ales la HR@1; fara GAT, HR@1 scade cu 23,21% (VI).

## Limitari declarate de autori
- Nu trateaza bug-uri de logica a programului si nici probleme "silentioase" care nu produc tipare anormale in date (VI.A).
- Necesita colectarea tuturor celor trei tipuri de date pentru a functiona cel mai bine (VI.A).
- Este supervizat si cere multe date etichetate. Autorii sugereaza pseudo-etichete nesupervizate revizuite de ingineri (VI.A).
- Evaluare pe doua seturi de date simulate (benchmark-uri cu defecte injectate), pentru ca nu exista seturi publice multi-modale. Baseline-urile fara cod public au fost reimplementate (VI.B).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - benchmark-uri de microservicii (TrainTicket, SocialNetwork) (V.A).
- UE reale sau emulate?: nu se aplica - cereri de utilizator generate de simulatoare de cereri (V.A).
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu.
- executa actiuni automat (bucla inchisa)?: nu - detectie si localizare, fara mitigare.
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu - impartire 60/40 pe date colectate cu defecte injectate.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu - metrici de detectie si localizare.
- observa traficul la SCP / proxy?: nu - trace-urile sunt colectate prin instrumentare Jaeger, fara proxy.
