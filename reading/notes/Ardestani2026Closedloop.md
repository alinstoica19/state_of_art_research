# Towards zero-touch network orchestration: An NWDAF-centered standards-compliant closed-loop approach (2026)
Cheie: Ardestani2026Closedloop . DOI/link: 10.52953/svmm1934 . Sursa textului: versiunea publicata (ITU J-FET, vol. 7, nr. 2, iunie 2026), integral: https://www.itu.int/dms_pub/itu-s/opb/jnl/S-JNL-VOL7.ISSUE2-2026-A12-PDF-E.pdf
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Trecerea la operare zero-touch / AI-native cere inchiderea buclei intre colectarea datelor, analitica si controlul automat. NWDAF 3GPP ofera baza standardizata pentru analitica, dar realizarea lui practica ca enabler de automatizare ramane in mare parte neexplorata (rezumat, Sec. 1). Autorii spun ca lucrarile anterioare au trei limitari: lipsa observabilitatii conforme cu standardul (captura pasiva de pachete sau exporturi indirecte din control plane, in loc de Event Exposure Service, EES), lipsa integrarii analitica-actiune (bucla ramane deschisa) si lipsa gestiunii ciclului de viata al modelelor ML (MLOps) in implementarile NWDAF. Adauga ca evaluarea cantitativa a costului colectarii/analizei/raportarii este limitata. Intrebarea declarata (Sec. 3): se poate realiza practic o bucla inchisa conforma cu standardul si la ce cost.

## Ce propun (metoda, pe scurt)
Un framework NWDAF-centrat, construit modular pe codul NWDAF din OAI si integrat cu Open5GS (Sec. 3). Componente:
- UPF Event Exposure Service (UPF EES) implementat in UPF-ul Open5GS: evenimente "usage-measures", "usage-trends", "QoS-monitoring", granularitate per-flow / per-session (Tabel 2). Colectarea pe hot path foloseste un modul de pregatire a datelor separat de generarea notificarilor, cu ring buffer lock-free SPSC (Sec. 3.1.2). Intarzierea raportata este intarzierea interna a UPF (microsecunde), plus pierderea de pachete (Sec. 3.1.3).
- NWDAF cu SBI (client UPF, stocare MongoDB), motoare de analitica, NBI, si ML Model Provision Service (MLMPS) integrat cu MLflow (registry, versionare, API admin) (Sec. 3.2, Tabel 3).
- NWDAF Subscriber adaugat in SMF si PCF, ca acestea sa consume analitica si sa actioneze (Sec. 3.3).
- Aplicare de rate la UPF prin token bucket (GBR, MBR per flow; AMBR per sesiune), capacitate bucket 1.2x rata (Sec. 3.3.2, Fig. 5).
Doua cazuri de utilizare:
1. Detectie de bot (analitica "abnormal behaviour") cu model random forest pe trasaturi de graf in stil BotChase (grade, grade ponderate, betweenness centrality), antrenat pe CTU-13 (scenariile 1, 2, 3, 5: Neris, Rbot, Virut) plus trafic benign colectat din propriul testbed; actiune: SMF elibereaza sesiunea PDU a UE suspect prin N4 (Sec. 4).
2. Adaptare QoS la congestie: motor de analitica "user data congestion" (NSI din severitate, persistenta, escaladare, scope pentru intarziere si pierdere; Ec. 1-6; praguri Tabel 9 si 10), PCF cu heuristica (Algoritm 1, Tabel 11 si 12, Ec. 7) care scaleaza MBR-ul regulilor PCC si Session-AMBR si trimite actualizarea catre SMF (Sec. 5).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Open5GS desfasurat pe Kubernetes, cu modificari in UPF, SMF, PCF; UERANSIM pentru gNB si UE (Sec. 4.5.1). Un singur gNB si un singur slice in setup-ul de congestie (Sec. 5.2.2).
- Bot: scanare Nmap (--script http-open-proxy) catre 20 de servere cu IP-uri distincte (Sec. 4.5.1). Date de antrenare: CTU-13 (public) + trafic benign colectat in testbed (Sec. 4.3.1).
- Congestie: UPF limitat ca bottleneck (pod UPF: CPU request 200m / limit 400m; memorie 512Mi / 1024Mi, Tabel 13); AMBR 15 Mbps DL si 100 Mbps UL; doua reguli PCC GBR (VoIP: UDP 16384-20000, GBR 64/64 Kbps, MBR 128/128 Kbps, 5QI 1; gaming: UDP 27000-27999, GBR 5/10 Mbps, MBR 10/20 Mbps, 5QI 3; Tabel 14). Trafic non-GBR cu iperf; trafic GBR usor generat cu script UDP pe UE (60 s). Un server de laborator ca destinatie.
- Overhead: iperf3 de la un UE, ping de la alt UE; 50-200 UE la 200 Mbps total (Sec. 6.1.2).
- Uplink GBR nu a putut fi evaluat din lipsa suportului RAN (Sec. 3.3.2, 5.4.1).

