# B5GEMINI: Digital Twin Network for 5G and Beyond (2022)
Cheie: Mozo2022B5Gemini . DOI/link: https://doi.org/10.1109/noms54207.2022.9789810 . Sursa textului: integral: PDF urcat de autor (B5GEMINI_Digital_Twin_Network_for_5G_and_Beyond.pdf)
Sectiunea din plan: A . Tema: digital twin
Autori: Alberto Mozo, Amit Karamchandani, Mario Sanz, Jose Ignacio Moreno (Universidad Politecnica de Madrid), Antonio Pastor (Telefonica I+D). NOMS 2022; 6 pagini.
Tip: lucrare de arhitectura si viziune de proiect, fara evaluare experimentala. Sectiunile urmeaza sablonul pentru vision papers.

## Problema (cum o formuleaza autorii)
Un Digital Twin Network (DTN) permite validarea functionalitatilor noi si analiza efectului unor politici fara interactiune directa cu reteaua fizica. Modelele 5G/6G sunt complexe, deci autorii cer folosirea AI pentru auto-invatare. Ei mai observa ca lipseste cercetarea sistematica despre metodele ML potrivite pentru construirea DTN si despre interoperabilitatea lor cu restul elementelor DTN (Sectiunile I-II). Lucrarea urmareste obiectivele draft-ului IETF NMRG despre DTN (draft-zhou-nmrg-digitaltwin-network-concepts-06).

## Structura si taxonomia propusa
Proiectul B5GEMINI are doua subproiecte: B5GEMINI-INFRA (infrastructura DTN) si B5GEMINI-AIUC (componente AI si cazuri de utilizare). Arhitectura (Sectiunea III, Fig. 1) contine:
- **Intrari pentru generarea DT:**
  - automata: agenti inteligenti colecteaza topologia, hardware-ul, software-ul si starile in JSON/XML;
  - manuala: fisiere incarcate de operator.
- **Modul de deployment:** Terraform IaaS, pe orice cloud (AWS, Google Cloud, Azure, IBM) sau pe vSphere, cu o biblioteca de VM-uri si containere Docker.
- **Modul de configurare si provizionare a DT-urilor:** modeleaza fiecare DT si interconexiunile, pentru a simula reteaua 5G tinta.
- **Modul de monitorizare:** port mirroring in subretele, pentru generarea de dataset-uri.
- **Modul de generare si injectie de trafic:** pe baza modelelor de trafic 5G.
- **Pipeline-uri:** V2V (intre DT-uri) si P2V (intre DTN si reteaua fizica, bucla de feedback).
- **Modul AI/ML:** agenti care optimizeaza politicile (rutare, plasarea resurselor) sau prezic defectele. Modificarile facute in DTN sunt replicate in lumea fizica prin pipeline-ul P2V.

Platforma de baza este Mouseworld Lab de la Telefonica I+D (Sectiunea IV):
- arhitectura NFV cu NFVO, ETSI NFV MANO extins, OSM si OpenStack;
- un Topology Generator (sabloane NSD/VNFD prin interfata ETSI NFV SOL-005) si un Experiment Launcher (configurari day-2);
- doua scenarii definite: detectia malware de cryptomining si atacuri DNS.

## Lucrari/sisteme acoperite (cu numar)
- Related work trece prin aproximativ 9 lucrari despre DT/DTN cu AI. Exemple: plasarea DT prin DRL; federated learning pentru DT in IIoT; DT pentru MEC; IDT pentru retele vehiculare SDN; DTN 5G pentru orase (Sectiunea II).
- Bibliografia are 15 referinte.
- Cinci cazuri de utilizare AI pentru B5GEMINI (IV.A-E):
  1. DTN pentru aplicatii smart (trafic etichetat automat pentru antrenarea si validarea ML);
  2. ML pentru deployment-ul si configurarea DTN (inclusiv RL care propune modificari in DTN);
  3. antrenare si inferenta distribuita la cerere cu vGPU;
  4. ML as a Service;
  5. optimizarea consumului de energie.
- Cinci componente AI planificate: date sintetice cu GAN, AutoML, GNN, explicabilitate, intent-based networking.

## Directii deschise declarate
- Virtualizarea GPU depinde de tehnologie proprietara (de exemplu NVIDIA). Autorii o considera principala provocare pentru adoptie la scara si asteapta solutii mai deschise (IV.C).
- Este necesara cercetare sistematica asupra metodelor ML pentru construirea DTN (II).
- Datele sintetice generate cu GAN sunt propuse pentru problemele de confidentialitate si pentru lipsa datelor publice (IV, componenta A).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Nu exista evaluare experimentala. Este descrisa infrastructura (Terraform, VM-uri, Docker, OSM, OpenStack) si Mouseworld Lab.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Nu sunt raportate rezultate numerice.

## Limitari declarate de autori
Nedeclarate explicit, in afara dependentei de virtualizarea GPU proprietara (IV.C).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - DTN-ul trebuie sa "simuleze reteaua 5G tinta" (III.C), dar nu este numita o implementare de core 5G.
- UE reale sau emulate?: nedeclarat.
- digital twin al retelei?: da - arhitectura DTN propusa (III).
- prezice efectul unei actiuni inainte de a o aplica?: propus - modificarile facute de agentii AI in DTN sunt replicate apoi in reteaua fizica (III.G); este evaluarea politicilor in DTN (I), fara implementare raportata.
- executa actiuni automat (bucla inchisa)?: propus (III.G), neevaluat.
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu (fara experimente).
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu.
- observa traficul la SCP / proxy?: nu.
