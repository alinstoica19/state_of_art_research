# Real-Time Monitoring of 5G Networks: An NWDAF and ML Based KPI Prediction (2024)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Bayleyegn2024Kpiprediction . DOI/link: https://doi.org/10.1109/netsoft60951.2024.10588931 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Rezumatul spune ca, pe masura ce retelele trec la medii virtualizate, monitorizarea si analiza devin provocari; pentru monitorizare eficienta si aplicarea SLA-urilor, retelele virtualizate trebuie sa fie observabile pentru furnizori si operatori.

## Ce propun (metoda, pe scurt)
O solutie de monitorizare in timp real pentru 5G Service-Based Architecture (SBA), bazata pe un NWDAF dezvoltat de autori, cu acces prin interfata standardizata. NWDAF este extins cu modele ML care prezic KPI-uri legate de traficul de retea. Metricile din 5G core sunt trimise intr-o baza de date Prometheus, iar Grafana este folosit pentru vizualizare.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Tip de testbed (real, emulat sau simulat): nedeclarat in rezumat.
Unelte: NWDAF dezvoltat de autori, modele ML (tipul nedeclarat), Prometheus, Grafana.
Scara: nedeclarata in rezumat.
Date: metrici colectate din 5G core (tipul si volumul nedeclarate).

## Experimente si metrici
Rezumatul mentioneaza "development and evaluation" si demonstrarea monitorizarii in timp real, dar nu descrie experimentele sau metricile de evaluare.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Nu sunt raportate cifre in rezumat. Rezumatul afirma doar ca solutia "allows and demonstrates" monitorizarea in timp real. Fara trimitere la tabel/figura.

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nedeclarat - (rezumat): se mentioneaza metrici colectate din 5G core, fara detalii despre implementare.
- UE reale sau emulate? nedeclarat - (rezumat)
- digital twin al retelei? nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica? nedeclarat - (rezumat): predictia vizeaza KPI-uri de trafic; nu se mentioneaza actiuni.
- executa actiuni automat (bucla inchisa)? nedeclarat - (rezumat)
- multi-site / geo-redundanta / failover de baza de date? nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nedeclarat - (rezumat)
- observa traficul la SCP / proxy? nedeclarat - (rezumat)
