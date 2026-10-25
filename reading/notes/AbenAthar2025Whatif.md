# Network Digital Twin for Route Optimization in 5G/B5G Transport Slicing with What-If Analysis (2025)
Cheie: AbenAthar2025Whatif . DOI/link: https://doi.org/10.1109/iccworkshops67674.2025.11162404 . Sursa textului: integral: arXiv v1 (2505.04879v1)
Sectiunea din plan: C . Tema: nedeclarata

## Problema (cum o formuleaza autorii)
Reteaua de transport (RAN-core) din 5G/B5G ruteaza de regula dupa politici predefinite bazate pe cost (OSPF), fara a lua in calcul eterogenitatea traficului sau congestia. Modificari ale retelei (linkuri, politici de rutare, slice-uri noi) sunt riscante deoarece decizii ineficiente pot produce congestie, pierderi si latenta. Autorii identifica o lipsa in literatura privind buclele inchise care folosesc contrapartea virtuala pentru a testa implementari noi si pentru a evalua fiabilitatea modelului in predictia performantei. Intrebari de cercetare: cat de precisa este predictia twin-ului fata de performanta reala dupa aplicarea actiunii, si cum variaza performanta NDT cu dimensiunea retelei (Sec. III).

## Ce propun (metoda, pe scurt)
Platforma NDT pentru domeniul de transport, cu urmatoarele componente (Fig. 1, Sec. III-IV): retea fizica (switch-uri, graf orientat), control plane (ONOS + aplicatii SDN prin Northbound REST, intents), sistem de monitorizare (Data Collector + Database cu metrici de flux si de link), virtual twin ca model surogat GNN (arhitectura MPNN cu etape multiple de message passing si mecanism de atentie, derivata din Route-Net Fermi si din lucrarea Modesto et al.), sistem de recomandare (rute alternative la incalcare de SLA: Random sau PPO/Reinforcement Learning) si un strat Network Application. Fluxul: la detectarea unei incalcari SLA (cedare de switch) se activeaza recomandarea, twin-ul prezice latenta pentru fiecare ruta propusa (what-if), operatorul accepta sau respinge, iar ruta aprobata este instalata prin ONOS in reteaua fizica.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Retea fizica emulata: Mininet 2.3.0, ONOS 2.7, OpenVSwitch 2.13.8, Ubuntu 20.04.4, Python 3.8.19 (Tabel I). Pachete de 125 bytes; eMBB 10 Mbps / 10 ms max, URLLC 1 Mbps / 1 ms max; slice-urile sunt distinse prin campul ToS al antetului IP, trafic UDP.
- Trei topologii generate sintetic: 8 noduri / 15 linkuri, 16 / 27, 30 / 75 (toate linkurile unidirectionale). Traficul pleaca dintr-un nod si converge intr-un alt nod indepartat; capacitatea este suficienta, deci congestia nu este luata in calcul, focus pe intarzierea pe cale.
- GNN pre-antrenat pe setul GNNet 2023 (topologii de 5-8 noduri) si testat pe topologii cu alt numar de noduri. Intrari (Tabel II): bandwidth mediu, dimensiune medie pachet, rata pachete, propagation delay (flux); capacitate si incarcare (link).
- Nu este vorba de un core 5G; domeniul este reteaua de transport.

## Experimente si metrici
Scenariu de cedare a unui switch folosit de slice (trei esecuri, instantele N2/N4/N6, noua ruta la N3/N5/N7), in topologia de 30 noduri; latenta medie URLLC si eMBB cu rutare ONOS default (OSPF), Random si AI-based (Fig. 4-5). Fig. 3 arata rutele propuse si predictiile GNN pentru 16 noduri. Metrica: MAPE intre latenta prezisa de twin si latenta masurata in reteaua fizica dupa aplicarea solutiei, pe slice si pe topologie (Tabel III).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Tabel III (MAPE latenta E2E, Random / AI-based): 8 noduri URLLC 1.73% / 1.89%, eMBB 1.84% / 1.82%; 16 noduri URLLC 1.92% / 1.67%, eMBB 1.95% / 1.81%; 30 noduri URLLC 2.12% / 2.28%, eMBB 2.10% / 2.15%. Autorii raporteaza MAPE de aproximativ 1% pentru 8 si 16 noduri si 2% pentru 30 de noduri. In Fig. 4-5 latenta medie in perioada fara ruta este de aproximativ 30 ms (descrisa ca foarte mare).

## Limitari declarate de autori
Traficul a fost limitat din cauza constrangerilor computationale; congestia nu este modelata (capacitate suficienta); lucrari viitoare: compararea algoritmilor de optimizare cu congestie si cerinte variabile, includerea timpului de raspuns in decizie si precalcularea what-if pentru decizii pre-stocate la defecte critice.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu - Sec. IV-V: retea de transport emulata in Mininet/ONOS, fara core 5G
- UE reale sau emulate? nu - Sec. IV-A, Tabel I: fluxuri UDP generate intre noduri, fara UE
- digital twin al retelei? da - Sec. III-IV: NDT cu twin GNN surogat si sincronizare cu reteaua fizica
- prezice efectul unei actiuni inainte de a o aplica? da - Sec. III: what-if, twin-ul prezice latenta fiecarei rute propuse inainte de instalare
- executa actiuni automat (bucla inchisa)? nu - Sec. III, Fig. 2: operatorul aproba sau respinge solutia (om in bucla); instalarea ulterioara prin ONOS este automata
- multi-site / geo-redundanta / failover de baza de date? nu - Sec. V: se testeaza doar cedarea unui switch si rerutarea; failover de baza de date nedeclarat
- evaluare prospectiva (predictie fixata inainte de experiment)? da - Sec. V, Tabel III: predictia twin-ului este comparata cu latenta masurata dupa implementare (comparatie predictie-masuratoare in aceeasi rulare); formularea ca protocol prospectiv fixat in prealabil nu este declarata
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - Sec. V: latenta E2E pe slice, fara utilizatori/sesiuni
- observa traficul la SCP / proxy? nu - nedeclarat (metrici de flux colectate de Data Collector, Sec. IV-C)
