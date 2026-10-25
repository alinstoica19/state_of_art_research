# Deep Learning-Based Log Anomaly Detection for 5G Core Network (2023)
Cheie: Tan2023Loganomaly . DOI/link: https://doi.org/10.1109/iccc57788.2023.10233555 . Sursa textului: DOAR REZUMAT
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Sectiunea din plan: B
## Problema (cum o formuleaza autorii)
Adoptarea virtualizarii functiilor de retea (NFV) in core-ul 5G aduce flexibilitate, dar si complexitate crescuta si probabilitate mai mare de anomalii. Cercetarile existente se concentreaza pe anomalii externe, detectate prin analiza traficului de retea; autorii mentioneaza nevoia de a identifica abnormalitati si defecte interne din 5G CN.
## Ce propun (metoda, pe scurt)
Un framework de detectie a anomaliilor din loguri, bazat pe deep learning (DL), pentru 5G CN. Framework-ul cuprinde parsarea logurilor, gruparea logurilor, extragerea de caracteristici (feature extraction) si antrenarea modelului; fiecare modul are functii distincte, pentru utilizare combinata in situatii diferite.
## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Un testbed 5G nativ cloud (cloud-native) pentru colectarea unui set de date cu loguri de 5G CN de volum mare, in care sunt injectate mai multe tipuri de anomalii. Volumul exact si uneltele: nedeclarat in rezumat.
## Experimente si metrici
Evaluarea se face pe datele colectate; metrica mentionata este scorul F1. Alte detalii: nedeclarat in rezumat.
## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
"Cel mai bun F1 score obtinut depaseste 97%" (cifra exacta din rezumat: "exceeds 97%"). Tabel/figura: nedeclarat in rezumat.
## Limitari declarate de autori
Nedeclarat in rezumat.
## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - (rezumat: se mentioneaza un testbed 5G cloud-native, fara detalii despre implementarea core-ului)
- UE reale sau emulate?: nedeclarat - (rezumat: nu mentioneaza)
- digital twin al retelei?: nedeclarat - (rezumat: nu mentioneaza)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat: nu mentioneaza)
- executa actiuni automat (bucla inchisa)?: nedeclarat - (rezumat: descrie detectia din loguri, nu actiuni automate)
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat: nu mentioneaza)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat: nu mentioneaza)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat: nu mentioneaza)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat: sursa datelor sunt logurile; SCP si proxy nu sunt mentionate)
