# LLM-Powered Agentic AI for 5G/6G Networks: A Tutorial and Survey on Architectures, Protocols, and Standardization (2026)
Cheie: Ameur2026Agenticsurvey . DOI/link: arXiv:2607.16066 (https://arxiv.org/abs/2607.16066) . Sursa textului: integral, arXiv v1 (17 Iul 2026), https://arxiv.org/pdf/2607.16066
Sectiunea din plan: A
## Problema (cum o formuleaza autorii)
Agentic AI bazat pe LLM marcheaza trecerea de la automatizare bazata pe reguli la control autonom, orientat pe obiective, al retelelor de generatie urmatoare (NGN). Autorii afirma ca sondajele existente trateaza izolat domeniile (LLM in 6G, teorie agentica, securitatea/protocoalele agentilor, viziuni AGI-native), lasand sub-explorate integrarea de protocoale, evaluarea si alinierea cu standardizarea (Tab. 1). Sustin ca nicio lucrare anterioara nu trateaza impreuna LLM-uri, concepte agentice, protocoale agentice, evaluare/benchmark-uri, integrare in retea si standardizare.
## Ce propun (metoda, pe scurt)
Tutorial plus survey in doua parti. Partea I: Sec. 2 (arhitectura NGN: control plane RAN/TN/CN/Edge-Cloud, management plane cu IBN si ZSM, AI-native plane) si Sec. 3 (de la LLM la Agentic AI; strategii de adaptare LLM, Tab. 2; concepte: agenti, memorie, tool-uri, planning; sabloane arhitecturale ReAct, AutoGPT, Agentic RAG, Multi-Agent Systems, Tab. 3; protocoale MCP, A2A, ANP, ACP, AP2 si integrarea lor in 6G, Tab. 4; metode de evaluare: metrici la nivel de task, de interactiune cu tool-uri, de eficienta/sistem). Partea II: Sec. 4 (survey pe taxonomie: control plane, management plane, AI-native plane; Tab. 5-7), Sec. 5 (standardizare si proiecte 6G; Tab. 8-9), Sec. 6 (provocari deschise), Sec. 7 concluzii. Metodologie de selectie: cautari pe Google Scholar cu cuvinte-cheie (Agentic AI, LLM agents, Next Generation Network, 5G, 6G), cu pre-selectie pentru sondajele conexe (Sec. 1.2).
Continut relevant pentru core/NWDAF: Tab. 5 include categoria "Data Ops." (NWDAF-style collection si log semanticization) cu referinte [43, 87, 110, 136, 137]; Sec. 4.3.1 descrie lucrarea Quadrini et al. [136] care foloseste NWDAF pentru colectarea traficului real al core-ului 5G; Tab. 6 listeaza o lucrare MAS ierarhic cu Agentic RAG + MCP si tool "KB + NWDAF" pe domeniul Core (NWDAF) [77]. Sec. 4.1.3 (Core Network): semantic routing prin LLM [108], Mobile-LLaMA [111], A-Core si Agentic-AI Core [112-114], LLM-Slice [115, 116]. Sec. 4.2 (IBN/ZSM): pipeline-uri de intent translation, conflict resolution, assurance, LaMA-SON, IBN-ZTSA.
## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Nu este lucrare experimentala; nu are testbed propriu. Mentioneaza ca exemple ale lucrarilor revizuite: ONOS/Ryu (SDN), ns-3 (GenoNet), Ollama cu diverse LLM-uri (Tab. 6). Sec. 6.5 propune ca directie viitoare benchmark-uri pe platforme de emulare Open5GS, OpenAirInterface si Free5GC.
## Experimente si metrici
Nu este lucrare experimentala. Tab. 6 compara lucrari din management plane pe: arhitectura agentica, LLM, memorie, tool-uri, domeniu, KPI (ex. accuracy, execution time, LLM-as-Judge, success rate). Tab. 7 listeaza benchmark-uri telecom (TeleQnA, TeleTables, TelAgentBench, MM-Telco, TeleMath, TSpec-LLM, TeleYAML, alpha3-Bench) cu metrici.
## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Constatari formulate de autori (nu masuratori proprii):
- Sec. 4.1 (sinteza): rationamentul LLM nu poate satisface cerinte de control sub 10 ms; sunt necesare decompozitii ierarhice non-RT/near-RT; overhead-ul de semnalizare E2/A1/O1 este insuficient cuantificat.
- Sec. 4.2 (sinteza): fidelitatea traducerii intentiilor scade la ambiguitate si politici conflictuale; overhead-ul inter-agent este rar masurat fata de constrangerile ZSM; abordarile hibride LLM-DRL nu au garantii formale de stabilitate.
- Sec. 4.3 (sinteza): lipsa interfetelor standardizate intre iesirile NWDAF si reprezentari pregatite pentru LLM duce la preprocesare ad hoc; evaluarea ramane fragmentata.
- Tab. 8: 3GPP (TR 22.870), ETSI ZSM/ENI (GR 056, GS 059, GR 062), TM Forum, ITU-T, O-RAN Alliance, IETF, GSMA, cu goluri tehnice deschise per organizatie; Sec. 5.1 identifica trei goluri recurente (identitate/credentiale pentru agenti efemeri; interoperabilitate la nivel de fir intre ETSI GS 059, A2A si interfete 3GPP N-series; compromisul latenta-acuratete la plasarea agentilor).
- Tab. 9: proiecte SUNRISE-6G (2024-2027), 6G-INTENSE (2024-2027), 6G-DALI (2025-2028, agenti peste noduri compatibile NWDAF), FLECON-6G (2025-2028, agenti care interogheaza starea unui Network Digital Twin), OPEN6G (2022-in curs, AgentRAN, digital twin care valideaza actiunile inainte de comiterea in RAN live).
- Sec. 6.2: LLM de 7B-70B parametri necesita 14 GB pana la 140 GB memorie GPU pentru inferenta; compresia reduce memoria de 4-8 ori.
- Sec. 6.3: bucle near-RT RIC de 10 ms-1 s; modele 30B-70B pe un GPU single high-end: raspuns de ordinul 200 ms pana la cateva secunde per query.
- Sec. 6.4: 82.4% dintre modelele evaluate sunt compromise prin comunicare inter-agent, 52.9% prin RAG backdoor, 41.2% prin injectie directa (citat din [177]).
## Limitari declarate de autori
Sec. 6 enumera provocari: lipsa garantiilor deterministe (halucinatii, cascading hallucinations), cost computational si energetic, latenta de inferenta vs. scale de timp de control, vulnerabilitati de securitate in sisteme multi-agent, lipsa benchmark-urilor telecom specifice, explicabilitate/guvernanta/conformitate (EU AI Act, suveranitate date). Sec. 4.2 mentioneaza ca s-a ales deliberat extinderea focusului pe management plane.
## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu - survey/tutorial, fara implementare proprie
- UE reale sau emulate? nu - fara experimente proprii
- digital twin al retelei? nu - nu construiesc unul; mentioneaza FLECON-6G si OPEN6G ca proiecte cu digital twin (Sec. 5.2, Tab. 9)
- prezice efectul unei actiuni inainte de a o aplica? nu - fara sistem propriu; descrie digital-twin validation gating in OPEN6G (Sec. 5.2)
- executa actiuni automat (bucla inchisa)? nu - fara sistem propriu; surveyeaza lucrari cu control closed-loop agentic (Sec. 4.2.2)
- multi-site / geo-redundanta / failover de baza de date? nedeclarat
- evaluare prospectiva (predictie fixata inainte de experiment)? nu - nu este lucrare experimentala
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - fara masuratori proprii
- observa traficul la SCP / proxy? nedeclarat
