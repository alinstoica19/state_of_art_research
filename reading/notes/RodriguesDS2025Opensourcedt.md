# Open-Source 5G Digital Twin: Virtualizing Core and RAN for Network Replication (2025)
Cheie: RodriguesDS2025Opensourcedt . DOI/link: https://doi.org/10.1109/icton67126.2025.11125422 . Sursa textului: integral: versiunea acceptata de autori (repository UPC, upcommons.upc.edu, PDF cu notificare IEEE 2025)
Sectiunea din plan: C . Tema: nedeclarata

## Problema (cum o formuleaza autorii)
Complexitatea retelelor 5G face dificila testarea, optimizarea si depanarea fara a perturba retelele de productie. Autorii sustin ca un digital twin (Mobile Networks Digital Twin, MNDT) ofera replici virtuale care evolueaza sincron cu reteaua fizica, iar simularea singura poate fi insuficienta, ceea ce motiveaza emularea unei retele reale. Lucrarea este prima faza dintr-un proiect in trei faze (faza 1: replica virtuala; fazele urmatoare: sincronizare in timp real si antrenare AI/ML pentru autonomie).

## Ce propun (metoda, pe scurt)
O metodologie propusa (formulata la viitor: "will") pentru a crea un digital twin al unei retele 5G de cercetare pe doua campusuri universitare folosind componente open-source. Reteaua fizica de referinta (Sec. III-A): doua instante core 5G SA redundante (Release 17), cate una pe campus, cu Compact Mobility Units (CMU) care grupeaza AUSF, AMF, UDM, SMF, UPF; trei unitati radio n40 (FR1, 2300 MHz) si doua n258 (FR2) pe campus, un BBU pe locatie; legatura prin fibra optica cu latenta sub o milisecunda. Arhitectura twin-ului (Sec. III-B): trei straturi (virtualizare core, virtualizare RAN, emulare de canal), NF-uri in containere, infrastructura OpenStack. Se vor compara Open5GS, free5GC si OpenAirInterface; pentru RAN: UERANSIM (emulare gNB si UE, configurat pentru MIMO 4T4R/2T2R) si srsRAN (aspecte FR2). Sunt prevazute modele RF specifice campusurilor, simulare de handover, latenta si backhaul.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Nu exista experimente in lucrare: este o propunere de metodologie si plan de implementare. Unelte planificate: Open5GS, free5GC, OAI (core), UERANSIM, srsRAN (RAN), OpenStack, containere (mentionat si Kubernetes in recomandari). Scara tintei: doua campusuri, cinci unitati radio pe campus. Date: nu sunt folosite.

## Experimente si metrici
Plan de evaluare (Sec. VI), neexecutat: latenta planului de control (timpi de inregistrare si de stabilire a sesiunii, fizic vs digital, sub sarcina variabila), throughput UL/DL, utilizare CPU/memorie/retea; calitatea legaturii radio, rata de succes si latenta handover; fidelitatea twin-ului: tinta de diferenta sub 10% intre timpii procedurilor de control-plane fizic vs digital, acuratetea throughput-ului, corelatia tiparelor de utilizare a resurselor. Sunt planificate si ghiduri (Sec. VII) pentru alegerea core-ului si configurarea OpenStack.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Nu sunt raportate rezultate masurate. Singurele afirmatii despre rezultate sunt asteptari: Open5GS "expected" sa aiba performanta superioara in control plane (timpi mici de inregistrare), free5GC "anticipated" sa aiba consum minim de resurse, OAI "expected" sa ofere throughput mare pe planul de date (Sec. III-B-1). Singura cifra de tinta: diferenta sub 10% la timpii procedurilor (Sec. VI-C).

## Limitari declarate de autori
Lucrarea descrie doar prima faza; sincronizarea bidirectionala si modelele AI/ML apartin fazelor ulterioare (Sec. VIII). Stratul de transport nu este in centrul implementarii (Sec. III-A). Alte limitari nedeclarate explicit.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nedeclarat ca realizat - Sec. III-IV: implementare planificata cu Open5GS/free5GC/OAI, fara raportare de rezultate
- UE reale sau emulate? emulate (planificat) - Sec. III-B-2: UERANSIM
- digital twin al retelei? da, ca proiect/propunere - Sec. I, III (neimplementat complet in lucrare)
- prezice efectul unei actiuni inainte de a o aplica? nedeclarat - Sec. I: mentionat ca motivatie generala (testare fara perturbare), nu ca mecanism
- executa actiuni automat (bucla inchisa)? nu - Sec. VIII: sincronizarea si autonomia sunt faze viitoare
- multi-site / geo-redundanta / failover de baza de date? multi-site da pentru reteaua fizica de referinta (doua campusuri, doua core redundante, Sec. III-A); failover de baza de date nedeclarat
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat - Sec. III-B: apar doar asteptari pentru cele trei core-uri, fara experiment
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - Sec. VI: metrici planificate (timpi de inregistrare/sesiune), nemasurate
- observa traficul la SCP / proxy? nedeclarat