## Experimente si metrici
- Timp de raspuns al buclei atac -> mitigare, cu interval de colectare 1, 3, 5 s, 20 repetari, medie si deviatie standard; UE blocat detectat prin esecuri de ping (timeout 0.5 s); t1 = prima raportare a traficului malitios la NWDAF SBI, t2 = detectie, t3 = UE blocat (Sec. 4.5.2, Fig. 8).
- Efectul ajustarii de rata de catre PCF asupra pierderii si RTT ale fluxurilor GBR (voce, gaming), cu si fara ajustare, 20 runde de 60 s, 3 UE cu trafic de fundal, medii pe ferestre de 5 s cu interval de incredere 95% (Sec. 5.4.2, Fig. 11-16). Recuperarea ratei dezactivata in aceste experimente.
- Overhead UPF EES: varianta de baza, EES fara abonati, EES cu 1 abonat (rapoarte per-flow volum la 3 s); intarziere one-way, CPU, memorie la 600/800/1000 Mbps (Fig. 17-19); numar UE 50-200 (Fig. 20); overhead de semnalizare (Sec. 6.1.3).
- Resurse NWDAF (CPU SBI, NBI-Event, MLMPS) la intervale 1-5 s (Fig. 21; textul indica 1-5 s, figura arata 1, 3, 5, 10 s) (Sec. 6.2).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Mitigare bot (Fig. 8): timpul pana la prima raportare la NWDAF este mai mic decat perioada de subscriptie in toate cazurile; timpul de mitigare este aproape acelasi pentru 1/3/5 s, dar intervale mai scurte dau mitigare mai rapida; golul principal de latenta este timpul de detectie al modelului ML (Sec. 4.5.2, 4.6). Valorile numerice nu apar in text, doar in figura.
- GBR sub sarcina non-GBR (Fig. 11, 12): fara ajustare pierderea voce ramane intre aprox. 8% si 10%; cu ajustare scade de la aprox. 8% la aprox. 1%; RTT fara ajustare intre aprox. 12.5 si 15 ms, cu ajustare de la aprox. 12.5 ms la aprox. 3 ms (Sec. 5.4.2.1).
- Rulare individuala (Fig. 13): ajustari aplicate 0.90, apoi 0.55, apoi 0.45; pierderea scade si ramane sub 2.5%; RTT incepe sa scada cam 5 s dupa pierdere.
- Sarcina combinata GBR + non-GBR (Fig. 14-16): pierderea voce scade de la 40% la 20% cu ajustare; pierderea gaming creste cu aprox. 10%; pierderea non-GBR creste (Sec. 5.4.2.2). Gaming 15 Mbps DL, voce 60 Kbps DL.
- Overhead UPF EES (Fig. 17-20): la 1000 Mbps, +0.11 ms intarziere one-way fata de baza; CPU suplimentar sub 6.5% la toate ratele testate; memorie stabila, fara drift; de la 50 la 200 UE: +aprox. 36 millicores CPU si +2.84 MiB memorie (Sec. 6.1.1, 6.1.2).
- Semnalizare (Sec. 6.1.3): raport de volum la 3 s: aprox. 14 Kbps pentru 2 UE cu 2 fluxuri fiecare, 52 Kbps pentru 4 UE cu 4 fluxuri fiecare. Bot detection la 1 s: aprox. 4 Kbps, reductibil la 1 Kbps cu campuri minime; aprox. 17 octeti in plus per UE anormal detectat.
- MLMPS (Sec. 6.2, Fig. 21): CPU 281 millicores (CI 95%: 240-323) cand e desfasurat fara motor; consuma substantial mai mult decat celelalte module NWDAF, care sunt usoare; CPU SBI/NBI scade la intervale mai lungi.
- Demonstratia de enforcement AMBR (Fig. 5): AMBR DL 15 Mbps; primul flux la 17 Mbps limitat la aprox. 15 Mbps; la intrarea celui de-al doilea flux, rata primului scade (bucket partajat).
- Textul nu raporteaza acuratete/precizie/recall pentru modelul de bot detection.

