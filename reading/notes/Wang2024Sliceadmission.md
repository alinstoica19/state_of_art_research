# Digital twin-assisted flexible slice admission control for 5G core network: A deep reinforcement learning approach (2024)
Cheie: Wang2024Sliceadmission . DOI/link: https://doi.org/10.1016/j.future.2023.12.018 . Sursa textului: integral: PDF urcat de autor (1-s2.0-S0167739X23004806-main.pdf)
Sectiunea din plan: A . Tema: digital twin
Autori: Jiadai Wang, Jingyi Li, Jiajia Liu (Northwestern Polytechnical University; Xidian University). Future Generation Computer Systems 153 (2024) 467-476.

## Problema (cum o formuleaza autorii)
Resursele core-ului 5G sunt limitate, iar operatorul trebuie sa accepte sau sa respinga cereri de slice pentru a-si maximiza venitul. Autorii observa ca lucrarile existente trateaza doar acceptarea sau respingerea completa a unei cereri si rareori admiterea partiala. Slice-urile best-effort tolereaza o reducere a resurselor cerute. In plus, un agent DRL antrenat direct in reteaua fizica produce multe decizii neoptime in faza de explorare, cu impact asupra functionarii retelei (Sectiunea 1).

## Ce propun (metoda, pe scurt)
- **Schema FSAC (flexible slice admission control):** bazata pe Deep Q-Learning (DQL), cu experience replay si retea tinta. Admite partial cererile de slice; un factor de scalare λn (0 < λn ≤ 1) limiteaza cat pot fi reduse resursele cerute.
  - Starea include resursele ramase, starea cererilor, proportiile de admitere si venitul curent (dimensiune 3 + 2W).
  - Actiunea creste, scade sau pastreaza proportia de admitere a fiecarei cereri din fereastra de procesare de marime W.
  - Recompensa este venitul de desfasurare a slice-urilor (Sectiunea 3).
- **Incercarea de desfasurare a slice-ului:** doua variante.
  - Fina, la nivel de VNF (Algoritmul 2, greedy): nodul cu cele mai multe resurse de procesare plus cel mai scurt drum pentru fiecare link virtual.
  - Grosiera, la nivel de resource pool.
- **Cadru digital twin in trei planuri** (planul entitatilor fizice, planul DT, planul aplicatiilor), cu referire la draft-urile IETF despre digital twin network (Fig. 1).
  - Planul DT contine un modul data warehouse (CPU pe noduri, bandwidth pe link-uri), un model de baza (graful topologiei) si un model functional, in care ruleaza agentul DRL.
  - Agentul exploreaza in DT; configuratia rezultata este transmisa apoi planului fizic (Sectiunea 2.2).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Simulare programatica in Python 3.9 si PyTorch. Autorii declara ca adopta simularea programatica in locul unei platforme DT reale (Sectiunea 3.4).
- Trei tipuri de slice, toate cu AMF, SMF si UPF:
  - eMBB: 2 AMF, 1 SMF, 1 UPF;
  - URLLC: 1 AMF, 1 SMF, 1 UPF plus 4 VNF de backup;
  - mMTC: 3 AMF, 1 SMF, 1 UPF.
- Cerintele de resurse:
  - procesare: 10 unitati per VNF si 5 per VNF de backup;
  - transmisie per link virtual: 3 / 2 / 1 unitati pentru eMBB / URLLC / mMTC;
  - λ = 0,7 / 1 / 0,5; profit per slice 2 / 1,5 / 1 (Sectiunea 4.1).
- Sosiri de cereri Poisson cu rata 0,1 si tip aleator.
- Sase topologii din Topology Zoo: Arpanet (4 noduri), Getnet (7), Abilene (11), Easynet (19), Arn (30), Cesnet (52). Getnet este implicita.
- Valori implicite: 25 unitati de procesare per nod, 20 unitati per link, W = 5.
- DQL (Tabelul 1):
  - 2 straturi ascunse x 50 neuroni;
  - mini-batch 256, replay memory 1000, actualizarea retelei tinta la 200;
  - learning rate 0,001, discount 0,8, ε scazut de la 1 la 0,1.
