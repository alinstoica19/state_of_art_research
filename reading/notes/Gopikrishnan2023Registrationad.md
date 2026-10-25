# Anomaly Detection using a Semi-Supervised Deep Learning Model on Open 5G Core Metrics during User-Equipment Registration (2023)
Cheie: Gopikrishnan2023Registrationad . DOI/link: https://doi.org/10.1109/cscn60443.2023.10453203 . Sursa textului: DOAR REZUMAT
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Sectiunea din plan: B
## Problema (cum o formuleaza autorii)
Examinarea si detectia anomaliilor in metricile cheie ale modulelor NF din core, in timpul inregistrarii echipamentului utilizator (UE), este considerata importanta pentru QoS in retelele 5G. Autorii spun ca metodele de monitorizare existente trec adesea cu vederea aceste abordari de detectie a anomaliilor din perspectiva planului de date.
## Ce propun (metoda, pe scurt)
Autorii se concentreaza exclusiv pe modelul semi-supervizat LSTM AutoEncoder (LSTM AE) pentru detectia anomaliilor. Se analizeaza metricile de CPU si memorie in timpul inregistrarii UE, iar anomaliile legate de stres sunt identificate.
## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Simulari efectuate pe Open 5G Core. Scara si volumul datelor: nedeclarat in rezumat.
## Experimente si metrici
Simulari in timpul inregistrarii UE, cu analiza metricilor de CPU si memorie ale modulelor NF. Metrica de acuratete este mentionata; alte metrici: nedeclarat in rezumat.
## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Modelul LSTM AE atinge o acuratete "over 97%" si ofera, conform autorilor, performanta superioara de detectie cu mai putine false positives. Tabel/figura: nedeclarat in rezumat.
## Limitari declarate de autori
Nedeclarat in rezumat.
## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - (rezumat: simulari efectuate pe Open 5G Core)
- UE reale sau emulate?: nedeclarat - (rezumat: se mentioneaza simulari si inregistrarea UE, dar nu se precizeaza daca UE sunt reale sau emulate)
- digital twin al retelei?: nedeclarat - (rezumat: nu mentioneaza)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat: nu mentioneaza)
- executa actiuni automat (bucla inchisa)?: nedeclarat - (rezumat: descrie detectia anomaliilor)
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat: nu mentioneaza)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat: nu mentioneaza)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu - (rezumat: metricile analizate sunt CPU si memorie ale modulelor NF in timpul inregistrarii UE, nu date la nivel de utilizator)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat: nu mentioneaza SCP sau proxy)
