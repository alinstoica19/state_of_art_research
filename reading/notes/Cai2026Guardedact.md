# Can AI Remediate Backend Failures Safely? GuardedAct with Blast-Radius-Aware Sandboxing (2026)
Cheie: Cai2026Guardedact . DOI/link: https://arxiv.org/abs/2609.11264 . Sursa textului: integral: arXiv (versiune neprecizata in fisier)
Sectiunea din plan: 0 . Tema: nedeclarata

## Problema (cum o formuleaza autorii)
LLM-urile pot genera actiuni de remediere pentru defecte de microservicii, dar executarea directa a actiunilor generate in productie risca daune colaterale in cascada, uneori mai mari decat defectul initial (Sec. I). Autorii cer ca remedierea generata de AI sa fie tratata ca cod nesigur si verificata inainte de executie.

## Ce propun (metoda, pe scurt)
GuardedAct, un cadru "sandbox-first" in patru faze (Fig. 1, Sec. III): (1) preia un raport de diagnostic, graful de dependente intre servicii si un snapshot de telemetrie (CPU, memorie, latenta, rata de erori); (2) un LLM produce o lista ordonata de actiuni candidate dintr-un vocabular tipizat (restart, drain, traffic_shifting, rate_limiting, configuration_rollback); (3) fiecare actiune este simulata intr-un sandbox de tip digital twin (stub-uri containerizate care reproduc graful de dependente, reluand 5 minute de telemetrie, orizont de propagare 60 s simulate) si se calculeaza blast radius B(a_i) = suma w(s)*p(s|a_i) pe serviciile aflate la cel mult d=3 salturi (Ec. 1), cu eticheta de risc low/medium/high (percentile 33/66 pe 50 de incidente istorice); (4) un "rollback-confidence gate": RC(a_i) = 1 - B(a_i)/B_max * (1 - r(a_i)) (Ec. 2), cu scoruri de reversibilitate r calibrate pe 30 de trasee etichetate (rollback de configuratie 0.90, rate limiting 0.45, traffic shifting 0.30, drain 0.20, restart 0.10); actiunea se executa automat daca RC depaseste pragul tau (implicit 0.6), altfel este escaladata la revizuire umana (Ec. 3).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Aplicatia DeathStarBench social-network pe cluster Kubernetes cu 30 de pod-uri de microservicii (Sec. IV-A). Cinci defecte injectate: saturare CPU (stress-ng 95% pe compose-post), timeout downstream (intarziere 5 s pe user-timeline), memory leak (home-timeline), misconfigurare (rate-limit invalid prin ConfigMap pe nginx), jitter de retea (200 ms intre media service si MongoDB). Baseline-uri: Direct LLM (nivel GPT-4, executie imediata), Rule-Based (runbook fix), Typed (fara sandbox), GuardedAct; acelasi prompt, temperatura 0.2. Fiecare scenariu repetat de 100 ori, 500 de incercari in total. Nu este un core 5G.

## Experimente si metrici
Recovery Rate (revenire la sanatate in 5 minute), Collateral Damage Rate (servicii neafectate anterior degradate dupa remediere), MTTR, Rollback Success Rate, Human Intervention Rate. Serviciu sanatos: p99 in limita +20% fata de baseline si erori sub 1% pentru trei verificari consecutive la 10 s. Analiza per scenariu (Fig. 2), ablatii: fara sandbox / fara blast-radius / fara RC gate (Fig. 3a), sensibilitate la prag (Fig. 3b).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Tabelul I (medii pe 100 de incercari/scenariu), Direct LLM / Rule-Based / Typed / GuardedAct: Recovery 64.0 / 66.0 / 78.0 / 87.4 %; Collateral 25.6 / 19.8 / 14.2 / 5.2 %; MTTR 59.6 / 60.0 / 52.6 / 61.4 s; Rollback success 55.0 / 62.0 / 70.0 / 90.0 %; Human intervention 0.0 / 0.0 / 0.0 / 35.0 %. Overhead sandbox mediu 8.2 s per actiune. Recovery 92% pe saturarea CPU. Direct LLM are 35% daune colaterale pe memory leak (Fig. 2b). Ablatii: eliminarea sandbox-ului scade recovery cu 10-12 puncte pe memory leak si misconfigurare; eliminarea RC gate scade recovery cu 14-20 puncte. Prag tau de la 0.3 la 0.9: harm de la 12% la sub 2%, recovery de la 94% la 65%, interventie umana de la 5% la 80%; interval recomandat [0.55, 0.70] (Fig. 3b).

## Limitari declarate de autori
Sandbox-ul aproximeaza productia cu telemetrie reluata si nu surprinde tot nedeterminismul; predictorul presupune graf de dependente complet; evaluare pe un singur benchmark cu cinci tipuri de defecte; robustetea la diagnostic RCA zgomotos ramane viitor; o actiune aparent sigura in sandbox dar aplicata pe serviciul gresit poate fi totusi executata; nu e validata pe trasee industriale; pentru recuperari sub o secunda ar fi nevoie de un model mai usor (Sec. VI, VII).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu - Sec. IV-A: aplicatie de microservicii DeathStarBench, nu 5G
- UE reale sau emulate? nu - Sec. IV-A: fara UE
- digital twin al retelei? da - Sec. III-D: sandbox "digital twin" al clusterului de microservicii (stub-uri containerizate), nu al unei retele 5G
- prezice efectul unei actiuni inainte de a o aplica? da - Sec. III-B, III-D: simuleaza fiecare actiune si estimeaza blast radius
- executa actiuni automat (bucla inchisa)? da - Sec. III-C: auto-executie a actiunilor cu RC peste prag, restul escaladate
- multi-site / geo-redundanta / failover de baza de date? nedeclarat
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat - Sec. III-B indica semnal "prospectiv" din simulare cu replay, dar fara protocol de predictie pre-inregistrata
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - Sec. IV-C: metrici la nivel de serviciu (p99, rata de erori, recovery)
- observa traficul la SCP / proxy? nedeclarat
