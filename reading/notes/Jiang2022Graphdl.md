# Graph-based deep learning for communication networks: A survey (2022)
Cheie: Jiang2022Graphdl . DOI/link: https://doi.org/10.1016/j.comcom.2021.12.015 . Sursa textului: integral: arXiv v2 (22 decembrie 2021, versiune preprint)
Sectiunea din plan: C . Tema: GNN / modelare retea (survey)
Autori: Weiwei Jiang (Tsinghua University), autor unic. Publicat in Computer Communications (Elsevier); textul consultat este preprint-ul arXiv 2106.02533v2.

## Problema (cum o formuleaza autorii)
- Retelele de comunicatii au probleme nerezolvate complet: rutare, load balancing, power control, alocare de resurse, virtual network embedding in SDN. Configurarea manuala devine ineficienta (Sectiunea 1).
- Modelele deep learning clasice sunt proiectate pentru date euclidiene (imagini, video) si nu folosesc topologia retelei. GNN-urile sunt propuse pentru date pe grafuri si, dupa autor, generalizeaza la topologii nevazute (1, 3.3).
- Autorul afirma ca este primul survey despre aplicarea deep learning pe grafuri in retele de comunicatii, acoperind atat scenarii wired cat si wireless (Rezumat).

## Structura si taxonomia propusa
- **Sectiunea 2, metodologie:** cautare cu doua grupuri de cuvinte-cheie (tehnici pe grafuri: GNN, GCN, GAT, GraphSAGE, MPNN etc.; retele si probleme: wireless, cellular, SDN, traffic prediction, routing, SFC, VNF etc.), in bazele ACM, Elsevier, IEEE, Springer, Wiley, plus Google Scholar. Sunt incluse lucrari de workshop, conferinta, jurnal si preprint-uri arXiv (Tabelele 2-4).
- **Sectiunea 3, introducere in modelele pe grafuri:** grafuri in retele de comunicatii (3.1), modele (3.2), avantaje si dezavantaje (3.3).
- **Sectiunea 4, retele wireless:** general (4.1, Tabelul 5), celulare (4.2, Tabelul 6: rutare multipath 5G, traffic prediction, power control, network slicing, VNE), alte retele wireless (4.3, Tabelul 7: cognitive radio, D2D etc.).
- **Sectiunea 5, retele wired:** cinci aspecte (network modeling, configuration, prediction, management, security; Tabelul 8) si trei cazuri speciale (blockchain, data center, retele optice; Tabelul 9).
- **Sectiunea 6, SDN** (Tabelul 10): network modeling (RouteNet), rutare, plasare SFC, migrare de fluxuri, plasare/management de VNF, predictie de resurse VNF.
- Pentru fiecare lucrare, tabelele listeaza problema si solutia (modelul GNN folosit).

## Lucrari/sisteme acoperite (cu numar)
- 81 de lucrari selectate, publicate intre 2016 si primele cinci luni ale lui 2021 (Sectiunea 2, Fig. 2).
- 14 lucrari in 2019, 43 in 2020 (crestere de 207%), 20 in primele cinci luni din 2021.
- Scenariul wireless are cele mai multe lucrari (Fig. 3).
- Un repository GitHub public urmareste lucrarile noi (Rezumat).

## Directii deschise declarate
- **Limitari ale GNN discutate in 3.3:** putine seturi de date deschise pentru antrenare; adancimea modelelor (performanta scade peste doua straturi GCN, over-smoothing); stabilitatea sub perturbatii stocastice (link failure, congestie) si atacuri adversariale; explicabilitatea in domeniul retelelor nerezolvata.
- **Sectiunea 7:**
  - combinarea GNN cu alte tehnici AI: GRU pentru traffic prediction, DRL pentru alocare de resurse, rutare si VNE; GAN pentru lipsa datelor de antrenare (necombinate cu GNN in retele, in perimetrul survey-ului); AutoML pentru parametrii GNN;
  - aplicarea pe retele mai mari: in majoritatea studiilor topologia are sub 100 de noduri; solutii posibile sunt partitionarea grafului si calculul paralel; autorul intreaba daca castigurile mici justifica costul computational fata de metodele traditionale;
  - aplicarea GNN in scenarii de retea putin studiate.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu (survey).
- UE reale sau emulate?: nedeclarat.
- digital twin al retelei?: nu - network modeling cu GNN (de exemplu RouteNet, estimarea metricilor end-to-end din topologie, rutare si matrice de trafic) este descris in 5 si 6, fara termenul digital twin.
- prezice efectul unei actiuni inainte de a o aplica?: partial (la nivel de survey) - modelele de network modeling estimeaza metrici pentru retele inexistente, pentru decizii de deployment (5).
- executa actiuni automat (bucla inchisa)?: nedeclarat - lucrarile DRL+GNN sunt listate, fara discutie despre bucla inchisa.
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu.
- observa traficul la SCP / proxy?: nu.
