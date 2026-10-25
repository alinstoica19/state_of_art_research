# Type-Safe Decision Frameworks for Agentic 5G Control: A Theory-Driven Testbed Characterization of Where They Can Be Applied (2026)
Cheie: Kourtis2026Typesafeagents . DOI/link: arXiv:2609.33689 . Sursa textului: integral, arXiv v1 (2609.33689v1, 27 Sep 2026): https://arxiv.org/pdf/2609.33689
Sectiunea din plan: B

## Problema (cum o formuleaza autorii)
Un controller agentic in 5G/O-RAN poate executa doar actiuni din setul de optiuni expus de retea, deci iesirea trebuie sa fie un element al unui set declarat, nu text liber. LLM-urile esueaza acest contract prin format, parsing sau raspuns la o alta intrebare. Framework-urile "type-safe" (care intorc o distributie de probabilitate peste optiuni) garanteaza tipul iesirii, dar nu au fost caracterizate fata de constrangerile controlului 5G: deadline-uri, tipul intrebarii declarat la runtime, numarul de etichete necesare inainte ca o actiune sa fie de incredere, co-locarea mai multor modele pe un singur GPU de edge. Intrebari: ce ofera, cat costa si unde se poate aplica fiecare.

## Ce propun (metoda, pe scurt)
O caracterizare bazata pe teorie a trei framework-uri: Jev (model hosted, TypeSafe AI, jev-1.13.0), Laya (encoder tipat open, 421M parametri, ModernBERT-large) si AnyJev (retrofit zero-label al unui LLM deschis, aici Qwen3-8B). Cadrul teoretic are opt axe (A0-A8, Tabel I) si rezultate formale: gate optim act/escalate/abstain (Teorema 1, Corolar 1), plafon de fezabilitate a escaladarii (Lema 1), conditie de stabilitate la co-locare (Prop. 1), conformal risk control per tip cu prag minim de etichete (Teorema 2, Lema 2: 19 etichete la alpha=0.05, 9 la 0.10), limita de type-mismatch (Prop. 2) si predicate de aplicabilitate (Prop. 3: timeliness, type, coverage, cardinality). Rezultatul este o "harta de aplicabilitate" de la framework la clasa de decizie 5G (Fig. 6).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Core: Open5GS 2.8.0, cu pereche SMF/UPF per slice (eMBB, URLLC, mMTC). UE si gNB emulate cu UERANSIM (doua patch-uri locale: PDU session resource modify, clasificare QoS-flow uplink). srsRAN prin ZeroMQ disponibil, dar fara rezultate de timing RAN. Fara radio real.
- Bucla de politici (Plane B): NWDAF (open5gs-nwdaf) -> loop agent -> serviciu de decizie tipat (/v1/judge) -> politica instalata prin N5 la PCF, apoi N7 la SMF, PFCP la UPF. Plane A (E2/near-RT RIC) nu este inchis.
- Hardware: GPU edge NVIDIA L4 (SM clock blocat la 1050 MHz) pentru latenta; RTX 4090 pentru antrenare/acuratete; System-2 = Qwen3-8B (bf16 si AWQ 4-bit) sub vLLM 0.30.0. Host-ul de decizie si core-ul sunt pe noduri hypervisor diferite, pe VLAN-ul de management 1 GbE partajat.
- Date: corpus inghetat "v2" cu 3,645 itemi de test, 8 clase de decizie cunoscute (handover cu k in {4..64} vecini, SLA breach, urgency, anomaly severity), etichete generate din reguli de simulator; partitii train/calibration/test/shift; corpusuri derivate: 8 template-uri declarate la runtime (2,400 itemi test) si 4 reformulari. Itemii contin stare de retea (KPM-uri slice, RSRP, incarcare). Endpoint-uri pre-inregistrate (non-inferioritate 3 pts, bootstrap 10,000, 5 seed-uri); abaterile sunt jurnalizate.

