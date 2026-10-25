# ECHO: A Reliable Distributed Cellular Core Network for Hyper-scale Public Clouds (2018)
Cheie: Nguyen2018Echo . DOI/link: https://doi.org/10.1145/3241539.3241564 . Sursa textului: integral: versiunea autorilor gazduita de Microsoft Research (microsoft.com/en-us/research/wp-content/uploads/2018/07/ECHO-Mobicom.pdf), gasita prin pagina publicatiei MSR
Sectiunea din plan: C . Tema: core distribuit fiabil in cloud public / geo-redundanta
Autori: Binh Nguyen, Tian Zhang, Bozidar Radunovic, Ryan Stutsman, Thomas Karagiannis, Jakub Kocur, Jacobus Van der Merwe (University of Utah; Microsoft Research; Core Network Dynamics). ACM MobiCom 2018, New Delhi; 16 pagini.

## Problema (cum o formuleaza autorii)
Intrebarea este daca un core celular (control plane EPC) poate rula pe un cloud public hyper-scale (AWS, Azure). Trei provocari (1):
- **Fiabilitate:** SLA-urile cloud sunt de "four 9s", si doar pentru servicii replicate pe mai multe VM-uri, in timp ce un core cere pana la "five 9s".
- **Failover:** detectia defectelor in cloud public dureaza de ordinul a 10 s, iar timeout-urile core-ului sunt de ordinul a 1 s.
- **Consistenta starii sesiunilor:** starea este distribuita intre componente si dispozitive. Control plane-ul este o masina de stari distribuita per UE, cu "side effects" (de exemplu Modify Bearer Request catre SGW/PGW) si timere (2).

Experimente motivationale cu un Nexus 5, un eNodeB ip.access si OpenEPC (3.1):
- dupa 5 incercari de Attach esuate (1 minut), UE-ul intra intr-o stare silentioasa timp de 12 minute;
- daca MME pierde contextul UE, UE-ul ramane fara serviciu 54 de minute.

## Ce propun (metoda, pe scurt)
- **ECHO** (4):
  - fiecare componenta (MME, SGW, PGW) este replicata pe mai multe VM-uri in spatele unui load balancer;
  - componentele sunt refactorizate in frontend-uri de procesare stateless plus o stocare persistenta foarte disponibila, comuna (ZooKeeper);
  - ECHO ramane disponibil si consistent cat timp o majoritate a VM-urilor, intr-un DC sau intre DC-uri, este accesibila.
- **Protocol end-to-end de replicare a masinii de stari** (4.3, Algoritmul 1):
  - un agent "entry point", considerat fiabil, pe statia de baza: adauga ID de cerere, UE-ID si timer, si reincearca pana la confirmare;
  - componentele cloud non-blocante executa cererile atomic si in ordine, cu actualizari conditionate de versiunea znode-ului ZK;
  - cererile si starile vechi sunt detectate; la handover se foloseste un protocol in doua faze, asemanator Paxos;
  - operatiile SGW/PGW sunt facute idempotente.
- **Implementare** (5): agent eNodeB in C (aproximativ 5.000 de linii) pe un small cell COTS si un proxy SCTP->TCP (Azure nu suporta SCTP); modificari in OpenEPC; client ZooKeeper; deployment pe Azure.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- **Studiu de disponibilitate de 3 luni** intr-un cloud public mare (3.3, Tabelul 1): 3 DC-uri (doua in Europa, unul in SUA), cate doua clustere de 3 VM-uri per DC, ping TCP la 1 s intre VM-uri si Azure Application Insights (din 10 locatii, la 10 minute).
- **ECHO pe Azure:** un DC sau trei DC-uri, cu configuratii ZK diferite (Tabelul 2); telefoane reale (Nexus 5) si sarcini sintetice (1000 de UE emulate pe un eNodeB).
- Rulare de 7 zile pe un DC, cu reboot-uri de noduri si crash-uri de proces injectate la 1% dintre mesajele S1AP.
- **Trial live de 3 luni:** agentul ECHO pe cinci eNodeB IP Access E40, cu 40 de utilizatori.