- Rezultatele sunt medii pe 10 rulari cu 1000 de episoade fiecare (cu exceptia Fig. 8).

## Experimente si metrici
- Metrici: slice acceptance ratio (Ec. 1), slice deployment revenue (Ec. 2) si blocking ratio of unacceptable decisions (Ec. 3).
- Sunt comparate patru scheme: FSAC (coarse), FSAC (fine), RLCAC (admitere completa bazata pe DRL, inspirata din [6]) si FCFS.
- Parametrii variati:
  - capacitatea de procesare (Fig. 3) si de transmisie (Fig. 4);
  - marimea ferestrei W (Fig. 5);
  - factorul de castig aditional (Fig. 6);
  - topologia (Fig. 7a: 25 unitati per nod; Fig. 7b: 200 unitati totale impartite egal);
  - convergenta cu schimbari de mediu la episoadele 1500 si 3000 (Fig. 8);
  - blocking ratio in primele 500 de episoade (Fig. 9). O decizie e considerata inacceptabila daca obtine sub 70% din venitul optim.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Venitul si rata de acceptare cresc cu capacitatea, apoi se stabilizeaza. FSAC are venit si rata de acceptare mai mari decat RLCAC si FCFS (Fig. 3-4), iar FSAC (coarse) e peste FSAC (fine). Rezultatele sunt date doar grafic.
- La rata de acceptare similara, RLCAC obtine venit mai mare decat FCFS (Fig. 3-4).
- Fig. 7b, cu 200 unitati totale:
  - in topologia de 52 noduri revin aproximativ 3,85 unitati per nod, iar majoritatea schemelor devin ineficiente;
  - in topologia de 19 noduri revin aproximativ 10,53 unitati per nod si venitul este relativ mare.
- Schema converge rapid si se readapteaza dupa schimbarile de la episoadele 1500 si 3000 (Fig. 8).
- Ratele deciziilor inacceptabile in faza de explorare sunt peste 25% la toate capacitatile testate (Fig. 9). Autorii prezinta aceasta valoare ca argument pentru explorarea in DT.

## Limitari declarate de autori
- Construirea unui mediu DT este costisitoare si depinde de date deschise, in timp real si de calitate. Datele reale ridica riscuri de confidentialitate si securitate, iar DT nu are inca un standard industrial larg acceptat (Sectiunea 3.4).
- Lucrarea se concentreaza pe caracteristicile generale ale DT, nu pe implementare, si foloseste simulare programatica.
- Safe RL si offline RL sunt discutate ca alternative pe care autorii le considera nepotrivite pentru obiectivul lor (Sectiunea 3.4).
- Ca lucrari viitoare, autorii propun conditii mai complexe si o platforma DT construita pe retele si echipamente reale (Sectiunea 5).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - Sectiunea 3.4 si 4.1: simulare programatica; NF-urile sunt modelate ca VNF cu unitati de resurse.
- UE reale sau emulate?: nu - Sectiunea 4.1: doar cereri de slice generate Poisson.
- digital twin al retelei?: da (cadru conceptual simulat) - Sectiunea 2, Fig. 1.
- prezice efectul unei actiuni inainte de a o aplica?: da (in sensul explorarii DRL in DT inainte de aplicarea configuratiei pe reteaua fizica) - Sectiunea 2.2.
- executa actiuni automat (bucla inchisa)?: da (in simulare: agentul DRL decide admiterea si alocarea) - Sectiunea 3.3.
- multi-site / geo-redundanta / failover de baza de date?: nu - backup-uri de VNF modelate doar ca resurse pentru URLLC (Sectiunea 4.1), fara failover evaluat.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu - metricile sunt la nivel de cereri de slice si venit.
- observa traficul la SCP / proxy?: nu.
