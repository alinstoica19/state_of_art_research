# OnSlicing: Online End-to-End Network Slicing with Reinforcement Learning (2021)
Cheie: Liu2021Onslicing . DOI/link: 10.1145/3485983.3494850 (arXiv:2111.01616) . Sursa textului: integral, arXiv v1 (2 nov. 2021): https://arxiv.org/pdf/2111.01616v1
Sectiunea din plan: B . Tema: nedeclarat

## Problema (cum o formuleaza autorii)
Online deep reinforcement learning (DRL) poate elimina diferenta simulare-realitate, dar explorarea aleatoare a DRL incalca SLA-urile slice-urilor si constrangerile de resurse ale infrastructurii. Autorii vor orchestrare cross-domain (RAN, transport, core, edge) cu utilizare minima de resurse si SLA respectat pe tot parcursul invatarii online (Sec. 1). Politicile DRL antrenate offline sufera de discrepanta fata de reteaua reala; o politica DRL online se comporta mai prost decat una bazata pe reguli in faza timpurie (Sec. 1, 5).

## Ce propun (metoda, pe scurt)
- OnSlicing: sistem de slicing end-to-end alcatuit dintr-un manager (patru domain managers: RDM, TDM, CDM, EDM) si un orchestrator cu cate un agent DRL per slice (Sec. 2, Fig. 1).
- Constraint-aware policy update: incalcarea SLA intra ca penalitate in functia de recompensa prin metoda primal-dual Lagrangian, peste PPO (Sec. 3, Eq. 3-5).
- Proactive baseline switching: o retea neuronala cu inferenta variationala estimeaza media si deviatia functiei de cost a politicii de baza (rule-based); daca costul cumulat plus costul asteptat al politicii de baza depaseste pragul SLA, politica de baza preia restul episodului (Sec. 3).
- Distributed coordination: un action modifier in fiecare agent si un parameter coordinator in fiecare infrastructura modifica actiunile astfel incat constrangerile de resurse sa fie respectate (Sec. 4).
- Learning from baseline: agentii imita offline politica rule-based inainte de invatarea online (Sec. 5).
- Domain managers implementati cu REST API unificat pentru configurare la scara de subsecunde (Sec. 6).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Testbed hardware (Fig. 8, Sec. 6): OpenAirInterface (eNB LTE 2.6 GHz/20 MHz si gNB 3.5 GHz/40 MHz pe calculatoare Intel i7, USRP B210, FlexRAN), 3 smartphone-uri POCO F2 Pro (LTE si 5G NSA EN-DC) intr-o cusca Faraday; switch SDN Ruckus ICX 7150-C12P cu OpenDayLight si OpenFlow 1.3; core OpenAir-CN (HSS, MME, SPGW-C, SPGW-U in containere Docker, arhitectura CUPS); edge cu Docker pe workstation i7.
- Trei slice-uri cu aplicatii Android si servere Python: MAR (cerinta: latenta medie round-trip 500 ms), HVS (30 FPS), RDC (fiabilitate 99.999%) (Sec. 7.1).
- Trafic: dataset Telecom Italia (Provincia Trento), scalat la capacitatea testbed-ului (5 utilizatori/s MAR, 2 HVS, 100 RDC), sosiri dupa proces Poisson (Sec. 7.1).
- Interval de configurare: 15 minute; prag SLA C_max = 5% (Sec. 7.1).
- Agenti in PyTorch 1.5, retele 128x64x32 (Sec. 6).
- Scara mare: utilizatori emulati cu platforma OAI (nFAPI), restul testbed-ului neschimbat (Sec. 7.2, Fig. 18-19).
- Baseline-uri comparate: OnRL, Baseline (rule-based), Model_Based.

## Experimente si metrici
- Utilizare medie de resurse (%) si incalcare medie SLA (%), dupa terminarea invatarii (Tabel 1) si pe parcursul invatarii online (Fig. 9, 11).
- Ablatii: OnSlicing-NB (fara baseline switching), OnSlicing-NE (fara estimator), zgomot Gaussian de varianta 1.0 pe estimator (Tabel 2, Fig. 13); metode de action modification (projection) si zgomot pe action modifier (Tabel 3).
- Comparatie 4G LTE vs 5G NR: ping delay, throughput iperf3, performanta slice-urilor (Fig. 16-17, Tabel 4).
- Emulare la scara: numar de utilizatori MAR emulati, numar de slice-uri emulate, numar de interactiuni agent-domain manager (Fig. 18-19).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Tabel 1 (utilizare resurse / incalcare SLA): OnSlicing 20.19 / 0.00; OnRL 23.08 / 15.40; Baseline 52.18 / 0.00; Model_Based 59.04 / 3.13. Textul: OnSlicing foloseste cu 12.5%, 61.3% si 65.8% mai putine resurse decat OnRL, Baseline si Model_Based.
- Rezumat: incalcare SLA de 0.06% pe tot parcursul invatarii online (Abstract); spike-uri de incalcare maxim 1% (Sec. 7.2, Fig. 12).
- Fig. 13: OnSlicing-NB are incalcare medie SLA 2.94%; OnSlicing-NE 0.33%.
- Interactiuni agent-domain manager: in medie 1.83 cu parameter initialization (Sec. 7.2, Tabel 3); sub aproximativ 3 la scara (Fig. 19).
- LTE vs NR: throughput iperf3 6.71 Mbps UL / 14.3 Mbps DL (LTE) si 11.5 Mbps UL / 18.5 Mbps DL (NR); ping delay mediu NR 11.99 ms (Sec. 7.2, Fig. 16). Tabel 4: utilizare 43.5 +- 3.27 si 45.9 +- 4.48 (atribuirea pe retea in tabel nu a putut fi verificata din extragerea textului).

## Limitari declarate de autori
Sec. 9 (Discussion): testbed la scara mica; la scara mare pot aparea state space foarte mare si intarzieri de enforcement eterogene (PRB in milisecunde, scalare server in secunde); explorarea este limitata de baseline switching si poate incetini invatarea; online learning poate dura saptamani sau luni in retele operationale unde orchestrarea are loc la scara de ore; predictiile estimatorului pot fi inexacte pentru stari nevazute, iar Baseline este chemat tarziu (Fig. 12).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu in sens 5GC: core-ul este OpenAir-CN (EPC cu CUPS: HSS, MME, SPGW-C/U), cu RAN 4G LTE si 5G NR NSA (Sec. 6).
- UE reale sau emulate? ambele - 3 smartphone-uri reale; UE emulate OAI pentru scara mare (Sec. 6, 7.2).
- digital twin al retelei? nu - nu este mentionat.
- prezice efectul unei actiuni inainte de a o aplica? partial - estimatorul prezice costul politicii de baza si decide trecerea pe Baseline; action modifier ajusteaza actiunile pentru constrangeri (Sec. 3, 4); nu exista model al efectului fiecarei actiuni in sens de twin.
- executa actiuni automat (bucla inchisa)? da - agentii configureaza resursele RAN/TN/CN/EN la fiecare interval de 15 minute (Sec. 2, 7.1).
- multi-site / geo-redundanta / failover de baza de date? nu - un singur testbed.
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - metrici per slice (latenta cadre, FPS, fiabilitate) agregate in SLA (Sec. 7.1); nu sunt metrici de inregistrari sau sesiuni.
- observa traficul la SCP / proxy? nu - SCP nu este mentionat; CDM atribuie utilizatori la SPGW-U dupa IMSI cu round-robin (Sec. 6).
