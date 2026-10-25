# Network Digital Twin (NDT): Concepts and Reference Architecture (2026)
Cheie: IRTFNMRG2026Ndtarch . DOI/link: https://datatracker.ietf.org/doc/draft-irtf-nmrg-network-digital-twin-arch/ . Sursa textului: integral, draft-irtf-nmrg-network-digital-twin-arch-13 (1 iulie 2026, IRTF NMRG, Informational, expira 2 ian. 2027): https://www.ietf.org/archive/id/draft-irtf-nmrg-network-digital-twin-arch-13.txt
Sectiunea din plan: Standarde . Tema: Network Digital Twin
## Problema (cum o formuleaza autorii)
Cresterea scarii si a cerintelor retelelor face operarea complexa; introducerea de inovatii este dificila din cauza riscului de a perturba serviciile existente si a costului incercarilor fara platforme de emulare fiabile (Sec. 1). Documentul afirma ca nu exista o definitie unificata a caracteristicilor NDT in industrie (Sec. 4) si ca cercetarea este la inceput, cu aplicatii centrate pe scenarii specifice (Sec. 3.2).
## Ce propun (scop si continut)
Document informational al IRTF NMRG (consens al grupului, nu candidat la standard Internet) care ofera: o prezentare a conceptului NDT, definitii de baza, o arhitectura de referinta, scenarii de aplicare, beneficii si provocari (rezumat, Sec. 1).
- Definitii (Sec. 2.2): Digital Twin, Network Digital Twin, Physical Network.
- Cinci elemente cheie ale NDT (Sec. 4, Fig. 1): Data, Models, Mapping, Interfaces, Logic (analyze, diagnose, optimize, control, emulate). Mapping: one-to-one (pairing, vertical) si one-to-many (coupling, horizontal). Se mentioneaza repeatability si reproducibility; interactiunea in timp real nu e obligatorie pentru toate cazurile.
- Arhitectura de referinta (Sec. 7, Fig. 2): Data Repository, Service Mapping Models (Basic models si Functional models), Network Digital Twin Management; interfete de intrare/iesire. Reteaua reala poate fi, intre altele, retea de acces mobila, transport, mobile core, backbone, data center; documentul se concentreaza pe retele relevante IETF (IP bearer, data center).
- Exemplu de realizare (Sec. 8, Fig. 3): NDT ca element central intr-un controler bazat pe intentii, cu "outer loop" (intent-assurance) si "inner loop" in care solutiile candidate sunt evaluate in NDT ca "sandbox" inainte de actionare.
- Tehnologii de sustinere (Sec. 9): colectare de date (SNMP, NETCONF, IPFIX, telemetrie, subscriptii YANG), modelare (NS-3, Mininet, EVE-NG, GNS-3; abstractizari matematice, bottleneck structures; modele AI/ML), vizualizare, trei tipuri de interfete (network-facing, application-facing, internal), twinning management (orchestration of twins, collaboration management, conflict detection and resolution, energy-efficient twinning).
- Interactiunea cu Intent-Based Networking (Sec. 10), referinta la RFC 9315.
- Scenarii (Sec. 11): human training, ML training, DevOps-oriented certification, network fuzzing, network inventory management.
## Clauze relevante (numar clauza - ce defineste)
- Sec. 4 - cele cinci elemente NDT si tipurile de mapping.
- Sec. 5 - beneficii: (a) fidelitate ridicata prin date in timp real; (b) risc redus la aplicarea automata de configuratii dupa analiza si verificari in twin; (c) reparare automata in bucla inchisa a defectelor, cu strategia de corectie verificata in twin; plus subsectiuni 5.1-5.5 (cost total de operare, decizii, evaluare mai sigura, confidentialitate, training).
- Sec. 6 - provocari: scara, interoperabilitate, modelarea datelor, cerinte de timp real, riscuri de securitate.
- Sec. 7 - componente functionale (Data Repository, Service Mapping Models, NDT Management).
- Sec. 8 - bucla interioara/exterioara cu NDT in controler bazat pe intentii.
- Sec. 9.5 - twinning management, inclusiv energy-efficient twinning.
- Sec. 10 - NDT ca enabler pentru IBN.
- Sec. 12 - perspective de cercetare: sinergia NDT cu LLM si AI Agents; NDT ca "sandbox" de verificare a actiunilor agentilor autonomi si de atenuare a halucinatiilor; integrarea Agentic AI + NDT ca factor spre niveluri mai ridicate de autonomie.
- Sec. 13 - securitate: gestiunea datelor, confidentialitate, securitatea sistemului, retelei si operationala, redundanta/failover si backup/recovery ale NDT.
## Entitati, servicii si parametri definiti
Entitati conceptuale: Digital Twin, Network Digital Twin, Physical Network, Data Repository, Service Mapping Models (Basic models: modele de element de retea si topologie; Functional models: analiza, emulare, diagnoza, predictie, asigurare), NDT Management (gestioneaza operarea pe sesiuni, ciclul de viata, performanta si consumul de resurse, topologie, configuratie, performanta, securitate). Interfete: network-facing (candidate SNMP, NETCONF), application-facing (candidat RESTful), internal (candidate XMPP, HTTP/3). Documentul nu defineste parametri numerici sau mesaje de protocol; nu contine sectiune IANA (Sec. 14).
## Limitari declarate de autori
Sec. 12: constructia unui NDT complet ramane provocatoare in privinta acuratetei datelor, complexitatii modelarii si sincronizarii in timp real; sunt necesare standardizarea interfetelor si modelelor de date. Sec. 7: documentul se concentreaza pe retele relevante IETF (IP bearer, data center). Sec. 3.2: cercetarea in domeniu este "still in its infancy". Sec. 4: interactiunea in timp real nu este obligatorie in toate cazurile de utilizare.
## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu - document conceptual; mobile core mentionat doar ca tip posibil de retea reala (Sec. 7).
- UE reale sau emulate? nedeclarat (document conceptual).
- digital twin al retelei? da - obiectul documentului (Sec. 2-4, 7).
- prezice efectul unei actiuni inainte de a o aplica? da, descriptiv - impactul solutiilor candidate evaluat in NDT inainte de actuare (Sec. 1, 5, 8); nu exista implementare.
- executa actiuni automat (bucla inchisa)? descris conceptual - bucla inchisa de automatizare si reparare automata (Sec. 5, 8, 9.5); nu exista implementare.
- multi-site / geo-redundanta / failover de baza de date? nedeclarat pentru o implementare; Sec. 13 mentioneaza redundanta si failover pentru NDT, iar Sec. 7 mentioneaza NDT in mai multe domenii administrative.
- evaluare prospectiva (predictie fixata inainte de experiment)? nu - fara experimente.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - fara experimente.
- observa traficul la SCP / proxy? nu - SCP nu este mentionat.
