# Procedure-Aware Stateless Systems for 5G & Beyond Core Networks (2023)
Cheie: Goshi2023Statelessprocedures . DOI/link: https://doi.org/10.1109/globecom54140.2023.10437306 . Sursa textului: integral: versiunea autorilor din repository-ul institutional mediaTUM (mediatum.ub.tum.de/1733372)
Sectiunea din plan: C . Tema: core stateless / managementul starii
Autori: Endri Goshi, Vignesh Karunakaran, Hasanin Harkous, Rastin Pries, Wolfgang Kellerer (Technical University of Munich; Nokia). IEEE GLOBECOM 2023.

## Problema (cum o formuleaza autorii)
- Deployment-urile stateful nu au flexibilitatea ceruta de orchestrarea cloud-native: starea este legata de o instanta si se pierde la terminare sau defect. Deployment-urile stateless (starea in UDSF) costa latenta si scalabilitate din cauza tranzactiilor frecvente cu starea (I, II).
- Statelessness poate fi tranzactional (starea este citita si scrisa la fiecare interactiune intre NF-uri; NF-ul se poate recupera si in mijlocul unei proceduri, dar costa mai mult) sau procedural (starea este citita la inceputul si scrisa la sfarsitul procedurii). Majoritatea NF-urilor, cu exceptia AMF si SMF, nu stiu ce procedura se executa, deci doar varianta tranzactionala este fezabila pentru ele (II, IV).

## Ce propun (metoda, pe scurt)
Doua mecanisme care fac sistemul constient de procedura, folosind AMF ca punct de intrare constient de procedura (IV):
- **Piggyback-based:**
  - structura global_ue_ctx (un dictionar per UE cu contextele tuturor NF-urilor stateless, fara redundanta);
  - AMF o citeste din UDSF la inceputul procedurii si o scrie la sfarsit;
  - contextul relevant pentru NF-urile urmatoare este atasat cererilor HTTP, iar contextele actualizate sunt atasate raspunsurilor (Fig. 3);
  - au fost modificate AUSF, SMF, PCF si UDM.
- **Proactive-Push:**
  - AMF cere UDSF-ului sa impinga contextul UE catre NF-urile implicate, care il pastreaza local pe durata procedurii;
  - la final, AMF declanseaza un pull, prin care UDSF colecteaza contextul actualizat de la fiecare NF; copiile locale sunt apoi sterse (Fig. 4);
  - API-ul UDSF si SBI-urile AUSF, SMF, PCF si UDM au fost extinse.
- Baseline: Stateless Free5GC [4], cu AMF stateless procedural si celelalte NF-uri stateless tranzactional.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Cluster Kubernetes cu 1 master si 11 workeri DELL OptiPlex 9020 (i7-4770, 16 GB), switch de 1 Gb, un NF per nod (V, Fig. 5).
- Prometheus, Envoy-Proxy ca sidecar (intercepteaza traficul NF-urilor si colecteaza metrici HTTP) si un exportor de metrici per nod (la 1 s).
- gNBEmu: emulator gNB si UE care trimite cereri reale catre core.
- Patru proceduri: Registration, PDU Session Establishment, PDU Session Release, Deregistration.
- Sarcina: 25, 50, 100 si 150 de UE noi pe secunda, cu timp inter-sosire de 3 ms; 45 s per masurare, 8 campanii per scenariu.

## Experimente si metrici
- Procedure Completion Time (PCT), de la primul mesaj al UE pana la ultimul raspuns din core (Fig. 6).
- Utilizarea medie a CPU per NF (Fig. 7).
- Memoria si payload-ul HTTP au fost masurate, dar nu sunt prezentate; autorii spun ca sunt foarte apropiate de baseline.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- **PCT** (Fig. 6):
  - Registration: Piggyback -44%, Proactive-Push -14% fata de baseline;
  - Deregistration: Piggyback -70%, Proactive-Push -30%;
  - PDU Session Establishment: Piggyback similar cu baseline-ul, Proactive-Push -13%;
  - PDU Session Release: Piggyback +17% (din cauza comunicarii asincrone), Proactive-Push -22%.
- **CPU** (Fig. 7):
  - Piggyback: -10% la Registration si -38% la Deregistration, dar aproximativ +10% la PDU Establishment si Release (procesarea global_ue_ctx in AMF si SMF);
  - Proactive-Push: -21% la PDU Session Release, aproximativ egal la PDU Establishment si Deregistration, +8% la Registration cu 150 de UE.
- Nu exista un mecanism optim pentru toate procedurile: Piggyback este mai bun la procedurile sincrone, Proactive-Push la cele asincrone (V.C).

## Limitari declarate de autori
- Niciuna dintre abordari nu este optima pentru toate procedurile (V.C).
- Lucrare viitoare: un sistem hibrid, cu clasificarea procedurilor in sincrone si asincrone (VI).
- Spre deosebire de varianta tranzactionala, varianta procedurala nu se poate recupera dupa un defect aparut in mijlocul unei proceduri (II).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - Stateless Free5GC modificat (AMF, AUSF, SMF, PCF, UDM, UDSF) pe Kubernetes (IV, V).
- UE reale sau emulate?: emulate - gNBEmu (V).
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu.
- executa actiuni automat (bucla inchisa)?: nu.
- multi-site / geo-redundanta / failover de baza de date?: nu - starea este externalizata in UDSF pentru rezilienta la defecte de instanta, dar defectele nu sunt evaluate.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: da - timpul de finalizare a Registration, Deregistration si PDU Session Establishment/Release pentru UE emulate (Fig. 6).
- observa traficul la SCP / proxy?: partial - Envoy-Proxy ca sidecar intercepteaza tot traficul NF-urilor si colecteaza metrici HTTP; nu este SCP 3GPP (V).
