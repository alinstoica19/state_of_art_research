# Agentic-NWDAF: Enabling Intent-driven Agentic Intelligence for Autonomous 6G Network Analytics (2026)
Cheie: Ameur2026Agenticnwdaf . DOI/link: https://doi.org/10.1109/icc59461.2026.11587766 . Sursa textului: integral: PDF urcat de autor (Agentic-NWDAF_Enabling_Intent-driven_Agentic_Intelligence_for_Autonomous_6G_Network_Analytics.pdf)
Sectiunea din plan: A . Tema: analitica
Autori: Mazene Ameur, Bouziane Brik, Adlen Ksentini (EURECOM; University of Sharjah). ICC 2026; 6 pagini; proiect UE 6G-DALI.

## Problema (cum o formuleaza autorii)
3GPP (TS 29.520) si ETSI ENI definesc modul in care OSS interactioneaza cu NWDAF prin API-uri service-based. Autorii considera aceste interactiuni procedurale: subscrieri statice la analitica si triggere pe reguli. Ca urmare, intentiile operatorului nu pot fi interpretate dinamic.

Lucrarile NLP/LLM pentru intent-based management au, dupa autori, cinci limite (Sectiunea II):
- nu trateaza orchestrarea analiticii NWDAF;
- se bazeaza pe NLP sau pe un singur LLM fine-tuned;
- depind de reprezentari structurate predefinite, de exemplu JSON;
- nu sunt proiectate pentru OSS de nivel telecom;
- relatia OSS-NWDAF din standarde ramane o strangulare pe drumul spre retele autonome.

## Ce propun (metoda, pe scurt)
- **Agentic-NWDAF:** un strat de orchestrare care traduce intentiile OSS din limbaj natural in apeluri de servicii NWDAF (Sectiunea III).
- **Trei straturi:**
  - stratul operatorului, numit de autori "User Plane Layer";
  - stratul agentic OSS-NWDAF;
  - stratul de infrastructura cu MTLF (MLModelTraining, MLModelProvisioning) si AnLF (AnalyticsInfo, SubscriptionAnalytics) (Fig. 1).
- **Agentii:**
  - Chatbot Agent: valideaza intentia si o structureaza;
  - Planner;
  - API Selector: ia specificatiile 3GPP prin MCP;
  - Payload Generation;
  - Validator;
  - Executor: apeleaza AnLF/MTLF prin MCP;
  - Monitoring: raporteaza rezultatele inapoi la OSS.
- **Doua servere MCP:** unul expune serviciile NWDAF, celalalt ofera acces la documentatia API 3GPP. Retrieval prin MCP inlocuieste fine-tuning-ul.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- **Implementare:** CrewAI, modele locale prin Ollama, ChromaDB ca vector database, servere MCP implementate cu FastMCP (IV.C).
- **Hardware:** NVIDIA Jetson AGX Orin (GPU Ampere cu 2.048 nuclee, 64 Tensor Cores, 64 GB memorie).
- **Core:** OAI NWDAF extins, in OAI 5G Core Network, cu MTLF si AnLF.
- **Modele evaluate:**
  - non-reasoning: Llama3.1:8B, Qwen3:8B, Mistral:7B, Falcon3:7B;
  - reasoning: DeepSeek-R1:14B, Phi4-Reasoning:14B, GPT-OSS:20B;
  - judecator: Mixtral 8x7B (LLM-as-a-Judge);
  - o singura instanta LLM pentru toti agentii.
- **Benchmark:** 100 de "golden intents" derivate din specificatiile 3GPP, acoperind categoriile de analitica NWDAF. Au fost adnotate de experti si revizuite de specialisti externi de la EURECOM si din proiecte UE (IV.A).
- Numarul de UE si traficul din core nu sunt declarate.

## Experimente si metrici
- Task Success Rate (TSR), Tool Selection Accuracy (TSA), timpul de executie si consumul de tokeni pe 15 categorii de intentii (Fig. 2-5).
- Scor LLM-as-a-Judge pe o scala din 5 (Fig. 6).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- TSR (Fig. 2):
  - Mistral-7B si Qwen-8B ating aproximativ 75-78%; Falcon-7B are cel mai mic TSR;
  - gpt-oss-20B si DeepSeek-R1-14B depasesc 85-90%.
- TSA (Fig. 3): gpt-oss-20B aproximativ 95%; Falcon-7B si LLaMA-8B intre 70 si 78%.
- Timp de executie (Fig. 4): modelele reasoning au intre aproximativ 90 s si peste 170 s; modelele non-reasoning sub 50 s.
- Tokeni (Fig. 5): gpt-oss-20B peste 22.000 la intentiile complexe; DeepSeek-14B si Phi4-14B peste 18.000; modelele non-reasoning intre 12.000 si 16.000.
- LLM-as-a-Judge (Fig. 6): Falcon-7B 2,4; Qwen-8B, LLaMA-8B si Mistral-7B intre 3,0 si 3,5; Phi4-14B, DeepSeek-14B si gpt-oss-20B intre 4,0 si 4,8.
- Valorile sunt citite in text din figuri. Nu exista tabel numeric.

## Limitari declarate de autori
- Cerintele de calcul si de infrastructura ale LLM-urilor mari in productie; consistenta performantei, costul si ciclul de viata al modelelor (IV.E).
- Scorurile LLM-as-a-Judge pot varia, deoarece evaluatorii MoE pot favoriza cereri API fluente si bine structurate in detrimentul fidelitatii semantice (IV.D.2).
- Setup-urile multi-model si heterogene nu au fost explorate (IV.C).
- Lucrari viitoare: reducerea amprentei de calcul a agentilor (V).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - OAI 5G Core cu OAI NWDAF extins (MTLF, AnLF) (IV.C).
- UE reale sau emulate?: nedeclarat.
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu - Validator Agent verifica doar conformitatea payload-ului cu API-ul (III.B).
- executa actiuni automat (bucla inchisa)?: partial - apeluri automate de servicii de analitica NWDAF; nu sunt actiuni asupra configuratiei retelei (III.B).
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat (benchmark-ul de 100 de intentii este etichetat de experti; nu se precizeaza daca a fost fixat inainte de dezvoltare).
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu - metricile sunt la nivelul traducerii intentiilor.
- observa traficul la SCP / proxy?: nu.
