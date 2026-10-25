# A Dynamic UPF Fault Recovery Mechanism for Enhanced Resilience in 5G Core Networks (2026)
Cheie: Behnaminia2026Upfrecovery . DOI/link: arXiv:2610.03245 (v1, 2 Oct 2026) . Sursa textului: integral, arXiv v1 PDF: https://arxiv.org/pdf/2610.03245 (cod: https://github.com/ION-Lab-Organization/smf)
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Defectarea UPF intrerupe serviciul pentru utilizatorii conectati. Instrumentele Kubernetes/Docker trateaza NF ca fara stare: la repornire UPF devine o instanta noua si pierde contextul sesiunilor PDU (StatefulSets si Services nu pastreaza conexiunile active). Lucrarile existente se concentreaza pe control plane sau pe infrastructura, nu pe pastrarea starii sesiunii in data plane.

## Ce propun (metoda, pe scurt)
- Mecanism la nivel de aplicatie, modificat doar in SMF (OAI): la detectarea pornirii unui UPF deja inregistrat (potrivire IP), SMF il recunoaste ca instanta repornita, filtreaza sesiunile PDU dupa node ID al UPF si retransmite contextul prin 4 mesaje N4/PFCP (Tabel I): N4 Session Establishment Request/Response (PDR, FAR, DNN, S-NSSAI; UL F-TEID) si N4 Session Modification Request/Response (DL F-TEID), fara implicarea AMF.
- Detectie: heartbeat si notificare de pornire de la UPF; se foloseste a doua metoda.
- Mecanism de selectie UPF "failure-aware": lista sortata dupa numarul de defecte (crescator) si apoi timpul de la ultimul defect (descrescator), cu verificare de compatibilitate S-NSSAI/DNN si interfete N3/N6.
- Scenarii discutate: active-standby vs. restart simplu al unui UPF (ales ultimul); SMF ales ca punct de pornire a procedurii.
- Script de monitorizare care lanseaza un UPF de rezerva cu aceeasi adresa IP.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
OAI 5G Core v1.5.0, Ubuntu 20.04 (kernel 5.15.0-122), Docker 27.1.1, Docker-Compose 1.29.2; totul pe un singur calculator (Fig. 4); oai-gnb si oai-nr-ue (simulatoare RAN si UE); un slice cu SMF dedicat si UPF (spgwu); container Ext-Dn ca retea externa; SMF modificat, restul imaginilor OAI oficiale. Defectul simulat prin oprirea si repornirea containerului UPF. Trafic generat cu iperf (TCP, UDP) si ping. Numarul de UE nu este precizat explicit.

## Experimente si metrici
TCP si UDP cu iperf (latenta, latime de banda, in doua faze: in timpul defectului si dupa restaurare); ping pentru pierdere de pachete si RTT; script de monitorizare pentru inlocuire automata a UPF (timp de recuperare pana la primul ping reusit).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- TCP (Fig. 5): latime de banda initiala aproximativ 1.05 Mbps; scade la zero la secunda 8; recuperare declansata la secunda 10 (intrerupere de aproximativ 2 secunde); dupa restaurare depaseste 4 Mbps, apoi se stabilizeaza in jur de 1.05 Mbps.
- UDP (Fig. 6): aproximativ 1.05 Mbps stabil, fara intreruperi majore; avertisment de pierdere de pachete spre finalul testului, in faza de recuperare.
- Ping (Fig. 7): din 111 pachete transmise, 93 primite, pierdere 16.2%; RTT minim 3.0 ms, mediu 6.0 ms, maxim 10.3 ms, mdev 1.7 ms.
- Inlocuire automata a UPF cu script (Fig. 8): timp de recuperare de aproximativ 14 secunde (o rulare).
- Mecanismul de selectie failure-aware: descris, fara rezultate numerice raportate.

## Limitari declarate de autori
Detectia prin heartbeat poate rata o repornire mai rapida decat perioada heartbeat; se presupune infrastructura cu restart automat al containerelor si IP static; scenariul restart simplu implica timp de nefunctionare mai mare; modelul active-standby necesita reconfigurare dinamica a tunelului in gNB si semnalizare suplimentara (extensie viitoare, la fel UPF pool); selectia failure-aware este un punct de plecare (viitor: criterii de ordonare, load si latenta); UDP nu garanteaza livrarea, deci pierderea la comutare ramane o provocare; inlocuirea containerului dureaza mai mult din cauza costului de pornire.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? da - OAI 5G Core v1.5.0 cu SMF modificat (Sec. V)
- UE reale sau emulate? emulate - oai-nr-ue si oai-gnb (Sec. V)
- digital twin al retelei? nu (nu este mentionat in metoda)
- prezice efectul unei actiuni inainte de a o aplica? nu - mecanism reactiv; selectia foloseste istoricul defectelor, nu o predictie (Sec. IV.B.4)
- executa actiuni automat (bucla inchisa)? da - restaurarea contextului declansata de SMF la detectia pornirii UPF si script de monitorizare care lanseaza UPF de rezerva (Sec. IV.A, V.D)
- multi-site / geo-redundanta / failover de baza de date? nu - totul pe un singur calculator (Fig. 4); failover de UPF la nivel de container, nu de baza de date
- evaluare prospectiva (predictie fixata inainte de experiment)? nu (Sec. V)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? da, la nivel de flux/sesiune: throughput TCP/UDP, pierdere si RTT ping prin sesiunea UE (Sec. V.A-C); nu se masoara inregistrari de abonati
- observa traficul la SCP / proxy? nu - SMF observa UPF prin N4/PFCP; SCP nementionat (Sec. III-IV)
