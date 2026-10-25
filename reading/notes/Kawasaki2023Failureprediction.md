# Failure Prediction in Cloud Native 5G Core With eBPF-based Observability (2023)
Cheie: Kawasaki2023Failureprediction . DOI/link: https://doi.org/10.1109/vtc2023-spring57618.2023.10200028 . Sursa textului: integral: PDF urcat de autor (Failure_Prediction_in_Cloud_Native_5G_Core_With_eBPF-based_Observability.pdf)
Sectiunea din plan: A . Tema: rezilienta
Autori: Junichi Kawasaki, Daiki Koyama, Takuya Miyasaka, Tomohiro Otani (KDDI Research; KDDI Corporation). IEEE VTC2023-Spring; 6 pagini.

## Problema (cum o formuleaza autorii)
Autorii disting doua tipuri de defecte. Cele care afecteaza imediat serviciul (de exemplu fibra taiata) pot fi tratate doar dupa producere. Cele care se agraveaza treptat (de exemplu cresterea graduala a pierderilor de pachete) pot fi prezise. Cu CNF-urile, numarul de NF-uri si complexitatea legaturilor cresc, ceea ce face operarea proactiva mai dificila. Pentru o predictie fiabila a defectelor sunt necesare date de antrenare cu granularitate fina (Sectiunea I).

## Ce propun (metoda, pe scurt)
- **Arhitectura cu doua blocuri** (Sectiunea III, Fig. 1):
  - **colectarea datelor din trei surse:**
    - eBPF: 14 unelte BCC (Tabelul 1). execsnoop, runqlat, runqlen si funccount sunt alese pentru suprasarcina CPU; uneltele TCP si solisten pentru pierderile de pachete. O tabela de corelare PID/IP atribuie metricile CNF-ului sursa.
    - cAdvisor: metrici de baza ale containerelor.
    - 5G-exporter: numara din logurile CNF cererile, succesele si esecurile pentru registration, deregistration, PDU session creation si release.
  - **predictia defectelor** cu LSTM: prezice evolutia viitoare a metricilor, inclusiv KPI-uri 5G (numarul de esecuri de inregistrare UE, throughput).
- O alarma este ridicata cand valoarea prezisa trece de un prag h, calculat prin regula trei sigma pe esantioanele normale (III.C, IV.C).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- **Server fizic de laborator:** Linux 5.4, 2 x Intel Xeon Gold 6142, 256 GB RAM.
- **CNF-uri 5GC pe Kubernetes 1.22.2 cu Open5GCore release 6:** AUSF, UDM, SMF, AMF, NRF, plus UE si gNB simulate, doua UPF-uri si un DN (IV.A, Fig. 2).
- **Trafic:** Benchmarking Tool (BT, simulator UE/gNB din Open5GCore) repeta constant registration si deregistration; trafic de date intre UE si DN cu iPerf.
- **Scenarii de defect**, fiecare crescand liniar pe 600 s (IV.B):
  - packet-loss: pierderi pe bridge-ul control plane-ului 5GC, de la 0% la 5%;
  - CPU-overload: utilizarea CPU pe UPF2, de la 0% la 100%.
- **Date:** colectate la fiecare 10 s; 3326 de metrici (2262 eBPF, 1048 cAdvisor, 16 5G-exporter).
  - antrenare: 150 esantioane per scenariu de defect plus 450 normale (prima perioada);
  - test: 75 per scenariu de defect plus 225 normale (a doua perioada).
- **LSTM** (Tabelul 2): Adam, learning rate 0,001, activari ReLU si Linear. Numarul de epoci si batch size-ul nu apar in textul extras.

## Experimente si metrici
- Tinta pentru packet-loss: numarul de esecuri de inregistrare UE. Tinta pentru CPU-overload: throughput-ul downstream pe UPF2.
- Momentul tinta de predictie este 600 s. Modelul primeste date intre t-60 si t-10 si prezice pana la 600-t secunde inainte. Timpul t variaza din 30 in 30 de secunde, intre 90 si 300 (IV.C-D).
- Se compara modele antrenate pe date eBPF, cAdvisor si 5G-exporter, cu precision, recall si F1.
- Pentru packet-loss, la t = 210, se face selectie de caracteristici pe uneltele TCP (11 seturi; Tabelul 3).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- **Packet-loss** (Fig. 4):
  - la t = 90, toate scorurile F1 sunt sub 0,4;
  - modelul eBPF depaseste F1 0,9 la t = 210;
  - modelele cAdvisor si 5G-exporter nu ating F1 > 0,9 nici la t = 300.
- **CPU-overload** (Fig. 6): modelul eBPF atinge F1 > 0,9 la t = 150, iar cAdvisor la t = 180. Modelul 5G-exporter nu se imbunatateste.
- **Selectia de caracteristici la t = 210** (Tabelul 3):

| Set de caracteristici | Nr. caracteristici | Precision | Recall | F1 |
|---|---|---|---|---|
| all eBPF | 2262 | 1,000 | 0,947 | 0,973 |
| tcpretrans | — | 0,962 | 1,000 | 0,980 |
| tcprtt | — | 0,926 | 1,000 | 0,962 |
| tcpwin | — | 0,708 | 1,000 | 0,829 |
| tcpdrop | — | 0,521 | 1,000 | 0,685 |
| eBPF fara tcpretrans, tcprtt, tcpwin | — | 0,421 | 0,960 | 0,585 |

  Celelalte unelte au F1 intre 0,406 si 0,475.

## Limitari declarate de autori
- Se studiaza o singura metoda ML (LSTM); alte metode raman pentru lucrari viitoare (III.C).
- Lucrari viitoare: evaluarea overhead-ului de monitorizare eBPF, retele mai mari, scenarii mai complexe precum degradarea pe termen lung (V).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - Open5GCore release 6 pe Kubernetes (IV.A).
- UE reale sau emulate?: emulate - Benchmarking Tool (simulator UE/gNB din Open5GCore) (IV.A).
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu - prezice evolutia KPI-urilor sub defect, nu efectul unei actiuni.
- executa actiuni automat (bucla inchisa)?: nu - doar alarme de defect viitor (III.C).
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu - modelele sunt antrenate pe prima perioada si testate pe a doua, fara predictii fixate dinaintea experimentului.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: da - numarul de esecuri de inregistrare UE (tinta la packet-loss) si throughput-ul UPF2 (IV.C).
- observa traficul la SCP / proxy?: nu - observabilitate eBPF la nivel de kernel si container, nu la SCP.
