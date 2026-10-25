# Neutrino: A Fast and Consistent Edge-Based Cellular Control Plane (2023)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.

Cheie: Ahmad2023Neutrino . DOI/link: https://doi.org/10.1109/tnet.2022.3202496 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: C . Tema: nedeclarata

## Problema (cum o formuleaza autorii)
Retelele 5G si urmatoarele generatii vizeaza tactile internet si aplicatii imersive in timp real, cu latenta foarte mica si fiabilitate foarte mare, ceea ce impune cerinte noi asupra core-ului celular. Control plane-ul este o componenta cheie: timpul de finalizare a operatiilor de control (de exemplu mobility handoff, service establishment) afecteaza direct intarzierea resimtita de aplicatiile utilizatorilor finali.

## Ce propun (metoda, pe scurt)
Neutrino, un control plane celular care ofera utilizatorilor abstractia unui acces fiabil la serviciile celulare, cu latenta redusa. Detaliile mecanismelor interne sunt nedeclarate in rezumat.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Rezumatul mentioneaza "testbed evaluations" bazate pe trace-uri reale de trafic de control celular. Unelte, scara (nr. UE, NF, noduri) si detalii de implementare: nedeclarate in rezumat.

## Experimente si metrici
Timp de finalizare a procedurilor de control (fara defecte si in prezenta defectelor de control plane); performanta aplicatiilor AR/VR si a masinilor autonome. Restul: nedeclarat in rezumat.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Conform rezumatului: imbunatatire a timpilor de finalizare a procedurilor de control de pana la 3.1x fara defecte si pana la 5.6x in prezenta defectelor de control plane, fata de 5G existent. Pentru aplicatii: imbunatatiri de pana la 2.5x (AR/VR) si 2.8x (self-driving cars). Trimiteri la tabele/figuri: nedeclarate in rezumat.

## Limitari declarate de autori
Nedeclarate in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nedeclarat (rezumatul vorbeste de testbed, fara detalii despre implementare)
- UE reale sau emulate? nedeclarat
- digital twin al retelei? nedeclarat
- prezice efectul unei actiuni inainte de a o aplica? nedeclarat
- executa actiuni automat (bucla inchisa)? nedeclarat
- multi-site / geo-redundanta / failover de baza de date? nedeclarat (rezumatul mentioneaza evaluare sub defecte de control plane, fara alte detalii)
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nedeclarat (se masoara timpi de finalizare a procedurilor si performanta aplicatiilor, conform rezumatului)
- observa traficul la SCP / proxy? nedeclarat
