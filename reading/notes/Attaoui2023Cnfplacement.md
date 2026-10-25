# VNF and CNF Placement in 5G: Recent Advances and Future Trends (2023)
Cheie: Attaoui2023Cnfplacement . DOI/link: https://doi.org/10.1109/tnsm.2023.3264005 . Sursa textului: integral: versiunea publicata (IEEE TNSM, acces deschis CC BY 4.0; https://ieeexplore.ieee.org/ielx7/4275028/5699970/10090468.pdf, prin Unpaywall)
Sectiunea din plan: C . Tema: SBA/selectie NF (plasarea VNF/CNF, survey)
Autori: Wissal Attaoui, Essaid Sabir, Halima Elbiaze, Mohsen Guizani. IEEE Transactions on Network and Service Management, 2023.

## Problema (cum o formuleaza autorii)
Plasarea VNF-urilor in infrastructuri de gazduire este o provocare tehnica majora. Ea influenteaza performanta, fiabilitatea si costurile, iar problema este NP-hard. Virtualizarea include si microservicii, containere si sisteme cloud-native, de aceea a doua parte a lucrarii trateaza plasarea CNF-urilor in edge si fog computing (Rezumat). Autorii afirma ca survey-urile anterioare nu trateaza plasarea CNF-urilor in contextul 5G (I.E, Tabelul I).

## Structura si taxonomia propusa
- **Metodologie** (I.C, Fig. 3):
  - cautare in Google Scholar dupa cuvinte-cheie in titlu: 294 de articole;
  - filtrare pe edituri (ACM, IEEE, Elsevier, MDPI, Springer, Wiley, Taylor & Francis): 217;
  - citirea rezumatelor: 176;
  - eliminarea lucrarilor scurte (sub 6 pagini): 162 de articole.
  - Perioada este 2016-2022 (I.D mentioneaza 2016-2021). Plasarea simpla de VM in cloud este exclusa.
- **Structura:**
  - Sectiunea II: concepte de cloud, edge, fog si virtualizare (VM, VNF, container, CNF);
  - Sectiunea III: plasarea VNF, cu provocari, solutii si clasificare (Tabelele III-V);
  - Sectiunea IV: plasarea CNF/containerelor in cloud, edge si fog (Tabelele VI-VIII).
- **Clasificare dubla** (Fig. 17):
  - dupa obiectiv (sase): reducerea consumului de energie, reducerea costului, maximizarea utilizarii resurselor, reducerea latentei, minimizarea interferentei de trafic, maximizarea QoS;
  - dupa metoda:
    - heuristice;
    - meta-heuristice (de exemplu Tabu search, swarm intelligence, algoritmi evolutivi, simulated annealing);
    - machine learning (regresie, clustering, deep learning, Q-learning, R-learning).
  - Abordarile sunt de asemenea online (dinamice) sau offline (statice) (III.C).

## Lucrari/sisteme acoperite (cu numar)
- 162 de articole selectate (I.C).
- Tabelul I compara lucrarea cu 7 survey-uri anterioare ([11]-[17]).
- Sunt mentionate si proiecte open-source: ONAP, OSM, Mosaic 5G, Open5GCore (I.E).

## Directii deschise declarate
- **Constatari din tabele** (V.A):
  - energia este folosita rar ca metrica pentru plasarea VNF;
  - traficul este putin investigat pentru plasarea containerelor;
  - utilizarea resurselor si latenta sunt cele mai tratate.
  - Autorii afirma ca algoritmii DL dau rezultate mai bune decat cei heuristici, meta-heuristici si greedy.
- **Provocari viitoare** (V.B):
  - coexistenta VNF si CNF in aceeasi arhitectura;
  - migrarea containerelor, rar acoperita de modelele de scheduling;
  - scheduling constient de securitate;
  - predictia sarcinii prin DL pentru consolidare, load balancing si provizionare;
  - strategii multi-obiectiv (energie, SLA, QoS);
  - descentralizarea deciziilor de scheduling pe mai multe servere edge, cu putine lucrari pana acum.
- Lucrari viitoare ale autorilor: comparatie intre scheduling centralizat si descentralizat; decizie multi-obiectiv rezolvata prin RL.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu (survey).
- UE reale sau emulate?: nu (survey).
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu (survey).
- executa actiuni automat (bucla inchisa)?: nu (survey); trateaza algoritmi de plasare, inclusiv RL.
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat; plasarea in cloud, edge si fog este tratata ca problema de optimizare.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu.
- observa traficul la SCP / proxy?: nu.
