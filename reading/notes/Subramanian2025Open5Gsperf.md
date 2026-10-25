# Performance Evaluation of 5G Core Network Control-Plane Using Open5GS and Kubernetes (2025)
NOTA: nota scrisa doar din rezumat; textul integral nu este disponibil din surse libere legale.
Cheie: Subramanian2025Open5Gsperf . DOI/link: https://doi.org/10.1109/comsnets63942.2025.10885600 . Sursa textului: DOAR REZUMAT (OpenAlex)
Sectiunea din plan: C . Tema: core open-source / benchmarking control plane
Autori: Sooraj Subramanian M S, Madhan Raj Kanagarathinam, Krishna Moorthy Sivalingam. COMSNETS 2025 (conform DOI).

## Problema (cum o formuleaza autorii)
Control plane-ul 5G gestioneaza semnalizarea si functiile de control pentru conectivitate si livrarea serviciilor. Lucrarea isi propune o evaluare de performanta a control plane-ului unui core 5G desfasurat cu Open5GS si Kubernetes (rezumat).

## Ce propun (metoda, pe scurt)
Evaluare sistematica a latentei, throughput-ului si utilizarii resurselor la diverse niveluri de sarcina. Lucrarea genereaza si trace-uri de pachete in timp real din experimentul la scara mare, anuntate ca publice (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Testbed la scara mare cu peste 50.000 de UE simulate; Open5GS pe Kubernetes (rezumat). Generatorul de UE si dimensiunea clusterului sunt nedeclarate in rezumat.

## Experimente si metrici
Latenta, throughput si utilizarea resurselor sub diverse conditii de sarcina; scalabilitate si eficienta resurselor (rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Nedeclarat in rezumat (nu sunt raportate cifre). Autorii spun ca rezultatele ghideaza dimensionarea unui cluster Kubernetes pentru workload-ul 5G Core si alegerea NF-urilor prioritare pentru scalare (rezumat).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - Open5GS pe Kubernetes (rezumat).
- UE reale sau emulate?: emulate/simulate - peste 50.000 de UE simulate (rezumat).
- digital twin al retelei?: nu - nementionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: nu - evaluare de performanta (rezumat).
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - metricile sunt latenta, throughput si resurse; procedurile masurate nu sunt numite in rezumat.
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
