# Design of an AI-driven Network Digital Twin for advanced 5G-6G network management (2024)
Cheie: Karamchandani2024B5Geminindt . DOI/link: https://doi.org/10.1109/noms59830.2024.10575106 . Sursa textului: integral: PDF urcat de autor (Design_of_an_AI-driven_Network_Digital_Twin_for_advanced_5G-6G_network_management.pdf)
Sectiunea din plan: A . Tema: digital twin
Autori: Amit Karamchandani, Mario Sanz, Angela Burgaleta, Luis de la Cal, Alberto Mozo, Jose Ignacio Moreno (UPM), Antonio Pastor, Diego R. Lopez (Telefonica I+D). 3rd International Workshop on Technologies for Network Twins (TNT 2024), workshop al NOMS 2024; 7 pagini.

## Problema (cum o formuleaza autorii)
Generarea de dataset-uri de trafic in retele operationale este limitata de restrictiile operatorilor si de confidentialitate. Emularea atacurilor cibernetice pe retele reale risca intreruperi pentru utilizatori. Dupa autori, literatura despre NDT pentru 5G/6G se concentreaza pe prototiparea in faza de design. Lucrarea propune NDT ca mediu experimental controlat pentru generarea de date sintetice si pentru antrenarea si validarea modelelor AI (Sectiunea I).

## Ce propun (metoda, pe scurt)
- **Arhitectura NDT a proiectului B5GEMINI**, cu doua straturi (Sectiunea IV, Fig. 1):
  - **stratul de aplicatii;**
  - **stratul NDT**, cu trei componente:
    - NDT Data Storage: sursa unica de adevar, conform cadrului IETF;
    - NDT Services: orchestrare NFV cu OpenStack, OSM si Kubernetes; deployment din sabloane; slice-uri sau experimente multiple; generatoare de trafic; injectie PCAP; conectivitate Internet; emulare 5G pentru transport;
    - NDT Control.
  - Straturile comunica printr-un Data Fabric care organizeaza datele intr-un knowledge graph.
- **Uneltele open-source enumerate** (II.A): Kubernetes, Kubernetes Network Emulator, Containerlab, Vrnetlab, MetaLB, free5GC, STGUTG (generator de trafic de semnalizare si de utilizator pentru core 5G), OSM, OpenStack, plus generatoare hardware.
- **Agenda AI** (III): GAN pentru date sintetice; robustete la atacuri adversariale; Green-AI si AutoML; trei cazuri de utilizare (trafic criptat de atac, VR social, multimedia cu ALTO si RL).
- **Cazul de utilizare detaliat (V):** atac DoS prin DoH (DNS over HTTPS) flooding intr-o retea 5G emulata, cu detectie ML pe statistici de flux.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Topologia (Fig. 2): control plane, data plane si gNB ca functii virtualizate conectate la reteaua de transport. Mai multi clienti sunt atasati la gNB, iar UPF-ul are conectivitate Internet. Topologia este descrisa printr-un descriptor YAML.
- Implementarea concreta de core 5G din caz nu este numita; free5GC si STGUTG apar in lista de unelte a platformei.
- Atacul consta in trafic heavy-hitter sintetic de la clienti virtualizati catre serverul DoH.
- Sunt planificate masuratori pe link-urile de transport, pe routere si de utilizare a resurselor (CPU, memorie, I/O) pe NF-urile de control si data plane.
- Pentru antrenare sunt planificate statistici de flux extrase cu Tstat si trei clase: 0 = trafic normal, 1 = DoH standard, 2 = DoH flooding (V.C).
- Numarul de UE si scara nu sunt declarate.

## Experimente si metrici
Experimentele de detectie nu sunt inca realizate. Autorii scriu ca asteapta dataset-ul generat in NDT pentru antrenare si validare (V.C). Sunt planificati arbori de decizie si retele neuronale, cu partitionare train/validation/test.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Nu sunt raportate rezultate numerice. Faza este descrisa ca exploratorie; metricile si arhitectura scenariului se pot schimba (V.B).

## Limitari declarate de autori
- Faza exploratorie: metricile si arhitectura sunt sub rezerva modificarilor (V.B).
- Scalabilitatea componentelor si a arhitecturii NDT pentru deployment-uri mari, multi-domeniu si heterogene urmeaza sa fie evaluata (VI).
- Lucrari viitoare: alte tipuri de amenintari decat DDoS si adaptare prin RL (VI).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: neclar - control/data plane virtualizate in topologia emulata (V.A); free5GC este listat ca unealta a platformei (II.A), dar nu este numit explicit in cazul de utilizare.
- UE reale sau emulate?: emulate - clienti virtualizati cu generator sintetic de trafic (V.A).
- digital twin al retelei?: da - NDT B5GEMINI (IV).
- prezice efectul unei actiuni inainte de a o aplica?: propus - mitigarile vor fi aplicate intai in NDT si transferate in reteaua reala dupa validare (V.C); neimplementat.
- executa actiuni automat (bucla inchisa)?: propus - rate limiting sau redirectionarea traficului dupa detectie (V.C); neevaluat.
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu (fara experimente).
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu.
- observa traficul la SCP / proxy?: nu.
