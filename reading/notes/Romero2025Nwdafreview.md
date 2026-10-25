# Towards Network Data Analytics in 5G Systems and Beyond (2025)
Cheie: Romero2025Nwdafreview . DOI/link: 10.14209/sbrt.2025.1571141712 . Sursa textului: integral, versiunea publicata (SBrT 2025), https://biblioteca.sbrt.org.br/articlefile/4772.pdf
Sectiunea din plan: A
## Problema (cum o formuleaza autorii)
Datele sunt un activ critic, dar subutilizate de operatorii mobili (MNO), spre deosebire de jucatorii OTT; operatorii trateaza conectivitatea ca pe o commodity. NWDAF (introdus de 3GPP din Release 15) ofera analitica si predictii, dar cercetarea academica s-ar fi concentrat pe un set limitat de metode si use case-uri, determinat de disponibilitatea dataset-urilor. Autorii vor sa lege eforturile 3GPP de cercetarea academica.
## Ce propun (metoda, pe scurt)
Lucrare de tip review (nu experimentala), cu trei contributii: (1) prezinta evolutia NWDAF in standardele 3GPP (Rel. 15-19, plus propunere pentru Rel. 20); (2) rezuma implementarile academice ale NWDAF; (3) propun doua use case-uri noi: NWDAF-assisted Charging Bypass Fraud Detection (detectia abuzului de trafic zero-rated prin corelarea comportamentului utilizatorilor cu charging records) si NWDAF Open Gateway Network Interface (NWDAF ca motor de analitica intre API-uri Open Gateway/CAMARA si NF-uri, cu MFAF). Metodologie: cautare "NWDAF" in Scopus (95 articole, 79 in IEEE Xplore), retrageri limitate la IEEE Xplore; din peste 70 de articole, 23 selectate pentru analiza detaliata (implementare, domeniu de use case, disponibilitate cod/dataset, algoritmi ML).
Continut standardizare: use case-uri pe categorii Slice/Network/Service/User (Tab. I): 1 use case in Rel. 15, 10 in Rel. 16, 15 in Rel. 17, 21 in Rel. 18, 23 in Rel. 19, unul nou propus in Rel. 20 (Abnormal UPF traffic pattern). Arhitectura: monolitica in Rel. 16; distribuita in Rel. 17 (AnLF si MTLF, plus ADRF, DCCF, MFAF); Rel. 18 aduce roaming, Horizontal Federated Learning, partajare de modele ML multi-vendor, monitorizarea performantei NWDAF; Rel. 19 lucreaza la Vertical Federated Learning (Fig. 2).
## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Nu este lucrare experimentala. Tab. III cataloghiaza lucrarile revizuite dupa Release, testbed, categorie use case, dataset, cod si algoritm ML. Testbed-urile mentionate in tabel: Open5GS, ANChOR, OAI, Free5GC (unele randuri fara testbed indicat). Textul observa utilizarea crescuta a Free5GC pentru Release-uri recente si Open5GS/OAI pentru cele mai vechi.
## Experimente si metrici
Nu este lucrare experimentala. Dimensiunile de analiza ale revizuirii: abordare de implementare, domeniu de use case, disponibilitate cod si dataset, algoritmi ML.
## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Numar use case-uri NWDAF pe release: 1 / 10 / 15 / 21 / 23 pentru Rel. 15 / 16 / 17 / 18 / 19 (Sec. II, Fig. 1, Tab. I).
- 95 articole in Scopus, 79 in IEEE Xplore, 23 selectate (Sec. IV); "mai mult de 70" articole analizate (rezumat, Sec. VII).
- Tab. III: 23 lucrari (refs. [15]-[37]) cu release 16, 17 sau 18; nicio lucrare care sa foloseasca Rel. 19 sau mai nou (Sec. V).
- Algoritmi ML intalniti: Decision Trees, Random Forest, XGBoost, LSTM, RNN, GRU, K-Means, SVM, MLP, CNN, SARIMA, Fuzzy, Autoencoder, Isolation Forest, un LLM etc. (Tab. III, Sec. V).
- Se mentioneaza ca use case-ul slice load level (in 3GPP din Rel. 15) a fost abordat de un singur studiu (Sec. V).
- Niciunul dintre cele mai folosite proiecte open source 5G nu include oficial NWDAF in repository; doar putine proiecte isi publica implementarea (Sec. V).
- Dataset-uri: mix de reale, sintetice si benchmark; unele lucrari le partajeaza (Sec. V). Citeaza un studiu Ericsson conform caruia majoritatea intreprinderilor vor incepe trial-uri de network slicing pana in 2026.
## Limitari declarate de autori
Cautarea restransa la IEEE Xplore pentru consistenta metodologica (Sec. IV). Lipsa de date reale (slicing putin desfasurat comercial) si cod partajat limitat sunt prezentate ca bariere ale domeniului (Sec. V). Use case-urile noi sunt explorative, fara abordare standardizata sau studii complete (Sec. VI).
## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu - lucrare review; mentioneaza doar implementari din alte lucrari (Sec. V)
- UE reale sau emulate? nu - nu exista experimente proprii (Sec. IV-V)
- digital twin al retelei? nu - nu este tratat (Sec. II-VII)
- prezice efectul unei actiuni inainte de a o aplica? nu - nu exista metoda proprie; NWDAF este descris ca furnizor de analitica si predictii (Sec. II)
- executa actiuni automat (bucla inchisa)? nu - nu exista sistem propriu; NWDAF descris ca "control loop" pentru self-healing la nivel conceptual (Sec. V)
- multi-site / geo-redundanta / failover de baza de date? nedeclarat
- evaluare prospectiva (predictie fixata inainte de experiment)? nu - nu este lucrare experimentala
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - nu exista masuratori proprii
- observa traficul la SCP / proxy? nedeclarat
