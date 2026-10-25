# Autoscaling Packet Core Network Functions with Deep Reinforcement Learning (2023)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Singh2023Drlautoscaling . DOI/link: https://doi.org/10.1109/noms56928.2023.10154312 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: B

## Problema (cum o formuleaza autorii)
Scalabilitatea functiilor de retea (NF) inseamna scalarea resurselor cloud alocate NF-urilor in functie de incarcarea de lucru, pentru a garanta QoS. Lucrarea investigheaza cum poate fi aplicat Deep Reinforcement Learning (DRL) ca solutie proactiva la aceasta problema.

## Ce propun (metoda, pe scurt)
Metoda DRL foloseste algoritmul Dueling Double Deep Q-network (D3QN), cu o functie de recompensa care tine cont de utilizarea resurselor si de incarcarea de lucru. Metoda DRL este comparata cu o abordare traditionala bazata pe praguri.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Testbed care ruleaza o functie open-source de packet core, furnizata de proiectul Magma. Scara si datele: nedeclarat in rezumat.

## Experimente si metrici
Comparatie intre metoda DRL si abordarea traditionala bazata pe praguri, pe testbed. Metrici mentionate: numarul de sesiuni picate si utilizarea resurselor.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Metodele de scalare bazate pe DRL imbunatatesc QoS prin reducerea numarului de sesiuni picate cu un factor de pana la 100, mentinand in acelasi timp utilizarea resurselor intr-un interval definit. Trimitere la tabel/figura: nedeclarat in rezumat.

## Limitari declarate de autori
nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - (rezumat); se mentioneaza un packet core open-source (Magma) pe testbed, dar 5G nu apare in rezumat
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat); scalarea este descrisa ca proactiva, dar nu se spune ca efectul actiunilor este prezis
- executa actiuni automat (bucla inchisa)?: da - (rezumat); metoda realizeaza autoscaling al resurselor cloud alocate NF-urilor
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: da - (rezumat); metrica principala este numarul de sesiuni picate
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
