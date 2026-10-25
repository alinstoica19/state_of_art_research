# TEGRA: A Flexible & Scalable NextGen Mobile Core (2025)
Cheie: Saleem2025Tegra . DOI/link: https://arxiv.org/abs/2509.07410 . Sursa textului: integral: arXiv 2509.07410v1 (9 septembrie 2025)
Sectiunea din plan: C . Tema: SBA / scalabilitate si rezilienta core
Autori: Bilal Saleem, Omar Basit, Jiayi Meng, Iftekhar Alam, Ajay Thakur, Christian Maciocco, Muhammad Shahbaz, Y. Charlie Hu, Larry Peterson (Purdue; Intel; University of Michigan; UT Arlington; Princeton). Preprint.

## Problema (cum o formuleaza autorii)
- Core-urile SBA sunt flexibile, dar propunerile recente pentru performanta (L2 5GC, Magma, CoreKube) revin la tehnici NFV: consolidarea serviciilor pe un singur server sau intr-un singur binar monolit stateless. Asta castiga latenta, dar pierde flexibilitatea (amestecul de furnizori, CI/CD) (1, Fig. 1-2).
- Masuratori pe Aether (3.1, Fig. 3-4):
  - sub 20 ms pentru un singur UE la REG, PDU si SR;
  - latenta creste abrupt de la 32 de UE, iar PDU ajunge la 1000 ms;
  - cu trace-uri reale, limita de latenta este depasita la aproximativ 20.000 de UE;
  - resursele nu sunt bottleneck-ul: la 256 de UE se folosesc 9,96 din 80 de nuclee si 0,4 din 72 GB;
  - bottleneck-ul este congestia comunicarii intre servicii: intarzierea AMF-UDM creste cu un ordin de marime de la 1 la 256 de UE.
- Patru provocari specifice core-ului (3.2):
  - C1: mesaje bidirectionale (upstream prin SCTP de la UE, downstream prin PFCP de la UPF) care trebuie procesate stateful de aceeasi instanta;
  - C2: dependente complexe, de tip mesh, intre servicii, care variaza pe evenimente; service mesh-urile clasice (Linkerd, Istio) nu sunt adecvate;
  - C3: incarcare inegala intre servicii (de exemplu la SR, AMF are de aproximativ patru ori incarcarea SMF, Tabelul 2);
  - C4: timeout-uri si retransmisii ierarhice (T3550, T3580, T3510) care pot fi folosite pentru recuperarea dupa defecte.
- CoreKube este, dupa autori, incomplet: suporta doar mesaje upstream prin SCTP, fara PFCP downstream (nota de subsol 2).

## Ce propun (metoda, pe scurt)
- **TEGRA**, core SBA conform 3GPP, cu soft state: contextul per UE este pastrat in instanta si scris asincron in stocare. O instanta noua citeste sincron ultima stare consolidata dupa terminarea scrierilor in curs (4).
- **Patru tipare de microservicii** (4.1.1, Fig. 6):
  - P1 Gateway: terminarea SCTP si PFCP, separat de AMF si SMF;
  - P2 Long-Running: AMF, SMF, NRF;
  - P3 Ephemeral: celelalte servicii;
  - P4 Storage.
- **UELB:** load balancing sticky pe UE, astfel incat toate mesajele unui UE ajung la aceeasi instanta (4.2).
- **DRSM:** partajare distribuita a starii si a incarcarii prin publish/subscribe, cu MongoDB (TTL, tranzactii atomice, change streams) folosit ca broker prin NRF (4, 5).
- Autoscaling fin per serviciu.
- **Implementare** (5): Go 1.18.3, pe baza Aether. Aproximativ 4.100 de linii modificate (AMF 51%, SMF 15%, AUSF 12%, UDM 12%) si un gateway nou de aproximativ 2.800 de linii; cache persistent per UE in Redis 7.4.2.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Edge cloud on-premise cu Proxmox VE 7.4: trei servere Intel Gold 5220R (96 de nuclee), NIC Intel X710 40G, switch Tofino1, overlay EVPN-VxLAN (6.1.1, Fig. 5).
- Alocare de nuclee: 10 pentru gateway, 10 pentru stocare, 10 pentru Kubernetes, 50 pentru core.
- gNBSimRT: extensie proprie a gNBSim (Aether), cu UE si gNB emulate si profiluri de evenimente (REG, PDU, SR).
- Doua tipuri de trace-uri:
  - sintetice: cereri closed-loop;
  - reale: timpi inter-sosire dintr-un trace de o saptamana de la un operator mare, cu aproximativ 40.000 de UE esantionate.
