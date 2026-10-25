# Availability and Reliability of Core Networks (4G/5G) From a Deployment Standpoint (2025)
NOTA: nota scrisa doar din rezumat; textul integral nu este disponibil din surse libere legale.
Cheie: Mandal2025Coreavailability . DOI/link: https://doi.org/10.1109/tsc.2025.3528332 . Sursa textului: DOAR REZUMAT (OpenAlex)
Sectiunea din plan: C . Tema: disponibilitate / fiabilitate core (model analitic)
Autori: Priyatosh Mandal (autor unic, conform metadatelor). IEEE Transactions on Services Computing, 2025.

## Problema (cum o formuleaza autorii)
Core-urile 4G LTE sau 5G service-based pot fi create ca un set de VNF-uri, adica un network service (NS), desfasurat pe o platforma cloud. Un VNF este o masina virtuala cu software specializat. Lucrarea analizeaza disponibilitatea si fiabilitatea NS in functie de plasarea nodurilor core (rezumat).

## Ce propun (metoda, pe scurt)
Model matematic al disponibilitatii NS pentru doua plasari: toate nodurile core intr-o singura VM (SVM) sau in mai multe VM-uri (MVM). Analiza ia in calcul defectele nodului gazda, ale VM-urilor si ale nodurilor core. Este analizata si fiabilitatea NS pentru cele doua plasari (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Analiza matematica (rezumat). Parametrii de defect si recuperare folositi sunt nedeclarati in rezumat.

## Experimente si metrici
Comparatia disponibilitatii si fiabilitatii NS bazate pe SVM vs. MVM (rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Un deployment NS bazat pe SVM poate aduce un castig de peste 14% in disponibilitate si de peste 100% in fiabilitate fata de un deployment MVM (rezumat).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - model matematic al unui NS de VNF-uri core 4G/5G (rezumat).
- UE reale sau emulate?: nu se aplica - (rezumat)
- digital twin al retelei?: nu - nementionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica?: partial - modelul estimeaza analitic disponibilitatea si fiabilitatea pentru plasari alternative inainte de deployment (rezumat).
- executa actiuni automat (bucla inchisa)?: nu - (rezumat)
- multi-site / geo-redundanta / failover de baza de date?: partial - sunt modelate defectele gazdei, VM-urilor si nodurilor core; multi-site si failover de baza de date nu sunt mentionate (rezumat).
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu - metrici de disponibilitate si fiabilitate (rezumat).
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
