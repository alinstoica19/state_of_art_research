# Intelligent network data analytics function in 5G cellular networks using machine learning (2020)
Cheie: Sevgican2020Nwdaf . DOI/link: 10.1109/jcn.2020.000019 . Sursa textului: versiunea publicata (J. Commun. Netw., vol. 22, no. 3, iunie 2020), open access, https://ieeexplore.ieee.org/ielx7/5449605/9143569/09143579.pdf
Sectiunea din plan: A
## Problema (cum o formuleaza autorii)
NWDAF este o functie 5G noua, definita de 3GPP, care ofera analitice altor NF si poate folosi orice algoritm ML/AI. Autorii spun ca literatura despre NWDAF este putin dezvoltata, ca unele parti din specificatiile 3GPP sunt lasate necompletate si ca nu exista seturi de date reale de trafic gNodeB 5G SA potrivite pentru scenariile NWDAF studiate. Se concentreaza pe trei capabilitati: informatii despre comportament anormal al unui grup de UE, comportament asteptat al unui grup de UE si network load performance intr-o zona de interes (in practica: clasificare de anomalii si predictie de load).
## Ce propun (metoda, pe scurt)
- Descriu structura si protocoalele NWDAF din documentele 3GPP (servicii Nnwdaf events subscription si analytics information; consumatori NF; surse de date NF prin Nnf).
- Genereaza un set de date sintetic, bazat pe celule (cell-based), cu campuri inspirate din specificatiile 3GPP (data rate, network area information, subscription categories, personal equipment ID); setul este publicat (repo GitHub nwdaf_data).
- Predictia load-ului: tratata ca serie de timp, cu trei modele (regresie liniara LR, LSTM, RNN), pe features extrase din ratele de date anterioare (last2/4/8_mean, per_change_last2/3/4, change_last2/3/4; se selecteaza last2_mean si toate per_change).
- Detectia anomaliilor: clasificare binara (normal/anomalie) cu logistic regression si XGBoost, cu tratarea dezechilibrului de clase (class weight, respectiv reducerea efectului clasei dominante).
## Setup experimental (testbed real / emulare / simulare; unelte: Open5GS, free5GC, OAI, UERANSIM, ns-3, Kubernetes...; scara: nr. UE, NF, noduri; date: trafic real, trace-uri, sintetice)
- Simulare; generatorul de date implementat in Python (Sec. V). Nu sunt folosite Open5GS, free5GC, OAI, UERANSIM, ns-3 sau Kubernetes (nu apar in text).
- Topologie fixa: 5 celule RRU, 3 categorii de abonati (platinum, gold, silver), 5 tipuri de echipamente (IoT, vehicle, cell phone, smartwatch, tablet) (Sec. IV.B, Fig. 4). Nu se modeleaza UE individuale, ci grupuri (categorie x tip x celula) cu incarcare agregata.
- Date sintetice: 6 luni de trafic, snapshot la fiecare 15 minute; handover intre celule adiacente cu rate medii dependente de ora (Tabel 2), distributie Gaussiana N(mu, mu/8) (Ec. 1); incarcari initiale in Gbps (Tabel 3); anomalii (crestere brusca de trafic, cu crestere exponentiala in perioada anomaliei, momente alese aleator) etichetate pentru ground truth.
- Arhitectura RNN: un strat RNN, patru straturi ascunse, un strat de iesire; LSTM la fel (Sec. VI.B). Loss: MAE.
## Experimente si metrici
- Load prediction pentru fiecare combinatie celula-categorie (15 scenarii); metrici MAPE si MAE (Tabel 4); curbe timp vs data rate pentru doua scenarii (Fig. 7).
- Anomaly detection: AUC-ROC, accuracy, precision (Tabel 5, mediat peste tipurile de device); curbe ROC pentru celulele 3 si 4, cell phone, 3 categorii (Fig. 8).
## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Tabel 4, medii: MAPE LR 0.615, LSTM 0.544, RNN 0.560; MAE LR 0.247, LSTM 0.213, RNN 0.202. LSTM si RNN sunt sub LR in toate scenariile; RNN sub LSTM in aproximativ jumatate din scenarii; LSTM mai bun la MAPE in medie, RNN mai bun la MAE in medie. Textul spune ca LSTM urmareste mai bine ratele stabile, RNN pe cele instabile (Fig. 7).
- Tabel 5, medii: Logistic regression AUC-ROC 87.0%, accuracy 55.6%, precision 76.9%; XGBoost AUC-ROC 90.7%, accuracy 62.6%, precision 77.3%. (In Tabel 5, celula 3 Gold XGBoost accuracy apare ca 89.8%, valoare diferita de restul randurilor din text.)
- Fig. 8: AUC-ROC celula 3 (cell phone): XGB 0.87/0.87/0.88 vs LogReg 0.83/0.83/0.84 (silver/gold/platinum); celula 4: XGB 0.91/0.90/0.91 vs LogReg 0.86/0.84/0.85. Categoria de abonat nu influenteaza semnificativ performanta, conform textului.
## Limitari declarate de autori
- Datele sunt sintetice; autorii spun ca modelele de regresie ar putea avea performanta mai slaba in implementari reale, iar modelele complexe ar trebui sa dea performanta similara (Sec. VII.A).
- Topologie fixa de 5 celule in simulari (Sec. IV.B).
- Probleme deschise: clasificare multi-label a anomaliilor, imbogatirea datelor pentru analitice la nivel de network slice, detectia de communication pattern, alte modele AI/ML si alte capabilitati NWDAF (Sec. VIII).
## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu - NWDAF si NF-urile sunt descrise conceptual; datele vin dintr-un generator Python (Sec. III-V)
- UE reale sau emulate? nici una - UE sunt grupuri modelate statistic in simulare (Sec. IV-V)
- digital twin al retelei? nu - nu este mentionat conceptul de digital twin; este un set de date sintetic plus modele ML (Sec. V-VI)
- prezice efectul unei actiuni inainte de a o aplica? nu - se prezic load si anomalii, nu efectul unor actiuni (Sec. VI)
- executa actiuni automat (bucla inchisa)? nu - doar analitice, fara actiuni (Sec. III, VII)
- multi-site / geo-redundanta / failover de baza de date? nu - nu este abordat; doar celule in topologie simulata (Sec. IV)
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat - evaluare retrospectiva pe date sintetice; protocolul de impartire train/test nu este detaliat in text (Sec. VII)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - metrici la nivel de celula/categorie/tip device (Tabel 4, 5)
- observa traficul la SCP / proxy? nu - SCP/proxy nu apar; datele vin ca campuri de la NF-uri simulate (Sec. V)
