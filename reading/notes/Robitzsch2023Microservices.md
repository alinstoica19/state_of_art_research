# Prospects on the adoption of a microservice-based architecture in 5G systems and beyond (2023)
Cheie: Robitzsch2023Microservices . DOI/link: https://doi.org/10.1016/j.comnet.2023.110058 . Sursa textului: integral: Zenodo record 10554682 (acces deschis; manuscris marcat "Preprint submitted to Computer Networks", 6 decembrie 2023)
Sectiunea din plan: C . Tema: SBA/selectie NF (microservicii in 5GC)
Autori: Sebastian Robitzsch (InterDigital Europe), Marco Centenaro, Nicola di Pietro, Arif Ishaq (Athonet/HPE), Luis Cordeiro, Andre S. Gomes (OneSource), Peter Sanders (Everbridge). Computer Networks vol. 237, 2023, art. 110058.
Tip: lucrare de pozitie si arhitectura, cu trei exemple de descompunere implementate; fara evaluare cantitativa.

## Problema (cum o formuleaza autorii)
- Lucrarea discuta adoptarea conceptelor de microservicii si cloud-native in reteaua mobila. Autorii sustin ca este nevoie de o adaptare netriviala a core-ului 5G si de reproiectarea NF-urilor ca microservicii (Rezumat).
- Serviciile NF definite de 3GPP nu sunt complet compatibile cu definitia microserviciilor: responsabilitatile serviciilor 3GPP nu sunt independente si unele sunt duplicate. De aceea maparea 1:1 serviciu-3GPP -> microserviciu nu functioneaza (Sectiunea 4).

## Ce propun (metoda, pe scurt)
- **Criterii de descompunere** (3.1; discutate si in proiectul NGMN ODIN):
  - mitigarea bottleneck-urilor si executie paralela;
  - rezilienta: functiile cu cerinte de inalta disponibilitate izolate in microservicii dedicate;
  - dependenta de stare.
- Pentru securitate: JWT si DevSecOps.
- Un API Gateway, ca microserviciu separat in fiecare NF, expune SBI-ul 3GPP (compatibilitate cu standardul) si izoleaza microserviciile interne (Sectiunea 4).
- **Trei exemple de descompunere**:
  - **UDM:** Authorisation Service, UE Context Service, Monitoring & Notification Service plus API Gateway. Microserviciile nu partajeaza date; UDR extern este optional (4.1, Fig. 2).
  - **NEF:** API Gateway stateless plus UE Communication Policies, Subscription & Notification si IoT & Low-power Communication (4.2, Fig. 3).
  - **CBCF:** Ingest API stateless, CB Kernel, Cell Selection, drivere 2G/3G/4G/5G si gestionarea subscrierilor la AMF/NRF (4.3, Fig. 4).
- **Viziune beyond-5G** (Sectiunea 5, Fig. 5):
  - SCP-ul (Model C/D) ar inlocui service bus-ul 5GC si poate si bus-ul intern al NF-urilor;
  - interfetele N2/N4 ar fi rutate tot prin SCP;
  - SCP cu Name-Based Routing, cu FQDN-uri de forma nf.domeniu-parinte (de exemplu nrf.foo.com).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Cele trei NF-uri au fost implementate si testate la TRL 8 in proiectul FUDGE-5G (4).
- UDM: prototip folosit intr-un demonstrator de provizionare la cerere a unui Network Slice Subnet, cu SBMA 3GPP, orchestrator ETSI MANO si NFVI [19].
- NEF: teste de stres preliminare (cereri de schimbare a politicii QoS de la AF la PCF), comparand microservicii consolidate pe o masina cu microservicii distribuite (cate unul pe masina). Rezultatele nu sunt detaliate in lucrare (4.2).
- CBCF: integrat cu core-ul Cumucore 5GC si demonstrat la Telenor (Norvegia) cu aproximativ zece telefoane 5G de cateva marci (4.3).

## Experimente si metrici
Nu sunt raportate metrici cantitative. Sunt descrise demonstratii functionale si un test preliminar nedetaliat.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- CBCF: telefoanele au afisat mesajul de avertizare la cateva secunde dupa initierea lui (4.3).
- NEF: testele preliminare au aratat diferente de performanta intre configuratii, nedetaliate (4.2).

## Limitari declarate de autori
- Descompunerea poate creste complexitatea dezvoltarii (multe interfete interne, sisteme complexe de distributie a evenimentelor) si suprafata de atac (3.2).
- O analiza exhaustiva a tuturor NF-urilor nu este fezabila; sunt alese trei exemple (4).
- Arhitectura beyond-5G necesita standardizarea denumirilor, a inregistrarii la SCP, a izolarii si a QoS (5).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - NF-uri descompuse implementate si integrate cu un 5GC comercial (Cumucore), la TRL 8 (4.3).
- UE reale sau emulate?: reale - aproximativ zece telefoane 5G in demonstratia CBCF (4.3).
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu.
- executa actiuni automat (bucla inchisa)?: nu.
- multi-site / geo-redundanta / failover de baza de date?: nu evaluat; rezilienta este un criteriu de descompunere (3.1), iar segmentarea datelor in deployment-uri distribuite este discutata (3.2).
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: partial - receptia avertizarii pe telefoane, calitativ (4.3).
- observa traficul la SCP / proxy?: discutat conceptual - SCP ca service bus beyond-5G (Sectiunea 5); nu este evaluat.
