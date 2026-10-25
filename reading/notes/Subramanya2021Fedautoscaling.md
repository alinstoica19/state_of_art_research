# Centralized and Federated Learning for Predictive VNF Autoscaling in Multi-Domain 5G Networks and Beyond (2021)
Cheie: Subramanya2021Fedautoscaling . DOI/link: https://doi.org/10.1109/tnsm.2021.3050955 . Sursa textului: integral: versiunea trimisa (submittedVersion), repository iris.unitn.it (FINAL VERSION.pdf)
Sectiunea din plan: C . Tema: nedeclarata

## Problema (cum o formuleaza autorii)
Autoscaling-ul VNF/VMAF (aplicatii MEC virtualizate) in platformele NFV/MEC este in mod curent reactiv (ex. prag CPU 80%), iar alegerea resurselor corecte este dificila; exista un compromis intre cost si QoS (SLA, ex. round-trip-time). In scenarii multi-domain (mai multi operatori sau mai multe zone geografice ale unui operator) agregarea centralizata a datelor intampina restrictii de confidentialitate (GDPR), cost de banda si risc de single point of failure. Problema este modelata ca forecasting de serii de timp al numarului viitor de instante VNF (sau de unitati de 100 millicore CPU) pe baza traficului asteptat.

## Ce propun (metoda, pe scurt)
- Modele deep learning pentru predictia incarcarii: FFNN, LSTM, CNN-LSTM (un pas) si encoder-decoder LSTM / CNN-LSTM (multi-step, 3 pasi), pentru scalare orizontala si verticala.
- Doua mapari de la trafic la resurse: QoS-prioritizata (ceil, Ec. 3) si cost-prioritizata (floor, Ec. 4).
- Invatare centralizata (CL, TensorFlow) comparata cu invatare federata (PyTorch + PySyft), in doua variante: FL fara model averaging (modelul global trece secvential prin gazde) si FL cu model averaging (FedAvg).
- Prototip de orchestrare Kubernetes "AI-driven": bucla MAPE (Monitor-Analyze-Plan-Execute) extinsa peste Kubernetes; kubelet = Monitor, modelul CL/FL = Analyze+Plan, kube-scheduler (replica sets / update deployment) = Execute; comparat cu HPA/VPA native (reactive). Comunicatia master-workers pentru FL prin websocket.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Date: trafic real de la un operator comercial, 3 statii de baza, 43 zile consecutive, esantionare orara (3096 esantioane; 3072 folosite in simulare), impartire 60/20/20 train/val/test (Sec. IV-D, Tabel I). Setul nu poate fi publicat (NDA).
- Simulare: 3 ME host-uri, max 10 VNF per gazda, 1000 millicore per VNF, pas vertical de 100 millicore; 10 rulari per caz; FL cu 4 workeri virtuali PySyft (1 server + 3 ME host) (Sec. VI-A).
- Prototip (Sec. V-B, V-C, VI-C): platforma MEC "lightMEC" (LTE base station, LTE core network, mobile edge host cu Open vSwitch, Click modular router, elemente S1AP Monitor si GTP encap/decap), aplicatie MEC = web server nginx in containere; cluster Kubernetes cu 1 master si 3 workeri (ME host, Intel Core i7 1.8 GHz, 4 nuclee), retea overlay Flannel, Prometheus/Grafana, Metrics Server. Pentru prototip se presupune granularitate de 5 minute in loc de 1 ora; sarcina generata ca cereri web (Fig. 9, ~80 minute). Config reactiv: HPA la 30 s, toleranta 5%, prag 100 millicore, asteptare 3 min dupa scale-up si 5 min dupa scale-down; VPA la 10 s, mod Auto, asteptare ~5 min.

