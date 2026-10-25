# Dual Self-Attention is What You Need for Model Drift Detection in 6G Networks (2025)
Cheie: Ameur2025Driftdetection . DOI/link: https://doi.org/10.1109/tmlcn.2025.3576727 . Sursa textului: integral: PDF editor, licenta CC BY 4.0 (IEEE TMLCN)
Sectiunea din plan: C . Tema: MLOps / drift al modelelor
Autori: Mazene Ameur, Bouziane Brik, Adlen Ksentini (EURECOM; University of Sharjah). IEEE Transactions on Machine Learning in Communications and Networking, vol. 3, 2025. Finantare: proiectul Horizon 6G-DALI.

## Problema (cum o formuleaza autorii)
- AI/ML sunt prezentate ca baza arhitecturii si operarii 6G si a ZSM. Mediul dinamic duce la model drift: data drift (univariat sau multivariat), label drift si concept drift. Concept drift este considerat cel mai greu de detectat, pentru ca distributiile observabile pot ramane neschimbate (I, Fig. 1).
- Gap declarat (I.A):
  - metodele supervizate cer etichete ground truth, adesea indisponibile;
  - metodele nesupervizate au dificultati cu concept drift si FPR ridicat;
  - metodele bazate pe XAI (SHAP, LRP) au overhead computational mare, nepotrivit pentru timp real, si performeaza slab pe serii de timp, cu multe false negative.

## Ce propun (metoda, pe scurt)
- **DSA-AE (Dual Self-Attention AutoEncoder)**, un singur model pentru toate formele de drift (III):
  - autoencoder care reconstruieste atat caracteristicile de intrare cat si predictiile modelului monitorizat (etichetele sunt intrari suplimentare, deci nu e nevoie de un autoencoder separat pentru label drift);
  - data/label drift: distanta Mahalanobis a erorii de reconstructie, comparata cu pragul sigma2;
  - concept drift: doua blocuri de self-attention (pe caracteristici si temporal), combinate cu ponderea alpha; distanta cosinus intre scorurile de atentie curente si cele de referinta din validare, comparata cu pragul sigma1.
- **Flux in doua etape** (III.A, Fig. 2):
  - offline: colectare de date din RAN, Core, Edge, preprocesare, antrenarea modelului ML, construirea unei baze de cunostinte caracteristici-predictii, antrenarea DSA-AE si inregistrarea scorurilor de atentie de referinta;
  - online: aceeasi preprocesare pe datele de inferenta, DSA-AE semnaleaza drift-ul si sursa lui.
- Pragurile sunt dependente de caz de utilizare si sunt alese de expert, cu accent pe F1 (III.E). Complexitate declarata: O(Nd + d²) pentru reconstructie si Mahalanobis, O(N²d) pentru atentie; o singura trecere forward per fereastra la inferenta.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Trei seturi de date publice, impartite cronologic 80/20 (IV.A, Tabelul 2):
  - **Milano** (Telecom Italia, un an): volum de trafic internet; model LSTM de forecasting;
  - **Ireland** (trace-uri 5G de la un operator irlandez, 2019-2020; Netflix, Amazon Prime, download; static si in masina): model LSTM pentru DL/UL bitrate;
  - **EURECOM** (facilitatea 5G EURECOM, core OAI): utilizarea CPU si RAM a AMF, timpi de inregistrare; model FNN care prezice resursele AMF.
- Drift-ul este introdus artificial: de exemplu 23,4% drift simulat pe Milano, prin trafic anormal (V.D.1). Concept drift pe Ireland: antrenare pe Netflix static (interval 2 s), inferenta pe download in mod driving (interval 30 s) (V.D.3).
- DSA-AE in PyTorch 2.0.1 (hidden 64, latent 32, MSE, Adam 0,001, 50 de epoci); modelele monitorizate in TensorFlow 2.17.0. Hardware: CPU AMD cu 8 nuclee, 16 GB RAM, GPU RTX 3050 Ti (IV.C).

## Experimente si metrici
- Limitarea XAI pe serii de timp: SHAP si LRP pe Milano si Ireland (V.C, Fig. 9-12).
- Detectia data drift, label drift si concept drift (V.D, Fig. 13-19).
- Efectul ponderii alpha (V.E, Fig. 20).
- Comparatie cu ADWIN, EDDM si un detector bazat pe XAI [18], pe ferestre de 32, 64 si 128; metrici FPR, recall, precision, F1 si latenta de detectie ("drift detection delay" din specificatia ETSI [53]). Drift aleator pe date, predictii si dependente; drift sezonier, recurent si gradual (V.F, Tabelul 3).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- SHAP si LRP pe LSTM se concentreaza pe ultimii pasi de timp ai secventei (Fig. 9-12, V.C).
- Label drift: banda de eroare de reconstructie peste 22,5 la pasii 5-7 (Fig. 15).
- Alpha optim: aproximativ 0,6-0,7 pentru seriile de timp si 0,3-0,4 pentru EURECOM; valorile extreme (aproape 0 sau 1) scad acuratetea (Fig. 20).
- Tabelul 3 (valorile tabelului sunt imagine in PDF; cifrele de mai jos sunt cele din text):
  - DSA-AE are cele mai mari precision, recall si F1, pana la 93,5%; pe Milano si Ireland metodele traditionale au scoruri in jur de 77%;
  - ADWIN are cele mai mici intarzieri, dar acuratete mai mica; detectorul XAI are FPR mai mare pe serii de timp si intarzieri de ore, uneori zile;
  - fata de media metodelor de referinta: castig de F1 intre 10,56% si 15,02% (medie 13,6%) si reducere a latentei intre 90,84% si 97,59% (medie 94,7%) (V.F).
- Fereastra 32 detecteaza mai repede, dar cu acuratete mai mica; fereastra 128 are acuratete mai buna si latenta mai mare (V.F).

## Limitari declarate de autori
- Pragurile sigma1 si sigma2 depind de caz si trebuie ajustate; selectia este facuta de expert (III.A, III.E).
- Optimizarea suplimentara a complexitatii ramane lucrare viitoare (III.E).
- Adaptarea la drift (continual learning) nu este tratata si este lucrare viitoare (VI).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: partial - setul de date EURECOM provine dintr-un core OAI real (metrici AMF); detectorul ruleaza offline pe seturi de date (IV.A).
- UE reale sau emulate?: nedeclarat pentru EURECOM; Ireland contine trace-uri de la terminale reale (IV.A).
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu - detecteaza drift; nu evalueaza actiuni.
- executa actiuni automat (bucla inchisa)?: nu - semnaleaza drift-ul; adaptarea este lucrare viitoare (VI).
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu - drift injectat artificial pe seturi de date istorice.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu - metrici de detectie (F1, FPR, latenta).
- observa traficul la SCP / proxy?: nu.
