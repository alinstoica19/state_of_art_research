# Fair Federated Learning for Multi-Task 6G NWDAF Network Anomaly Detection (2024)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Zhang2025Fairfl . DOI/link: https://doi.org/10.1109/tits.2024.3461679 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
NWDAF din 6G permite operatorilor sa integreze analiza bazata pe ML pentru a identifica si trata comportamente anormale ale dispozitivelor utilizator. Autorii indica o problema de cerinte diferite ale sarcinilor atunci cand acelasi model ML este folosit pentru optimizarea mai multor sarcini. Modelul multi-task este folosit pentru detectia anomaliilor de trafic in diferite tipuri de dispozitive utilizator.

## Ce propun (metoda, pe scurt)
Aplicarea fair federated learning (FL) la arhitectura NWDAF din 3GPP, cu un model ML multi-task. Tehnica propusa: global alternating gradient projection (AGP), cu doua faze de proiectie a gradientului in fiecare iteratie, care actualizeaza sarcinile la intervale regulate si ofera o versiune regularizata a gradientului functiei obiectiv multi-task.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Rezultatele sunt descrise ca "simulation results". Tipul exact al simulatorului, unelte, scara si seturile de date: nedeclarate in rezumat.

## Experimente si metrici
Evaluare experimentala a modelului multi-task si a FL propus. Metricile exacte (de performanta de detectie si de overhead de comunicare): nedeclarate in rezumat.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Autorii afirma ca modelul multi-task propus detecteaza simultan anomaliile de trafic ale diferitelor tipuri de dispozitive, ca depaseste modelele state-of-the-art in detectia anomaliilor multi-task, si ca FL propus are un overhead de comunicare mai mic decat NWDAF traditional, fara a afecta performanta ML. Rezumatul nu contine cifre si nu trimite la tabele sau figuri.

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - (rezumat: aplicat arhitecturii NWDAF din 3GPP; nu e precizat daca exista un core 5G implementat)
- UE reale sau emulate?: nedeclarat - (rezumat: "simulation results", fara UE reale sau emulate mentionate)
- digital twin al retelei?: nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: nedeclarat - (rezumat)
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat: detectie de anomalii pe tipuri de dispozitive utilizator; nu sunt precizate inregistrari sau sesiuni)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
