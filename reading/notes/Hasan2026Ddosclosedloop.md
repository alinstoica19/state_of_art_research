# From Detection to Policy: Calibrated and Explainable Closed-Loop DDoS Management in 5G/B5G Networks (2026)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Hasan2026Ddosclosedloop . DOI/link: https://doi.org/10.1109/tnsm.2026.3701638 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: B

## Problema (cum o formuleaza autorii)
Gestionarea in bucla inchisa a atacurilor DDoS in retelele 5G trebuie sa echilibreze blocarea atacurilor cu siguranta operationala, minimizand daunele colaterale asupra utilizatorilor legitimi. Autorii spun ca operatorii care folosesc NWDAF se confrunta cu un dilemă: solutiile de securitate bazate pe ML existente ofera clasificari binare, dar nu au un mecanism care sa transforme iesirile modelului in actiuni de mitigare cuantificabile, proportionale si automate.

## Ce propun (metoda, pe scurt)
Un framework in doua etape care mapeaza analiza de retea pe decizii de mitigare gradate, folosind o poarta de decizie calibrata pe risc si praguri de politica bazate pe severitate.
- Etapa 1: Isotonic Regression calibreaza iesirile modelului si declanseaza mitigarea doar pentru detectiile cu incredere mare, pentru a reduce daunele din falsele pozitive.
- Etapa 2: pentru amenintarile admise, Dynamic Mitigation Severity Score (DMSS) cuantifica severitatea prin agregarea contributiilor SHAP normalizate ale unor caracteristici cheie 5G.
- Pragurile, optimizate pentru a minimiza terminarile de utilizatori legitimi ("benign terminations"), aleg una dintre trei actiuni: Terminate, Throttle sau Monitor.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Experimentele sunt rulate pe un "public 5G DDoS testbed" (rezumatul nu spune daca testbed-ul este real sau emulat). Unelte mentionate: Isotonic Regression, SHAP. Scara, volumul de date si detaliile testbed-ului: nedeclarat in rezumat.

## Experimente si metrici
Comparatie cu baseline-uri de deep learning, despre care autorii spun ca sunt "prone to severe collateral damage". Metrici mentionate: acoperirea amenintarilor (threat coverage), numarul de terminari ale utilizatorilor legitimi, Expected Calibration Error (ECE) si fiabilitatea probabilitatilor. Analiza de sensibilitate asupra pragurilor de politica, in mai multe puncte de operare.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Rezultate descrise calitativ in rezumat: framework-ul "maintains high threat coverage while nearly eliminating benign terminations"; calibrarea "further reduces Expected Calibration Error (ECE)"; DMSS ranks volumetric floods as the most severe attacks; pragurile de politica raman stabile in analiza de sensibilitate. Cifre exacte: nedeclarat in rezumat. Trimitere la tabel/figura: nedeclarat in rezumat.

## Limitari declarate de autori
nedeclarat in rezumat

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nedeclarat - (rezumat): rezumatul mentioneaza un testbed 5G DDoS public, fara detalii despre implementarea core-ului.
- UE reale sau emulate? nedeclarat - (rezumat): nu se specifica.
- digital twin al retelei? nedeclarat - (rezumat): nu se mentioneaza.
- prezice efectul unei actiuni inainte de a o aplica? nedeclarat - (rezumat): rezumatul descrie selectia actiunii pe baza severitatii, nu o predictie a efectului ei.
- executa actiuni automat (bucla inchisa)? da - (rezumat): framework-ul "supports closed-loop mitigation"; rezumatul descrie selectia a trei actiuni (Terminate, Throttle, Monitor).
- multi-site / geo-redundanta / failover de baza de date? nedeclarat - (rezumat): nu se mentioneaza.
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat - (rezumat): nu se mentioneaza.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nedeclarat - (rezumat): se vorbeste despre "benign terminations", dar unitatea de masura nu este precizata.
- observa traficul la SCP / proxy? nedeclarat - (rezumat): nu se mentioneaza.
