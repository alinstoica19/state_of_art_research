# Investigating Inter-NF Dependencies in Cloud-Native 5G Core Networks (2021)
Cheie: Goshi2021Internf . DOI/link: https://doi.org/10.23919/cnsm52442.2021.9615565 . Sursa textului: integral: versiunea autorilor din mediaTUM (mediatum.ub.tum.de/1620043)
Sectiunea din plan: C . Tema: SBA / dependente intre NF-uri / resurse
Autori: Endri Goshi, Michael Jarschel, Rastin Pries, Mu He, Wolfgang Kellerer (TU Munchen; Nokia Bell Labs). CNSM 2021.
Nota de proces: la prima incercare din aceasta rulare, mediaTUM nu a raspuns si nota a fost scrisa din rezumat. La reincercare, PDF-ul a fost accesibil, iar nota a fost rescrisa din textul integral.

## Problema (cum o formuleaza autorii)
- Descompunerea functionala mare si deployment-ul distribuit din SBA creeaza dependente stranse intre NF-uri. Intelegerea lor este necesara pentru alocarea eficienta a resurselor, evitarea bottleneck-urilor si optimizarea scalarii (I).
- Lucrarile anterioare se concentreaza pe un singur NF (de exemplu scalarea AMF [13]) sau pe arhitecturi alternative, nu pe dependentele dintre NF-uri intr-un deployment Rel-15 (III).

## Ce propun (metoda, pe scurt)
- Studiu experimental al dependentelor dintre NF-uri pentru procedurile Registration si Deregistration, cu free5GC pe Kubernetes (IV, V).
- Emulator gNB si UE scris in Go: Registration, Deregistration, PDU Session Establishment si Release; IMSI si chei generate, UE introdusi in baza de date. Executia este secventiala per instanta de emulator (IV.B).
- Autorii au contribuit la free5GC, pentru ca NF-urile sa anunte IP-uri de Kubernetes Service la inregistrarea in NRF (II.B).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- 11 noduri hardware: master si colector de masuratori, 9 noduri NF (un NF per nod: AMF, AUSF, NRF, NSSF, PCF, SMF, UDM, UDR, UPF) si un nod de emulare. Switch 1G, DELL OptiPlex 9020 (i7-4770, 16 GB), Ubuntu 18.04, Docker 19.03.12, Kubernetes 1.17.17, free5GC 3.0.5, MongoDB (IV.A, Fig. 2).
- Constrangeri observate:
  - executia paralela a multor UE intr-un emulator a dus la overflow in buffer-ul socket-urilor SCTP si la caderea AMF, de aceea s-au folosit mai multe instante de emulator;
  - UPF nu a putut gestiona multe proceduri PDU simultane, deci acestea au fost excluse (IV.B-C).
- 4.500 de UE impartite egal intre 5, 10, 20 sau 30 de emulatoare in paralel. MongoDB ajunge la aproximativ 600% CPU, deci traficul nu a fost crescut mai mult (V.A-B).
- Scenarii (V.A):
  - I: fara limite de resurse;
  - II: bottleneck artificial, prin limitarea CPU a unui NF (UDM la 1 nucleu, valoarea medie observata la Registration cu 10 emulatoare).

## Experimente si metrici
- Utilizarea CPU per NF, colectata la 200 ms; maximul este 800% (8 nuclee) (Fig. 4, 6).
- Rapoartele de utilizare CPU intre NF-uri, cu UDM ca referinta (Fig. 5, 7).
- Procedure Completion Time per UE: Registration de la RegistrationRequest la RegistrationComplete; Deregistration pana la UEContextReleaseComplete (Fig. 8).
- Memoria nu este KPI (statica); I/O de retea este lasat pentru lucrari viitoare.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Registration declanseaza un lant mare de NF-uri, cu NRF si AMF cele mai solicitate (Fig. 4).
- Rapoartele de utilizare CPU dintre NF-uri raman aproape constante cand traficul creste, ceea ce arata ca NF-urile sunt strans cuplate (Fig. 5, 7).
- Rapoartele difera intre proceduri: de exemplu AMF/UDM este aproximativ 1,6 la Registration si 2,2 la Deregistration (V.B).
- Limitarea UDM la 1 nucleu creste PCT-ul Registration si blocheaza intregul core; celelalte NF-uri nu isi pot folosi resursele. Comportamentul a fost acelasi la limitarea altor NF-uri (rezultate neprezentate) (V.C, Fig. 8).
- Autorii propun orchestrarea core-ului pe lanturi per procedura, nu pe NF-uri separate (V.B).

## Limitari declarate de autori
- Sunt evaluate doar Registration si Deregistration; procedurile PDU sunt excluse din cauza limitarilor UPF (IV.C).
- Executia este secventiala per emulator, din cauza limitarii AMF/SCTP in free5GC (IV.B).
- Traficul nu a fost crescut peste saturarea MongoDB (V.B).
- Lucrari viitoare: orchestrare per procedura si mecanisme de scalare a lanturilor, comparate cu scalarea per NF (VI).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - free5GC 3.0.5 pe Kubernetes (IV.A).
- UE reale sau emulate?: emulate - emulator gNB si UE propriu (IV.B).
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu.
- executa actiuni automat (bucla inchisa)?: nu.
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: da - timpul de finalizare a Registration si Deregistration per UE emulat (Fig. 8).
- observa traficul la SCP / proxy?: nu.
