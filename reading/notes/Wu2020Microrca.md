# MicroRCA: Root Cause Localization of Performance Issues in Microservices (2020)
Cheie: Wu2020Microrca . DOI/link: https://doi.org/10.1109/noms47738.2020.9110353 . Sursa textului: integral: versiunea submitted din HAL (hal-02441640v1, depusa la 16 ianuarie 2020)
Sectiunea din plan: C . Tema: anomalii/RCA / microservicii
Autori: Li Wu, Johan Tordsson, Erik Elmroth, Odej Kao (Elastisys; TU Berlin; Umea University). IEEE/IFIP NOMS 2020, Budapesta.

## Problema (cum o formuleaza autorii)
- Diagnosticarea problemelor de performanta in microservicii este dificila (I):
  - dependente complexe (de exemplu Uber cu 4000 de microservicii);
  - numar mare de metrici (Netflix expune 2 milioane, Uber 500 de milioane);
  - servicii eterogene tehnologic;
  - actualizari frecvente.
- Abordarile existente fie cer instrumentarea aplicatiei (log, trace), fie analizeaza foarte multe metrici, fie ordoneaza cauzele dupa corelatia cu serviciile front-end. Ultimele nu gasesc serviciile back-end defecte cu impact mic asupra front-end-ului (I, II).

## Ce propun (metoda, pe scurt)
- **MicroRCA**, independent de aplicatie, pentru microservicii in containere, fara instrumentare (III, IV):
  - metrici de aplicatie (timpi de raspuns intre perechi de servicii, prin service mesh) si de sistem (container, host), stocate intr-o baza de date de serii de timp;
  - detectie de anomalii pe timpii de raspuns, cu BIRCH (clustering online nesupravegheat);
  - **graf atribuit** cu noduri de servicii si de host-uri: muchii de apel intre servicii si muchii serviciu-host pentru colocare;
  - extragerea subgrafului anormal;
  - ponderarea muchiilor cu corelatia Pearson: alpha pentru muchiile anormale; corelatia timpilor de raspuns pentru vecinii normali; corelatia maxima cu CPU, memorie, I/O si retea pentru host-uri (Algoritmul 1);
  - scorul de anomalie al serviciului combina ponderea medie cu corelatia dintre timpul de raspuns si resursele containerului;
  - ordonarea cauzelor cu Personalized PageRank.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Cluster Kubernetes in Google Cloud Engine: un nod master si patru workeri (trei pentru microservicii, unul pentru colectare), plus un server extern pentru generarea sarcinii (V.A, Tabelul I).
- Benchmark Sock-shop: 13 microservicii eterogene, REST/HTTP; fiecare cu 1 vCPU, 1 GB si o singura replica.
- Sarcina: Locust cu 500 de utilizatori si aproximativ 600 de cereri pe secunda, distribuite dupa un comportament de utilizator realist (Tabelul II).
- Colectare: Istio, Prometheus (la 5 s) si node-exporter.
- Defecte: latenta (tc), CPU hog si memory leak (stress-ng); fiecare dureaza 1 minut si este repetat de 5 ori; 95 de cazuri in total (Tabelul III).
- Baseline-uri: selectie aleatoare (RS), MonitorRank, Microscope. Toate folosesc rezultatele de detectie ale MicroRCA.

## Experimente si metrici
- PR@k (k = 1, 2, 3) si MAP pe tipuri de defect si pe servicii (Fig. 3-4, Tabelele IV-V).
- Sensibilitatea la calitatea detectiei (F1 per caz, Fig. 5), la alpha (Fig. 6) si la pragul de detectie (Fig. 7).
- Overhead (Tabelul VI).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- **Tabelul V** (per ansamblu):

| Metrica | RS | MonitorRank | Microscope | MicroRCA |
|---|---|---|---|---|
| PR@1 | 0,21 | 0,41 | 0,79 | 0,89 |
| PR@3 | 0,46 | 0,65 | 0,86 | 1,0 |
| MAP | 0,58 | 0,73 | 0,85 | 0,97 |

- Pentru defectele de latenta, PR@1 este 0,89 pentru MicroRCA, fata de 0,66 pentru Microscope.
- Fata de baseline-uri, PR@1 este cu cel putin 13% mai mare si MAP cu cel putin 15%. Imbunatatirea medie a MAP fata de MonitorRank si Microscope este 24% (V.B).
- Majoritatea serviciilor au MAP intre 80% si 100% si PR@1 mediu peste 80%; exceptiile sunt shipping si payment (servicii putin solicitate si non-compute-intensive) (Fig. 3).
- Cu F1 de detectie sub 0,4, MicroRCA pune 13 din 18 defecte pe primul loc (Fig. 5).
- **Overhead** (Tabelul VI): colectarea datelor consuma 0,6 vCPU si 1511 MB RAM; detectia dureaza 0,01 s, construirea grafului 3,3 s si localizarea 0,03 s (8 nuclee).
- Alpha optim este 0,55; MAP ramane peste 96% pentru alpha intre 0,15 si 1,0 (Fig. 6).

## Limitari declarate de autori
- Se aplica doar anomaliilor care se manifesta ca timp de raspuns crescut (V.A).
- Overhead-ul colectarii de date este "a little high"; autorii vor sa exploreze unelte de monitorizare mai usoare (V.D).
- Alpha trebuie ajustat in functie de modulul de detectie folosit (V.D).
- Precizie mai mica pentru serviciile cu putine cereri sau non-compute-intensive (V.B).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - benchmark Sock-shop pe Kubernetes (V.A).
- UE reale sau emulate?: nu se aplica - utilizatori web emulati cu Locust (V.A).
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu.
- executa actiuni automat (bucla inchisa)?: nu - localizare in timp real, fara mitigare.
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu - PR@k si MAP pentru localizare.
- observa traficul la SCP / proxy?: partial - timpii de raspuns intre servicii sunt colectati prin service mesh-ul Istio (proxy-uri side-car); nu este SCP 3GPP (V.A).
