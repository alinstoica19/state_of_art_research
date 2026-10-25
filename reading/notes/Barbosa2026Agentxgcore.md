# Agent xG Core: Agentic AI for Next-Generation Mobile Core Network (2026)
Cheie: Barbosa2026Agentxgcore . DOI/link: 10.1109/mnet.2026.3699249 . Sursa textului: integral, arXiv v1 (2606.00417v1, 29 May 2026, acceptat la IEEE Network): https://arxiv.org/pdf/2606.00417
Sectiunea din plan: B

## Problema (cum o formuleaza autorii)
Core-ul 6G (xGC, "Beyond Next Generation Core") va avea mai multe NF-uri, iar managementul si orchestrarea devin greu de facut manual. Functiile AI din 3GPP (NWDAF, AnlF/MTLF din Rel-17, AI/ML in OAM din Rel-18/19) sunt descrise ca centralizate si orientate pe suport de decizie, nu pe control autonom in bucla inchisa. Lucrarile existente cu GenAI/IBN pentru core (deployment, orchestrare servicii, management NF) depind de interventia utilizatorului si nu trateaza intent-uri QoS pentru core-ul 5G si dincolo; lucrarile cu agentic AI se concentreaza pe RAN. Autorii identifica o lipsa de bucle inchise AI pentru self-optimization/self-organization in xGC si de demonstratii practice.

## Ce propun (metoda, pe scurt)
AgentxGCore: un strat "Agentic AI-native" care extinde arhitectura 3GPP si reutilizeaza API-urile 3GPP si MANO existente, expuse printr-un MCP Server. Componente (Fig. 3): Intent Manager (intent-uri one-shot si continuous control, apeleaza periodic Planner-ul), Network Planner Agent (interogheaza Monitor Tools, evalua LLM-ul daca intent-urile sunt satisfacute, produce un plan), Network Executor Agent (verifica fezabilitatea planului, alege tool-uri prin MCP, le executa; memorie contextuala ca sliding window marginit). Monitor Tools: metrici NWDAF, Prometheus/Kubernetes (CPU, RAM), AI Tools (modele DL de predictie trafic), External Tools. Execution Tools: API MANO (creare NF) si API 3GPP (politici PCF, modificare sesiuni SMF), plus AI Tools (ex. load balancing DL intre eUPF). Coordonare intre agenti in stil A2C/A2A, workflow ca graf cu scheme de mesaje. Sunt prezentate si o trecere in revista a evolutiei AI/ML in 3GPP si a modelelor AI (DL, GenAI, AI agents, Agentic AI), plus Tabelul I cu lucrari conexe.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Implementat ca extensie a OpenAirInterface (OAI) 5G Core, mediu Docker; API pentru activare/dezactivare noduri CN; API 3GPP expuse pentru PCF si SMF; tool-uri Prometheus (Sec. VI-B).
- RAN si utilizatori: gnbsim cu 21, 34, 55 si 89 utilizatori, rata de sosire 5 pe utilizator pe secunda.
- Date: dataset public de trafic [12] (Cloud Gaming, Live Streaming, Video on Demand), rezumat si injectat cu iperf3.
- Model AI de predictie: GRU pe seria temporala de downlink, orizont de predictie 10 s.
- LLM-uri comparate: Gemini Pro 2.5, Gemini Flash 2.5, GPT-4.1, GPT-4.1 Mini.
- Trei intent-uri: (1) pastrare downlink UPF in jur de 25 MB/s; (2) maxim 3 instante UPF, creare doar la cerere crescuta si distribuire utilizatori; (3) oprire UPF subutilizate fara utilizatori, cel putin o instanta ramasa (Sec. VI-A).

## Experimente si metrici
Variatie numar utilizatori (21, 34, 55, 89) x 4 LLM-uri. Metrici (Sec. VI-C): (i) timp mediu de executie (suma timpului in Agentic Engine: apeluri LLM si interactiuni LLM-tool); (ii) downlink mediu (apropierea de valoarea intent-ului); (iii) RTT mediu intre utilizator si serverul iPerf, rezultat al deciziilor de creare UPF si distribuire utilizatori.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Rezultatele sunt prezentate doar grafic (Fig. 4a-c in text; textul le numeste "Figure 2a-c"), fara valori numerice in text. Descriere: familia GPT are cele mai mici timpuri medii de executie (Fig. 4a), interpretat de autori ca subutilizare a tool-urilor, iar aceste modele se abat de la valoarea tinta de downlink (Fig. 4b). Modelele mai mari (GPT-4.1, Gemini Pro 2.5) sunt descrise ca "overthinking" pe sarcini continue simple, vizibil in RTT mai ales cu putini utilizatori (Fig. 4c). Gemini Flash are throughput apropiat de valoarea ceruta si control mai bun al RTT; cu putini utilizatori are timp de executie mai mare. Concluzia autorilor: modelele cu mai putini parametri satisfac mai bine obiectivele. Nu sunt raportate cifre exacte, nici variante/repetari.

## Limitari declarate de autori
Sec. VII (Open Research Issues): securitate (halucinatii, planuri gresite, activari/dezactivari continue de NF si intreruperi de sesiuni PDU daca agentul are control total; expunerea datelor catre LLM-uri remote); LLM local vs remote (latenta, disponibilitate, limite de cereri, hardware specializat pentru modele locale); overhead de mesaje si apeluri API de monitorizare continua. Ca directie viitoare: coordonare Core-RAN, intent-uri de nivel mai inalt. Concluzia mentioneaza evaluarea pe scenarii de load balancing.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? da - OAI 5G Core in Docker (Sec. VI-B)
- UE reale sau emulate? emulate - gnbsim (Sec. VI-B)
- digital twin al retelei? nu - nu este mentionat in sistem
- prezice efectul unei actiuni inainte de a o aplica? partial - model GRU prezice incarcarea de trafic la 10 s pentru a decide crearea unui UPF; nu se simuleaza efectul actiunii (Sec. VI-B)
- executa actiuni automat (bucla inchisa)? da - Executor apeleaza API MANO/3GPP, bucla Intent Manager-Planner-Executor (Sec. V, VI)
- multi-site / geo-redundanta / failover de baza de date? nu - nedeclarat/neabordat (un singur mediu Docker)
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? partial - throughput si RTT intre utilizator si serverul iPerf (Sec. VI-C); nu sunt raportate inregistrari/sesiuni ca metrici
- observa traficul la SCP / proxy? nu - observabilitate prin NWDAF, Prometheus, UPF; SCP nementionat
