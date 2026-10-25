# Digital Twins for 5G Networks: A Modeling and Deployment Methodology (2023)
Cheie: SanzRodrigo2023Mndtmethodology . DOI/link: 10.1109/ACCESS.2023.3267548 . Sursa textului: integral, versiunea publicata (IEEE Access vol. 11) din repository-ul UPM: https://oa.upm.es/81320/1/Digital_Twins_for_5G_Networks_A_Modeling_and_Deployment_Methodology.pdf
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Digital Twin-ul aplicat retelelor mobile (Mobile Networks Digital Twin, MNDT) depinde de precizia modelarii elementului fizic, iar retelele operatorilor sunt eterogene. Autorii identifica provocari deschise: colectare de date in timp real (topologie, configuratii, telemetrie), preprocesarea datelor pentru modelare bazata pe date, un cadru de desfasurare a twin-urilor pe arhitectura NFV aliniat la modelele de date ale platformelor MANO, interfete securizate intre elementul fizic si cel digital, si standardizare (ETSI, IETF). Frameworkurile existente (Eclipse Ditto, FIWARE, etc.) sunt considerate de autori nu 100% compatibile cu cazul MNDT.

## Ce propun (metoda, pe scurt)
- O metodologie in 7 faze pentru crearea automata a unui MNDT: (1) Data acquisition cu agenti in reteaua fizica (ALTO, SNMP, ICMP, Iperf3, OpenFlow), (2) Modeling (model simplificat, semantic, al retelei), (3) Adaptation (conversie in sabloane VNFD/NSD: TOSCA, Jinja2, YANG), (4) NFV deployment (Open Source MANO + OpenStack ca VIM, multi-VIM cu Docker Swarm/Kubernetes), (5) Provisioning (playbook-uri Ansible), (6) Interconnection (gateway-uri la marginea retelelor, mesagerie MQTT/Kafka/RabbitMQ, TLS cu criptografie post-cuantica prin liboqs/OpenSSL), (7) Feedback (bucla bidirectionala intre twin-uri).
- Doua stari ale sistemului: state 0 (creare, colectare topologie) si state 1 (monitorizare/telemetrie, fazele 4-5 eliminate, fazele 2, 3, 6 pastrate cu modificari minore).
- Core-ul 5G (planul de semnalizare) este tratat ca element fix, static, provizionat independent, atat in twin-ul fizic cat si in cel digital (nu este colectat in faza 1 si nu este modelat in faza 2).
- Arhitectura: module MNDT System Input, NFV Deployment (OpenMANO/OpenStack), Communication and Interconnection (pipeline V2V si P2V), Monitoring (port mirroring pentru seturi de date), Traffic Injection (STG/UTI: semnalizare NAS catre AMF, sesiuni PDU, trafic de utilizator prin tunel GTP catre UPF, fara RAN real).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Prototip centrat pe primele faze, in scenariu GNS3 (Fig. 9) care reproduce un caz de utilizare Industry 4.0: mai multe site-uri cu zone 5G independente conectate la un core prin retea de agregare cu echipamente Cisco; 5G Stand-Alone.
- Core 5G: free5GC. Injectie de trafic 5G: modulul STG/UTI.
- Agentul dezvoltat (autonom) descopera topologia prin SNMP (retea traditionala, hardware); OpenFlow pentru SDN este indicat ca urmatorul pas. Date: configuratii colectate din reteaua de test (topologie, interfete, rute), serializate in JSON (Fig. 10).
- Numarul de UE, NF sau noduri nu este specificat.

## Experimente si metrici
Evaluare (Sec. VII) calitativa a fazelor 1-3: agentul se conecteaza la un router din reteaua de agregare, face interogari SNMP (identificator, nume, interfete, adrese IP, numar de rute, segmente accesibile), construieste un model JSON si repeta procesul pe subretelele descoperite (foloseste snmpEngineID pentru a evita bucle); apoi transforma elementele in fisiere VNFD (sabloane TOSCA) si VLD. Se descrie si desfasurarea la nivel topologic pe Open Source MANO + OpenStack. Nu sunt raportate metrici cantitative.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Nu sunt raportate cifre. Rezultatul declarat: agentul obtine informatia minima necesara pentru a instantia reteaua ca twin digital pe o arhitectura NFV, genereaza N fisiere VNFD plus fisiere VLD (Sec. VII, Fig. 10 ca exemplu de reprezentare JSON a unui router R3 din agregare).

## Limitari declarate de autori
Lucrarea este intr-o faza initiala; sunt implementate doar primele trei faze (plus desfasurare topologica). Necesar in continuare: caracterizarea topologica a retelelor SDN prin OpenFlow; validarea interconectarii twin-urilor prin protocoale de mesagerie cu suport post-cuantic; reconfigurarea dinamica a MNDT pe baza deciziilor de optimizare (comutare intre state 0 si 1); determinarea parametrilor de utilizare a dispozitivelor (CPU, RAM) pentru dimensionarea resurselor in faza 4. Se presupune ca reteaua este stabila (rutare convergenta) si exista permisiuni de administrator pentru agenti.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? da - free5GC in testbed GNS3 (Sec. VI)
- UE reale sau emulate? emulate - STG/UTI emuleaza UE si injecteaza trafic fara RAN real (Sec. V.E, VI)
- digital twin al retelei? da la nivel de metodologie/arhitectura; twin-ul efectiv nu este inca creat in prototip, doar fazele 1-3 si desfasurare topologica (Sec. VII)
- prezice efectul unei actiuni inainte de a o aplica? nedeclarat ca experiment; mentionat doar ca scop general al DT (Sec. I, Abstract)
- executa actiuni automat (bucla inchisa)? nu in implementare - faza 7 Feedback este propusa, nevalidata (Sec. IV.G, VIII)
- multi-site / geo-redundanta / failover de baza de date? nu - site-uri industriale multiple in topologia de test, dar fara geo-redundanta sau failover (Sec. VI)
- evaluare prospectiva (predictie fixata inainte de experiment)? nu (Sec. VII)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu (Sec. VII)
- observa traficul la SCP / proxy? nu - nu apare SCP; monitorizare prin port mirroring pe subretele (Sec. V.D)
