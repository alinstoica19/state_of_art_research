# Monarch: Monitoring Architecture for 5G and Beyond Network Slices (2025)
NOTA: nota scrisa doar din rezumat; textul integral al versiunii TNSM nu este disponibil din surse libere legale. Exista pe arXiv (2306.01072v1) o versiune anterioara, de conferinta, cu titlu diferit (MonArch: Network Slice Monitoring Architecture for Cloud Native 5G Deployments); nu a fost folosita, fiind o alta lucrare.
Cheie: Saha2025Monarch . DOI/link: https://doi.org/10.1109/tnsm.2024.3479246 . Sursa textului: DOAR REZUMAT (OpenAlex)
Sectiunea din plan: C . Tema: monitorizare / observabilitate slice-uri
Autori: Niloy Saha, Nashid Shahriar, Muhammad Sulaiman, Noura Limam, Raouf Boutaba, Aladdin Saleh. IEEE Transactions on Network and Service Management (online 2024).

## Problema (cum o formuleaza autorii)
Algoritmii data-driven pentru orchestrarea si managementul automat al slice-urilor 5G depind de monitorizarea la timp si exacta a retelei. Monitorizarea trebuie sa acopere slice-urile end-to-end. Rezumatul enumera doua provocari: solutiile existente sunt fragmentate si nu coreleaza date din mai multe surse (segmente de retea); slice-urile diferite au cerinte diferite de KPI si granularitate, ceea ce cere ajustarea dinamica a KPI-urilor monitorizate si a ratelor de colectare, in timp real, pentru a reduce overhead-ul.

## Ce propun (metoda, pe scurt)
Monarch: arhitectura de monitorizare scalabila pentru deployment-uri 5G cloud-native, axata pe monitorizarea slice-urilor si calculul KPI-urilor per slice. Include un mecanism de monitorizare adaptiva, exemplificat printr-o euristica simpla.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Implementare pe un testbed de network slicing 5G, cu pana la 50 de slice-uri. Mecanismul adaptiv este evaluat pe un set de date 5G real (rezumat).

## Experimente si metrici
Doua scenarii: monitorizarea KPI-urilor la nivel de slice si la nivel de NF. Scalabilitate in functie de numarul de slice-uri (timp de ingestie). Overhead-ul si acuratetea monitorizarii adaptive.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Timp de ingestie constant intre 2,25 si 2,75 ms la numere variabile de slice-uri. Monitorizarea adaptiva reduce overhead-ul cu pana la 76%, cu acuratete descrisa ca acceptabila (rezumat; fara trimitere la tabel/figura).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - rezumatul mentioneaza un testbed 5G cloud-native cu slice-uri, fara a numi core-ul (rezumat).
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nu - nementionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: partial - ajustarea dinamica a ratelor de colectare (monitorizare adaptiva); actiuni asupra retelei nementionate (rezumat).
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu - metricile raportate sunt timp de ingestie si overhead de monitorizare (rezumat).
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
