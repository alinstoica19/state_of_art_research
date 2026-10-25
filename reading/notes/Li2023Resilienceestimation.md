# Estimating 5G Network Service Resilience Against Short Timescale Traffic Variation (2023)
Cheie: Li2023Resilienceestimation . DOI/link: https://doi.org/10.1109/tnsm.2023.3269673 . Sursa textului: integral: versiunea autorilor pe HAL (hal-04112527v1, depusa la 31 mai 2023)
Sectiunea din plan: C . Tema: rezilienta / model Petri / autoscaling
Autori: Rui Li, Bertrand Decocq, Anne Barros, Yi-Ping Fang, Zhiguo Zeng (CentraleSupelec si colaboratori, dupa biografii). IEEE Transactions on Network and Service Management, vol. 20, nr. 3, septembrie 2023.

## Problema (cum o formuleaza autorii)
- Variatia traficului este una dintre cele mai importante amenintari pentru rezilienta serviciilor 5G. Traficul pe termen lung poate fi prezis din date istorice; cel anormal pe termen scurt (secunde: DDoS, flash mobs, evenimente neprevazute) este greu de prezis si poate incalca cerintele de serviciu (I).
- Testarea pe o retea reala cu mii de utilizatori nu este practica, deci autorii propun simularea pe un model. Dupa autori, putine lucrari trateaza variatia de trafic pe termen scurt (I).

## Ce propun (metoda, pe scurt)
- **Model Petri Net ierarhic** al unei retele 5G virtualizate, cu procesarea pachetelor in microservicii (DU, CU, UPF), cozi limitate, management dinamic al microserviciilor si un NFV-MANO bazat pe Kubernetes, cu HPA (IV, Tabelele I-III).
- **Metrici** (V):
  - latenta end-to-end;
  - fiabilitatea serviciului (procentul de cereri nerespinse si cu intarziere sub cerinta), pe intervale de timp;
  - pierderea de rezilienta: aria degradarii fiabilitatii in timp (triunghiul de rezilienta Bruneau, Fig. 6);
  - costul resurselor: unitati CPU x secunde per pod.
- **Strategii comparate:**
  - fara autoscaling (No AS);
  - autoscaling HPA pe prag, verificat la 5 s (Basic AS);
  - HPA cu fereastra de stabilizare de 15 s (Win.AS);
  - izolare: prioritizare, slicing cu UPF dedicat cu resurse dublate, slicing cu aceleasi resurse totale.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Simulare cu evenimente discrete in Python/SimPy, Monte Carlo cu 2000 de rulari de 60 s (VI).
- Retea complet virtualizata cu doua servicii uplink pe acelasi lant DU-CU-UPF (Fig. 7):
  - serviciul 1: sensibil la latenta, pachete mici;
  - serviciul 2: IoT, cu cerinta de latenta mai relaxata.
- Parametri simplificati (Tabelele IV-V): 20 de unitati CPU per pod DU/CU, 40 per pod UPF; timpii de procesare sunt fixi.
- Patru tipare de trafic dupa t = 18 s: variatie constanta pe termen lung, variatie scurta, doua tipare fluctuante (Fig. 8). Serviciul 1 are mereu de doua ori rata serviciului 2.
- Cazul 2 (izolare): patru RAN locale si un CN centralizat; in zonele 2-4, utilizatorii serviciului 2 isi tripleaza traficul timp de 10 s.

## Experimente si metrici
- Cazul 1: latenta, fiabilitatea, pierderea de rezilienta si costul pentru No AS / Basic AS / Win.AS sub cele patru tipare (Fig. 9-15).
- Cazul 2: aceleasi metrici pentru fara izolare / prioritizare / doua variante de slicing (Fig. 16).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- **Variatie lunga:** Basic AS adauga imediat instante si controleaza congestia la aproximativ 20 s; Win.AS rezolva congestia mai incet; No AS are pierdere mare de rezilienta, mai ales pentru serviciul 1 (Fig. 9). Tinand cont de cost, autorii considera Win.AS cea mai economica solutie.
- **Variatie scurta:** Win.AS si No AS se comporta aproape la fel, cu congestie de aproximativ 5 s; Basic AS reduce congestia la aproximativ 2 s, dar foloseste cu aproximativ un sfert mai multe resurse (Fig. 10).
- **Trafic fluctuant:** Basic AS are rezilienta mai slaba decat No AS si cel mai mare cost; Win.AS este cel mai bun ca rezilienta, dar aproape de No AS (Fig. 11-12).
- **Izolare (cazul 2):** prioritizarea reduce mult pierderea de rezilienta a serviciului critic fara resurse suplimentare; slicing-ul cu resurse dublate protejeaza ambele servicii, cu aproximativ un sfert mai multe resurse; slicing-ul cu aceleasi resurse totale creste pierderea de rezilienta, din cauza marjelor mai mici (Fig. 16).
- Autorii prezinta modelul ca primul care estimeaza rezilienta serviciilor pe scara de timp scurta (VII).

## Limitari declarate de autori
- Parametrii sunt simplificati si fixi; timpii de procesare reali sunt greu de extras din teste end-to-end (VI, VII).
- Kubernetes este presupus fiabil; daca ar cadea, Basic AS si Win.AS s-ar comporta ca No AS (VI.A).
- Control plane-ul (semnalizarea) nu este modelat; este lucrare viitoare, de exemplu pentru trenuri de mare viteza (VII).
- Modelul este folosit offline. Autorii mentioneaza posibila integrare cu NWDAF pentru estimare in timp real si testarea pe o retea reala virtualizata, cand va fi disponibila (VII).
- Analiza de sensibilitate globala nu este facuta (VII).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - model Petri Net simulat (DU, CU, UPF; fara NF-uri de control plane) (IV, VI).
- UE reale sau emulate?: simulate - trafic generat stocastic (VI).
- digital twin al retelei?: nu - model de simulare offline; autorii mentioneaza doar posibila integrare in timp real cu NWDAF (VII).
- prezice efectul unei actiuni inainte de a o aplica?: da (offline) - modelul estimeaza pierderea de rezilienta si costul pentru strategii alternative de autoscaling si izolare (VI).
- executa actiuni automat (bucla inchisa)?: da (in simulare) - HPA din Kubernetes este modelat ca bucla de scalare (VI.A).
- multi-site / geo-redundanta / failover de baza de date?: partial - patru RAN locale si un CN centralizat in cazul 2 (VI.B); failover nu este modelat.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: partial - fiabilitatea si latenta serviciului per pachet, in simulare; nu inregistrari sau sesiuni (V).
- observa traficul la SCP / proxy?: nu.
