# 5GShield: HTTP/2 Anomaly Detection in 5G Service-Based Architecture (2023)
Cheie: Wehbe2023Http2Anomaly . DOI/link: https://doi.org/10.23919/ifipnetworking57963.2023.10186410 . Sursa textului: DOAR REZUMAT
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Sectiunea din plan: B
## Problema (cum o formuleaza autorii)
Core-ul 5G foloseste HTTP/2 pentru comunicarea intre NF-uri din SBA. Utilizarea HTTP/2 introduce vulnerabilitati; atacul de tip HTTP/2 stream multiplexing poate cauza Denial of Service (DoS) in 5G SBA. Autorii afirma ca solutiile de detectie a anomaliilor bazate pe flow, folosite in web, nu detecteaza aceste atacuri in reteaua 5G.
## Ce propun (metoda, pe scurt)
5GShield, un framework de detectie a anomaliilor la nivel de aplicatie (application-layer), care foloseste retele neuronale, in particular un Autoencoder.
## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Se implementioneaza un testbed 5G, se simuleaza atacul HTTP/2 stream multiplexing si se colecteaza date HTTP/2. Unelte si scara: nedeclarat in rezumat.
## Experimente si metrici
Detectia atacului HTTP/2 stream multiplexing si comparatia cu o solutie de detectie a anomaliilor bazata pe flow. Metrica: F1-score.
## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
5GShield: F1-score 0.992. Solutia bazata pe flow: F1-score 0.78. Tabel/figura: nedeclarat in rezumat.
## Limitari declarate de autori
Nedeclarat in rezumat.
## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - (rezumat: se mentioneaza un testbed 5G, fara detalii despre implementarea core-ului)
- UE reale sau emulate?: nedeclarat - (rezumat: nu mentioneaza)
- digital twin al retelei?: nedeclarat - (rezumat: nu mentioneaza)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat: nu mentioneaza)
- executa actiuni automat (bucla inchisa)?: nedeclarat - (rezumat: descrie detectia, nu actiuni automate)
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat: nu mentioneaza)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat: nu mentioneaza)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat: nu mentioneaza; datele sunt HTTP/2)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat: se analizeaza trafic HTTP/2 la nivel de aplicatie intre NF-uri; locul de observare, SCP sau proxy, nu este precizat)
