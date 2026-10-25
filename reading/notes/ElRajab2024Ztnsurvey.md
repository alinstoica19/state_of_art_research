# Zero-touch networks: Towards next-generation network automation (2024)
Cheie: ElRajab2024Ztnsurvey . DOI/link: https://doi.org/10.1016/j.comnet.2024.110294 . Sursa textului: integral: arXiv 2312.04159v1 (7 decembrie 2023; "Preprint submitted to Computer Networks")
Sectiunea din plan: C . Tema: bucle inchise (ZSM/ZTN, survey + studiu de caz AutoML)
Autori: Mirna El Rajab, Li Yang, Abdallah Shami (Western University). Computer Networks, 2024.

## Problema (cum o formuleaza autorii)
ZSM ofera autogestiune si self-healing pentru retelele 5G si urmatoarele (5G+), folosind ML pentru decizii inteligente cu interventie umana redusa. Aplicarea ML in ZSM are provocari: selectia modelelor, tuning-ul hiperparametrilor, drift-ul datelor. Autorii propun AutoML si digital twins ca solutii (Rezumat, 1).

## Structura si taxonomia propusa
- **Contributii** (Sectiunea 1):
  - standardul ZSM, arhitectura de referinta si proiecte;
  - aplicatii Zero-Touch Network Operation (ZNO): optimizare, controlul traficului, eficienta energetica, securitate;
  - provocarile ML in ZSM;
  - AutoML si DT ca solutii de automatizare;
  - descompunerea pipeline-ului AutoML;
  - un studiu de caz cu AutoML online;
  - provocari si directii viitoare.
- **Structura:**
  - Sectiunea 3: fundal ML, cu limitari pe familii de algoritmi;
  - Sectiunea 4: ZSM;
  - sectiunile urmatoare: aplicatii pe domenii, cu tabele de scheme pentru MEC (Tabelul 6), predictia traficului (Tabelul 7), eficienta energetica (Tabelul 9) si managementul increderii (Tabelul 11);
  - Sectiunea 8: securitate si confidentialitate, cu amenintari la UE, RAN, core (CN) si SDN;
  - Sectiunea 10: studiul de caz;
  - Sectiunea 11: provocari.
- **Studiul de caz** (Sectiunea 10): predictia throughput-ului aplicatiei cu un pipeline AutoML online.
  - Date: un dataset public de productie de la un operator mobil major din Irlanda, cu KPI-uri colectate client-side cu G-NetTrack Pro (4G si 5G, video streaming si descarcare de fisiere, doua tipare de mobilitate). Sunt formate 4 sub-dataset-uri.
  - Drift-ul este monitorizat pe baza performantei, cu prag dinamic, si declanseaza actualizarea incrementala a ponderilor. Autorii scriu ca nu au detectat drift real si l-au simulat (10.4).
  - Este propusa si o arhitectura 5G E2E care integreaza AutoML si ZSM (10.5, Fig. 9).

## Lucrari/sisteme acoperite (cu numar)
Tabelele de scheme pe domenii (Tabelele 3, 6, 7, 9, 11); numarul total de lucrari nu este declarat in sectiunile citite.

## Rezultate raportate (studiul de caz)
- Mediu de rulare: Python 3.10.11, i9-12900HK cu 14 nuclee, 32 GB RAM, GPU RTX 3060 de 6 GB. Metrici: MAE si MAPE; orizontul de predictie este 60 s (10.6).
- AutoML cu Seq2Seq are MAE si MAPE mai mici decat LSTM simplu si Seq2Seq simplu pe toate cele patru dataset-uri (Tabelul 14).
- Exemplu din text, 5G descarcare de fisiere: MAPE scade de la 6,52% la 4,76% si MAE de la aproximativ 0,17 la 0,11. Textul atribuie trecerea "de la LSTM la encoder-decoder", iar tabelul este greu de citit in extragere.

## Directii deschise declarate
Sectiunea 11:
- provocari ZSM: zero-touch management explicabil, ZSM de incredere, complexitatea computationala;
- provocari AutoML: interpretabilitate, scalabilitate, robustete, cold-start.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - studiul de caz foloseste un dataset client-side; arhitectura 5G este conceptuala (Fig. 9).
- UE reale sau emulate?: reale (in dataset-ul de productie) - KPI-uri colectate pe telefoane cu G-NetTrack Pro (10.2).
- digital twin al retelei?: discutat ca solutie pentru provocarile ML (contributia 4); nu este implementat.
- prezice efectul unei actiuni inainte de a o aplica?: nu - prezice throughput-ul aplicatiei.
- executa actiuni automat (bucla inchisa)?: partial - modelul se actualizeaza automat la drift; fara actiuni asupra retelei.
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: da - throughput-ul aplicatiei la utilizator (dataset).
- observa traficul la SCP / proxy?: nu.
