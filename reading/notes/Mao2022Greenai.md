# AI Models for Green Communications Towards 6G (2022)
Cheie: Mao2022Greenai . DOI/link: https://doi.org/10.1109/comst.2021.3130901 . Sursa textului: integral: arXiv 2101.01588v2 (11 ianuarie 2021; versiune submitted listata de Unpaywall). In arXiv titlul este "AI based Service Management for 6G Green Communications"; versiunea publicata poate diferi.
Sectiunea din plan: C . Tema: energie (AI pentru comunicatii verzi, survey)
Autori: Bomin Mao, Fengxiao Tang, Yuichi Kawamoto, Nei Kato (Tohoku University). IEEE Communications Surveys & Tutorials vol. 24(1), 2022; 281 de referinte in arXiv v2.

## Problema (cum o formuleaza autorii)
In 5G si 6G, infrastructura si numarul de terminale cresc exponential, deci si costul energetic. Cerintele 6G de QoS, securitate, flexibilitate si inteligenta complica cresterea eficientei energetice, iar energy harvesting complica controlul puterii si managementul retelei. Autorii prezinta AI ca solutie pentru aceste provocari si pentru reducerea interventiei umane. Survey-urile anterioare acopera retele specifice si relatia energie-comunicatie, nu tehnicile AI si nici perspectiva de calcul si stocare (Rezumat, I.B).

## Structura si taxonomia propusa
- **Sectiunea I.B:** survey-uri existente pe comunicatii verzi si energy harvesting (Tabelul I).
- **Sectiunea II, tehnici AI:** algoritmi traditionali (euristici), evolutia modelelor DL, metode de invatare viitoare.
- **Trei scenarii 6G:**
  - **comunicatii celulare (CNC)** (III): puterea consumata si eficienta energetica, deployment-ul si configurarea BS, controlul puterii si alocarea resurselor, BS cu energy harvesting;
  - **comunicatii machine-type (MTC)** (IV): modelarea consumului, acces la retea eficient energetic (Tabelul II), transmisii eficiente (Tabelul III), energy harvesting si partajare;
  - **comunicatii orientate pe calcul (COC)** (V): modelarea consumului, cloud si edge computing eficiente energetic, caching si livrare de continut verzi.

## Lucrari/sisteme acoperite (cu numar)
281 de referinte in arXiv v2; Tabelele II-III listeaza lucrari AI pentru MTC verde.

## Directii deschise declarate
Sectiunea VI:
- A. managementul verde al BS in HetNet 6G: asocierea utilizatorilor pentru oprirea BS redundante, predictia traficului, mobilitatii si canalului pentru reconfigurare anticipata, BS ca furnizor de calcul, stocare si energie;
- B. Space-Air-Ground Integrated Networks eficiente energetic;
- C. transmisii eficiente energetic bazate pe AI;
- D. energy harvesting si partajare imbunatatite prin AI;
- E. securitatea retelelor cu AI;
- F. modele AI usoare si design hardware.

Concluzia subliniaza ca trebuie luat in calcul consumul de energie al modelelor AI insesi.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu (survey; accent pe RAN, MTC si edge/cloud).
- UE reale sau emulate?: nu.
- digital twin al retelei?: nedeclarat.
- prezice efectul unei actiuni inainte de a o aplica?: nu; predictia traficului pentru reconfigurare anticipata este propusa ca directie (VI.A).
- executa actiuni automat (bucla inchisa)?: nu (survey).
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu.
- observa traficul la SCP / proxy?: nu.
