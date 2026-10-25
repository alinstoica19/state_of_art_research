# Deep Learning-Based Proactive Anomaly Detection for 5G Core Control Plane Network Function Interactions (2025)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Tan20255Gcguard . DOI/link: https://doi.org/10.1109/tccn.2025.3539660 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: B

## Problema (cum o formuleaza autorii)
Autorii spun ca Service-Based Architecture (SBA) din 3GPP face ca NF-urile critice din 5G CN sa fie mai vulnerabile la atacuri, din cauza vulnerabilitatilor interne ale NF-urilor implementate in software sau a interfetelor extinse aduse de SBA. Ei mentioneaza ca studiile existente privind securitatea 5G acorda putina atentie detectiei comportamentelor anormale ale NF-urilor din planul de control.

## Ce propun (metoda, pe scurt)
5GCGuard, o schema de detectie a anomaliilor care identifica interactiuni anormale intre NF-uri in 5G CN. Un model secvential bazat pe deep learning invata tiparele normale de interactiune si detecteaza anomaliile prin abaterea de la tiparul invatat. Elemente de design mentionate: mecanism de atentie (attention), multi-task learning, etichetare probabilista (probabilistic labeling) si decizia automata a pragului.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Autorii stabilesc un "cloud-native 5G testbed" pentru a evalua 5GCGuard. Detalii despre testbed, unelte si scara: nedeclarate in rezumat.

## Experimente si metrici
"Extensive evaluation" fata de scheme de comparatie; studii de caz care demonstreaza detectia proactiva a diferitelor tipuri de anomalii de interactiune NF. Metrici: nedeclarate in rezumat.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Rezultatele sunt descrise calitativ: autorii spun ca 5GCGuard are "superiority over comparison schemes" si ca studiile de caz arata ca detecteaza proactiv diverse anomalii de interactiune NF. Cifre exacte: nedeclarat in rezumat. Trimitere la tabel/figura: nedeclarat in rezumat.

## Limitari declarate de autori
nedeclarat in rezumat

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nedeclarat - (rezumat): se mentioneaza un "cloud-native 5G testbed", fara detalii despre componente.
- UE reale sau emulate? nedeclarat - (rezumat): nu se specifica.
- digital twin al retelei? nedeclarat - (rezumat): nu se mentioneaza.
- prezice efectul unei actiuni inainte de a o aplica? nedeclarat - (rezumat): rezumatul descrie detectia anomaliilor, nu predictia efectului unei actiuni.
- executa actiuni automat (bucla inchisa)? nedeclarat - (rezumat): rezumatul spune ca detectia permite "swift action to block attacks", fara a descrie o actiune executata automat.
- multi-site / geo-redundanta / failover de baza de date? nedeclarat - (rezumat): nu se mentioneaza.
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat - (rezumat): nu se mentioneaza.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nedeclarat - (rezumat): nu se mentioneaza; rezumatul vorbeste despre interactiuni intre NF-uri.
- observa traficul la SCP / proxy? nedeclarat - (rezumat): nu se mentioneaza.
