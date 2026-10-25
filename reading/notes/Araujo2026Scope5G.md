# SCOPE-5G: A Standards-Aligned Synthetic AMF Observability Dataset for Reproducible 5G Core Benchmarking (2026)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Araujo2026Scope5G . DOI/link: https://doi.org/10.1109/access.2026.3727225 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: B

## Problema (cum o formuleaza autorii)
Observabilitatea planului de control al core-ului 5G este esentiala pentru benchmarking, detectia anomaliilor si validarea metodelor de management al retelei. Autorii spun ca datasetele publice pentru analiza AMF sunt limitate si ca putine dintre ele folosesc semantica masuratorilor 3GPP.

## Ce propun (metoda, pe scurt)
SCOPE-5G, un framework configurabil pentru date sintetice de observabilitate AMF aliniate la standarde, si datasetul derivat SCOPE-5G Dataset. Autorii precizeaza ca datasetul nu poate inlocui telemetria reala a operatorilor de mobile. Framework-ul combina: semantica procedurilor centrate pe AMF, alinierea la nivel de coloana cu TS 28.552, dezagregarea resurselor pe mai multe slice-uri si anomalii etichetate cu debut gradual. Comportamentul procedurilor este modelat prin: tipare zilnice (diurnal), diferentiere zi lucratoare/weekend, dependenta pe termen lung, clustering al volatilitatii, coada M/M/1 pentru fiecare mesaj si injectarea de anomalii sigmoid.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Date sintetice generate de framework. Dataset: 60 de zile, granularitate de 15 minute, 21 de proceduri AMF pe trei slice-uri de retea, 112 coloane, 5.760 de randuri, dintre care 162 randuri etichetate cu anomalii, in opt tipuri de anomalii. Validare fata de opt referinte publice; datele Telecom Italia Call Detail Record (CDR) sunt folosite ca referinta. Rezumatul nu mentioneaza un testbed. Scripturile de evaluare sunt publicate.

## Experimente si metrici
Validare statistica fata de opt referinte publice. Metrici mentionate: corelatia Pearson, scor TV-complement, MAPE (pentru randurile la care se aplica) cu un prag de acceptare de 30%, si AUC pentru detectia de defecte, comparand anomaliile cu debut gradual cu cele cu debut in treapta (step).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Pearson r = 0.979 fata de datele Telecom Italia CDR.
- Scor TV-complement de 97.27%.
- Toate randurile validate cu MAPE aplicabil sunt sub pragul de 30%; trei dintre ele sunt in intervalul 15–30%.
- Inlocuirea anomaliilor cu debut sigmoid cu anomalii treapta (step) ridica AUC de la 0.919 la 0.998.
Trimitere la tabel/figura: nedeclarat in rezumat.

## Limitari declarate de autori
Datasetul nu poate inlocui telemetria reala de la operatorii de mobile (rezumatul spune ca "supports reproducible benchmarking and controlled experiments", nu ca il inlocuieste).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu - (rezumat): datele AMF sunt sintetice si generate de un model ("SCOPE-5G models procedure-level behavior...").
- UE reale sau emulate? nedeclarat - (rezumat): datele sunt sintetice; rezumatul nu descrie UE-uri.
- digital twin al retelei? nedeclarat - (rezumat): nu se mentioneaza ca un digital twin; datele sunt un model sintetic.
- prezice efectul unei actiuni inainte de a o aplica? nedeclarat - (rezumat): nu se mentioneaza.
- executa actiuni automat (bucla inchisa)? nedeclarat - (rezumat): nu se mentioneaza.
- multi-site / geo-redundanta / failover de baza de date? nedeclarat - (rezumat): nu se mentioneaza.
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat - (rezumat): nu se mentioneaza.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nedeclarat - (rezumat): datele sunt la granularitate de 15 minute pe proceduri AMF si slice-uri; rezumatul nu spune daca exista inregistrari la nivel de sesiune.
- observa traficul la SCP / proxy? nedeclarat - (rezumat): nu se mentioneaza.
