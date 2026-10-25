# LOCOMOTIVE 5G Core for 6G ready Resilient and Highly Available Network Slices and SFCs (2022)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Sarkar2022Locomotive . DOI/link: https://doi.org/10.23919/cnsm55787.2022.9964553 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Load Balancer (LB) are un rol important pentru High Availability (HA) si rezilienta 5GC scalabil; un LB ineficient intr-un NF poate duce la intreruperea totala a serviciului HA (rezumat).

## Ce propun (metoda, pe scurt)
- LOCOMOTIVE 5GC, care depaseste hot standby-ul tradițional in HA si rezilienta in conditii dinamice (rezumat).
- Framework dezvoltat in integralitate intr-un test-bed 5G conform 3GPP, cu XDP si eBPF (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Test-bed 5G conform 3GPP (rezumat); detalii despre scara si date nedeclarate.
- Unelte: XDP, eBPF (rezumat).
- Configuratie active-active in cluster (rezumat).

## Experimente si metrici
- Comparatie cu hot standby in plan de control, in conditii de supraincarcare neasteptata (fara defectarea LB) si in timpul defectarilor LB (rezumat).
- Disponibilitate in configuratie active-active (rezumat).
- Metrici: numarul de cereri de utilizator servite sau pierdute (rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Serveste cu 16% (cel putin) mai multe cereri de utilizator decat hot standby in plan de control, in supraincarcare neasteptata (fara defectarea LB) (rezumat).
- In timpul defectarilor LB, pierde cu 22% mai putine cereri de utilizator decat hot standby (rezumat).
- Disponibilitate cu 4% mai buna decat hot standby, in configuratie active-active (rezumat).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? da - framework dezvoltat in integralitate intr-un test-bed 5G conform 3GPP (rezumat).
- UE reale sau emulate? nedeclarat (rezumat).
- digital twin al retelei? nu - nu este mentionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica? nedeclarat (rezumat).
- executa actiuni automat (bucla inchisa)? nedeclarat (rezumat).
- multi-site / geo-redundanta / failover de baza de date? nedeclarat - configuratie active-active in cluster; geo-redundanta nementionata (rezumat).
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat (rezumat).
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? da - cereri de utilizator servite sau pierdute in plan de control (rezumat).
- observa traficul la SCP / proxy? nedeclarat - se mentioneaza load balancer-ul (LB), fara a preciza daca este SCP sau proxy (rezumat).
