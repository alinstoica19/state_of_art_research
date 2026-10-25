# Reliability and Availability in Virtualized Networks: A Survey on Standards, Modeling Approaches, and Research Challenges (2026)
Cheie: Mauro2026Availabilitysurvey . DOI/link: https://doi.org/10.1109/comst.2026.3670039 . Sursa textului: integral: arXiv 2503.22034v1 (27 martie 2025; preprint al versiunii IEEE COMST)
Sectiunea din plan: C . Tema: rezilienta (disponibilitate/fiabilitate NFV, survey)
Autori: Mario Di Mauro, Walter Cerroni, Fabio Postiglione, Massimo Tornatore, Kishor S. Trivedi. IEEE Communications Surveys & Tutorials, 2026; 220 de referinte in versiunea arXiv.

## Problema (cum o formuleaza autorii)
NFV distribuie componentele si creeaza interdependente puternice. Defectele devin mai greu de prezis, monitorizat si gestionat decat in retelele monolitice. Modelarea precisa a fiabilitatii (functionare corecta in conditii date) si a disponibilitatii (probabilitatea ca sistemul sa fie gata de folosire) este necesara pentru sisteme virtualizate tolerante la defecte. Autorii spun ca survey-urile existente doar mentioneaza tehnicile de modelare, fara detalii despre formalisme si fara clasificarea documentelor ETSI sau a uneltelor (Rezumat, II, II.A).

## Structura si taxonomia propusa
- **Sectiunea II:** survey-uri inrudite grupate pe domenii (cloud, componente NFV, sisteme software-defined, domenii specifice). Tabelul I le compara pe cinci criterii: tehnici si metrici, ghiduri standard, unelte software, exemple practice, caracter de tutorial.
- **Sectiunea III:** NFV, network slicing, SFC, SDN.
- **Sectiunea IV:** definitii si evaluare cantitativa a fiabilitatii si disponibilitatii (Tabelul II: valori uzuale de disponibilitate in regim stationar).
- **Sectiunea V:** standardizare, in special documentele ETSI NFV-REL (Tabelul III).
- **Sectiunea VI, formalisme**, cu exemple pe arhitecturi virtualizate si avantaje/dezavantaje:
  - non-state-space: Reliability Block Diagrams, Fault Trees;
  - state-space: Continuous-Time Markov Chains, Markov Reward Models, Multi-State Systems, Stochastic Petri Nets, Generalized SPN, Stochastic Activity Networks, Stochastic Reward Networks;
  - Tabelul IV mapeaza lucrarile pe formalismele non-state-space.
- **Sectiunea VII, unelte:** SHARPE, TimeNET, SPNP, Mercury, WebSPN, GreatSPN, CPN IDE, QPME si altele.
- **Sectiunea VIII:** concluzii si provocari.

## Lucrari/sisteme acoperite (cu numar)
220 de referinte; tabele de mapare referinta -> formalism (de exemplu Tabelul IV). Numarul exact de lucrari mapate nu a fost numarat aici.

## Directii deschise declarate
Sectiunea VIII:
- A. scalabilitate: modelarea comuna disponibilitate-fiabilitate-performanta in medii mari (cloud data centers, core-uri 5G), cu abordari hibride analitic + simulare aliniate la ETSI;
- B. toleranta la defecte si rezilienta: formalismele presupun configuratii statice; sunt necesare cadre adaptive cu detectie de anomalii, self-healing si strategii cross-layer pentru defecte tranzitorii si in cascada;
- C. securitate si incredere: redundanta mareste suprafata de atac;
- D. eficienta energetica: compromisul redundanta vs. energie;
- E. automatizare si orchestrare: unelte de orchestrare cu verificare bazata pe modele de fiabilitate/disponibilitate in timp real;
- F. standardizarea uneltelor software (sabloane si API-uri pentru VNF, VM, hypervisor);
- G. ML/AI integrat cu modele formale (lanturi Markov, fault trees) pentru evaluarea riscului, mentenanta predictiva si recuperare automata;
- H. tehnologii emergente: acceleratoare, containere, serverless si FaaS.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu (survey de modelare).
- UE reale sau emulate?: nu.
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu; verificarea orchestrarii pe baza modelelor de fiabilitate este propusa ca directie (VIII.E).
- executa actiuni automat (bucla inchisa)?: nu.
- multi-site / geo-redundanta / failover de baza de date?: tema generala (redundanta, failover/repair in modele); fara evaluare proprie.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu.
- observa traficul la SCP / proxy?: nu.
