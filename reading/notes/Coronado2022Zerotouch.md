# Zero Touch Management: A Survey of Network Automation Solutions for 5G and 6G Networks (2022)
Cheie: Coronado2022Zerotouch . DOI/link: 10.1109/comst.2022.3212586 . Sursa textului: integral, versiunea publicata (IEEE Commun. Surveys & Tutorials, vol. 24, no. 4, 2022; PDF cu antet IEEE, licenta CC BY, pagina 1 indica data publicarii 6 Oct 2022), https://iris.univpm.it/bitstream/11566/315192/2/Zero_Touch_Management_A_Survey_of_Network_Automation_Solutions_for_5G_and_6G_Networks.pdf
Sectiunea din plan: A
## Problema (cum o formuleaza autorii)
Retelele mobile devin tot mai eterogene si complexe, iar cererile aplicatiilor noi depasesc capacitatea de management manual. Autorii definesc zero-touch management (ZTM) ca management de retea complet autonom, cu supraveghere umana, si afirma ca lipsea un sondaj care sa lege ZTM/Autonomic Network Management (ANM) de cercetarea in retele mobile si wireless. Pretind ca este primul sondaj focalizat pe solutii ZTM si ANM pentru managementul retelelor 5G/6G, cu viziune tutorial asupra paradigmelor, functii si cerinte din toate segmentele retelei si analiza tehnologiilor-suport (Sec. III-D).
## Ce propun (metoda, pe scurt)
Survey cu structura in sapte sectiuni (Fig. 1): II paradigme de management (Active Networks, SON, ANM, PBNM, IBN etc., Tab. II); III lucrari conexe si scop (Tab. III); IV ZSM: concept si arhitectura ETSI ZSM (domenii de management, Data Services, Domain/Cross-domain Integration Fabric, bucle inchise; Fig. 2), plus alte standarde (ETSI ENI, 3GPP SA2/SA5 inclusiv NWDAF, TM Forum ZOOM, MEF LSO); V tehnologii-suport (control programatic, virtualizare si orchestrare, data analytics si closed-loop control, tehnici AI, rezumat in Tab. IV); VI solutii pe segmente de retea: RAN, Distributed Core, Distributed Edge, End-to-End (Tab. V-VIII); VII provocari viitoare. Autorii noteaza ca predictive network maintenance nu este tratat (granularitate temporala diferita), amanat pentru un alt sondaj (Sec. VI-D).
Distributed Core (Sec. VI-B) acopera: core network slicing, scalabilitatea NF-urilor din core 5G (scalare reactiva vs proactiva, ex. AMF) si service automation pentru core (microservicii, Kubernetes, blockchain). Exemple descrise: [189] framework zero-touch pentru slicing cu testbed core 5G conform 3GPP si OSM ca NFVO; [191] monitorizare/analitica/selectie de slice in NSMF si NSSF; [193] predictor integrat ca implementare NWDAF; [200], [201] scalare proactiva a AMF pe baza de forecasting; [202] modul de analitica integrat cu Open5GCore; [204] provisioning cu Kubernetes si AIOps cu NWDAF si MDAF; [205] Kube5G cu Kube5G-Operator; [206] NoStack (sidecar pentru SBA); [207] c/e split pentru relocarea NF-urilor.
## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Nu este lucrare experimentala; nu are testbed propriu. Descrie setup-urile lucrarilor citate, de ex.: Open5GCore (ref. [213]) pentru [202]; testbed core 5G conform 3GPP cu OSM pentru [189]; testbed experimental pentru video streaming in [194]; trafic sintetic eMBB/URLLC/mMTC in [191]; date reale de trafic mobil in [188]; simulari in [199]-[201].
## Experimente si metrici
Nu este lucrare experimentala. Tabelele sintetizeaza lucrarile dupa tehnica de automatizare (SL/UL/RL/DL, optimizare, euristici), functie de management si segment (Tab. V RAN, Tab. VI Distributed Core, Tab. VII Distributed Edge, Tab. VIII End-to-End).
## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Cifre din lucrari citate (nu rezultate proprii), din Sec. VI-B:
- [190] DeepSlice: acuratete de aproximativ 95% pentru prezicerea categoriei de slice pentru tipuri de dispozitive necunoscute.
- [199]: reducere de 50% a duratei de antrenare fara afectarea preciziei (simulare).
- [194]: actiuni de scalare verticala/orizontala in aproximativ 15 s.
- [198]: Q-Learning + Gaussian Processes; tinta mean response time sub 1 ms fara violari.
- [205] Kube5G: timpi de provisioning sub doua minute, reconfigurare sub un minut.
- [202]: modelul Prophet are erori mai mici decat ARIMA pentru CPU si memorie.
Concluzii formulate de autori (Sec. VI-B): scarce lucrari iau in calcul interoperabilitatea; lipsesc evaluari ale limitelor de scalabilitate si complexitate pentru volume mari de date heterogene de monitorizare.
## Limitari declarate de autori
Sec. VII: lipsa seturilor de date reprezentative si etichetate (date 5G reale rare, necoerenta intre operatori, dinamica retelei); explainable ZTM (majoritatea lucrarilor folosesc modele black-box); trustworthy ZTM (partajarea datelor operationale si increderea intre domenii; propun Operational Data Lake si Permissioned Distributed Ledger). Sec. VI-D: lipsa evaluarii vectorilor de atac pentru modele AI/ML in 5G/6G, necesitatea fallback-urilor, confidentialitate (FL cu blockchain, homomorphic encryption). Sec. VI-D: predictive network maintenance exclus din scop.
## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu - survey; descrie implementari din lucrari citate (ex. Open5GCore, Kube5G; Sec. VI-B)
- UE reale sau emulate? nu - fara experimente proprii
- digital twin al retelei? nu - nu este tema lucrarii
- prezice efectul unei actiuni inainte de a o aplica? nu - fara sistem propriu; descrie scalare proactiva pe baza de forecasting in lucrari citate (Sec. VI-B)
- executa actiuni automat (bucla inchisa)? nu - fara sistem propriu; closed-loop este tema centrala de survey (Sec. IV, V-C, VI)
- multi-site / geo-redundanta / failover de baza de date? nedeclarat - mentioneaza "failover" doar la Kube5G-Operator in lucrari citate (Sec. VI-B)
- evaluare prospectiva (predictie fixata inainte de experiment)? nu - nu este lucrare experimentala
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - fara masuratori proprii
- observa traficul la SCP / proxy? nedeclarat
