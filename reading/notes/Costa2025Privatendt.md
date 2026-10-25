# A Network Digital Twin of a 5G Private Network: Designing a Proof-of-Concept from Theory to Practice (2025)
Cheie: Costa2025Privatendt . DOI/link: arXiv:2510.12458 . Sursa textului: arXiv v1 (14 Oct 2025), https://arxiv.org/pdf/2510.12458
Sectiunea din plan: A
## Problema (cum o formuleaza autorii)
Network Digital Twin (NDT) este prezentat ca tehnologie cheie pentru retelele viitoare, dar autorii spun ca exista multe lucrari teoretice si foarte putine implementari reale. Lucrarea descrie caracteristicile unui NDT (standarde, sincronizare, scalabilitate, securitate, evaluare) si ofera un exemplu practic pe o retea 5G privata reala dintr-un laborator.
## Ce propun (metoda, pe scurt)
- Parte de survey/concepte: ISO 23247 (patru domenii), ITU-T Y.3090, drafturi IETF (NDT reference architecture, data generation), provocari de sincronizare si indicatori (Twin Alignment Ratio, State Consistency Index, Update Latency, Data Freshness, Synchronization Frequency, deviation of prediction) (Sec. 1).
- Implementare: Network Physical Twin = Amarisoft Callbox Classic (RAN + core intr-un singur dispozitiv, 2 SIM-uri, 2 telefoane). NDT construit peste emulatorul ComNetsEmu (Mininet + Docker), cu Open5GS (core) si UERANSIM (gNB si UE), 4 containere (RAN, MEC, 2 host-uri cloud), switch-uri OpenVSwitch, legaturi 10 Mbps cu latenta variabila, doua network slice-uri (MEC si cloud) (Sec. 2.2, Fig. 4).
- Metodologie in trei etape (Sec. 2.3-2.4): (1) data acquisition: configuratia (APN/DNN, IP, banda per tunel, nr. utilizatori) extrasa din mme.cfg al Amarisoft, in JSON, transferata prin SSH/SFTP (paramiko); (2) modeling: configurare Open5GS (smf.yaml, nssf.yaml, amf.yaml) si UERANSIM; (3) synchronization: trafic real capturat cu tcpdump pe interfata tun2 a dispozitivului fizic, ferestre de T secunde in pcap, transferat in NDT si reluat cu tcpreplay. NDT-ul ofera astfel imaginea retelei cu intarziere T + intarzierea de comunicatie.
- Software open source: https://github.com/fabrizio-granelli/Amarisoft.digital.twin
## Setup experimental (testbed real / emulare / simulare; unelte: Open5GS, free5GC, OAI, UERANSIM, ns-3, Kubernetes...; scara: nr. UE, NF, noduri; date: trafic real, trace-uri, sintetice)
- Twin fizic: testbed real indoor (Amarisoft Callbox Classic, telefoane mobile); twin digital: emulare (ComNetsEmu, Open5GS, UERANSIM). NDT si NPT conectate printr-un LAN Ethernet de 1 Gbps; ceasurile sunt aliniate pentru comparatie; T = 120 s in toate experimentele (Sec. 3).
- Scara: 2 UE (doua telefoane), 4 containere in NDT.
- Date: trafic real capturat (pcap) din NPT si reluat in NDT.
## Experimente si metrici
Patru scenarii de trafic, cu graficul de throughput al NPT deasupra si al NDT dedesubt: (1) doua UE pornite, inregistrate, navigare web (Fig. 6); (2) streaming YouTube (Fig. 7); (3) apeluri vocale intre cele doua telefoane, prin interfata IMS (Fig. 8); (4) live streaming Facebook, in principal uplink (Fig. 9). Evaluarea este comparatie vizuala de throughput; nu sunt definite metrici numerice de eroare in text.
## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Nu sunt raportate cifre de acuratete. Autorii spun ca graficele NPT si NDT sunt foarte similare ca forma si timp in Fig. 6-9 (la apeluri vocale: "aproape similar", Fig. 8) si concluzioneaza ca NDT reproduce cu acuratete ridicata comportamentul si starea sistemului 5G. Intarzierea declarata a NDT fata de NPT este T plus intarzierea de comunicatie (T = 120 s) (Sec. 2.4, 3).
## Limitari declarate de autori
- Legatura este unidirectionala (fizic -> twin); legatura inversa (twin -> fizic, bucla inchisa) este lucru viitor (Sec. 4).
- Intarziere de sincronizare (decalaj intre ceasurile twin-ului si ale retelei fizice); reducerea ei prin predictie de trafic este lucru viitor (Sec. 4, 5).
- Replicarea topologiei, setup-ului si traficului presupune transfer de date considerabil, care poate constrange canalul si introduce intarziere; ce date trebuie transferate ramane o problema deschisa, fara abordari formale in literatura (Sec. 4).
- Predictia starii NDT cu ML/AI este propusa ca directie viitoare, nu implementata (Sec. 4).
## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? da - Open5GS in NDT; core real (Amarisoft) in twin-ul fizic (Sec. 2.1-2.2)
- UE reale sau emulate? ambele - 2 telefoane reale in NPT; UE emulate cu UERANSIM in NDT (Sec. 2.1, 2.2, 3)
- digital twin al retelei? da - NDT al unei retele private 5G, construit pe emulator (Sec. 2-3)
- prezice efectul unei actiuni inainte de a o aplica? nu - mentionat ca posibilitate/viitor (Sec. 4); nu este demonstrat
- executa actiuni automat (bucla inchisa)? nu - legatura unidirectionala; bucla inchisa e lucru viitor (Sec. 4)
- multi-site / geo-redundanta / failover de baza de date? nu - un singur laborator si un singur NDT (Sec. 3)
- evaluare prospectiva (predictie fixata inainte de experiment)? nu - nu exista predictie; comparatie replay vs original (Sec. 3)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - throughput de trafic; inregistrarea UE e doar pas de scenariu in Fig. 6, fara metrica (Sec. 3)
- observa traficul la SCP / proxy? nu - captura pcap pe interfata tun2 a dispozitivului fizic; SCP/proxy nu apar (Sec. 2.4)
