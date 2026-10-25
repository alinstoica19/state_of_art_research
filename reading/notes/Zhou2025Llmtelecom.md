# Large Language Model (LLM) for Telecommunications: A Comprehensive Survey on Principles, Key Techniques, and Opportunities (2025)
Cheie: Zhou2025Llmtelecom . DOI/link: https://doi.org/10.1109/comst.2024.3465447 . Sursa textului: integral: arXiv 2405.10825v2 (16 septembrie 2024; acceptat in IEEE COMST)
Sectiunea din plan: C . Tema: bucle inchise (LLM pentru telecom, survey)
Autori: Hao Zhou, Chengming Hu, Ye Yuan, Yufei Cui, Yili Jin, Can Chen, Haolun Wu, Dun Yuan, Li Jiang, Di Wu, Xue Liu, Charlie Zhang, Xianbin Wang, Jiangchuan Liu. IEEE Communications Surveys & Tutorials, 2025; 208 referinte in arXiv v2.

## Problema (cum o formuleaza autorii)
Progresul tehnicilor LLM ofera oportunitati de automatizare a multor sarcini din telecom. Dupa pre-antrenare si fine-tuning, un LLM poate executa sarcini diverse pe baza instructiunilor umane, ceea ce autorii leaga de un 6G bazat pe AGI. Survey-urile existente se concentreaza mai ales pe tehnicile fundamentale ale LLM (pre-antrenare, deployment) (Rezumat, II, Tabelul I).

## Structura si taxonomia propusa
- **Sectiunea II:** comparatie cu survey-urile existente ([15]-[17], [28]-[35]).
- **Sectiunea III, fundamente LLM:**
  - arhitectura, pre-antrenare, fine-tuning, inferenta si prompting, metrici de evaluare;
  - deployment in retelele telecom (cloud, edge, mobil);
  - analiza fundamentelor in domeniul telecom.
- **Patru clase de probleme:**
  - **generare** (IV): cunostinte de domeniu, cod, configurarea retelei;
  - **clasificare** (V): securitate si detectia atacurilor, text, imagini, trafic criptat;
  - **optimizare** (VI): proiectarea automata a functiei de recompensa pentru RL, verbal RL, LLM ca optimizator black-box, optimizare convexa asistata de LLM, design de algoritmi euristici;
  - **predictie** (VII): modele fundationale pre-antrenate pentru predictie zero-shot, LLM pre-antrenate inghetate, LLM fine-tuned, LLM multi-modale.
- Fiecare sectiune se incheie cu "Discussions and Analyses".

## Lucrari/sisteme acoperite (cu numar)
208 referinte in versiunea arXiv v2.

## Directii deschise declarate
Sectiunea VIII:
- **Provocari:**
  - antrenarea de LLM specifice telecom (intrebari si raspunsuri, troubleshooting, clasificarea specificatiilor);
  - deployment practic;
  - prompt engineering pentru telecom.
- **Directii viitoare:**
  - LLM multi-modale (sensing 6G, beamforming mmWave/THz);
  - planificare multi-pas;
  - alocarea resurselor si optimizarea retelei;
  - ML clasic imbunatatit cu LLM;
  - implementari reale in industrie;
  - compresia modelelor si inferenta rapida;
  - reducerea halucinatiilor;
  - LLM augmentate prin retrieval;
  - LLM economice si accesibile.
- Concluzia mentioneaza costul si seturile de date drept provocari-cheie.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu (survey).
- UE reale sau emulate?: nu.
- digital twin al retelei?: nedeclarat in sectiunile citite.
- prezice efectul unei actiuni inainte de a o aplica?: nu.
- executa actiuni automat (bucla inchisa)?: tema partiala - optimizare si RL asistate de LLM (VI); nu este evaluat propriu.
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu.
- observa traficul la SCP / proxy?: nu.
