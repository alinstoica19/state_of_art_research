# Granomaly: A Framework for Anomaly Detection in 5G Core Network Control Plane Traffic with Temporal Graph Neural Networks (2025)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Fritz2025Granomaly . DOI/link: https://doi.org/10.1109/noms57970.2025.11073582 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: B

## Problema (cum o formuleaza autorii)
Autorii spun ca arhitectura bazata pe servicii din 5G core, separarea planurilor de control si utilizator, precum si integrarea ML/AI prin NWDAF au imbunatatit detectia anomaliilor, dar ramane dificila identificarea atacurilor necunoscute, in special in traficul criptat. Ei spun ca metodele ML actuale nu folosesc adesea structura de graf temporal a traficului de retea, ceea ce le limiteaza eficienta.

## Ce propun (metoda, pe scurt)
Granomaly, un framework de detectie a anomaliilor care foloseste Temporal Graph Neural Networks (TGNN) pentru a analiza traficul din planul de control din 5G core. Framework-ul include: un core 5G simulat, doua seturi de date de benchmark adaptate pentru detectia anomaliilor cu TGNN si aplicarea a doua metode TGNN.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Core-ul 5G este simulat ("a simulated 5G core network"). Include doua seturi de date de benchmark. Scara si detaliile unelte: nedeclarate in rezumat.

## Experimente si metrici
Rezumatul nu descrie metrici sau protocolul experimental.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Rezultatele sunt descrise calitativ: TGNN-urile "effectively detect subtle traffic anomalies", ceea ce autorii leaga de imbunatatirea robustetii si securitatii retelelor 5G. Cifre exacte: nedeclarat in rezumat. Trimitere la tabel/figura: nedeclarat in rezumat. Observatie: in textul extras din rezumat apare o ruptura de caractere ("TG NN s ... anomalies”), deci fraza exacta nu poate fi reconstituita fara textul integral.

## Limitari declarate de autori
nedeclarat in rezumat

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu - (rezumat): core-ul 5G este simulat ("a simulated 5G core network").
- UE reale sau emulate? nedeclarat - (rezumat): nu se specifica.
- digital twin al retelei? nedeclarat - (rezumat): nu se mentioneaza; rezumatul spune doar ca core-ul este simulat.
- prezice efectul unei actiuni inainte de a o aplica? nedeclarat - (rezumat): nu se mentioneaza.
- executa actiuni automat (bucla inchisa)? nedeclarat - (rezumat): nu se mentioneaza.
- multi-site / geo-redundanta / failover de baza de date? nedeclarat - (rezumat): nu se mentioneaza.
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat - (rezumat): nu se mentioneaza.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nedeclarat - (rezumat): nu se mentioneaza; rezumatul vorbeste despre trafic de plan de control.
- observa traficul la SCP / proxy? nedeclarat - (rezumat): nu se mentioneaza.
