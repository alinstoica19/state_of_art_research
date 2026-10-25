# Petri Net-Based Model for 5G and Beyond Networks Resilience Evaluation (2022)
Cheie: Li2022Petrinet . DOI/link: https://doi.org/10.1109/icin53892.2022.9758134 . Sursa textului: integral: versiunea autorilor pe HAL (hal-03648310v1)
Sectiunea din plan: C . Tema: rezilienta / disponibilitate / model Petri
Autori: Rui Li, Bertrand Decocq, Anne Barros, Yiping Fang, Zhiguo Zeng (Orange; Laboratoire Genie Industriel, CentraleSupelec, Universite Paris-Saclay). ICIN 2022.

## Problema (cum o formuleaza autorii)
- NFV in RAN si core aduce riscuri noi, iar rezilienta nu mai priveste doar infrastructura, ci si elementele virtuale si livrarea serviciilor. Dupa autori, rezilienta 5G nu a fost studiata suficient (I).
- Metodele de evaluare existente (diagrame bloc de fiabilitate, lanturi Markov) nu modeleaza impreuna infrastructura, virtualizarea, nivelurile retelei si dependentele dintre ele. Virtualizarea bazata pe containere este rar modelata (II).

## Ce propun (metoda, pe scurt)
- **Timed Stochastic Colored Petri Net (TSCPN)** pentru o retea 5G pe trei niveluri (III):
  - nivelul serviciilor: SFC-ul, cu pachete ca tokeni, transport si procesare;
  - nivelul elementelor NFV: VNF-uri descompuse in microservicii in containere/pod-uri (Kubernetes), cozi de pachete, selectia serviciului prin functii de garda;
  - nivelul infrastructurii: servere fizice si legaturi, cu resurse.
- **Self-healing Kubernetes modelat:** probe de liveness, terminarea pod-urilor defecte si crearea altora pe noduri cu resurse disponibile (Fig. 5). Defecte de pod (software) si de nod (fizic), cu distributie exponentiala.
- Autoscaling-ul este lasat pentru lucrari viitoare.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Simulare Monte Carlo in CPN Tools: 20.000 de iteratii, fiecare acoperind 50 de ani de functionare. Rularea dureaza intre o jumatate de ora si doua ore pe un PC cu Windows 10, CPU 2,10 GHz, 8 GB (IV).
- Un VNF cu doua microservicii, fiecare cu trei replici initiale, intr-un data center (IV, Tabelul I):
  - MTTF pod 1258 h, MTTF nod 8760 h, MTTR nod 0,5 h;
  - terminarea unui pod 30 s, instantierea unui pod 5 s, crearea unui nod 1 s;
  - 3 pod-uri per nod, 4 servere;
  - perioada probei de self-healing: 0 (imediat), 2, 5 si 10 s.

## Experimente si metrici
- Disponibilitatea unui microserviciu: fractiunea de timp in care numarul de pod-uri disponibile este cel putin numarul dorit de replici.
- Disponibilitatea VNF-ului: ambele microservicii cu cel putin trei replici (Fig. 6).
- Efectul perioadei probei asupra disponibilitatii (Fig. 7).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Cu detectie imediata si trei replici dorite, disponibilitatea unui microserviciu este 99,9996712% ("5 nines"). Cu o replica dorita (si trei initiale), disponibilitatea ajunge la "9 nines" (Fig. 6).
- Disponibilitatea VNF-ului este 99,9993523%, cu IC 95% [99,9993520304%, 99,9993526071%] (IV).
- Cu proba la 10 s, disponibilitatea VNF-ului scade la 99,9987198% ("4 nines"), cu IC 95% [99,9987192945%, 99,9987202301%] (Fig. 7). Autorii sugereaza ca perioada probei poate fi optimizata pentru a economisi energie, respectand cerinta de disponibilitate.

## Limitari declarate de autori
- Rezultatele sunt descrise ca optimiste, pentru ca nu sunt luate in calcul defectele de retea si mentenanta (V).
- Parametrii trebuie rafinati cu date de la experti si furnizori (V).
- Lucrari viitoare: autoscaling, extinderea de la un VNF la un SFC complet, un caz real din verticale (V).
- Reteaua de transport este presupusa perfect fiabila (III.B).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - model Petri Net al unui VNF generic cu microservicii (III, IV).
- UE reale sau emulate?: nu se aplica - pachetele sunt modelate ca tokeni; studiul de caz nu foloseste trafic de utilizator (IV).
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: da (offline) - estimeaza disponibilitatea pentru diferite configuratii de replici si de perioada a probei (IV).
- executa actiuni automat (bucla inchisa)?: da (in simulare) - self-healing-ul Kubernetes este modelat (III.D.4).
- multi-site / geo-redundanta / failover de baza de date?: nu - un singur data center (IV).
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu - disponibilitatea microserviciilor si a VNF-ului.
- observa traficul la SCP / proxy?: nu.
