# COREX: Framework for Distributed Digital Twins of 5G/6G Network Topologies and Automated Experiment Executions (2026)
Cheie: BenllochCaballero2026Corex . DOI/link: 10.1109/tnsm.2026.3699692 . Sursa textului: accepted author manuscript (IEEE TNSM, nu e versiunea finala editata), repozitoriul Aston, https://publications.aston.ac.uk/id/eprint/49190/1/AAM_COREX_Framework_for_distributed_digital_twins_of_5G_6G_network_topologies_and_automated_experiment_executions.pdf
Sectiunea din plan: A
## Problema (cum o formuleaza autorii)
Cercetarea B5G/6G cere framework-uri care sa emuleze topologii complexe, sa automatizeze experimentele si sa permita studii de securitate cibernetica. Emulatoarele (CORE, ns-3) cer curba de invatare mare si nu automatizeaza; testbed-urile cer configurare manuala si nu ofera orchestrare unificata host-emulator-container; emulatoarele 5G usoare nu au datapath multi-tenant programabil si suport de mobilitate. Problema formulata: lipsa unui framework care sa desfasoare, configureze si execute scenarii B5G/6G complexe repetabil si scalabil.
## Ce propun (metoda, pe scurt)
- COREX (CORE eXecutor): framework de automatizare scris in principal in Bash, cu un orchestrator si patru controllere: Host Resource Controller (HRC), Emulator Resource Controller (ERC), Node Resource Controller (NRC), Logging Controller (LC); un fisier de configurare descrie topologia, use case-ul si componentele software (Sec. III.A, Fig. 1).
- Cinci faze de executie: setup, configuration, experiment, results, restoring (Fig. 2), cu modele de timp T_total = T_setup + T_config + T_exp + T_results + T_restore (Ec. 1-7), complexitate declarata liniara in noduri/legaturi, cu factori liniari pentru tenants si UE.
- Multi-tenancy cu Open vSwitch (daemon OVS izolat per container) si encapsulare VXLAN cu cheie per tenant (Alg. 1); mobilitatea UE prin tunele GTP recreate intre CU-uri emulate (handover logic, fara emularea semnalului radio); mirror interfaces pentru NIDS.
- Executie distribuita pe mai multe masini fizice, comutata printr-o variabila de configurare, comenzi prin SSH (Cod 3, Fig. 4).
- Caz de utilizare: DDoS UDP flood cu UE infectate (Bonesi) si o bucla de self-protection (detectie, planificare, mitigare) bazata pe Traffic Control (TC). Autorii precizeaza ca COREX nu este un algoritm ML/DL de management, ci orchestrarea pe care astfel de algoritmi pot fi antrenati si validati (Sec. III.B).
## Setup experimental (testbed real / emulare / simulare; unelte: Open5GS, free5GC, OAI, UERANSIM, ns-3, Kubernetes...; scara: nr. UE, NF, noduri; date: trafic real, trace-uri, sintetice)
- Emulare in timp real cu CORE (Common Open Research Emulator), containere, Linux namespaces, OVS, GTP, VXLAN/GRE; legatura radio emulata fara parametri fizici (EMANE mentionat ca optiune, nefolosit). Nu sunt folosite Open5GS/free5GC/OAI/UERANSIM (nu apar in setup); ns-3 apare doar ca termen de comparatie in Tabel I.
- Hardware: pana la patru masini cu Ubuntu 20.04, Intel Xeon E5-2650 2.8 GHz, 64 GB RAM DDR3, switch Ethernet 10 Gbps (Sec. IV).
- Configuratii (Tabel II, 18 experimente): UE in {2, 4, 8, 16, 32, 64}; banda per UE in {16, 32, 64} Mbps; 1 Edge server, 1 Core server; 2 tenants; UDP; 3 componente software de log per server; durata atac fixa 120 s; rezultate medii pe 10 rulari per experiment.
- Date: trafic sintetic generat (DDoS); fara trafic real din operator. Se citeaza raportul Cloudflare Q3 2025 ca justificare a parametrilor atacului.
## Experimente si metrici
1. Timp de executie pe faze (deployment, configuration, attack, log collection, restoring) vs nr. UE (Tabel III, Fig. 5a/5b).
2. Performanta de banda in segmentul Edge: banda asteptata vs obtinuta, 2 UE si 64 UE (Fig. 6a, 6b).
3. Mitigare cognitiva self-protection: serii de timp ale benzii inainte/dupa punctul de mitigare pentru 8 si 32 UE atacatoare (Fig. 7a, 7b). Evaluarea presupune etichetare perfecta a traficului benign/malitios (fara fals pozitive/negative); obiectivul declarat nu este acuratetea detectiei.
## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Tabel III, timp total mediu (s) pentru 2/4/8/16/32/64 UE: 717.0, 699.0, 731.0, 785.0, 1000.0, 1191.0 (Min Total/Max Total: 714/727, 690/712, 770/812, 777/801, 988/1021, 1172/1212, asa cum sunt tiparite; pentru 8 UE media 731 este in afara intervalului min-max tiparit). Deployment: 87.0, 95.0, 112.0, 145.0, 212.0, 347.0 s. Configuration: 168.0, 172.0, 180.0, 196.0, 230.0, 303.0 s. Attack: 133.0, 134.0, 134.0, 134.0, 137.0, 140.0 s. Log collection: 289.0, 257.0, 263.0, 266.0, 285.0, 259.0 s. Restoring: 40.0, 41.0, 42.0, 44.0, 136.0, 142.0 s.
- Textul spune ca deployment si restoring cresc exponential in vizualizarea log (Fig. 5b); scenariul cu 64 UE genereaza peste 240 namespace-uri Linux; intregul ciclu cu 64 UE ia sub 1192 s.
- Fig. 6a (2 UE): banda obtinuta 31.87, 63.88, 127.92 Mbps pentru 32, 64, 128 Mbps asteptati (99.6%, 99.8%, 99.9%). Fig. 6b (64 UE): 532.30, 1050.43, 2089.25 Mbps pentru 1024, 2048, 4096 Mbps asteptati (52.0%, 51.3%, 51.0%). Textul mai spune ca in abordarea distribuita banda obtinuta creste cu 51.01%.
- Fig. 7: pentru 8 atacatori atacul mitigat scade la 0 (mitigare 100%) in 10 secunde; pentru 32 atacatori nu se atinge 100% in fereastra de 120 s: mitigare aprox. 54%, de la 480 Mbps la 220 Mbps, in 80 s; degradarea e atribuita saturarii CPU/I/O, nu clasificarii gresite.
- Lucrari anterioare ale autorilor (nu rezultate noi aici): mitigare UDP flood de pana la 300 Mbps in 57 s [38]; convergenta mitigarii in cel mult 90 s in studiile anterioare.
## Limitari declarate de autori
- Atacuri cu durata fixa; atacuri adaptive/variabile sunt lucru viitor. Etichetare perfecta presupusa; analiza fals pozitive/negative cu trafic multi-tenant este lucru viitor.
- Scalabilitatea in topologii mari este limitata de contentia CPU din scenariul DDoS (generatoare Bonesi, procesare de pachete in kernel, clasificare OVS), nu de CORE/COREX conform autorilor; la scara mare ar trebui generatoare mai usoare sau hardware suplimentar.
- Mobilitatea e doar la nivel logic, fara emularea semnalului radio. Deployment si restoring necesita optimizare pentru scalabilitate.
- Implementari reale ar cere integrare cu datapath-uri accelerate hardware (DPDK, SR-IOV) si componente control-plane carrier-grade. COREX ar putea fi adaptat la Kubernetes, Docker sau infrastructuri 5G cloud-native (afirmat, nedemonstrat).
- Tabel I indica pentru COREX limita cheie "Use-case CPU dependent".
## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu - topologie emulata cu containere, OVS si tunele GTP; nu este mentionat un core 5G cu NF-uri (AMF, SMF etc.) in setup (Sec. III.C, IV)
- UE reale sau emulate? emulate - UE sunt containere/namespace-uri cu generatoare de trafic (Sec. III.D, IV)
- digital twin al retelei? da - se autointituleaza framework pentru digital twins distribuite ale topologiilor B5G/6G, create prin emulare; nu e prezentata sincronizare cu o retea fizica concreta (Sec. I, III)
- prezice efectul unei actiuni inainte de a o aplica? nu - nu se prezic efecte; se executa experimente pe twin (Sec. III.B, IV)
- executa actiuni automat (bucla inchisa)? da - bucla de self-protection detecteaza, planifica si mitigheaza DDoS automat, in emulare (TC) (Sec. IV, IV.C); orchestrarea experimentului e automata
- multi-site / geo-redundanta / failover de baza de date? nu - distribuit pe pana la 4 masini intr-un singur laborator, fara failover; DB doar pentru loguri (Sec. III.E, IV)
- evaluare prospectiva (predictie fixata inainte de experiment)? nu - nu exista predictii; benzile "asteptate" sunt tinte de atac (Sec. IV.B)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - metrici de timp de orchestrare si banda; nu inregistrari/sesiuni UE (Sec. IV)
- observa traficul la SCP / proxy? nu - mirror interfaces pentru NIDS pe datapath, fara SCP/proxy (Sec. III.C)
