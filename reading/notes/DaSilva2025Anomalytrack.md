# AnomalyTrack: Scalable and Self-Adaptive Anomaly Detection in Large-Scale 5G Networks (2025)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: DaSilva2025Anomalytrack . DOI/link: https://doi.org/10.1109/iscc65549.2025.11326411 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: B

## Problema (cum o formuleaza autorii)
Autorii spun ca retelele mobile de generatie urmatoare, care evolueaza de la 5G Stand-alone (5G SA) spre 6G, necesita adaptabilitate in timp real pentru a monitoriza implementari mari si dinamice. Metodele de monitorizare traditionale se confrunta cu volumul in crestere si interdependenta indicatorilor de performanta (KPI), ceea ce limiteaza eficienta detectiei bazate pe praguri (threshold-based).

## Ce propun (metoda, pe scurt)
AnomalyTrack, un framework scalabil si auto-adaptiv de detectie a anomaliilor care, potrivit rezumatului: (i) detaliaza parametrii exacti de implementare ai LOF, COF, IF-LOF, ARIMA si SARIMA, pentru reproductibilitate; (ii) specifica plasarea fizica si amprenta de resurse in interiorul 5G core; (iii) cuantifica ce KPI-uri contribuie cel mai mult la acuratetea detectiei.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Testat pe "one year of real-world data from a commercial Mobile Network Operator" (un an de date reale de la un operator comercial de retea mobila). Scara: 524019 serii de timp KPI, procesate la fiecare 30 de minute. Unelte: LOF, COF, IF-LOF, ARIMA, SARIMA. Rezumatul nu specifica daca exista un testbed separat.

## Experimente si metrici
Rezumatul mentioneaza acuratetea detectiei si latenta de inferenta; detalii despre protocolul experimental: nedeclarate in rezumat.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Acuratete de detectie de 97%.
- Latente de inferenta sub 5 s.
- 96.5% mai rapid decat monitorizarea conventionala (cifra este citita din formatarea LaTeX a rezumatului).
Trimitere la tabel/figura: nedeclarat in rezumat.

## Limitari declarate de autori
nedeclarat in rezumat

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nedeclarat - (rezumat): rezumatul descrie plasarea si amprenta de resurse in 5G core, dar nu spune ce implementare de core este folosita.
- UE reale sau emulate? nedeclarat - (rezumat): datele sunt reale, de la un operator comercial; rezumatul nu descrie UE-urile.
- digital twin al retelei? nedeclarat - (rezumat): nu se mentioneaza.
- prezice efectul unei actiuni inainte de a o aplica? nedeclarat - (rezumat): nu se mentioneaza.
- executa actiuni automat (bucla inchisa)? nedeclarat - (rezumat): rezumatul vorbeste despre "zero-touch automation" ca directie, fara a descrie actiuni automate executate.
- multi-site / geo-redundanta / failover de baza de date? nedeclarat - (rezumat): nu se mentioneaza.
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat - (rezumat): nu se mentioneaza.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nedeclarat - (rezumat): datele sunt serii de timp KPI; nu se mentioneaza inregistrari sau sesiuni.
- observa traficul la SCP / proxy? nedeclarat - (rezumat): nu se mentioneaza.
