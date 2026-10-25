# Machine Learning-Assisted Closed-Control Loops for Beyond 5G Multi-Domain Zero-Touch Networks (2022)
Cheie: DeSousa2022Mlclosedloops . DOI/link: https://doi.org/10.1007/s10922-022-09651-x . Sursa textului: integral: PDF gazduit de grupul autorilor (INTRIG, Unicamp: intrig.dca.fee.unicamp.br/wp-content/papercite-data/pdf/sousa_rul_2022.pdf), gasit prin cautare web; versiunea publicata Springer
Sectiunea din plan: C . Tema: bucle inchise ZSM / ML / self-healing multi-domeniu
Autori: Nathan Franklin Saraiva de Sousa, Md Tariqul Islam, Raza Ul Mustafa, Danny Alex Lachos Perez, Christian Esteve Rothenberg (Unicamp), Pedro Henrique Gomes (Ericsson). Journal of Network and Systems Management, vol. 30, art. 46, 2022. Finantare: Ericsson Brazil Innovation Center.

## Problema (cum o formuleaza autorii)
- Serviciile end-to-end din B5G se construiesc pe resurse din mai multe domenii si tehnologii. ETSI ZSM urmareste automatizarea cross-domain prin bucle de control inchise (CCL) si AI (1, 2).
- In managementul defectelor, ML poate sustine RCA atunci cand sunt incalcate QoE sau SLA. Este necesara colaborarea intre buclele din domenii diferite (1).

## Ce propun (metoda, pe scurt)
- **Arhitectura CCL multi-domeniu** bazata pe ETSI ZSM, cu domenii de management (MD) pentru Edge (MEC), RAN, Transport, Cloud si un E2E MD (3, Tabelul 1).
- **Caz de utilizare** (4, Fig. 4), self-healing pentru streaming video DASH:
  1. pierderile de pachete din transport nu depasesc pragul de politica al domeniului de transport, deci bucla lui nu porneste;
  2. Edge MD detecteaza incalcarea QoE, dar nu are o actiune locala;
  3. problema este escaladata la E2E MD, care cere rapoarte de stare de la toate domeniile;
  4. Transport MD face RCA cu ML si indica legatura defecta;
  5. E2E MD decide migrarea serverului video in alt DC si o ruta noua.
- **Edge QoE Probe** (5): monitorizare pasiva, neinvaziva, a traficului criptat la MEC. Caracteristici QoS temporale (throughput, numar de pachete, dimensiunea pachetelor, timpul inter-sosire) pe ferestre curenta, de trend si de sesiune, cu granularitate de 0,5 s; clasificatoare supervizate pentru rezolutie si bitrate.
- **RCA in transport** (6): un "network digital twin" emulat al retelei de transport, cu aceeasi topologie si caracteristici de legatura. In acest mediu sunt injectate defecte pe fiecare legatura, iar un clasificator invata sa coreleze QoS si QoE cu legatura defecta. Inferenta se face online, pe reteaua reala.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Emulare cu Mininet-WiFi, client goDASH (metrici QoE obiective per segment), server Caddy, trafic de fond D-ITG (aproximativ 20% din traficul mediu), Linux tc si tcpdump. Limitarile de legatura urmeaza trace-uri celulare reale 3G, 4G si 5G (7).
- **Experimentul 1 (Edge):** un AP si un OvS; HTTPS si QUIC; sase algoritmi ABR. 252 de caracteristici QoS (HTTPS) si 168 (QUIC). 105.613 inregistrari HTTPS si 100.757 QUIC, la 0,5 s. Clasificatoare: LR, KNN, GNB, SVM, DT, RF, MLP, cu cautare grid si 5-fold CV, pe un Xeon Silver 4114.
- **Experimentul 2 (Transport):** 8 switch-uri OvS si 8 clienti goDASH. Capacitatea unei legaturi este degradata cu caracteristicile trace-ului 5G, pe rand pentru fiecare legatura. Clasificatoare: RF, ANN, KNN.

## Experimente si metrici
- Acuratetea si timpul de antrenare ale clasificatoarelor (Tabelul 2); subseturi de caracteristici (Tabelul 3).
- Matrici de confuzie si precision, recall, F1 pentru localizarea legaturii defecte (Fig. 8, Tabelul 4).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- **Experimentul 1:**
  - DT si RF au acuratete de aproape 90% pe HTTPS si peste 90% pe QUIC; RF este cu aproximativ 3 puncte peste DT si a fost ales;
  - GNB se antreneaza cel mai repede, dar este cel mai putin precis; SVM are cel mai lung timp de antrenare (Tabelul 2);
  - doar caracteristicile ferestrei de sesiune dau 98% (HTTPS) si 99% (QUIC); top-15 caracteristici dau rezultate similare cu setul complet (Tabelul 3).
- **Experimentul 2:**
  - RF are precision, recall si F1 de 97% fiecare, cu acuratete peste 94% pe majoritatea interfetelor;
  - ANN identifica corect in medie 85-86% dintre legaturi, cu precision 93%;
  - KNN are precision 80% si 70% acuratete pe trei interfete (Tabelul 4, Fig. 8).

## Limitari declarate de autori
- Lucrari viitoare (9):
  - integrarea tuturor componentelor intr-un singur setup experimental;
  - scalabilitatea si adaptarea la schimbari de topologie;
  - reevaluarea modelelor, colectarea ground truth-ului si generalizarea;
  - evaluarea timpilor de escaladare si delegare in colaborarea ierarhica dintre bucle;
  - practici standardizate de benchmarking NFV.
- Experimentele sunt separate pe domenii, cu testbed-uri diferite (7).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - emulare de retele de acces si transport cu Mininet-WiFi; core-ul nu este implementat (7).
- UE reale sau emulate?: emulate - clienti goDASH in Mininet-WiFi, cu conditii de legatura din trace-uri 3G/4G/5G reale (7).
- digital twin al retelei?: da (in termenii autorilor) - un mirror emulat al retelei de transport folosit ca sandbox ML (6).
- prezice efectul unei actiuni inainte de a o aplica?: nu - DT-ul este folosit pentru antrenarea RCA, nu pentru evaluarea actiunilor de remediere.
- executa actiuni automat (bucla inchisa)?: partial - fluxul de self-healing cu migrare si rerutare este descris la nivel de arhitectura (Fig. 4); experimentele evalueaza doar detectia QoE si RCA (7).
- multi-site / geo-redundanta / failover de baza de date?: partial (conceptual) - migrarea serverului video in alt DC, in cazul de utilizare (4).
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: partial - QoE video (rezolutie, bitrate) a clientilor emulati, folosit ca ground truth si tinta (7.1); nu inregistrari sau sesiuni 5G.
- observa traficul la SCP / proxy?: nu - monitorizarea este pasiva la AP/MEC si pe interfetele switch-urilor.
