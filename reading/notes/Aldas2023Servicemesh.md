# Cloud-Native Service Mesh Readiness for 5G and Beyond (2023)
Cheie: Aldas2023Servicemesh . DOI/link: https://doi.org/10.1109/access.2023.3335994 . Sursa textului: integral: versiunea publicata (IEEE Access, acces deschis CC BY-NC-ND 4.0; https://ieeexplore.ieee.org/ielx7/6287639/6514899/10327727.pdf, prin Unpaywall)
Sectiunea din plan: C . Tema: SBA/selectie NF (SCP, service mesh)
Autori: Saidulu Aldas (Intel), Andrew Babakian (VMware). IEEE Access, 2023.

## Problema (cum o formuleaza autorii)
- SBA-ul 5G aduce un volum mare de mesaje intre servicii, iar gestionarea cererilor si rezilienta devin dificile.
- Comunicarea directa intre NF-uri a dus la overhead, latente mai mari, lipsa load balancing-ului si a observabilitatii unificate (I).
- SCP-ul (Rel-16) este definit de 3GPP ca ghid si protocol, nu ca implementare; vendorii trebuie sa-l realizeze.
- Lucrarea examineaza service mesh-ul ca mijloc de a prelua functionalitatea SCP si extensiile necesare pentru semantica 5G (I).

## Ce propun (metoda, pe scurt)
- Ghid arhitectural pentru extinderea service mesh-ului (Istio ca control plane, Envoy ca data plane) pentru semnalizarea core-ului 5G. Extensiile 5G sunt in proxy-ul Envoy (Sectiunile III-IV).
- Trei scenarii de deployment (V):
  1. comunicare directa fara SCP (NF -> NRF -> NF);
  2. SCP standalone, ca microserviciu separat cu proxy Envoy centralizat;
  3. SCP ca filtru WASM in sidecar-ul Envoy, in acelasi pod cu NF-ul; descoperirea si comunicarea se fac in pod.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- free5GC: AMF, SMF, PCF, AUSF, NSSF, UPF, UDM, UDR plus MongoDB.
- UERANSIM ca generator de sarcina: procedura de deregistration trimite SCTP catre AMF, iar AMF comunica pe SBI prin HTTP/2.
- Istio/Envoy cu extensii 5G; un singur cluster Kubernetes (Docker); pentru scenariul 3, sidecar Envoy in fiecare pod de NF.
- Hardware: doua servere Intel Xeon Scalable generatia 3, conectate prin 100G.
- Latenta este masurata intre UDM si UDR (V).
- Numarul de UE si de repetari nu este declarat.

## Experimente si metrici
Latenta de descoperire si de comunicare intre NF-uri (UDM-UDR) in cele trei scenarii (Tabelul 1).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Tabelul 1 este o imagine in PDF; valorile numerice nu sunt disponibile ca text.
- Scenariul 2 (SCP centralizat) are latente mai mari decat scenariul 3 (SCP in pod) si cere mai multa memorie si calcul.
- Autorii afirma ca scenariul 3 atinge latente sub-milisecunda, conform cerintelor 3GPP TS 22.261 §6.4.2.1 si Anexa A.

## Limitari declarate de autori
Nu sunt declarate limitari explicite. Sectiunea VI enumera directii viitoare:
- descoperire specifica pe network slice (NSSAI), cu Global Namespace per slice si un NRF comun pentru mai multe slice-uri;
- semantica de descoperire specifica domeniului 5G (coduri de eroare 3GPP, raspunsuri adaptate fiecarui consumator, mai multe candidate);
- descoperire low-latency care tine evidenta latentei si sarcinii NF-urilor destinatie;
- tratarea mesajelor 5G custom: header-ele 3gpp-Sbi-Oci (notificari de overload) si 3gpp-Sbi-Message-Priority, pentru load balancing constient de 5G si congestion control.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - free5GC (V).
- UE reale sau emulate?: emulate - UERANSIM (V).
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu.
- executa actiuni automat (bucla inchisa)?: nu; load balancing-ul pe baza 3gpp-Sbi-Oci este propus ca extensie viitoare (VI).
- multi-site / geo-redundanta / failover de baza de date?: nu - un singur cluster; GNS peste mai multe medii/cloud-uri este discutat conceptual (VI).
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu - latenta UDM-UDR in procedura de deregistration.
- observa traficul la SCP / proxy?: da - SCP implementat in service mesh (Envoy), standalone sau ca sidecar (V).
