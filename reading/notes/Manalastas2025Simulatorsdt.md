# From Simulators to Digital Twins for Enabling Emerging Cellular Networks: A Tutorial and Survey (2025)
Cheie: Manalastas2025Simulatorsdt . DOI/link: https://doi.org/10.1109/comst.2024.3490178 . Sursa textului: integral: arXiv 2411.08907v1
Sectiunea din plan: C . Tema: digital twin (simulatoare ca nucleu DT, survey/tutorial)
Autori: Marvin Manalastas, Muhammad Umar Bin Farooq, Syed Muhammad Asad Zaidi, Haneya Naeem Qureshi, Yusuf Abdulrahman Sambo, Ali Imran. IEEE Communications Surveys & Tutorials, 2025.

## Problema (cum o formuleaza autorii)
- Simulatoarele permit evaluarea si testarea fara riscul de a intrerupe reteaua reala. Modelele digitale ale sistemului (Digital System Models, DSM), de exemplu simulatoarele system-level, devin piesa centrala pentru digital twins.
- Autorii spun ca survey-urile despre simulatoare celulare sunt putine, insuficient de cuprinzatoare si folosesc metrici generice (GUI, limbaj, licenta, modularitate), nu metrici specifice 5G (I.B).

## Structura si taxonomia propusa
- **Sectiunea II, tutorial:** rolurile, punctele tari si limitele simulatoarelor; tipuri link-level, system-level, network-level si interactiunea dintre ele.
- **Sectiunea III, cerinte de design** derivate din componentele 5G&B: New Radio, arhitectura retelei, cazuri de utilizare, securitate si confidentialitate.
- **Sectiunea IV, taxonomie si evaluare** cu metrici traditionale; include instrumente comerciale de planificare si optimizare.
- **Sectiunea V, metrici noi specifice 5G** aplicate pe simulatoare system-level:
  - realism: propagare, canal, handover, mobilitate, cerere de trafic, geometrie, model de amenintare (Tabelul IX);
  - completitudine;
  - eficienta computationala, cu tehnici de reducere a complexitatii: procesare paralela, pre-generarea trace-urilor de canal si de utilizatori, abstractizarea PHY/MAC (Tabelul XI).
  - Rezulta o matrice de aplicabilitate simulator x tema de cercetare (Tabelul XIII) si un rezumat al pregatirii pentru DT (Tabelul XII).
  - Un cadru de evolutie DSM -> DT (V.F): un DSM devine DT doar prin legatura cu reteaua reala si calibrare continua pe masuratori reale.
- **Sectiunea VI:** provocari si solutii (HetNets, maparea link-to-system, sisteme distribuite cu trafic variabil, modele de canal precise, complexitate computationala extrema, rolul AI in DSM).
- **Sectiunea VII:** provocari specifice 6G (caracteristici noi, aplicatii noi, tehnologii de baza, financiare).

## Lucrari/sisteme acoperite (cu numar)
- Peste 35 de simulatoare link-level, system-level, network-level si comerciale (I.B, VIII).
- Autorii spun ca este primul survey care discuta simulatoare comerciale de nivel industrial.

## Directii deschise declarate
- Transformarea DSM-urilor in DT complete prin conectare la retelele reale. Sunt de studiat cerintele, arhitectura si componentele legaturii, precum si acuratetea, integritatea, securitatea si confidentialitatea datelor; standardizarea este propusa (VIII).
- Lipsesc simulatoare pentru imbunatatiri de securitate in retea (VIII).
- Abordari AI/ML pentru reducerea complexitatii DSM, cu constrangerile "iron triangle" (realism, completitudine, eficienta).
- Metricile vor trebui adaptate pentru 6G.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu (survey). Simulatoarele analizate sunt in principal RAN si system-level.
- UE reale sau emulate?: nu (survey).
- digital twin al retelei?: da (tema) - cadrul DSM -> DT (V.F); legatura cu reteaua reala este declarata in afara scopului (I.B, contributia 4).
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat.
- executa actiuni automat (bucla inchisa)?: nu.
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu.
- observa traficul la SCP / proxy?: nu.
