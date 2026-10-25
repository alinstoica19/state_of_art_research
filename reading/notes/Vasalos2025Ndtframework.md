# Design and Evaluation of a Network Digital Twin Framework for 5G/6G Architectures (2025)
Cheie: Vasalos2025Ndtframework . DOI/link: https://doi.org/10.1109/dcoss-iot65416.2025.00139 . Sursa textului: integral: versiunea autorilor pe Zenodo (record 18401029, CC BY 4.0, DCOSS_IOT_Paper.pdf)
Sectiunea din plan: C . Tema: digital twin al retelei / core 5G
Autori: Ioannis Vasalos, Maria Christopoulou, Averkios Vasalos, Michail Alexandros Kourtis, Nikos Dimitriou, George Xylouris (NCSR Demokritos, Grecia). DCOSS-IoT 2025. Finantare: proiectele SNS JU 6G-CLOUD si MARE.

## Problema (cum o formuleaza autorii)
- AI nativ in 6G are nevoie de date multe si diverse pentru antrenarea si actualizarea modelelor, iar generarea lor direct din reteaua fizica este adesea impracticabila (cost, complexitate, constrangeri de timp real). NDT-urile pot emula conditiile curente, pot genera date sintetice realiste si pot fi folosite pentru antrenarea si optimizarea modelelor inainte de deployment (I.A).
- Fata de lucrarile anterioare, autorii spun ca:
  - nu folosesc simulare, ci o mapare unu-la-unu cu reteaua fizica, pe date reale de control si user plane (fata de [12]);
  - extind evaluarea la capacitate si dinamica traficului, nu doar fidelitatea topologiei (fata de [10]);
  - ofera implementare full-stack si validare numerica, nu doar metodologie (fata de [11]) (I.C).

## Ce propun (metoda, pe scurt)
- **Arhitectura NDT** (II, Fig. 2), pe baza ITU-T Y.3090:
  - NDT Data Repository: colectare, preprocesare, management, stocare;
  - NDT Engine: maparea retelei fizice (PN), serviciul de modelare a retelei, instante multiple NDT 1..n;
  - NDT Management: orchestrator, lifecycle management, evaluarea performantei, vizualizare, securitate si data governance.
- **Fluxuri de date pentru AI/ML** (III, Tabelul I): RAN (loguri UE si gNB, NGAP, RRC, throughput), core (loguri AMF, SMF, UPF: inregistrare, sesiuni, QoS flow, PFCP/GTP-U, descoperire NF, decizii de scalare si slicing) si resurse de calcul.
- **Implementare** (IV):
  - NDT Engine: Open5GS (AMF, SMF, UPF etc.) si UERANSIM (UE si gNB emulate);
  - Data Repository: Prometheus;
  - orchestrator si lifecycle: KATANA;
  - vizualizare: Grafana.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Retea fizica: Amarisoft (gNB si 5GC software), SA, NR TDD, 2x2 MIMO, 50 MHz la 3,5 GHz (V).
- Doua UE, fiecare prezent atat in reteaua fizica cat si in NDT, cu acelasi tipar de trafic. SLA QoS: UE1 15 Mbps, UE2 10 Mbps (V).
- Durata experimentului si numarul de repetitii sunt nedeclarate.

## Experimente si metrici
- Throughput uplink per UE si total, in reteaua fizica (Fig. 3) si in NDT (Fig. 4), vizualizat in Grafana.
- Comparatie calitativa a logurilor generate de AMF, SMF si UPF in reteaua fizica (Amarisoft) si in NDT (Open5GS) (tabelul cu exemple de loguri).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Throughput uplink: 15 Mbps (UE1), 10 Mbps (UE2) si 25 Mbps total, atat in reteaua fizica cat si in NDT (Fig. 3-4).
- Autorii afirma ca logurile generate de NDT sunt identice cu cele din reteaua fizica (V). Exemplele din tabel arata insa formate de log diferite (Amarisoft vs. Open5GS journalctl) pentru aceeasi procedura de inregistrare si stabilire a sesiunii.
- Nu este raportata o metrica numerica de fidelitate (eroare, distanta intre distributii).

## Limitari declarate de autori
- Lucrari viitoare: dezvoltarea sub-blocurilor pentru reprezentarea detaliata a functiilor RAN, intr-o arhitectura service-based convergenta RAN-core (VI).
- Alte limitari nu sunt declarate explicit.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - Amarisoft 5GC in reteaua fizica si Open5GS in NDT (IV, V).
- UE reale sau emulate?: ambele - doua UE in reteaua fizica Amarisoft (tipul lor nu este precizat) si UERANSIM in NDT (IV, V).
- digital twin al retelei?: da - NDT bazat pe Open5GS si UERANSIM, orchestrat cu KATANA (IV).
- prezice efectul unei actiuni inainte de a o aplica?: nu in evaluare - NDT-ul este propus pentru testarea si antrenarea offline a modelelor AI/ML inainte de aplicarea lor pe reteaua fizica (VI), dar nu este evaluat pentru asta.
- executa actiuni automat (bucla inchisa)?: nu - buclele inchise sunt mentionate ca utilizare posibila a datelor (III).
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: partial - throughput uplink per UE; logurile de inregistrare si sesiune sunt comparate calitativ (V).
- observa traficul la SCP / proxy?: nu.