## Experimente si metrici
MAE, MSE, RMSE (box plots, se compara medianele) pentru: Naive (persistence sezonier, 24 h) vs FFNN vs LSTM vs CNN-LSTM, pentru ambele obiective (Fig. 6); encoder-decoder la pasii 1-3 (Fig. 7); CL vs FL (Fig. 8, Tabel II). In prototip: round-trip-time mediu si numar de containere/unitati CPU in timp, reactiv vs predictiv (Fig. 10-11), QoS vs cost (Fig. 12), CL vs FL pentru scalare orizontala si verticala (Fig. 13-14). Cautare hiperparametri prin grid search si "baby-sitting" (Sec. IV-E).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- QoS-prioritizat, CL, un pas (Fig. 6): CNN-LSTM 0.54 MAE / 1.36 MSE / 1.16 RMSE; LSTM 0.55 / 1.39 / 1.17; FFNN 0.64 / 1.42 / 1.19; Persistence 4.35 / 13.94 / 3.73.
- Cost-prioritizat (Fig. 6): LSTM 0.31 / 1.01 / 1; FFNN 0.42 / 0.94 / 0.96; CNN-LSTM 0.44 / 1.44 / 1.2; Persistence 3.28 / 12.32 / 3.51.
- Encoder-decoder (Fig. 7): pasul 1 CNN-LSTM 0.06 / 0.01 / 0.06 vs LSTM 0.52 / 0.58 / 0.52; pasul 2 CNN-LSTM 0.08 / 0.01 / 0.08 vs LSTM 0.72 / 1.15 / 0.72; pasul 3 CNN-LSTM 0.18 / 0.07 / 0.18 vs LSTM 0.82 / 1.46 / 0.82.
- Tabel II (mediane, MAE/MSE/RMSE): FFNN CL 0.64/1.42/1.19, FL fara MA 3.12/11.62/3.40, FL cu MA 3.41/11.96/3.45; LSTM CL 0.55/1.32/1.14, FL fara MA 1.44/3.45/1.85, FL cu MA 1.49/3.62/1.9; CNN-LSTM CL 0.54/1.36/1.16, FL fara MA 1.62/3.8/1.94, FL cu MA 1.80/3.96/1.98.
- Prototip: autoscalingul reactiv reactioneaza lent la varfuri (asteptare 3-5 min HPA), cu RTT mai mare decat varianta predictiva (Fig. 10-11). La minutul 20 (Fig. 12): QoS-prioritizat 4 VNF cu RTT 76 (unitate de timp raportata "seconds" in text), cost-prioritizat 3 VNF cu RTT 106, deci cu 25% mai ieftin dar QoS mai slab. Modelele FL cresc RTT fata de CL; la scalarea verticala RTT este semnificativ mai mare decat la cea orizontala din cauza repornirii podurilor (Fig. 14).

## Limitari declarate de autori
- FL mai slab decat CL din cauza datelor non-IID pe gazde (distanta EMD).
- Antrenarea pe ME host maximizeaza CPU la 100% (i7 1.8 GHz, 4 nuclee), ceea ce incetineste restul proceselor; recunoscut ca dezavantaj al FL.
- Un caz (minutul 75, Fig. 12) in care reteaua QoS-prioritizata a prezis 9 containere vs 10 la cost-prioritizat, neexplicat din cauza naturii black-box; explicabilitate (XAI) ca lucru viitor.
- Setul de date nu include rafale scurte (medii orare), nu se cunoaste tipul de trafic (gamma constant); doar VNF stateless (fara migrare de stare); FL peer-to-peer in afara scopului; cautarea hiperparametrilor este costisitoare.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu - Sec. V-B: platforma foloseste LTE core (SGW/PGW/MME/HSS) si LTE base station, nu un core 5G; aplicatia scalata este un nginx
- UE reale sau emulate? nedeclarat (traficul este generat ca cereri web, Sec. VI-C, Fig. 9)
- digital twin al retelei? nu - nedeclarat in lucrare
- prezice efectul unei actiuni inainte de a o aplica? nu - Sec. IV-VI: se prezice incarcarea viitoare (forecasting), nu efectul unei actiuni de scalare
- executa actiuni automat (bucla inchisa)? da - Sec. V-C: bucla MAPE in prototipul Kubernetes, Execute prin replica sets / update deployment
- multi-site / geo-redundanta / failover de baza de date? nu - multi-domain cu 3 ME host si FL, dar fara failover de baza de date (Sec. IV-A); geo-redundanta nedeclarata
- evaluare prospectiva (predictie fixata inainte de experiment)? nu - Sec. VI: evaluare pe set de test retrospectiv (split 60/20/20); in prototip se reia traficul din dataset
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - metrici de RTT al aplicatiei MEC si erori de predictie (Sec. VI), nu inregistrari/sesiuni
- observa traficul la SCP / proxy? nu - nedeclarat (se colecteaza metrici CPU prin kubelet, Sec. V-C)
