# Revamping the Resilience and High Availability of 5G Core for 6G Ready Network Slices (2023)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Vittal2024Resilientcore . DOI/link: https://doi.org/10.1109/tnsm.2023.3348137 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Autorii descriu arhitectura bazata pe servicii a 5G Core (5GC), care poate fi implementata cu Network Function Virtualization (NFV) in forma de network slices. Spun ca diversitatea serviciilor din slice-uri ridica provocari pentru operatorii de retea in proiectarea unui 5GC robust, scalabil si rezilient.

## Ce propun (metoda, pe scurt)
Propun un 5GC auto-rezilient care combina Column Generation (CG) bazat pe Integer Linear Programming cu Deep Learning (LSTM), intr-o closed loop automation cu paradigma Self Organizing Network. In situatii neprevazute de supraincarcare si defectare a instantelor de serviciu, tehnica CG imbunatateste planificarea si servirea cererilor din planul de control. Metoda LSTM prezice disponibilitatea instantelor de serviciu ale Network Functions (NF) din 5GC. Prin derivarea numarului optim de instante pentru fiecare NF, abordarea este descrisa ca sustinand scalarea si reconfigurarea slice-urilor.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Nedeclarat in rezumat: rezumatul nu precizeaza testbed-ul, simularea, scara sau datele.

## Experimente si metrici
Comparatie a tehnicii CG cu solutiile state-of-the-art existente, pe numarul de cereri ale utilizatorilor abandonate in slice-urile delay-tolerant si delay-sensitive. Pentru LSTM se raporteaza acuratetea de invatare.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- CG abandoneaza cu 15% mai putine cereri in slice-urile delay-tolerant si cu 5% mai putine in slice-urile delay-sensitive, fata de solutiile state-of-the-art existente
- LSTM: 95% learning accuracy, pentru predictia disponibilitatii instantelor NF
Trimitere la tabel/figura: nedeclarata in rezumat.

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - (rezumat): se mentioneaza construirea unui 5GC, fara detalii despre implementare
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat): LSTM prezice disponibilitatea instantelor NF, fara legatura explicita cu o actiune
- executa actiuni automat (bucla inchisa)?: da - (rezumat): closed loop automation cu Self Organizing Network
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: da - (rezumat): numarul de cereri ale utilizatorilor abandonate
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
