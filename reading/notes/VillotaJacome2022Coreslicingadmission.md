# Admission Control for 5G Core Network Slicing Based on Deep Reinforcement Learning (2022)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: VillotaJacome2022Coreslicingadmission . DOI/link: https://doi.org/10.1109/jsyst.2022.3172658 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: B

## Problema (cum o formuleaza autorii)
Admission control-ul si alocarea resurselor sunt esentiale pentru network slicing, dar mecanismele existente se concentreaza pe slicing-ul radio access network (RAN). Lucrarea vizeaza slicing-ul in core-ul 5G, pentru cazurile de utilizare cu cerinte QoS distincte.

## Ce propun (metoda, pe scurt)
Doua solutii de admission control: SARA, bazata pe reinforcement learning, si DSARA, bazata pe deep reinforcement learning. Ambele tin cont de cerintele QoS ale cazurilor de utilizare 5G, diferentiaza nodurile core de nodurile edge si proceseaza cererile de slice-uri in ferestre de timp, pentru a favoriza profitul furnizorului de servicii si utilizarea resurselor.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Nedeclarat in rezumat.

## Experimente si metrici
Nedeclarat in rezumat. Rezumatul mentioneaza ca obiective profitul furnizorului si utilizarea resurselor, fara a descrie metricile experimentale.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Rezumatul nu contine cifre si nu trimite la tabel sau figura. Afirma ca SARA si DSARA depasesc mecanismele existente de admission control si alocare a resurselor pentru slicing-ul in core-ul 5G.

## Limitari declarate de autori
nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - (rezumat); se vorbeste despre slicing in core-ul 5G, dar nu se precizeaza daca este implementat sau modelat
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: nedeclarat - (rezumat); admission control-ul decide asupra cererilor de slice, dar nu se spune explicit ca bucla este inchisa
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
