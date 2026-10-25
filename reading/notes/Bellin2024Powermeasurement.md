# A measurement-based approach to analyze the power consumption of the softwarized 5G core (2024)
Cheie: Bellin2024Powermeasurement . DOI/link: 10.1016/j.comnet.2024.110312 (arXiv:2502.13879) . Sursa textului: integral, arXiv v1 (19 feb. 2025, preprint trimis la Computer Networks): https://arxiv.org/pdf/2502.13879v1
Sectiunea din plan: B . Tema: energy-efficiency al 5GC

## Problema (cum o formuleaza autorii)
Tranzitia de la implementari legacy la NFV face mai dificila evaluarea consumului de energie si a amprentei de carbon a 5GC; impactul designului 5GC virtualizat nu este inca analizat pe deplin, iar modelarea consumului este dificila datorita heterogenitatii hardware si a tehnologiilor de virtualizare (Sec. 1). Se noteaza ca alegerea hardware-ului si a hypervisor-ului influenteaza puternic consumul.

## Ce propun (metoda, pe scurt)
- Abordare bazata pe masuratori pentru consumul VNF-urilor 5GC, cu un sistem proof-of-concept de monitorizare in timp real a puterii, descris ca alimentand un orchestrator de retea pentru decizii OAM (Sec. 1.1, 3.1, Fig. 1).
- Doua tipuri de contoare: hardware (smart-plug-uri Meross MSS310 interogate prin HTTP) si software (Scaphandre v0.5.0, bazat pe RAPL), plus throughput si utilizare CPU cu psutil (Sec. 3.2, 3.4).
- Modelare liniara a diferentei dintre cele doua contoare: P_hw = P_sw + alpha*T + c (Ec. 1).
- Textul mentioneaza eforturi de extindere a NF-urilor SBA (NWDAF, NEF) pentru observabilitate energetica (Sec. 3.1); acestea nu sunt implementate in lucrare.
- Datele colectate sunt puse la dispozitie public (Sec. 1.1, 7).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- 5 unitati Intel NUC (3 cu i5-7260U 2.20 GHz, 8 GB RAM; 2 cu i5-1145G7 2.60 GHz), Ubuntu 20.04, switch gigabit cu 5 porturi (Sec. 3.3, Fig. 2).
- Open5GS in trei configuratii: Bare Metal (BM), VM (QEMU/KVM), Container (CO, Docker, fiecare NF in container separat); plus Free5GC pe BM.
- UERANSIM pentru RAN si UE simulate; trafic cu Iperf3 si D-ITG; un NUC controler cu Redis (pub/sub) si scripturi Python.
- Trafic uplink, 100-800 Mbps in pasi de 100 Mbps; esantioane la fiecare secunda pe 30 s, pornind de la stare idle (Sec. 4.2). Baseline cu stress-ng (Sec. 4.1). Experiment cu 1, 2 si 10 UE (Sec. 4.5).

## Experimente si metrici
Putere (mW) in functie de sarcina CPU artificiala (Fig. 3); BM/VM/CO la niveluri de trafic, cu ambele contoare (Fig. 4-6, Tabel 1); Open5GS vs Free5GC pe BM (Fig. 7); consum per proces cu Scaphandre (Fig. 8); mai multe UE (Fig. 9-10). Metrici: putere, throughput, utilizare CPU.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Sarcina CPU (Fig. 3): relatie neliniara (interpolare polinomiala de grad 4); 0-20% crestere rapida, 20-80% crestere mica cu variabilitate mare, 80-100% consum mare (Turbo Boost).
- Fig. 4a: BM cel mai eficient; VM nu sustine peste 700 Mbps si consuma pana la 80% mai mult decat BM; CO consuma cu 25% mai mult decat BM la trafic maxim. Fig. 4b (Scaphandre): CO pana la 50% si VM pana la 175% mai mult decat BM.
- Tabel 1 (alpha, c): VM 9.99886 / 7338; BM 4.63977 / 7845; CO 6.46334 / 7575.
- Free5GC consuma aproape 40% mai putin decat Open5GS la 800 Mbps (Fig. 7), atribuit procesarii in kernel (GTP5G) fata de user space.
- Per proces (Fig. 8): in Open5GS UPF-ul domina consumul; in Free5GC consumul UPF e neglijabil; Scaphandre insusi consuma o putere mica dar semnificativa. Autorii noteaza inexactitati ale masuratorilor per proces.
- 1, 2, 10 UE: fara variatii substantiale in afara intervalului de incredere (Fig. 9-10).

## Limitari declarate de autori
Hardware limitat, dificil de simulat multe UE; putine solutii pentru trafic realist de abonati; scenarii precum massive IoT ar putea da rezultate diferite (Sec. 4.5). Inexactitati Scaphandre la nivel de proces (Sec. 4.4); contoarele software acopera doar CPU/RAM. Nu urmaresc un model general de putere (Sec. 5). Viitor: integrare intr-o platforma de orchestrare si antrenarea unui algoritm de reinforcement learning pentru eficienta energetica (Sec. 6).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? da - Open5GS si Free5GC (Sec. 3.3).
- UE reale sau emulate? emulate - UERANSIM (Sec. 3.3).
- digital twin al retelei? nu - nu este mentionat.
- prezice efectul unei actiuni inainte de a o aplica? nu.
- executa actiuni automat (bucla inchisa)? nu - doar monitorizare; orchestratorul este conceptual (Fig. 1, Sec. 3.1).
- multi-site / geo-redundanta / failover de baza de date? nu - un singur nod edge emulat; MongoDB doar ca proces masurat.
- evaluare prospectiva (predictie fixata inainte de experiment)? nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - puterea si throughput-ul, nu metrici per sesiune/inregistrare.
- observa traficul la SCP / proxy? nu - SCP nu este mentionat; traficul e masurat pe interfetele NUC.
