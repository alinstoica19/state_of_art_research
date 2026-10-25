# Unsupervised Graph-Sequence Anomaly Detection for 5G Core Network Control Plane Traffic (2023)
Cheie: Wang2023Graphsequence . DOI/link: https://doi.org/10.1109/icpads60453.2023.00230 . Sursa textului: DOAR REZUMAT
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Sectiunea din plan: B
## Problema (cum o formuleaza autorii)
5GC foloseste o arhitectura bazata pe servicii (SBA) care descompune planul de control in mai multe NF-uri independente, care expun interfete. Autorii spun ca acest lucru face planul de control mai expus la atacuri externe. Metodele existente de detectie a anomaliilor se concentreaza pe statistici de trafic si sunt greu de aplicat in planul de control 5GC.
## Ce propun (metoda, pe scurt)
GSAD, o metoda de detectie a anomaliilor bazata pe analiza graf-secventa, pentru traficul planului de control 5GC. Traficul este modelat ca un graf orientat, pentru informatia topologica si de interactiune intre NF-uri. Se folosesc normalizing flows cu dependente temporale pentru informatia secventiala. GSAD combina informatia topologica cu cea secventiala pentru detectie fina (fine-grained).
## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Testbed 5GC folosind Free5GC si UERANSIM. Scara si volumul datelor: nedeclarat in rezumat.
## Experimente si metrici
Evaluare in "various scenarios" pe testbed-ul 5GC, comparata cu metode de baza (baselines). Metricile: nedeclarat in rezumat (se mentioneaza performanta de detectie).
## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Autorii raporteaza ca framework-ul "outperforms the baselines significantly in terms of detection performance". Cifre exacte: nedeclarat in rezumat.
## Limitari declarate de autori
Nedeclarat in rezumat.
## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - (rezumat: testbed 5GC cu Free5GC si UERANSIM)
- UE reale sau emulate?: nedeclarat - (rezumat: se mentioneaza UERANSIM, dar nu se precizeaza daca UE sunt reale sau emulate)
- digital twin al retelei?: nedeclarat - (rezumat: nu mentioneaza)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat: nu mentioneaza)
- executa actiuni automat (bucla inchisa)?: nedeclarat - (rezumat: descrie detectia anomaliilor)
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat: nu mentioneaza)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat: nu mentioneaza)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat: nu mentioneaza)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat: se analizeaza traficul planului de control; SCP si proxy nu sunt mentionate)
