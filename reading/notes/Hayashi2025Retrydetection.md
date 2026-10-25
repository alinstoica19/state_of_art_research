# Service Failure Detection via Connection Retry Analysis of User Traffic (2025)
NOTA: nota scrisa doar din rezumat; textul integral nu este disponibil din surse libere legale.
Cheie: Hayashi2025Retrydetection . DOI/link: https://doi.org/10.1109/noms57970.2025.11073597 . Sursa textului: DOAR REZUMAT (OpenAlex)
Sectiunea din plan: C . Tema: anomalii / detectie defecte din semnalizare
Autori: Naoki Hayashi, Fumio Katayama, Naoki Tateishi, Osamu Okino, Mitsuho Tahara. IEEE NOMS 2025.

## Problema (cum o formuleaza autorii)
Serviciile de telecomunicatii depind de multe echipamente si componente software; un singur defect sau o configurare gresita poate afecta serviciul. Uneori operatorii nu pot afla cauza sau nici macar daca a avut loc un defect, pentru ca mecanismele de monitorizare ale echipamentelor nu il detecteaza. Metodele conventionale se bazeaza pe volumul de trafic care intra si iese din echipamente si au dificultati cand fluctuatia volumului este mica (rezumat).

## Ce propun (metoda, pe scurt)
Metoda de detectie bazata pe observatia ca, la un defect sau la dificultati de comunicare, volumul diverselor semnale de control creste rapid, pentru restabilirea conexiunii utilizatorului. Metoda detecteaza aceasta crestere simultana a volumului semnalelor de control (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Evaluare pe date reale de trafic dintr-o retea de telecomunicatii (rezumat). Tipul retelei (4G/5G), interfetele observate si perioada sunt nedeclarate in rezumat.

## Experimente si metrici
Detectia defectelor si falsele detectii, comparate cu metodele conventionale bazate pe volum (rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Metoda detecteaza defecte greu de detectat de metodele conventionale, limitand falsele detectii (rezumat; fara cifre).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - date reale de operator; tipul de core nu este precizat in rezumat.
- UE reale sau emulate?: reale - trafic real de utilizatori (rezumat).
- digital twin al retelei?: nu - nementionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: nu - metoda de detectie (rezumat).
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: partial - reincercarile de conexiune ale utilizatorilor, observate in semnalizare (rezumat).
- observa traficul la SCP / proxy?: nedeclarat - semnalele de control observate; punctul de observare nu este precizat in rezumat.
