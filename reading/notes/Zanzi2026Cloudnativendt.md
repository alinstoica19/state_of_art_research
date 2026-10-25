# From Monitoring to Prediction: Hands-on Experience on Building a Cloud-Native Network Digital Twin for 5G Core (2026)
Cheie: Zanzi2026Cloudnativendt . DOI/link: https://doi.org/10.1109/icc59461.2026.11587512 . Sursa textului: integral: PDF urcat de autor (From_Monitoring_to_Prediction_Hands-on_Experience_on_Building_a_Cloud-Native_Network_Digital_Twin_for_5G_Core.pdf)
Sectiunea din plan: A . Tema: digital twin
Autori: Lanfranco Zanzi, Xi Li, Marco Liebsch (NEC Laboratories Europe), Fujita Satoshi, Datta Kalaswan, Sagara Mio (NEC Corporation). ICC 2026; 6 pagini.

## Problema (cum o formuleaza autorii)
Autorii observa ca majoritatea studiilor despre digital twins in telecom se opresc la arhitecturi teoretice sau la simulari proprietare izolate. Lipseste un cadru concret pentru un NDT live, sincronizat continuu cu date operationale ale unei retele comerciale, care sa permita operare in bucla inchisa in timp real (Sectiunea I). Monitorizarea traditionala nu surprinde corelatiile dintre metrici si nu prezice. Este dat exemplul unei defectiuni in cascada intre pod-uri dependente (Fig. 1). Lucrarile analizate nu abordeaza un mediu comercial la scara mare, cu servicii heterogene si constrangeri de timp real (II).

## Ce propun (metoda, pe scurt)
- **Cadru NDT cloud-native** pentru managementul performantei unui core 5G comercial (III.A, Fig. 2). Componente:
  - stiva 5GC comerciala containerizata pe AWS EKS (AMF, SMF, UDM, UPF, PCF), cu un emulator UE/RAN proprietar;
  - InfluxDB ca depozit central de serii de timp, in locul apelurilor catre AWS S3;
  - serviciu de preprocesare a logurilor, metricilor si KPI-urilor;
  - Grafana pentru vizualizare;
  - modele AI/ML ca microservicii separate, expuse prin API-uri Flask;
  - un "Policy Maker", care in lucrare este doar viziune (III.A.6). Ar recomanda reconfigurari, de exemplu mai multe resurse sau un pod nou, iar efectul lor ar fi testat in NDT inainte de aplicarea in sistemul live.
- **Pipeline de date** (III.B):
  - normalizare la structura {timestamp, pod, key, value};
  - esantionare sincronizata la 15 s;
  - alerte convertite in caracteristici numerice;
  - normalizare per pod.
- **Model de predictie** (III.C, Fig. 6): Transformer encoder.
  - Arhitectura: proiectie densa la 64 dimensiuni, layer norm, multi-head attention cu 4 capete si key dimension 64, strat dens de 128 unitati ReLU, dropout 0,1, positional encodings.
  - Prezice CPU per pod, probabilitatea si severitatea alertelor, plus etichete de avertizare timpurie (de exemplu CPU ≥ 90% in orizont).
  - Antrenare: Adam cu learning rate 1e-4, batch 64, 50 de epoci, split 70/30, pe GPU NVIDIA A30 de 24 GB.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Testbed pe Kubernetes cu core 5G virtualizat comercial (AMF, SMF, UPF etc.) pe AWS, cu trafic de la emulatorul proprietar UE/RAN (III.A, IV.A).
- Telemetrie: metrici Kubernetes, metrici specifice NF-urilor, loguri de evenimente si alerte Prometheus.
  - peste 60 GB de loguri brute;
  - peste 500 de caracteristici individuale;
  - cateva zile de trace-uri operationale, inclusiv teste de stres sintetice si scenarii de trafic normal (IV.A).
- Numarul de UE si de pod-uri nu este declarat.
- Inferenta masurata pe GPU NVIDIA A30 si pe CPU Intel Xeon Gold 6248R limitat la un singur nucleu.

## Experimente si metrici
- Timpul de antrenare, RMSE pentru predictia CPU, MAE pentru predictia alertelor si a severitatii, in functie de WINDOW SIZE si FUTURE STEPS (Fig. 7a-d).
- Curbele de loss la FUTURE STEPS = 10 si un exemplu de predictie CPU pentru un pod AMF (Fig. 8).
- Latenta de inferenta pe CPU si GPU (Fig. 9).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Timpul de antrenare creste aproape liniar cu WINDOW SIZE si FUTURE STEPS (Fig. 7a).
- RMSE-ul pentru CPU creste cu orizontul: moderat pe termen scurt, mai pronuntat dincolo de cateva minute (Fig. 7b). MAE-urile pentru alerte si severitate cresc si ele cu orizontul (Fig. 7c-d).
- Loss-urile de antrenare si validare converg fara overfitting (Fig. 8 stanga). Predictia CPU pentru pod-ul AMF urmareste fluctuatiile pe termen scurt si netezeste usor varfurile (Fig. 8 dreapta).
- Inferenta pe CPU si GPU este comparabila, cu CPU-ul uneori mai rapid; tipic cateva milisecunde per batch (Fig. 9).
- Textul nu da valori numerice exacte de RMSE/MAE; acestea sunt doar in figuri.

## Limitari declarate de autori
Nu sunt declarate limitari explicite. Autorii noteaza ca eroarea creste cu orizontul de predictie si ca GPU-ul ar avea avantaj la modele mai mari (IV.B). Lucrari viitoare: Agentic AI pentru procesarea logurilor, extragerea de cunostinte si definirea recuperarii sistemului (V).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - core 5G comercial containerizat pe AWS EKS (III.A).
- UE reale sau emulate?: emulate - emulator UE/RAN proprietar (III.A).
- digital twin al retelei?: da - NDT definit de autori ca pipeline de telemetrie, stocare, vizualizare si predictie, sincronizat cu deployment-ul live (III).
- prezice efectul unei actiuni inainte de a o aplica?: propus, neevaluat - Policy Maker ar testa politicile recomandate in NDT inainte de aplicare (III.A.6). Evaluarea acopera doar predictia CPU si a alertelor.
- executa actiuni automat (bucla inchisa)?: nedeclarat in experimente - Concluzia afirma suport pentru operare in bucla inchisa (V), dar nu sunt raportate actiuni executate.
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu - split 70/30 pe date colectate.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu - metricile sunt CPU, memorie si alerte per pod.
- observa traficul la SCP / proxy?: nu.
