# Digital Twin for Networking: A Data-Driven Performance Modeling Perspective (2023)
Cheie: Hui2023Dtperfmodel . DOI/link: https://doi.org/10.1109/mnet.119.2200080 . Sursa textului: integral: arXiv 2206.00310v1 (1 iunie 2022; versiunea publicata in IEEE Network poate diferi)
Sectiunea din plan: C . Tema: digital twin (modele de performanta data-driven, survey scurt)
Autori: Linbo Hui, Mowei Wang, Liang Zhang, Lu Lu, Yong Cui (Tsinghua University; China Mobile). IEEE Network, 2023.

## Problema (cum o formuleaza autorii)
Retelele devin complexe si heterogene, iar experimentele pe reteaua fizica sunt costisitoare si riscante. Digital Twin Network (DTN) permite evaluarea "what-if" a efectului modificarilor asupra performantei. Simularea si modelarea analitica sunt, dupa autori, ineficiente, imprecise si inflexibile: simulatoarele packet-level sunt cu 3-4 ordine de marime mai lente decat timpul real, iar teoria cozilor nu poate descrie, de exemplu, incast-ul. Autorii argumenteaza ca metodele data-driven sunt cele mai promitatoare (Rezumat, I).

## Structura si taxonomia propusa
- **Trei cerinte pentru modelele de performanta** (II):
  - fidelitate, pe trei niveluri temporale: long-term (exemplu RouteNet), short-term (xNet), one-to-one per pachet (MimicNet);
  - eficienta: mai rapid decat reteaua fizica, usor de desfasurat;
  - flexibilitate: abordare modulara sau stratificata, pentru a actualiza doar modulele afectate de mecanisme noi.
- **Comparatia modelelor selectate** (III, Tabelul I), dupa:
  - date: simulare, testbed, productie (de exemplu WISE pe CDN-ul Google, Sun et al. pe iQIYI);
  - intrari/iesiri;
  - stadiul modelului: metode clasice (Causal Bayesian Network, SVR) -> NN simple -> NN personalizate (de exemplu GNN);
  - scenarii de aplicare.
- **Constatare:** majoritatea lucrarilor selectate colecteaza date din simulare (III.B).

## Lucrari/sisteme acoperite (cu numar)
Tabelul I compara modelele selectate (referintele [2]-[15], printre care WISE, RouteNet, xNet, MimicNet). Numarul exact nu este declarat explicit in sectiunile citite.

## Directii deschise declarate
Sectiunea IV:
- **colectarea datelor:**
  - datele de productie sunt valoroase, dar limitate;
  - gap-ul simulare-realitate;
  - nu exista dataset-uri si benchmark-uri recunoscute pentru networking;
  - solutii posibile: telemetrie in retea, sincronizare precisa, augmentare cu cunostinte de domeniu, few-shot, self-supervised si transfer learning;
- **constructia modelelor:**
  - mecanisme globale/locale si spatiale/temporale incalcite (congestion control, cozi, rutare);
  - propun abordari modulare sau stratificate, combinatii analitic + NN si foundation models, de exemplu reteaua descrisa ca secvente de pachete;
- **aplicatii:**
  - optimizare bazata pe cautare si control bazat pe model;
  - DTN ca mediu sigur pentru explorarea politicilor RL si ca mediu de verificare pentru AIOps si self-driving networks.

Concluzie: utilizarile practice sunt rare din cauza lipsei de date de productie.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu (survey).
- UE reale sau emulate?: nu.
- digital twin al retelei?: da (tema) - DTN cu evaluare what-if (I, V).
- prezice efectul unei actiuni inainte de a o aplica?: da (tema) - evaluarea what-if a modificarilor este functia esentiala a DTN (V).
- executa actiuni automat (bucla inchisa)?: discutat - DTN ca mediu pentru RL si verificare (IV.C); nu este implementat.
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu.
- observa traficul la SCP / proxy?: nu.
