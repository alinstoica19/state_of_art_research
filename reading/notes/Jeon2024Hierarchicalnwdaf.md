# Hierarchical Network Data Analytics Framework for 6G Network Automation: Design and Implementation (2024)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Jeon2024Hierarchicalnwdaf . DOI/link: https://doi.org/10.1109/mic.2024.3369939 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Rezumatul spune ca gestionarea modularizata a functiilor de retea 5G necesita automatizare, iar un NWDAF conventional face atat inferenta, cat si antrenarea. Pentru un numar crescut de cereri de analiza, este greu de furnizat rezultatele in timp util functiilor de retea.

## Ce propun (metoda, pe scurt)
Un framework ierarhic de analiza (H-NDAF) in care taskurile de inferenta sunt distribuite mai multor leaf NWDAF, iar antrenarea se face la root NWDAF. Este prezentat un caz de utilizare pentru optimizarea politicii pentru fluxurile de date ale echipamentelor utilizator (UE).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Tip de testbed (real, emulat sau simulat): simulare ("extensive simulation results").
Unelte: software open source free5GC.
Scara: nedeclarata in rezumat.
Date: nedeclarate in rezumat.

## Experimente si metrici
Simulari in care sunt comparate acuratetea analizelor si timpul de furnizare a analizelor fata de NWDAF-ul conventional. Valorile metricilor nu sunt precizate.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Nu sunt raportate cifre in rezumat. Rezultatele declarate sunt calitative: H-NDAF furnizeaza rezultate "sufficiently accurate" si "faster analytics provision time" comparativ cu NWDAF-ul conventional. Fara trimitere la tabel/figura.

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nedeclarat - (rezumat): simularea foloseste free5GC; nu este detaliat statutul nucleului in simulare.
- UE reale sau emulate? nedeclarat - (rezumat): simulare; UE-urile nu sunt descrise.
- digital twin al retelei? nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica? nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)? nedeclarat - (rezumat): cazul de utilizare optimizeaza o politica, fara a detalia o bucla inchisa.
- multi-site / geo-redundanta / failover de baza de date? nedeclarat - (rezumat): inferenta este distribuita pe mai multi leaf NWDAF; nu se mentioneaza multi-site sau failover.
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nedeclarat - (rezumat)
- observa traficul la SCP / proxy? nedeclarat - (rezumat)
