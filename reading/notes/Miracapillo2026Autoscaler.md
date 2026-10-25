# Enabling Energy-Efficient Kubernetes Cluster Autoscaler (2026)
Cheie: Miracapillo2026Autoscaler . DOI/link: https://doi.org/10.1109/noms69089.2026.11668314 . Sursa textului: integral: versiunea acceptata a autorilor din repository-ul IRIS al Politecnico di Torino (handle 11583/3015814)
Sectiunea din plan: C . Tema: energie / autoscaling Kubernetes bare-metal
Autori: Riccardo Miracapillo, Stefano Galantino, Attilio Oliva, Fulvio Risso (Politecnico di Torino). IEEE NOMS 2026, Roma; lucrare demo de 3 pagini.

## Problema (cum o formuleaza autorii)
- In clusterele bare-metal subutilizate se iroseste energie, iar oprirea serverelor ar reduce costurile. Alegerea serverului de oprit este o problema complexa de optimizare: o alegere gresita poate satura resursele si compromite disponibilitatea (Rezumat, I).
- Cluster Autoscaler este reactiv si nu tine cont de timpul mare de pornire al serverelor bare-metal; Karpenter este limitat la ecosistemele furnizorilor cloud. Lucrarile de consolidare energetica tratează mai ales VM-uri ca "black box", fara a distinge sarcinile critice de cele "disposable" (I).
- Autoscaling-ul curent nu are "context awareness": cerintele aplicatiilor, logica de orchestrare si constrangerile fizice nu sunt integrate (I).

## Ce propun (metoda, pe scurt)
- **DREEM** (Dynamic node REallocation for Energy-optiMized Kubernetes clusters), cu trei controllere Kubernetes (II, Fig. 1):
  1. **Decizia de scalare**, dupa utilizarea medie a CPU:
     - reactiv: media pe ultimele N minute, comparata cu praguri;
     - predictiv: LSTM antrenat pe Alibaba Cluster Trace, pentru a compensa timpul de pornire a serverelor (pana la 20 de minute).
  2. **Selectia nodului**:
     - constrangeri dure, verificate printr-o simulare de scheduling, ca toate pod-urile de pe nodul candidat sa poata fi reprogramate;
     - constrangeri soft: afinitati, numarul de replici pe nod, Power Cycles (numarul cumulat de reporniri, ca masura a degradarii hardware) si Energy Profile (derivat din metrica WAP, normalizat pe nuclee, din date BMC si Prometheus) (Tabelul I);
     - problema MCDA: ponderi AHP si clasament TOPSIS; profilul ales (performance, balanced, energy) modifica ponderile.
  3. **Executia**: adaugarea sau eliminarea nodului prin ClusterAPI (cu Metal3 pentru bare-metal), inclusiv join/drain.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Demonstratie pe un cluster Kubernetes cu un nod de control si trei workeri (2x Xeon Gold 6442Y, 512 GB RAM fiecare) (III).
- Praguri: utilizare medie CPU intre 40% si 75%. Sarcina: aplicatie de microservicii µBench, scalata cu HPA, trafic generat cu Locust. Trei scenarii: scale-up, scale-down, fara scalare.

## Experimente si metrici
- Utilizarea medie a CPU in functie de numarul de workeri activi (Fig. 2); demonstrarea alegerii nodului optim.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Lucrarea nu raporteaza cifre de consum energetic sau de performanta. Rezumatul afirma calitativ ca DREEM reduce numarul mediu de noduri active si consumul de energie fara a compromite performanta si ca alege servere aproape optime conform constrangerilor.

## Limitari declarate de autori
- Lucrari viitoare (IV): selectie tinand cont de dependentele dintre servicii, integrare cu stocarea hiperconvergenta, includerea criticitatii serviciilor pentru pastrarea QoS in timpul scalarii.
- Lucrarea este o demonstratie pe un cluster mic, fara evaluare cantitativa.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - aplicatie de microservicii generica (µBench) pe Kubernetes (III).
- UE reale sau emulate?: nu se aplica - trafic HTTP generat cu Locust (III).
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: partial - o simulare de scheduling verifica, inainte de oprirea nodului, ca pod-urile pot fi reprogramate; LSTM-ul prezice sarcina, nu efectul actiunii (II.A-B).
- executa actiuni automat (bucla inchisa)?: da - pornirea si oprirea automata a nodurilor bare-metal prin ClusterAPI (II.C, III).
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu.
- observa traficul la SCP / proxy?: nu.
