# Digital-Twin assisted Root Cause Analysis of Anomalies in NFV Environment (2021)
NOTA: nota scrisa doar din rezumat; textul integral nu este disponibil din surse libere legale.
Cheie: Wang2021Digitaltwinrca . DOI/link: https://doi.org/10.1109/icc42927.2021.9500464 . Sursa textului: DOAR REZUMAT (OpenAlex)
Sectiunea din plan: C . Tema: digital twin / RCA NFV
Autori: Weili Wang, Qianbin Chen, Tong Liu, Lun Tang. IEEE ICC 2021.

## Problema (cum o formuleaza autorii)
NFV permite servicii noi cu cost de deployment mai mic, dar aduce probleme noi de management al defectelor. Anomaliile VM-urilor pot fi cauzate de componente defecte ale serverelor fizice pe care ruleaza sau de propagarea anomaliilor de la alte servere. Cand tiparele de date ale VM-urilor sunt detectate ca anormale, cauzele trebuie localizate precis, pentru recuperarea rapida a retelei (rezumat).

## Ce propun (metoda, pe scurt)
Un digital twin care capteaza in timp real matricea de dependenta anomalie-defect. Pe baza ei este formulata o problema dinamica de acoperire a multimilor (dynamic set-covering, DSC), modelata cu un set de modele Markov ascunse paralele, pentru a gasi la fiecare epoca de observare o multime minima de componente defecte care acopera toate VM-urile anormale. Problema DSC este descompusa cu ADMM in subprobleme independente, rezolvate distribuit (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Simulare (rezumat). Scara si parametrii sunt nedeclarati in rezumat.

## Experimente si metrici
Disponibilitatea si superioritatea algoritmului de RCA asistat de DT, in simulare (rezumat). Metricile si baseline-urile sunt nedeclarate in rezumat.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Nedeclarat in rezumat (nu sunt raportate cifre).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - mediu NFV generic simulat (VM-uri pe servere fizice) (rezumat).
- UE reale sau emulate?: nu se aplica - (rezumat)
- digital twin al retelei?: da (in termenii autorilor) - DT care mentine matricea de dependenta anomalie-defect in timp real (rezumat).
- prezice efectul unei actiuni inainte de a o aplica?: nu - DT-ul este folosit pentru localizarea cauzei, nu pentru evaluarea actiunilor (rezumat).
- executa actiuni automat (bucla inchisa)?: nu - localizare; recuperarea este mentionata ca scop (rezumat).
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu - simulare (rezumat).
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
