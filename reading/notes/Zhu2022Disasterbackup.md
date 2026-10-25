# Failure-Aware and Automated Disaster Backup in the 5G Core Network (2022)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Zhu2022Disasterbackup . DOI/link: https://doi.org/10.1109/ceccc56460.2022.10069046 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Pentru a atinge tinta de fiabilitate specificata de operator, operatorii cheltuiesc mai mult pentru redundanta 5G core; echilibrul intre cost si fiabilitate este dificil, iar o retea fara redundanta suficienta poate sa nu atinga fiabilitate ridicata (rezumat).

## Ce propun (metoda, pe scurt)
- Metoda inspirata din evolutia 5G-advanced si 6G, in care Network Data Analytics Function (NWDAF) asigura control si programare inteligente pe baza analizei datelor (rezumat).
- Home Subscriber Server (HSS) devine backup pentru Unified Data Management (UDM), prin transfer automat in timp real atunci cand NWDAF detecteaza ca toate UDM-urile esueaza (rezumat).
- Mecanismul si procedurile de backup automat de dezastru si de recuperare sunt descrise in detaliu (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Nedeclarat in rezumat.

## Experimente si metrici
- Analiza prin Fault Tree Analysis (FTA) si teoria probabilitatilor (rezumat).
- Evaluare calitativa si cantitativa (rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Nedeclarat in rezumat (nu sunt raportate cifre).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nedeclarat - rezumatul descrie o metoda si mecanisme, fara a preciza implementarea nucleului (rezumat).
- UE reale sau emulate? nedeclarat (rezumat).
- digital twin al retelei? nu - nu este mentionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica? nedeclarat - rezumatul spune ca eficienta este analizata prin FTA si teoria probabilitatilor, fara a descrie o predictie a unei actiuni (rezumat).
- executa actiuni automat (bucla inchisa)? da - transfer automat in timp real al backup-ului cand NWDAF detecteaza esecul (rezumat).
- multi-site / geo-redundanta / failover de baza de date? da - failover de baza de date: HSS ca backup pentru UDM (rezumat); locatiile si geo-redundanta nedeclarate.
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat (rezumat).
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nedeclarat (rezumat).
- observa traficul la SCP / proxy? nedeclarat (rezumat).
