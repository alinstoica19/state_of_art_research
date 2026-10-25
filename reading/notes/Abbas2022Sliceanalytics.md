# Ensemble Learning-based Network Data Analytics for Network Slice Orchestration and Management: An Intent-Based Networking Mechanism (2022)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Abbas2022Sliceanalytics . DOI/link: https://doi.org/10.1109/noms54207.2022.9789706 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Rezumatul spune ca orchestrarea si gestionarea autonoma a slicing-ului de retea end-to-end este critica, din cauza configurarii complexe a infrastructurii de baza. Analiza datelor este vazuta ca un mod de a gestiona proactiv resursele de retea; NWDAF din 5G SBA permite utilizarea tehnicilor AI/ML.

## Ce propun (metoda, pe scurt)
Un mecanism in bucla inchisa cu doua parti: (1) un mecanism de networking bazat pe intentii (IBN) pentru controlul, orchestrarea si gestionarea slicing-ului E2E; (2) un mecanism de analiza a datelor care foloseste algoritmi hibrizi de ensemble learning (EL) pentru predictia utilizarii resurselor si pentru detectia si mitigarea anomaliilor. Este propus un model de stacking ensemble learning (STEL) pentru predictia utilizarii resurselor. Modelele ML ajuta platforma IBN sa actualizeze si sa gestioneze proactiv resursele.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Tip de testbed (real, emulat sau simulat): nedeclarat in rezumat.
Unelte: modelul STEL (stacking ensemble learning), platforma IBN (detalii nedeclarate).
Scara: nedeclarata in rezumat.
Date: nedeclarate in rezumat.

## Experimente si metrici
Compararea modelului STEL pentru predictia utilizarii resurselor cu modele state-of-the-art. Metricile raportate sunt acuratetea predictiei si eroarea.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Modelul STEL "enhanced accuracy by approximately up to 20%" si "reduced the error by 45%" fata de modelele state-of-the-art. Rezumatul nu contine trimitere la tabel/figura.

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nedeclarat - (rezumat)
- UE reale sau emulate? nedeclarat - (rezumat)
- digital twin al retelei? nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica? nedeclarat - (rezumat): predictia vizeaza utilizarea resurselor, fara efectul unei actiuni.
- executa actiuni automat (bucla inchisa)? da - (rezumat): mecanism descris ca "closed-loop", in care modelele ML ajuta platforma IBN sa gestioneze resursele proactiv.
- multi-site / geo-redundanta / failover de baza de date? nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nedeclarat - (rezumat)
- observa traficul la SCP / proxy? nedeclarat - (rezumat)
