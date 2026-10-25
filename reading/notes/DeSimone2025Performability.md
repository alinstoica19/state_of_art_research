# Performability Management of 5G Service Chains with Rejuvenation: The Open5GS Use Case (2025)
NOTA: nota scrisa doar din rezumat; textul integral nu este disponibil din surse libere legale.
Cheie: DeSimone2025Performability . DOI/link: https://doi.org/10.1109/netsoft64993.2025.11080576 . Sursa textului: DOAR REZUMAT (OpenAlex)
Sectiunea din plan: C . Tema: performabilitate / disponibilitate core (model + testbed)
Autori: Luigi De Simone, Mario Di Mauro, M. Longo, Roberto Natella, F. Postiglione. IEEE NetSoft 2025.

## Problema (cum o formuleaza autorii)
Managementul performabilitatii (performanta si disponibilitate) a lanturilor de functii de serviciu (SFC) bazate pe 5G, inclusiv impactul software rejuvenation (rezumat).

## Ce propun (metoda, pe scurt)
Cadru stocastic care combina un model de cozi M/G/m pentru estimarea latentei cu Stochastic Reward Networks (SRN) pentru evaluarea disponibilitatii. Scopul este derivarea configuratiei 5G optime care respecta atat performanta (de exemplu un prag de intarziere), cat si disponibilitatea (de exemplu "five nines") (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Testbed bazat pe Open5GS, folosit pentru validarea modelului (rezumat). Generatorul de sarcina si scara sunt nedeclarate in rezumat.

## Experimente si metrici
Validarea modelului pe testbed; configuratii care echilibreaza performanta, disponibilitatea si utilizarea resurselor (rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Nedeclarat in rezumat (nu sunt raportate cifre).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - testbed Open5GS (rezumat).
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nu - nementionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica?: da (analitic) - modelul M/G/m + SRN estimeaza latenta si disponibilitatea configuratiilor, inclusiv cu rejuvenation, inainte de alegerea setarii (rezumat).
- executa actiuni automat (bucla inchisa)?: nedeclarat - rejuvenation este evaluat; automatizarea lui in bucla nu este precizata in rezumat.
- multi-site / geo-redundanta / failover de baza de date?: partial - disponibilitate (five nines) modelata; multi-site si failover de baza de date nu sunt mentionate (rezumat).
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
