# SAMMF: A Self-Adaptive Multi-Model Fusion Framework for NWDAF Traffic Anomaly Detection (2025)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Zhang2025Sammf . DOI/link: https://doi.org/10.1109/lnet.2025.3579358 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Autorii indica NWDAF ca solutie pentru detectia traficului anormal in 5G core (5GC). Abordarile existente folosesc in general un singur model, care au dificultati in a trata eficient datele de la functii de retea (NF) diferite.

## Ce propun (metoda, pe scurt)
Framework-ul Self-Adaptive Multi-Model Fusion (SAMMF) pentru NWDAF, cu patru module: colectarea datelor (statistici si colectie), preprocesarea datelor (curatare si feature engineering), antrenarea multi-model self-adaptive (selecteaza modele cu performanta ridicata din biblioteca de modele, folosind un algoritm cu prag adaptiv) si fuziunea multi-model (combina rezultatele modelelor selectate pentru rezultatul final).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Evaluare pe doua seturi de date de detectie a anomaliilor de retea, mentionate ca fiind frecvent folosite (numele lor nu sunt indicate in rezumat). Testbed, emulare sau simulare: nedeclarate in rezumat. Unelte si scara: nedeclarate.

## Experimente si metrici
Comparatie cu metode de baza (baseline) existente, pe cele doua seturi de date. Metricile exacte: nedeclarate in rezumat.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Autorii afirma ca, comparativ cu metodele de baza, SAMMF are "avantaje semnificative" in tratarea datelor de la NF-uri diferite. Rezumatul nu contine cifre si nu trimite la tabele sau figuri.

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - (rezumat: detectie in 5GC; nu e precizat daca exista un core 5G implementat)
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: nedeclarat - (rezumat)
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
