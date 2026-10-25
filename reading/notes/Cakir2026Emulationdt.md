# Emulation Digital Twin Framework: Case Study on NGAP Attacks in 5G Control Plane (2026)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Cakir2026Emulationdt . DOI/link: https://doi.org/10.1109/iccworkshops63917.2026.11586630 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Autorii spun ca protocoalele de signalizare din planul de control 5G pot fi exploatate pentru atacuri Denial-of-Service (DoS). Contramasurile trebuie evaluate in conditii realiste, iar framework-urile de emulare curente ofera automatizare limitata, ceea ce impiedica analiza what-if la scara larga si iterativa.

## Ce propun (metoda, pe scurt)
Propun Emulation Digital Twin (EDT) Framework, o arhitectura modulara pe trei straturi: (i) Emulation Layer, care foloseste Containerlab, UERANSIM si un Open5GS extins cu signalling hooks proiectate; (ii) Digital Twin (DT) Layer, care formeaza o reprezentare pe baza de graf si include module de detectie si mitigare a atacurilor; (iii) Orchestration Layer, care automatizeaza generarea de scenarii, deployment-ul, injectia de trafic/atac si managementul experimentelor.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Emulare, cu Containerlab, UERANSIM si Open5GS extins. Scara si datele folosite: nedeclarate in rezumat.

## Experimente si metrici
Studiu de caz: atac DoS asupra protocolului NGAP, executat pe interfata N2 dintre gNB si AMF. Metrici mentionate: reducerea complexitatii configurarii experimentale, masurata in linii de cod, si consumul de resurse.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Rezumatul raporteaza o reducere a complexitatii configurarii experimentale cu 81% in linii de cod. Se mentioneaza un consum de resurse suplimentar minim, fara cifra in rezumat. Trimitere la tabel/figura: nedeclarata in rezumat.

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - (rezumat): Open5GS extins cu signalling hooks proiectate
- UE reale sau emulate?: nu - (rezumat): Emulation Layer cu UERANSIM; UE reale nu sunt mentionate
- digital twin al retelei?: da - (rezumat): Digital Twin (DT) Layer cu reprezentare pe baza de graf
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: nedeclarat - (rezumat): exista module de mitigare, fara detalii despre declansarea lor automata
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
