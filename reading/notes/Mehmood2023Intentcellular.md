# Intent-driven autonomous network and service management in future cellular networks: A structured literature review (2023)
Cheie: Mehmood2023Intentcellular . DOI/link: https://doi.org/10.1016/j.comnet.2022.109477 . Sursa textului: integral: arXiv 2108.04560v3 (versiunea Computer Networks 220 (2023) 109477, CC BY)
Sectiunea din plan: C . Tema: bucle inchise (IBN in retele celulare, review structurat)
Autori: Kashif Mehmood, Katina Kralevska, David Palma (NTNU). Computer Networks vol. 220, 2023, art. 109477.

## Problema (cum o formuleaza autorii)
Retelele conduse de intentii sunt descrise de autori ca un pas spre management autonom. IBN ridica provocari: definirea contextuala a intentiilor, rolul actorilor si lipsa unei arhitecturi generalizate. Survey-urile existente ([10]-[12]) nu acopera, dupa autori, toate aspectele; aceasta lucrare se declara primul review structurat despre IBN (Rezumat, 1.2).

## Structura si taxonomia propusa
- **Protocol de cautare** (1.2):
  - patru intrebari de cercetare: intentiile declarative in design, operare si management beyond-5G; actori si cerinte; ciclul de viata IBN si componentele care convertesc intentiile in politici; tehnologii, compromisuri si provocari;
  - surse primare Scopus si IEEE Xplore, secundare ACM DL, ScienceDirect, Wiley;
  - 5484 de rezultate in perioada 2015-2021 (Tabelul 3: de exemplu Scopus 3211, IEEE Xplore 1158);
  - dupa eliminarea duplicatelor si filtrare raman 60 de studii unice.
- **Sectiunea 2:** definitie, intent vs. policy-based management, ciclul de viata al intentiei pe trei domenii (utilizator, procesare, implementare), actori si clasificare, adoptie in industrie.
- **Sectiunea 3:** modelarea serviciilor beyond-5G: evolutia si ecosistemul serviciilor, conformitate si assurance SLA, designul serviciilor, orchestrare.
- **Sectiunea 4, enablers:** SDN/NFV, ZSM si autonomous networking, Networks-2030, ETSI ENI, ML/AI.
- **Sectiunea 5:** un cadru arhitectural convergent de management bazat pe intentii, cu strat de aplicatie si strat de intentii (expresie si NBI, model de serviciu si orchestrare, assurance si optimizare, intent API), cu accent pe SLA si KPI-urile clientului.

## Lucrari/sisteme acoperite (cu numar)
60 de studii unice selectate din 5484 de rezultate (1.2).

## Directii deschise declarate
- Sectiunea 6: descrierea intentiilor; interpretarea si maparea pe servicii; rolul ML/AI in ciclul de viata; deployment IBN cu NFV/SDN; compatibilitatea limbajelor de modelare a datelor; intentii multi-domeniu; securitatea IBN.
- Concluzii-cheie din Rezumat:
  1. beneficiile IBN pentru retele autonome;
  2. intentiile trebuie integrate ca politici fundamentale in modelarea serviciilor si managementul retelei;
  3. sunt necesare modele de reprezentare a intentiilor abstracte si agnostice de domeniu;
  4. invatarea trebuie inclusa ca functie fundamentala in retelele autonome.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu (review).
- UE reale sau emulate?: nu.
- digital twin al retelei?: nedeclarat in sectiunile citite.
- prezice efectul unei actiuni inainte de a o aplica?: nu.
- executa actiuni automat (bucla inchisa)?: tema review-ului (assurance si optimizare in stratul de intentii, 5.2.3); fara implementare proprie.
- multi-site / geo-redundanta / failover de baza de date?: nu; intentiile multi-domeniu sunt o problema deschisa (6.6).
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu.
- observa traficul la SCP / proxy?: nu.