- Baseline-uri: Aether, Magma, Open5GS, free5GC, CoreKube. Pentru CoreKube autorii construiesc "~CoreKube", estimand liniile de cod si latenta functiilor lipsa (6.1.2).
- Metrici: latenta end-to-end per eveniment, timp per serviciu (OpenTelemetry), trafic SBI.

## Experimente si metrici
- Speedup fata de Aether la 32-256 de UE pentru REG, PDU si SR (Fig. 7).
- Autoscaling cu HPA (maxim 4 nuclee per instanta, tinta 60% CPU), sub sarcina SR closed-loop (Fig. 8).
- Intarzierea AMF-UDM in functie de numarul de instante (Fig. 9).
- Efectul cache-ului per UE si al DRSM (Tabelul 3).
- Defect provocat: stergerea SMF cu kubectl (Fig. 10).
- Costul adaugarii unui serviciu sau eveniment nou (linii de cod, fisiere).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- La 256 de UE, fata de Aether: speedup de 1,74x (REG), 1,5x (PDU) si 1,75x (SR). Peste 32 de UE, TEGRA are latenta mai mica decat Aether, free5GC, Magma si Open5GS (Fig. 7).
- Rezumatul raporteaza procesare de 20x, 11x si 1,75x mai rapida decat free5GC, Open5GS si Aether, si performanta comparabila cu CoreKube.
- Cu 4 instante, intarzierea dintre functii scade de pana la 10 ori (Fig. 9).
- Cache-ul per UE reduce apelurile la baza de date de la peste 10 la 1,1 (medie) per eveniment si timpul de acces cu 22 ms (REG), 37 ms (PDU) si 57 ms (SR) la 256 de UE. Fara DRSM, overhead-ul creste in medie cu 5,6 ms (6.3.3).
- **Defect SMF** (6.3.4, Fig. 10):
  - Aether pierde toata starea UE, iar UE-urile intra in timeout;
  - TEGRA cu o singura instanta: instanta noua recupereaza starea, iar AMF reincearca la 3 s; procesarea se reia in aproximativ 6 s;
  - TEGRA cu mai multe instante: alta instanta preia imediat mesajul UE afectat.
- **Flexibilitate** (6.3.5): un serviciu nou (NRF) inseamna o linie de configuratie in TEGRA, fata de 1.705 linii in 18 fisiere in CoreKube. Un eveniment nou (PDU) inseamna o linie in TEGRA, fata de 712 modificari in 6 fisiere in CoreKube.

## Limitari declarate de autori
- Latenta initiala este mai mare in TEGRA din cauza gateway-ului SCTP si a bazei de date, pana cand pornesc instante suplimentare (6.3.1).
- Timpul de executie domina in continuare latenta, iar optimizarile software singure nu sunt suficiente. Directia viitoare: co-optimizare hardware-software, cu offload pe SmartNIC-uri (8).
- Comparatia cu CoreKube foloseste un baseline augmentat estimat (~CoreKube), nu o implementare completa (6.1.2).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - TEGRA pe baza Aether, plus Aether, free5GC, Open5GS, Magma si CoreKube desfasurate pe Kubernetes (5, 6).
- UE reale sau emulate?: emulate - gNBSimRT; timpii inter-sosire provin dintr-un trace real de operator (6.1.1, 6.1.3).
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu.
- executa actiuni automat (bucla inchisa)?: da - autoscaling HPA si load balancing pe baza incarcarii partajate prin DRSM, plus recuperarea automata a starii dupa defect (4.2, 6.3).
- multi-site / geo-redundanta / failover de baza de date?: partial - failover de instanta SMF cu stare persistata in Redis (6.3.4); multi-site si failover de baza de date nu sunt evaluate.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: da - latenta end-to-end per UE pentru inregistrare, stabilirea sesiunii PDU si Service Request (Fig. 7-8, 10).
- observa traficul la SCP / proxy?: nu - SCP nu este folosit. Rutarea foloseste un gateway SCTP/PFCP si load balancing pe client (UELB), iar traficul SBI este observat cu OpenTelemetry (4, 6.1.3).
