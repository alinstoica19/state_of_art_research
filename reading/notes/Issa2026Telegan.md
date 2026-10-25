# TeleGAN-Core: A BiLSTM Dual-Autoencoder GAN for 5G Core Anomaly Detection (2026)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Issa2026Telegan . DOI/link: https://doi.org/10.1109/access.2026.3699648 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: B

## Problema (cum o formuleaza autorii)
Autorii spun ca pipeline-urile AIOps din 5GC proceseaza mii de fluxuri de telemetrie corelate, iar detectia anomaliilor in serii de timp multivariate (MTS) este dificila din cauza: cuplarii intre metrici (cross-metric coupling) provocate de contoare comune si masuratori derivate, non-stationaritatii provocate de actualizari software si de fluctuatiile traficului, si a etichetarii limitate a incidentelor.

## Ce propun (metoda, pe scurt)
TeleGAN-Core, o retea generativ-adversariala (GAN) pentru detectia anomaliilor de tip one-class in metricile de performanta 5GC. Atat generatorul, cat si un critic bazat pe autoencoder sunt implementate cu autoencodere BiLSTM. Criticul este antrenat ca model de "reconstruction energy", iar erorile de reconstructie ale generatorului si ale criticului sunt combinate printr-un scor de anomalie ponderat. Un pipeline de preprocesare cu caracteristici 5GC standardizeaza metricile eterogene si construieste fluxuri multivariate orientate pe servicii, pentru fiecare functie de retea si interfata.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Evaluare pe "production 5GC telemetry" (telemetrie de productie 5GC) si pe benchmark-urile industriale publice SWaT si WADI, folosind un protocol experimental unificat. Scara datelor si detaliile de productie: nedeclarat in rezumat.

## Experimente si metrici
Comparatie cu baseline-uri recurente, adversariale si bazate pe transformer ("the evaluated recurrent, adversarial, and transformer-based baselines"). Aspecte evaluate: performanta detectiei anomaliilor, echilibrul dintre precision si recall in conditii de dezechilibru de clase, si intarzierea detectiei la scara operationala de agregare.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Rezultatele sunt descrise calitativ: modelul "achieves stronger anomaly-detection performance" decat baseline-urile evaluate pe aceste seturi de date; pe telemetria 5GC detecteaza "most labeled anomaly episodes"; intarzierea de detectie este "low" la scara operationala de agregare. Cifre exacte: nedeclarat in rezumat. Trimitere la tabel/figura: nedeclarat in rezumat.

## Limitari declarate de autori
nedeclarat in rezumat

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nedeclarat - (rezumat): se mentioneaza telemetrie de productie 5GC, fara detalii despre implementarea core-ului.
- UE reale sau emulate? nedeclarat - (rezumat): nu se specifica.
- digital twin al retelei? nedeclarat - (rezumat): nu se mentioneaza.
- prezice efectul unei actiuni inainte de a o aplica? nedeclarat - (rezumat): nu se mentioneaza; rezumatul descrie detectia anomaliilor.
- executa actiuni automat (bucla inchisa)? nedeclarat - (rezumat): rezumatul vorbeste despre monitorizare aproape in timp real si despre "mitigate" doar ca obiectiv general al pipeline-urilor AIOps, fara a descrie actiuni executate.
- multi-site / geo-redundanta / failover de baza de date? nedeclarat - (rezumat): nu se mentioneaza.
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat - (rezumat): nu se mentioneaza.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nedeclarat - (rezumat): nu se mentioneaza; datele sunt metrici de telemetrie.
- observa traficul la SCP / proxy? nedeclarat - (rezumat): nu se mentioneaza.
