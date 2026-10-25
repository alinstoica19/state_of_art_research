# Network Digital Twin for 6G and Beyond: An End-to-End View Across Multi-Domain Network Ecosystems (2025)
Cheie: Tran2025Ndt6Gsurvey . DOI/link: 10.1109/ojcoms.2025.3599866 . Sursa textului: integral, arXiv v1 (2 Iun 2025), https://arxiv.org/pdf/2506.01609 (nu versiunea publicata IEEE OJ-COMS)
Sectiunea din plan: A
## Problema (cum o formuleaza autorii)
Retelele 6G+ trebuie sa sustina aplicatii (VR/XR, chirurgie la distanta, vehicule autonome, holografie) cu rate mari si latenta foarte mica, ceea ce face dificile proiectarea, planificarea, depanarea, optimizarea si mentenanta retelelor la scara mare fara a afecta experienta utilizatorului. Autorii prezinta Network Digital Twin (NDT) drept solutie: un model virtual al retelei reale, care permite simularea de proiecte, aplicarea de politici si reproducerea de scenarii de defect. Afirma ca sondajele existente se concentreaza pe domenii individuale (IoDT, edge, tehnologii-cheie) si pretind ca este primul sondaj care acopera o gama larga de domenii 6G din perspectiva academica si industriala (Tab. I).
## Ce propun (metoda, pe scurt)
Lucrare de tip survey, structurata ca arhitectura NDT end-to-end pe domenii (Fig. 1-2): II DT pentru RAN (DT-RAN: definitie, use case-uri precum predictive maintenance/fault management/optimizare, tehnologii: achizitie de date, ray tracing, accelerare, apoi DT pentru O-RAN si pentru intelligent surfaces/RIS); III transport networks (inclusiv DT pentru retele optice, Tab. IV); IV 5G and beyond core (5GCORE+); V cloud/edge computing; VI aplicatii (vehicular, security, blockchain, health, manufacturing); VII NTN (satelit, UAV); VIII retele cuantice; IX provocari si directii; X concluzii. Face distinctia DT vs simulator: DT integreaza date in timp real din sistemul fizic in bucla de simulare, cu flux bidirectional de informatie.
Sec. IV (5GCORE+): descrie NF-urile 5G (UPF, AMF, SMF, PCF, AF, SMSF, NSSF, AUSF, UDM, UDR) si interfetele N1-N35 (Fig. 7); motiveaza NDT pentru core prin reducerea costurilor, management/optimizare avansate, predictia defectelor/anomaliilor, planificare si securitate; apoi rezuma lucrari: [79] design NDT pentru core cu 7 faze, mediu de test cu GNS3 si free5gc; [80] 5GC-former si 5GC-Seq2Seq care reconstruiesc NF-urile core prin deep learning; [81] NDT pentru network slicing cu agenti DRL; [82] MVNOCoreSim, simulator la nivel de protocol pentru IoT; [83] PoC NDT pentru conectivitate in zbor; [84] NDT cu online learning pentru detectia DDoS; [77] NDT pentru detectie de defecte si auto-recuperare, bazat pe arhitectura China Mobile Research Institute (perceptie -> analiza -> decizie -> implementare).
## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Nu este lucrare experimentala; nu are testbed propriu. Descrie setup-urile lucrarilor citate (ex. GNS3 + free5gc in [79]; simulari in [80]; date din retea MVNO reala in [82]); mentioneaza exemple din industrie (ex. Ericsson [45], Colosseum [54] pentru DT O-RAN).
## Experimente si metrici
Nu este lucrare experimentala. Tab. IV rezuma lucrari de DT pentru retele optice (tehnologie, scop, metoda ML/AI); alte tabele sintetizeaza lucrari pe domenii.
## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Cifre raportate din lucrari citate (Sec. IV-C): 5GC-Seq2Seq si 5GC-former ating F1-score 99,997% si respectiv 99,999% [80]; framework DDoS cu online learning: 97% acuratete [84]; sursa [78] este citata pentru management zero-touch cu "99.99% automation". Nu exista rezultate proprii ale autorilor.
## Limitari declarate de autori
Sec. IX enumera provocari deschise: sincronizare in timp real si fuziune de date; scalabilitate si complexitate; modelare de inalta fidelitate a mediilor dinamice; explainable AI; securitate si confidentialitate (twin-ul ca tinta); consum de resurse si eficienta energetica.
## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu - survey; mentioneaza lucrari cu free5gc (Sec. IV-C)
- UE reale sau emulate? nu - fara experimente proprii
- digital twin al retelei? da - subiectul sondajului este NDT (Sec. I-X), dar nu construiesc unul propriu
- prezice efectul unei actiuni inainte de a o aplica? nu - nu exista sistem propriu; descrie conceptual ca DT permite testarea modificarilor inainte de rollout (Sec. I, II)
- executa actiuni automat (bucla inchisa)? nu - nu exista sistem propriu; discuta bucle inchise in lucrari citate (ex. [77], Sec. IV-C)
- multi-site / geo-redundanta / failover de baza de date? nedeclarat - doar mentiune a datelor distribuite geografic (Sec. II-A)
- evaluare prospectiva (predictie fixata inainte de experiment)? nu - nu este lucrare experimentala
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - fara masuratori proprii
- observa traficul la SCP / proxy? nedeclarat (SEPP apare doar in descrierea SMSF, Sec. IV-A)