## Experimente si metrici
Pe axe: A0/A1 tip si calitate pe tipuri cunoscute (acuratete); A2/A3 gate certificat (P(ACT si gresit), ACT rate) si etichete pentru tip nou (leave-one-family-out); A4 type conformance pe template-uri contrafactuale; A5 timeliness (latenta p50/p99, curba de serviciu System-2, co-locare la 20 Hz, catch-up batching, replay pe trace cu gate-uri); A6 cardinalitate; A7 reformulari; A8 energie (J/decizie) si suveranitate. Harta de aplicabilitate pe grila de deadline {100 ms, 500 ms, 1 s, 5 s, 60 s} cu epsilon=0.01, alpha=0.05, coverage floor 0.5.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Tabel II (k=4, p99 pe L4): acuratete tipuri cunoscute / question-reading / latenta p99 / J per decizie: Laya FT 0.90 / 0.41 / 25.8 ms / 1.10; Laya base 0.27 / 0.27 / 25.8 / 1.10; Encoder 0.92 / fara readout / 23.5 / 0.55; AnyJev-8B L0 0.44 / 0.81 / 283 / 19.6; AnyJev-8B L2 0.73 / fara readout / 94 / 6.6; Jev 0.67 / 0.99 / 596 / nemasurat.
- Tabel III (alpha=0.05): specialistii actioneaza pe 43-99% din decizii, AnyJev zero-shot cel mult 29%, Jev 8-78%. Celula SLA a AnyJev L0 depaseste bugetul (risc 0.199, circa 4x alpha).
- Tabel IV: etichete pana la actiune certificata pe familie noua (Laya / encoder): SLA 100/300, urgency 300/1000, handover 1000/>1000, anomaly 300/100. Claim-ul pre-inregistrat de 3x mai putine etichete a tinut in 2 din 4 familii.
- Type mismatch (Fig. 2, Tabel V): Laya FT a returnat raspunsul vechi pe 0.982-0.995 din perechi item-seed; pe "most loaded neighbour" 0.009; 0.801 din itemi au ajuns act-and-wrong. Rezultate safe/in limita/violare: Jev 6/1/0, AnyJev L0 4/3/0, Laya FT 1/6/0. Rezumat abstract: act-and-wrong cel mult 0.143 (Jev) si 0.137 (AnyJev).
- Timeliness: System-2 decodeaza la 22.1 ms/token dupa 94 ms primul token; la clasa de 1 s buget de 41 tokeni vs cel mai scurt raspuns 47 tokeni (45 cuantizat) (Fig. 3a). Co-locat, System-1 are 67 ms p99 la perioada de 50 ms; u* aproximativ 0.66 (Fig. 3b). Catch-up batching: p99 loop 142-146 ms pana la 1 req/s vs 2.0-29 s fara; 12-56% ratate la 100 ms, niciuna la 250 ms (Fig. 3c). Replay (Fig. 4): regula R1 reduce violarile SLA de la 0.068 la 0.044 la deadline x60, escaladand 14.2 din 3,645 decizii.
- Jev: p50 TCP 199 ms, warm p50 281 ms (k=4), cold 726 ms. Energie: 0.55 J (encoder), 1.10 J (Laya), 19.6 J (AnyJev-8B L0).
- Fig. 6 (harta): specialistii fine-tuned aplicabili de la 100 ms pe GPU dedicat (encoder 8/8, Laya 7/8); tipuri noi: Jev 6/8 (warm) si AnyJev L0 4/8 la 1 s.
- Tabel VI: rezultatele endpoint-urilor pre-inregistrate (ex. retention +0.138 [+0.114, +0.163]).

## Limitari declarate de autori
Sec. IX: (1) claim de eficienta a etichetelor tinut in 2 din 4 familii; (2) Laya FT este question-blind; (3) Plane A (E2/near-RT RIC) nu e inchis, rezultatele near-RT sunt in izolare si prin replay; (4) fara RAN real, timing RAN scopat printr-un real-time factor; (5) etichete din reguli de simulator; (6) un singur LLM 8B ca System-2 si ceiling de acuratete; (7) shift split slab; (8) Jev este hosted si versionat; (9) analizele reducerii group-and-final si ale buclei per framework sunt in versiune extinsa; (10) fine-tuning question-contrastive si partitionarea GPU (MPS) nemasurate, harta e pentru GPU dedicat; (11) confound backbone intre Laya si encoder; (12) razele de robustete certificate limitate de n=100.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? da - Open5GS 2.8.0 cu SMF/UPF per slice, NWDAF open5gs-nwdaf, PCF (Sec. V-A)
- UE reale sau emulate? emulate - UERANSIM, fara radio real (Sec. V-A, IX)
- digital twin al retelei? nu - mentionat doar la lucrari conexe (OpenTwin) (Sec. II-B)
- prezice efectul unei actiuni inainte de a o aplica? nu - deciziile sunt clasificari/alegeri tipate; nu se simuleaza efectul actiunii; fara etichete de rezultat pentru bucla (Sec. VI-G)
- executa actiuni automat (bucla inchisa)? da, partial - bucla core-policy NWDAF->PCF->SMF->UPF inchisa, deciziile zero-shot fara etichete de rezultat, deci stabileste integrare, nu calitatea politicii; Plane A nu e inchis (Sec. V-A, VI-G, IX)
- multi-site / geo-redundanta / failover de baza de date? nu - nedeclarat (un singur platform)
- evaluare prospectiva (predictie fixata inainte de experiment)? da - endpoint-uri pre-inregistrate, cu abateri jurnalizate (Sec. V-B, Tabel VI)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - metrici la nivel de decizie (acuratete, risc, latenta, energie) pe corpus sintetic (Sec. VI)
- observa traficul la SCP / proxy? nu - observare prin NWDAF pe loguri si contoare (Sec. V-A)
