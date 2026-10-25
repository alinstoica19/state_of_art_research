# PP5GS - An Efficient Procedure-Based and Stateless Architecture for Next-Generation Core Networks (2023)
Cheie: Goshi2023Pp5Gs . DOI/link: https://doi.org/10.1109/tnsm.2022.3230206 . Sursa textului: integral: versiunea autorilor din mediaTUM (mediatum.ub.tum.de/1695118)
Sectiunea din plan: C . Tema: SBA / arhitectura core stateless
Autori: Endri Goshi, Raffael Stahl, Hasanin Harkous, Mu He, Rastin Pries, Wolfgang Kellerer (TU Munchen; Nokia). IEEE Transactions on Network and Service Management (online 2022).
Nota de proces: la prima incercare din aceasta rulare, serverul mediaTUM nu a raspuns (timeout) si nota a fost scrisa din rezumat. La o reincercare ulterioara serverul a raspuns, iar nota a fost rescrisa din textul integral.

## Problema (cum o formuleaza autorii)
- Descompunerea functionala a SBA creste traficul de semnalizare intre NF-uri in timpul procedurilor si complica orchestrarea, din cauza dependentelor stranse dintre NF-uri (Rezumat, I).
- Dupa autori, offload-ul la edge al unor NF-uri individuale de control plane poate fi contraproductiv: costul comunicarii intre NF-uri pe durata procedurii degradeaza performanta (I).
- Lucrarea extinde o propunere conceptuala anterioara [13], care avea doar implementare si evaluare partiala (RegNF) (I).

## Ce propun (metoda, pe scurt)
- **Core stateless** (IV.A):
  - UDSF conform 3GPP Rel-15, cu stare serializata JSON in blocuri si inregistrari cu TTL; backend BadgerDB (embedded), ales dupa un benchmark cu Redis (Fig. 2); o singura instanta UDSF, pentru consistenta;
  - NRF si UDR folosesc MongoDB, iar NSSF nu are stare per UE;
  - AMF este stateless procedural; AUSF, PCF, SMF si UDM sunt stateless tranzactional.
- **Per-Procedure NFs (PPNF)** (IV.B): logica unei proceduri este integrata aproape complet intr-un singur NF stateless, cu NRF, UDR si UDSF partajate. Au fost implementate patru PPNF: Registration, PDU Session Establishment, PDU Session Release, Deregistration. Tabelul I listeaza NF-urile implicate in fiecare procedura (6 la Registration, 7 la PDU Establishment).
- Scalabilitate la nivel de functie (procedura), nu de instanta.
- **Unelte proprii:** emulator gNB+UE (gNBEmu, Anexa A) si emulator UPF (UPFe, Anexa B). Dezvoltare cu CI/CD.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- 11 noduri bare-metal, switch 1 Gb, Kubernetes 1.22.1 cu Calico, Docker 20.10.5, Ubuntu 18.04 (V.A, Fig. 4).
- 9 workeri DELL OptiPlex 9020 (i7-4770, 16 GB), un NF per nod; Envoy-Proxy langa NF-uri; Prometheus la 1 s.
- Sisteme comparate (Fig. 5):
  - Stateful Free5GC (baseline);
  - Stateless Free5GC;
  - Procedure-Pods (NF-urile unei proceduri in acelasi pod);
  - PP5GS.
- Sarcina: 25, 50, 100, 200 si 300 de UE noi pe secunda, IAT 3 ms, 45 s per scenariu, 8 campanii (Tabelul II). Configuratii suplimentare la 400 de UE pe secunda: IAT determinist 2,5 ms, bimodal si multimodal (Tabelul III).
- Edge offloading: 5 ms RTT injectat cu tc intre edge si core. Variante: core centralizat, AMF la edge, PPNF la edge (Fig. 11).

## Experimente si metrici
- Performanta emulatorului si coada de UE (Fig. 6); utilizarea CPU (Fig. 7); Procedure Completion Time (PCT) (Fig. 8-9).
- Numarul de cereri intre NF-uri (Fig. 10); PCT in scenariile de edge offloading (Fig. 12).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- **CPU** (V.C, Fig. 7):
  - Stateless Free5GC consuma mai mult decat Stateful: +43% (Registration), +49% (PDU Establishment), +98% (PDU Release), +89% (Deregistration), mai ales din cauza UDSF;
  - PP5GS consuma mai putin: -26% / -42% la Registration si -34% / -55% la PDU Establishment, fata de Stateful si respectiv Stateless; la procedurile simple este la nivelul Stateful.
- **PCT** (V.D, Fig. 8):
  - fata de baseline-ul Stateful, PP5GS este cu 42% mai rapid la Registration si cu 50% la PDU Establishment;
  - la procedurile simple este in medie cu aproximativ 12% si 8% mai lent, dar diferenta absoluta este de aproximativ 1 ms;
  - la 300 de UE pe secunda, Registration, Stateless Free5GC ajunge la 521 ms PCT mediu si Procedure-Pods la 11,48 s;
  - PP5GS ramane mai bun decat baseline-ul la toate cele trei tipare de trafic la 400 de UE pe secunda (Fig. 9).
- **Cereri intre NF-uri** (V.E, Fig. 10):
  - Registration: -57% fata de Stateful, -72% fata de Stateless;
  - PDU Establishment: -61% si -72%;
  - PDU Release si Deregistration: -50% si -40% fata de Stateful, -83% si -75% fata de Stateless.
- **Edge** (V.F, Fig. 12): mutarea doar a AMF la edge creste PCT-ul procedurilor complexe; PPNF la edge are PCT mai mic decat AMF la edge pentru Registration, PDU Establishment si PDU Release, si performanta similara la Deregistration.

## Limitari declarate de autori
- PP5GS are nevoie de un router de trafic constient de procedura intre gNB si PPNF-uri. Autorii sugereaza ca in generatiile viitoare acesta ar putea fi integrat in gNB (VI).
- Deployment-urile multi-vendor sunt mai greu de realizat in forma actuala; ar fi posibile daca fiecare PPNF vine de la alt furnizor, cu starea stocata la distanta (VI).
- Lucrari viitoare: data plane si impactul asupra experientei utilizatorului, autoscaling dinamic si comportamentul la defecte (VI).
- AMF nu cere context existent din UDSF la Registration, iar contextul nu este sters la Deregistration, pentru simplificarea testarii (IV.A).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - free5GC stateful si stateless, Procedure-Pods si PP5GS pe Kubernetes (IV, V).
- UE reale sau emulate?: emulate - gNBEmu, plus un UPF emulat (UPFe) (V.A, Anexele A-B).
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu.
- executa actiuni automat (bucla inchisa)?: nu - autoscaling-ul este lucrare viitoare (VI).
- multi-site / geo-redundanta / failover de baza de date?: partial - un scenariu edge/core cu 5 ms RTT emulat (V.F); o singura instanta UDSF, fara failover evaluat.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: da - timpul de finalizare a Registration, PDU Session Establishment/Release si Deregistration pentru UE emulate (Fig. 8-9, 12).
- observa traficul la SCP / proxy?: partial - Envoy-Proxy langa NF-uri pentru metrici; nu este SCP 3GPP (V.A).
