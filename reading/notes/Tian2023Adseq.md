# ADSeq-5GCN: Anomaly Detection from Network Traffic Sequences in 5G Core Network Control Plane (2023)
Cheie: Tian2023Adseq . DOI/link: https://doi.org/10.1109/hpsr57248.2023.10147931 . Sursa textului: DOAR REZUMAT
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Sectiunea din plan: B
## Problema (cum o formuleaza autorii)
Arhitectura bazata pe servicii (SBA) a 5G Core (5GC) largeste interfetele; unele NF-uri cheie pot deveni mai vulnerabile la NF-uri ostile interne sau la entitati externe malitioase, ceea ce ameninta componentele planului de control din 5GCN.
## Ce propun (metoda, pe scurt)
ADSeq-5GCN, un framework de detectie a anomaliilor la nivel de retea, bazat pe modelarea secventelor de trafic de retea. Se capteaza si se analizeaza traficul din planul de control al 5GCN. Se foloseste un Bi-LSTM pentru a invata interactiunile normale NF-la-NF si a detecta anomalii pe baza predictiei incorecte a evenimentelor de serviciu.
## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Testbed 5GCN cu Free5GC si UERANSIM. Scara si volumul datelor: nedeclarat in rezumat.
## Experimente si metrici
Evaluare pe testbed-ul 5GCN in mai multe scenarii. Metricile utilizate: nedeclarat in rezumat.
## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Autorii raporteaza ca metoda propusa are performanta "overwhelming" fata de modelele de baza (baselines). Cifre exacte: nedeclarat in rezumat.
## Limitari declarate de autori
Nedeclarat in rezumat.
## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - (rezumat: testbed 5GCN cu Free5GC si UERANSIM)
- UE reale sau emulate?: nedeclarat - (rezumat: se mentioneaza UERANSIM, dar nu se precizeaza daca UE sunt reale sau emulate)
- digital twin al retelei?: nedeclarat - (rezumat: nu mentioneaza un digital twin)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat: predictia se face pe evenimente de serviciu, nu pe efectul unei actiuni)
- executa actiuni automat (bucla inchisa)?: nedeclarat - (rezumat: descrie doar detectia anomaliilor)
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat: nu mentioneaza)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat: nu mentioneaza)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat: nu mentioneaza)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat: se captureaza traficul din planul de control; SCP si proxy nu sunt mentionate)
