# An NWDAF Approach to 5G Core Network Signaling Traffic: Analysis and Characterization (2022)
Cheie: Manias2022Signaling . DOI/link: 10.1109/globecom48099.2022.10000989 . Sursa textului: integral, arXiv v3 (19 oct 2022; "Accepted: IEEE GlobeCom 2022"): https://arxiv.org/pdf/2209.10428
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Abordarile data-driven sunt solutii promitatoare pentru performanta retelelor 5G si ulterioare, nefiind nevoie de modele precise ale problemei. Autorii afirma ca, dupa cunostinta lor, nu exista prototipuri experimentale functionale de core 5G si NWDAF; lucrarile anterioare au extrapolat din trafic 4G si de internet (Sec. I). Un prototip functional si un set de date specific core-ului 5G ar permite cercetarilor viitoare sa foloseasca date realiste pentru decizii de management (plasare NF, scalare etc.).

## Ce propun (metoda, pe scurt)
Contributii declarate (Sec. I): un prototip NWDAF functional; analiza datelor generate de retea pentru interactiunile NF-NF din core; folosirea invatarii nesupervizate pentru gruparea interactiunilor NF-NF; discutie despre aplicarea insight-urilor NWDAF in MANO inteligent.
Metoda (Sec. II, III): core Open5GS (Release 16) rulat in masini virtuale; NWDAF colecteaza prin port mirroring si Apache Kafka (pipeline si streaming, cu export in MongoDB prin Kafka Connect); pachetele sunt filtrate la cele cu sursa si destinatie NF de core; pentru fiecare pereche NF-NF se calculeaza lungimea medie, maxima, deviatia standard si numarul de pachete; aceste patru statistici, scalate, sunt trasaturile pentru k-Means cu k intre 2 si 7, rulat de mai multe ori pentru a reduce sensibilitatea la initializare.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Un singur server cu Hyper-V (hipervizor Type 1), cu o masina virtuala Linux (Ubuntu) per NF sau entitate; retea privata (Fig. 1). NF-uri: NRF, AMF, SMF, AUSF, UDM, UDR, PCF, NSSF, BSF, UPF. NF-urile ruleaza ca servicii/executabile Linux in VM-uri.
- RAN si UE: UERANSIM; un singur gNB; o singura gazda cu mai multe interfete de retea emuleaza mai multe UE (Sec. II). Numarul exact de UE nu este specificat.
- Open5GS fara NAT in reteaua privata; trafic UE incapsulat GTP catre UPF, care ofera conectivitate la Internet pentru aplicatii-exemplu.
- Colectare: 138 minute, 171,821 pachete capturate (Sec. III); port mirroring pe VM-urile sursa catre o gazda centrala. Set de date public: https://github.com/Western-OC2-Lab/5G-Core-Networks-Datasets. Pachetele de control-plane intre NF.

## Experimente si metrici
- Statistici de pachete de control per pereche NF-NF, ca heatmap-uri: lungime medie (Fig. 2), lungime maxima (Fig. 3), deviatie standard (Fig. 4), numar de pachete (Fig. 5, scala logaritmica) (Sec. IV-A).
- Distributia lungimii pachetelor cu NRF ca sursa (Fig. 6) si ca destinatie (Fig. 7) (Sec. IV-B).
- Clustering k-Means cu k=3, 5, 7 afisat in Fig. 8, 9, 10 (Sec. IV-C). Nu se raporteaza metrici de calitate a clusterelor (de exemplu silhouette); evaluarea este interpretativa.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Mesajele de la NF catre NRF au lungime medie mai mare decat cele de la NRF catre NF, atribuita inregistrarii initiale (PUT cu obiect JSON) (Fig. 2).
- Cele mai multe pachete sunt interactiunile NF-NRF, din heartbeat-ul periodic; interactiunea SMF/UPF are si ea multe pachete (UDP, PFCP, heartbeat periodic) (Fig. 5).
- Deviatie standard mare pentru AMF/SMF, atribuita stabilirii sesiunii PDU initiale si modificarilor ulterioare (Fig. 4).
- Asimetrii la perechile PCF-AMF si AMF-SMF, explicate prin crearea politicii individuale si prin raspunsul SMF cu informatie limitata (Sec. IV-A).
- Distributii NRF (Fig. 6, 7): doua varfuri pentru majoritatea NF (AMF si SMF mai putin pronuntate): varful stang corespunde confirmarilor TCP ACK, cel drept raspunsului HTTP 204 la heartbeat (NRF ca sursa) sau cererii PATCH heartbeat (NRF ca destinatie).
- Clustering: k=3 (Fig. 8) - clusterul 2 include toate interactiunile NF-NRF si UPF-SMF (multe pachete); clusterul 1 include perechile fara pachete, dar si SMF-UDM, ceea ce autorii interpreteaza ca indicand ca k=3 nu e ideal. k=5 (Fig. 9) - clusterul 1 contine doar perechile fara pachete; impartirile noi se coreleaza cu lungimea maxima a pachetelor (Fig. 3). k=7 (Fig. 10) - clusterul NF-NRF din k=3 se imparte in trei; un cluster contine AMF/PCF si AMF->SMF unidirectional.
- Singurele cifre numerice in text: 138 minute, 171,821 pachete; restul valorilor sunt in heatmap-uri.

## Limitari declarate de autori
- k-Means: performanta depinde de initializare; de aceea clusteringul a fost rulat de mai multe ori (Sec. III).
- k=3 nu este un numar ideal de clustere (Sec. IV-C).
- Din motive de concizie, sunt prezentate doar unele rezultate de clustering (Sec. IV-C).
- Lucrari viitoare: emularea completa a serviciilor NWDAF conform 3GPP (inclusiv ML model provisioning si analytics info), forecasting si management proactiv (Sec. VI).
- Se afirma ca prototipul are capabilitate de closed-loop automation, dar nu este implementata o bucla in aceasta lucrare (Sec. II).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? da - Open5GS Release 16 in VM-uri Hyper-V, plus UERANSIM (Sec. II)
- UE reale sau emulate? emulate - o gazda cu mai multe interfete de retea emuleaza UE prin UERANSIM (Sec. II)
- digital twin al retelei? nu - nu este mentionat
- prezice efectul unei actiuni inainte de a o aplica? nu - analiza descriptiva si clustering; forecasting doar ca viitor (Sec. IV, VI)
- executa actiuni automat (bucla inchisa)? nu - bucla inchisa e mentionata ca posibilitate a arhitecturii, nu demonstrata (Sec. II, V)
- multi-site / geo-redundanta / failover de baza de date? nu - un singur server fizic (Sec. II)
- evaluare prospectiva (predictie fixata inainte de experiment)? nu - nu exista predictii; analiza ex post pe captura de 138 min (Sec. III)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - statistici de pachete pe perechi NF-NF, fara metrici per UE (Sec. IV)
- observa traficul la SCP / proxy? nu - captura prin port mirroring la nivel de retea virtuala; SCP nu este mentionat (Sec. II)
