# AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks (2026)
Cheie: Moreira2026Agenticgreen . DOI/link: 10.1109/access.2026.3672699 (arXiv:2602.13290) . Sursa textului: integral, arXiv v1 (8 feb. 2026): https://arxiv.org/pdf/2602.13290v1
Sectiunea din plan: B . Tema: energy-aware / agentic UPF steering

## Problema (cum o formuleaza autorii)
Abordarile ZTN, SON si IBN nu ofera un mecanism practic de a traduce obiective umane de sustenabilitate in actiuni UPF verificabile, executate de unelte si ancorate continuu in telemetrie in timp real (Problem statement, Sec. I). Autorii afirma ca, dupa cunostintele lor, abordarile existente nu actioneaza direct UPF-ul 5G pentru obiective de management "verde".

## Ce propun (metoda, pe scurt)
- AGORA: agent LLM local, augmentat cu unelte, plasat in bucla de control a retelei; transforma intentii in limbaj natural in apeluri de unelte ancorate in telemetrie si in actiuni de rutare la UPF (Sec. I, III).
- Bucla in patru etape: ingestia intentiei, estimarea starii prin unelte, evaluarea politicii, actuare (Sec. III-B). Spatiul de actiuni este discret: route_to_MEC1 sau route_to_MEC2 (Ec. 1).
- Doua unelte: energy_mean_last_time(mec, delta) (proxy de energie din telemetrie) si upf_set_target(mec) (selectia egress a UPF). Textul mentioneaza ca in implementari conforme cu standardele unealta poate fi sustinuta de telemetria 3GPP Energy Information Function (EIF) (Sec. III-B).
- Regula de conformitate: migreaza la MEC1 daca puterea observata pe MEC2 depaseste pragul theta (Ec. 3); doi indicatori binari, tool compliance si action compliance (Ec. 7). Actuarea fara masurare prealabila e considerata necorespunzatoare (Sec. III-E).
- Suita de patru intentii (Tabel 2: Threshold, Policy-based cu prag 20 W, Contextual, Urgent), inclusiv formulari in portugheza (Sec. III-C).
- Energia per decizie: E = P x T (Ec. 5); energie per token (Ec. 6).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Platforma FABRIC, nod OpenStack cu AMD EPYC 7543, 64 GiB RAM, GPU NVIDIA A30 24 GB; Kubernetes v1.28.15 (Sec. IV-A).
- Core 5G: free5GC; un UPF cu interfata simpla de control; doua instante MEC (MEC1 doar CPU, tinta "verde"; MEC2 cu GPU, nod stresat) ca pod-uri separate (Sec. IV-B). Numarul de UE nu este precizat; UE-ul sondeaza tinta curenta cu ping si optional iperf3/UDP (Sec. IV-F).
- LLM: servite local cu vLLM (endpoint compatibil OpenAI): Qwen2.5 1.5B Instruct, Mistral 7B Instruct v0.2, Phi 3.5 Mini Instruct, OLMoE 1B-7B Instruct, Sabia 7B (model portughez) (Sec. IV-C).
- Telemetrie: Kepler (metrici de energie la nivel de container) si Prometheus, plus metrici vLLM (Sec. IV-D).
- Sarcina: stres CPU sintetic prin Chaos Mesh (StressChaos), asimetric (MEC2 incarcat mai mult), jurnalizat; agentul nu are acces la programul de stres (Sec. IV-E, IV-G).
- Rulari independente repetate, cu pornire la rece a serverului vLLM intre rulari; numarul de rulari R nu este dat explicit (Sec. III-G, IV-G).

## Experimente si metrici
Comparatie intre modele LLM: energia totala la MEC-ul activ, latenta de inferenta (CDF), energie per token, tokeni generati, relatia timp de inferenta - energie GPU - throughput, putere GPU, latenta ping si jitter la UE, probabilitatea de migrare in functie de puterea MEC2, selectivitate (TPR, PPV, FPR) pentru Qwen, profilul de incarcare CPU si distributia puterii/utilizarii GPU (Sec. V, Fig. 2-16).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Energie totala MEC activ (Fig. 2): OLMoE 502.6 J, Qwen 910.3 J, Mistral 4252.3 J, Phi 6089.9 J.
- Latenta de inferenta (Fig. 3): OLMoE mai ales sub 0.6 s; Qwen 0.7-1.0 s; Phi peste 6 s.
- Energie per token (Fig. 4): OLMoE 0.2654, Qwen 0.3183, Phi 0.5307, Mistral 1.1311 J/token.
- Tokeni generati (Fig. 5): Phi 14,350; Mistral 6,330; Qwen 4,232; OLMoE 2,450.
- Throughput (Fig. 7): OLMoE si Qwen aprox. 140-195 tokens/s; Mistral si Phi de regula sub 90 tokens/s.
- Latenta UE (Fig. 8): in banda de zeci de milisecunde; doar Qwen are ambele stari de migrare in date, cu distributie usor mai jos si mai ingusta cand migrarea e activa. Jitter (Fig. 9): Phi si Qwen aprox. 0.012-0.013, OLMoE 0.015, Mistral 0.017.
- Migrare (Fig. 11): doar Qwen declanseaza migrari cu probabilitate nenula, maxim aprox. 0.43; celelalte modele raman la zero.
- Qwen, selectivitate (Fig. 12): true positive rate 28.57%, positive predictive value 80.00%, false positive rate 15.38%; prag 20 W.
- GPU (Fig. 14): distributie bimodala, benzi in jur de 30-40 W si 160-175 W.

## Limitari declarate de autori
Lucrari viitoare (Sec. VI): mai multe LLM-uri deschise si configuratii multi-agent, suite de intentii mai mari si trafic mai divers (multi-slice, multi-tenant); interfete standardizate (MCP, Coral Protocol) in loc de wrappere ad hoc; semnale de intensitate de carbon, politici sensibile la risc; validare pe testbed-uri mai mari cu MEC heterogene si trace-uri reale. Concluzia mentioneaza ca decalajul este inchis "partially".

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? da - free5GC pe Kubernetes (Sec. IV-B).
- UE reale sau emulate? nedeclarat - UE-ul sondeaza tinta cu ping/iperf3; tipul (real/simulat) si numarul nu sunt precizate (Sec. IV-F).
- digital twin al retelei? nu - nu este implementat; apare doar in related work (Sec. II-C).
- prezice efectul unei actiuni inainte de a o aplica? nu - decizia se bazeaza pe puterea observata si pe prag (Ec. 3).
- executa actiuni automat (bucla inchisa)? da - upf_set_target actioneaza UPF-ul (Sec. III-B, V).
- multi-site / geo-redundanta / failover de baza de date? nu pentru geo-redundanta/DB; exista doua site-uri MEC ca pod-uri in acelasi cluster (Sec. IV-B).
- evaluare prospectiva (predictie fixata inainte de experiment)? nu - evaluare comparativa pe suita de intentii, fara predictie prestabilita.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - se masoara ping, jitter, pierdere UDP la UE, nu inregistrari/sesiuni (Sec. III-F, V).
- observa traficul la SCP / proxy? nu - SCP nu este mentionat; telemetria vine din Kepler/Prometheus.