## Limitari declarate de autori
- Intarzierea QoS monitoring raportata este doar intarzierea interna a UPF; componenta RAN (intarziere end-to-end UE-PSA UPF) lasata pentru lucrari viitoare (Sec. 3.1.3, 7).
- Uplink GBR neevaluat din lipsa suportului RAN (Sec. 3.3.2, 5.4.1).
- Algoritmul PCF este o heuristica simpla; propun inlocuirea cu politici invatate in viitor (Sec. 5.3.2, 7).
- Pragurile de severitate au fost alese empiric; definitia exacta a NSI nu e standardizata (Sec. 5.2.2, 5.2.3.1).
- Contributorii de trafic sunt identificati la nivel de flux, nu de aplicatie; selectia de zona de interes nu e aplicata (un singur gNB, un slice) (Sec. 5.2.2).
- Compromis declarat: colectare pe interval mai lung da mai multa informatie dar creste timpul de raspuns (Sec. 4.6).
- Sunt prezentate doar doua cazuri de utilizare de tip proof-of-concept (Sec. 7).
- Scalare la mai multe instante NWDAF (edge/core) este discutata ca directie, nu evaluata (Sec. 7).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? da - Open5GS modificat (UPF, SMF, PCF) pe Kubernetes (Sec. 3.4, 4.5.1)
- UE reale sau emulate? emulate - UERANSIM pentru gNB si UE (Sec. 4.5.1)
- digital twin al retelei? nu - nu este mentionat; analitica ruleaza pe date live din testbed (Sec. 3)
- prezice efectul unei actiuni inainte de a o aplica? nu - PCF aplica heuristica reactiva pe congestia raportata si compara cu starea anterioara; raportul de congestie este statistic, nu predictiv (Sec. 5.2.2, 5.3.2)
- executa actiuni automat (bucla inchisa)? da - SMF elibereaza sesiuni PDU, PCF ajusteaza MBR/AMBR, UPF aplica token bucket (Sec. 4.4, 5.3)
- multi-site / geo-redundanta / failover de baza de date? nu - un singur gNB, un testbed; instante NWDAF multiple doar discutate ca directie viitoare (Sec. 5.2.2, 7)
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat - nu se declara predictii fixate dinainte
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? da - pierdere si RTT pe fluxuri GBR ale UE, esecuri de ping ale UE blocat; nu masoara inregistrari (Sec. 4.5.2, 5.4.2)
- observa traficul la SCP / proxy? nu - telemetria vine din UPF EES (user plane) si SBI; SCP apare doar in diagrama arhitecturii standard (Fig. 2), nu ca punct de observare (Sec. 3.1)