## Experimente si metrici
- Disponibilitatea cloud-ului pe durate de intrerupere si niveluri (acelasi LB, acelasi DC, alt DC, din Internet) (Tabelul 1, Fig. 4).
- Latenta scrierilor ZK; latenta per mesaj si latenta perceputa de UE pentru Attach si Service Request (Fig. 11).
- Throughput la saturare; scenarii de defect (crash MME, Fig. 12); disponibilitate analitica.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- **Studiul cloud:** "five 9s" se obtin doar cu replicare pe mai multe VM-uri in zone de disponibilitate diferite ale aceluiasi DC. Pentru problemele de conectivitate din Internet este nevoie de prezenta in mai multe DC-uri regionale. Vazuta din Internet, disponibilitatea este cu aproximativ un ordin de marime mai mica, iar peste 20% dintre intreruperi dureaza 20 de minute sau mai mult (3.3). Valorile din Tabelul 1 sunt imagine in PDF; textul citeaza p = 0,99947 si q = 0,99991.
- **Analitic:** P(ZK) = 0,999999 pentru un ansamblu de 3 noduri; disponibilitatea unei componente cu t = 2 clustere DC este 0,99999999. Autorii concluzioneaza "six 9s", presupunand defecte independente.
- **Robustete:** in cele 7 zile, cu defecte injectate la 1% din mesaje, toate mesajele S1AP au fost procesate corect.
- **Latenta:** ECHO adauga aproximativ 7% (70 ms) la Attach fata de OpenEPC intr-un DC. Deployment-ul pe 3 DC-uri adauga aproximativ 40% (400 ms) la Attach, dar tolereaza pierderea unui DC. Introducerea arata un overhead sub 10% pentru latenta si throughput intr-un DC.
- **Throughput:** similar cu OpenEPC, aproximativ 900 de mesaje pe secunda, atat pe un DC cat si pe 3 DC-uri.
- **Crash MME** (Fig. 12): cu OpenEPC, UE-ul nu primeste serviciu din minutul 23 pana in minutul 56; cu ECHO si doua instante MME, UE-ul continua fara intrerupere vizibila.
- **Trial live:** fara degradare de performanta in 3 luni; incarcarea maxima a fost de 14 utilizatori per eNodeB.

## Limitari declarate de autori
- Stocarea este consistenta (linearizabila), deci, conform teoremei CAP, ECHO nu ramane disponibil daca nicio majoritate de DC-uri nu comunica. Autorii considera cazul extrem de rar (nota 4).
- Disponibilitatea calculata presupune independenta defectelor, ceea ce in practica nu este garantat (6).
- Deployment-ul multi-DC adauga latenta; propuneri: DC-uri mai apropiate si integrare mai stransa (7).
- Lucrarea priveste EPC (4G), nu core-ul 5G.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - core EPC (4G) implementat, bazat pe OpenEPC modificat, pe Azure (5).
- UE reale sau emulate?: ambele - telefoane Nexus 5 reale si 40 de utilizatori in trial-ul live; 1000 de UE emulate pentru throughput (6).
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu.
- executa actiuni automat (bucla inchisa)?: da - failover automat: agentul reincearca catre alta instanta sau alt DC, iar conflictele sunt rezolvate in stocare (4.3, Fig. 12).
- multi-site / geo-redundanta / failover de baza de date?: da - replicare pe 3 DC-uri Azure cu un ansamblu ZooKeeper geo-distribuit care tolereaza pierderea unui DC (Tabelul 2, 6).
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: da - latenta Attach si Service Request perceputa de UE si continuitatea serviciului la crash MME (Fig. 11-12).
- observa traficul la SCP / proxy?: partial - agentii ECHO sunt proxy-uri care intermediaza S1AP intre eNodeB si MME (SCTP->TCP); nu este SCP 5G (5).
