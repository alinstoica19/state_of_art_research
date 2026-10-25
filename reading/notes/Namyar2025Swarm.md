# Enhancing Network Failure Mitigation with Performance-Aware Ranking (SWARM, NSDI 2025) (2025)
Cheie: Namyar2025Swarm . DOI/link: https://arxiv.org/abs/2305.13792 . Sursa textului: integral: arXiv v2 (23 Jun 2025)
Sectiunea din plan: 0 . Tema: nedeclarata

## Problema (cum o formuleaza autorii)
Furnizorii cloud instaleaza mitigari (dezactivarea unor link-uri/switch-uri, re-rutare) pentru a reduce impactul defectelor din retelele de datacenter pana la reparatie. Sistemele existente de auto-mitigare (NetPilot, CorrOpt, playbook-urile operatorilor Azure) aleg actiunea dupa criterii locale simple sau metrici proxy globale (diversitatea cailor, utilizarea link-urilor, rata de pierderi), care pot produce mitigari inadecvate (Sec. 1, 2). Autorii formuleaza problema ca ordonare a mitigarilor dupa impactul asupra metricilor end-to-end la nivel de conexiune (CLP): throughput si flow completion time (FCT). Mitigarea trebuie sa fie aplicata in cca. 5 minute de la localizarea defectului (Sec. 1).

## Ce propun (metoda, pe scurt)
SWARM este un serviciu care ordoneaza mitigarile candidate dupa distributii estimate ale CLP (Sec. 3). Intrari: topologia, mitigarile in curs, patternul/locatia defectului, distributii de trafic (rata de sosire a fluxurilor, dimensiuni, probabilitati de comunicare server-server), mitigarile candidate si un comparator (priority sau linear). Un CLPEstimator esantioneaza K matrici de cerere si N esantioane de rutare (numere alese cu inegalitatea DKW pentru un nivel de incredere), estimeaza separat fluxurile lungi (model pe epoci, water-filling extins cu limita de throughput din pierderi, masurata empiric in testbed mic) si scurte (numar de RTT x RTT, din experimente offline), apoi construieste o distributie compusa si ordoneaza mitigarile. Scalare: algoritm max-min fair aproximativ, downscaling de trafic (dupa POP), paralelism/pipelining, warm start, reducerea numarului de epoci (Sec. 3.4). Actiunile acceptate includ dezactivarea link-ului/switch-ului, readucerea unui link dezactivat anterior, schimbarea ponderilor WCMP, mutarea traficului, nicio actiune (Tabelul 2).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Prototip de 1500 linii Python (Sec. 4).
- Emulare Mininet (stack TCP/IP real din kernel), topologie Clos (Fig. 2), 57 scenarii, peste 4000 ore de experimente; trafic si capacitati reduse de 120x; fiecare emulare 500 s, masurare pe fluxurile din [50,150) s; Cubic si BBR.
- Simulare ns-3 cu 128 servere, 32 ToR, 32 T1, 16 T2, link-uri 20 Gbps / 100 us, DCTCP; distributii de flux DCTCP si FbHadoop; peste 2100 ore (o rulare ns-3 paralelizata cu MPI: 6 ore/esantion).
- Testbed fizic: 32 servere, 6 ToR, 4 T1, 2 T2, switch-uri Arista 7050QX-32, 10 Gbps, 200 us; pierderi induse prin ACL si modificare firmware Broadcom; 3000 fluxuri/s.
- Date: log-uri de productie Azure pentru inter-sosiri; distributia dimensiunilor de flux din DCTCP; probabilitati server-server din literatura; 30 de trasee diferite. Parametri SWARM: 32 trasee de trafic, 1000 esantioane de rutare, epoca 200 ms, flux scurt <=150 KB.
- Baseline-uri: NetPilot (-Orig, -80, -99), CorrOpt (-25/-50/-75), playbook operator (-25/-50/-75).

## Experimente si metrici
Metrica principala: Performance Penalty (%), diferenta relativa fata de cea mai buna mitigare posibila, pe avg throughput (fluxuri lungi), 1p throughput (fluxuri lungi), 99p FCT (fluxuri scurte). Comparatori PriorityFCT si PriorityAvgT. Scenariul 1: corupere de pachete pe link cu redundanta; Scenariul 2: congestie pe un link; Scenariul 3: pierderi la ToR. Mai: scalabilitate (pana la 16K servere), sensibilitate la intrari, Cubic vs BBR, validare ns-3 si testbed, justificarea alegerilor de design.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Scenariul 1, PriorityFCT: penalizare maxima SWARM 0.1% pe FCT, fata de 79.3% la CorrOpt-75 (Fig. 7a); legenda Fig. 7: 793x penalizare mai mica pe 99p FCT in cel mai rau caz fata de urmatorul baseline. SWARM alege dintre nouă combinatii de actiuni si nu ia nicio actiune in peste 25% din cazuri (Fig. 8).
- Scenariul 2: SWARM <=0.1% pe FCT, urmatorul cel mai bun pana la 37.8% (Fig. 9).
- Scenariul 3: penalizare maxima FCT 28.9% la SWARM vs 57% la cel mai bun playbook (Fig. 10).
- Introducere: in cazuri complicate, SWARM alege o actiune cu doar 29% mai slaba decat cea optima; in scenariile 1 si 2 cel mult 9% mai slaba.
- Scalabilitate: sub 5 minute pentru topologie Clos cu 16K servere (Fig. 11a); max-min fair: 36.3x mai rapid, eroare <=0.9%; downscaling 2x: 73.6x; warm start + mai putine epoci: 105.7x, eroare <=1.2% (Fig. 11b,c).
- ns-3 (Fig. 12): SWARM gaseste mitigarea optima (dezactivarea doar a link-ului cu pierderi mari); baseline-urile au 32%-78% penalizare pe 99p FCT.
- Testbed fizic (Fig. 13): optim pe PriorityFCT, sub 1% penalizare pe PriorityAvgT; cea mai rea actiune are peste 1000% penalizare pe FCT.

## Limitari declarate de autori
Fara suport pentru transport lossless (RDMA), alte protocoale de rutare/topologii cu traffic engineering, mitigari cu efecte tranzitorii (ex. reboot de switch), localizare aproximativa a defectului, trafic WAN ignorat, doar doua clase de fluxuri; estimarile pot diferi de ce observa operatorii daca apare un defect neacoperit de esantionare sau traficul se schimba (Sec. 3.4, 5). Sensibilitate la puncte de inflexiune ale intrarilor (Sec. 4.3).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu - retea de datacenter, nu 5G (Sec. 4)
- UE reale sau emulate? nu - fara UE; servere/fluxuri in Mininet, ns-3 si testbed (Sec. 4.1)
- digital twin al retelei? nedeclarat - estimator analitic/empiric al CLP, nu denumit digital twin (Sec. 3)
- prezice efectul unei actiuni inainte de a o aplica? da - Sec. 3: estimeaza distributii CLP pentru fiecare mitigare candidata si le ordoneaza
- executa actiuni automat (bucla inchisa)? nu - Sec. 1, 3.2: SWARM ordoneaza mitigarile pentru operatori sau sisteme de auto-mitigare; aplicarea nu face parte din sistemul evaluat
- multi-site / geo-redundanta / failover de baza de date? nu - Sec. 4: un singur datacenter (topologie Clos)
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - Sec. 4.1: metrici la nivel de flux (FCT, throughput)
- observa traficul la SCP / proxy? nu - Sec. 3.2: foloseste distributii de trafic, nu un proxy
