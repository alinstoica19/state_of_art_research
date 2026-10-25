# Digital Twin For 5G Networks and Beyond: Domain Transfer and Network Behavior Classification for 6G Readiness (2025)
Cheie: Petrik2025Dtdomaintransfer . DOI/link: https://doi.org/10.1109/elmar66948.2025.11193997 . Sursa textului: integral: PDF urcat de autor (Digital_Twin_For_5G_Networks_and_Beyond_Domain_Transfer_and_Network_Behavior_Classification_for_6G_Readiness (1).pdf)
Sectiunea din plan: A . Tema: digital twin
Autori: Matej Petrik, David Truhlar, Michal Ries (Slovak University of Technology in Bratislava). 67th International Symposium ELMAR-2025, Zadar; 4 pagini. Cod si date publicate pe GitHub (xtruhlar/5GDigitalTwin).

## Problema (cum o formuleaza autorii)
Un DT pentru 5G trebuie sa aiba fidelitate suficienta fata de conditiile reale. Modelele ML antrenate doar pe date sintetice se transfera slab in retele reale (domain transfer). Autorii observa ca lucrarile existente se concentreaza pe simulare si modelare la nivel de sistem, nu pe clasificarea in timp real a comportamentului retelei, iar domain shift-ul sintetic-real este putin explorat (Sectiunile I-II).

## Ce propun (metoda, pe scurt)
- **DT 5G lightweight cu trei parti** (Sectiunea III.A):
  - partea fizica: un core Open5GS izolat, la care sunt conectate dispozitive mobile reale;
  - partea digitala: mediu containerizat cu UERANSIM, scripturi de trafic sintetic si un clasificator LSTM;
  - legatura de date: metrici si loguri colectate continuu prin Prometheus si interpretate de model, cu fine-tuning online cand exista date adnotate.
- **Clasificarea a sase scenarii de utilizare** (Tabelul I): Normal Operation, Video Streaming, Periodic Keep-Alive, Short Sessions (Burst, 10 MB), Load Registration (toate dispozitivele se conecteaza simultan) si Failed Authentication (IMSI invalid repetat).
- **Patru arhitecturi LSTM**, cu secvente de 60 de pasi:
  - Baseline: LSTM 64+32;
  - Robust: LSTM 128/64/32 cu dropout;
  - Batch Norm;
  - Attention.
  - Antrenare cu Adam, cross-entropy categoriala, class weighting si early stopping (III.C).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Masuratorile au fost facute in 5G Laboratory al Automotive Innovation Lab de la FIIT STU (III.B).
- **Dataset sintetic:** cele 6 scenarii, rulate cu Open5GS si UERANSIM.
- **Dataset real:** aceleasi componente DT, scenarii executate manual, etichete din timestamp-uri; folosit doar pentru testare.
- Ambele dataset-uri contin timestamp, metrici, loguri si eticheta, in format CSV.
- Unelte: Python, Docker, TensorFlow/Keras, Prometheus, Grafana.
- Numarul de UE (sintetice sau reale) nu este declarat.

## Experimente si metrici
Evaluare in trei etape (III.D):
1. pe date sintetice de test (split stratificat 80:20);
2. pe date reale fara modificari;
3. dupa fine-tuning pe 20% din datele reale, actualizand doar ultimele straturi.

Metrici: accuracy, precision, recall, F1-score.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Accuracy din Tabelul II (prima coloana):

| Model | Date sintetice | Date reale |
|---|---|---|
| Baseline | 0,949 | 0,14 |
| Robust | 0,900 | 0,44 |
| Batch Norm | 0,963 | 0,21 |
| Attention | 0,914 | 0,16 |

- Textul raporteaza 96,2% pentru Batch Norm pe date sintetice (IV.A); tabelul indica 0,963.
- Pe date reale, niciun model nu depaseste 44% accuracy (IV.A).
- Dupa fine-tuning pe 20% din datele reale, accuracy maxima este de aproximativ 50%. Doar 2 din 6 scenarii sunt clasificate fiabil, iar predictiile sunt dezechilibrate (IV.B).
- In timp real, sistemul actualizeaza predictia tipului de trafic la fiecare minut (IV.C).

## Limitari declarate de autori
- Domain transfer: modelele invata tipare specifice mediului sintetic. Traficul sintetic nu are variabilitatea si zgomotul din retele reale (evenimente de mobilitate, QoS fluctuant, comportament la nivel de aplicatie) (IV.B).
- Directii propuse: augmentarea cu date la nivel de pachet, domain adaptation, invatare self-supervised, dataset-uri hibride semi-realiste (IV.B, V).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - Open5GS (III.A).
- UE reale sau emulate?: ambele - UERANSIM pentru dataset-ul sintetic; dispozitive mobile reale conectate la core-ul Open5GS pentru dataset-ul real (III.A, III.B).
- digital twin al retelei?: da - DT 5G declarat de autori, cu partea fizica (Open5GS + dispozitive reale) si partea digitala (UERANSIM + model) (III.A).
- prezice efectul unei actiuni inainte de a o aplica?: nu - DT-ul clasifica starea retelei, nu evalueaza actiuni.
- executa actiuni automat (bucla inchisa)?: nu - doar clasificare si fine-tuning de model; reconfigurarea automata a core-ului este mentionata doar ca posibilitate (IV.C).
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: partial - scenariile includ inregistrari simultane si autentificari esuate, dar metricile raportate sunt de clasificare.
- observa traficul la SCP / proxy?: nu.
