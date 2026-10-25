# Towards zero downtime: Using machine learning to predict network failure in 5G and beyond (2023)
Cheie: Basikolo2023Zerodowntime . DOI/link: 10.52953/pyaf8065 . Sursa textului: integral, versiunea publicata (ITU Journal on Future and Evolving Technologies, Vol. 4, Issue 3, Sept. 2023, pp. 435-443): https://www.itu.int/dms_pub/itu-s/opb/jnl/S-JNL-VOL4.ISSUE3-2023-A31-PDF-E.pdf
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Detectarea si depanarea defectelor de retea se face de obicei reactiv (monitorizare reactiva, depanare manuala), ceea ce produce downtime si pierderi financiare (Sec. 1). Autorii urmaresc predictia unui eveniment de esec de retea intr-un core 5G inainte sa apara, astfel incat operatorii sa poata preveni downtime-ul. Intrebarea studiata: cat de devreme si cat de precis pot fi prezise esecurile viitoare din metrici (Sec. 3.1). Sec. 2 trece in revista cazuri de intreruperi (KDDI, Rogers, O2, Vodafone Idea) si lucrari ML de predictie a esecurilor, notand ca datasetele din acele lucrari provin fie doar din datacenter, fie doar de la statii de baza (Sec. 2.3).

## Ce propun (metoda, pe scurt)
- Se antreneaza modele de regresie supervizata pe serii de timp multivariate de la un core 5G cloud-native (CNF); iesirea continua este transformata in decizie binara (esec / normal) printr-un prag (Sec. 5.2).
- Tinta de predictie: numarul de esecuri de inregistrare UE (amf.amf.app.five-g.RM.RegInitFail) la 600 s (Sec. 4.1.1).
- "Proposed-SVR": un SVR modificat fata de cel clasic prin kernel sigmoid in locul RBF si prin schimbarea reciprocei parametrului de regularizare C de la 1 la 0.09 (Sec. 2.4, Sec. 4.2).
- Pasi de preprocesare: balansare cu SMOTE (450 puncte normale vs 150 anormale in setul de antrenare), standardizarea features, selectie de features dupa importanta calculata cu un clasificator XGBoost (Sec. 4.2).
- Doua task-uri: Task 1 foloseste toate metricile pentru a gasi cel mai mic timp de detectie t cu F1 > 0.9; Task 2 foloseste un subset de metrici pentru modele mai mici si mai rapide (Sec. 4.1).
- Modele comparate: random forest, gradient boosting regressor, SVR conventional, Bayesian ridge, CatBoost, XGBR (Sec. 2.4, rezumat); in figuri apar si ele comparate pentru t = 5, 10, 30 s.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Datele provin dintr-un testbed comercial furnizat de KDDI Research (problema ML5G-PS-005 din ITU AI/ML in 5G Challenge, ref. [37]); autorii folosesc datasetul furnizat, nu declara ca l-au generat ei (Sec. 3.1).
- Tinta: core 5G CNF rulat peste Kubernetes cu eBPF pentru observabilitate (Sec. 3.1). Trei tipuri de metrici: cAdvisor (basic), eBPF (fine-grained), metrici 5G obtinute prin numararea logurilor 5G.
- Injector de defecte: pierdere de pachete pe core 5G, cu rata crescand liniar; UE se inregistreaza si deregistreaza continuu. Eticheta anormala: br-cp_bridge-loss-congestion-with-time-start.
- Un ciclu de test: 90 s faza de pregatire (initializare retea 5G) + 600 s faza de inregistrare/deregistrare UE (Fig. 2).
- Date: 600 cicluri de test pentru antrenare, 300 pentru test (cu etichete si serii de timp). Numar total de features in Task 1: 3,325 (Sec. 6.1). Numarul de UE, de NF sau de noduri: nedeclarat.
- Tip UE (reale/emulate): nedeclarat.

## Experimente si metrici
- Task 1: toate cele 3,325 features, detectie la t = 5-30 s; metrici F1-score, accuracy, precision (Fig. 5, 6, 7).
- Detectie la t = 10 s: comparatie intre modele (Fig. 7).
- Fig. 8: F1 si accuracy ale proposed-SVR in functie de timpul de detectie.
- Task 2: reducerea numarului de features; relatia dintre numarul de features, timpul de detectie si F1 (Tabel 1, Fig. 9).
- Tabel 2: dimensiunea modelului, timpul de antrenare (600 esantioane) si de predictie (300 esantioane) in functie de numarul de features.
- Fig. 10: comparatie a timpului de detectie cu alte echipe din provocarea ITU 2022 (AutoML, LSTM), pentru F1 > 0.9.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Proposed-SVR obtine F1 > 0.9 la timp de detectie de 10 s (Sec. 6.1, Fig. 5); rezumatul spune ca prezice in 10 s daca un esec va aparea in urmatoarele 10 minute.
- La t = 10 s, accuracy proposed-SVR = 0.84, SVR traditional = 0.77, Bayesian ridge = 0.75 (Fig. 7, Sec. 6.1).
- Tabel 1 (proposed-SVR, Task 2; coloane: nr. features, timp [s], F1, prag): All, 10, 0.901, 0.40; 527, 20, 0.911, 0.57; 400, 35, 0.906, 0.55; 300, 36, 0.917, 0.62; 200, 36, 0.908, 1.11; 120, 40, 0.902, 1.30; 100, 52, 0.914, 1.14; 50, 61, 0.901, 1.74.
- Tabel 2 (nr. features, MB, antrenare s, predictie s): all 20.89 / 2.00 / 0.65; 527 3.31 / 0.32 / 0.10; 100 0.63 / 0.10 / 0.03; 64 0.39 / 0.08 / 0.03; 50 0.30 / 0.08 / 0.02; 1 0.01 / 0.03 / 0.01.
- Fig. 10: proposed-SVR 10 s (100 s incluzand faza de pregatire), fata de 30 s si 50 s raportate de alte echipe cu AutoML si LSTM pentru F1 similar (Sec. 6.2).
- Concluzie (Sec. 7): F1 > 0.9 si cu 527 features la t = 20 s.

## Limitari declarate de autori
Nu exista o sectiune de limitari. Textul nu enumera limitari explicite. Se noteaza ca numarul de features trebuie ales atent deoarece afecteaza generalizarea (Sec. 6.2).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? da, dar generat de terti - dataset de la un core 5G CNF pe Kubernetes cu eBPF (Sec. 3.1); autorii nu descriu o implementare proprie.
- UE reale sau emulate? nedeclarat - se mentioneaza inregistrare/deregistrare continua de UE, fara a preciza natura lor (Sec. 3.1).
- digital twin al retelei? nu - nu este mentionat (Sec. 3-6).
- prezice efectul unei actiuni inainte de a o aplica? nu - prezice aparitia unui esec indus de injector de defecte, nu efectul unei actiuni de management (Sec. 4.1).
- executa actiuni automat (bucla inchisa)? nu - doar predictie, fara actiuni (Sec. 4-7).
- multi-site / geo-redundanta / failover de baza de date? nedeclarat - nu apare in text.
- evaluare prospectiva (predictie fixata inainte de experiment)? nu - evaluare retrospectiva pe set de test de 300 cicluri din datasetul furnizat (Sec. 3.1, 6).
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? da, partial - tinta este numarul de esecuri de inregistrare UE (RegInitFail), un contor agregat (Sec. 4.1.1); F1/accuracy se calculeaza pe clasificarea esec/normal per ciclu.
- observa traficul la SCP / proxy? nu - metrici cAdvisor, eBPF si numarari de loguri 5G; SCP nu este mentionat (Sec. 3.1).
