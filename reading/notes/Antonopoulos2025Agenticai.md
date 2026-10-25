# AGILE-6G: Agentic AI for Autonomous Management of 6G Network/Application Services (2025)
Cheie: Antonopoulos2025Agenticai . DOI/link: https://doi.org/10.1109/mnet.2025.3644039 . Sursa textului: integral: versiunea autorilor pe Zenodo (record 18088116, AGILE6G_magazine_author_version.pdf; versiune acceptata, "content may change prior to final publication")
Sectiunea din plan: C . Tema: agenti AI / orchestrare autonoma
Autori: Angelos Antonopoulos, Elli Kartsakli, Nikolaos Bartzoudis, Dimitrios Brodimas, Dejan Vukobratovic, Dimitris Tsolkas, Ferran Diego, George Roumelas, Lechoslaw Tomaszewski (Nearby Computing; BSC-CNS; CTTC; Enakronic; IVI; Fogus; Telefonica I&D; UniSystems; Orange Polska). IEEE Network (magazine). Proiectul Horizon Europe SNS-JU UNITY-6G.

## Problema (cum o formuleaza autorii)
- Convergenta cloud, edge si retea face orchestrarea pe silozuri nesustenabila. Tratarea separata a orchestrarii de servicii si de retea duce la logica duplicata, decizii conflictuale si folosire ineficienta a resurselor (I).
- GenAI si LLM-urile au imbunatatit automatizarea, dar urmeaza fluxuri centralizate. Sistemele multi-agent recente sunt limitate la un singur domeniu (intent management sau orchestrare de servicii), nu au cunostinte comune si negociere cross-domain, si depind adesea de controllere centralizate (I).
- Provocari declarate: roluri si interfete sigure pentru agenti, negociere descentralizata stabila si echitabila, ontologii comune si integrarea dinamica a cunostintelor (de exemplu RAG), cu proveninta, control de acces si conformitate cu politici (I).

## Ce propun (metoda, pe scurt)
- **Elementele unui sistem multi-agent** (II, Fig. 1): un coordonator al stratului agentic (workflow-uri, context, memorie, guardrails, conflicte), o retea de agenti si unelte/module de cunostinte. Trei straturi de protocol: Agent-to-Context (exemplu MCP), Inter-Agent Communication (exemplu A2A) si Agent Interoperability Abstraction (exemplu ACP).
- **Domain Agentic System (DAS)** (III, Fig. 2): subsistem multi-agent cu scop delimitat, cu opt functionalitati (intent handling, planificare, conformitate cu politici, monitorizare, rezolvarea conflictelor, managementul cunostintelor, coordonare, securitate si incredere). Contine:
  - agenti cu un "agent shell" comun (memorie persistenta, API-uri, identificatori unici);
  - Service Engines non-autonome (optimizare, detectie de anomalii), apelate de agenti;
  - comunicare interna (gRPC, REST-over-MQTT, event streaming) si interfete northbound (TMF intent APIs, CAMARA).
- **Modelul cognitiv PREPARE:** Perception, Reasoning, Planning, Action, Reflection, Memory, prezentat ca extensie a buclelor MAPE-K/OODA. Om in bucla este posibil la puncte critice.
- **Arhitectura AGILE-6G** (IV, Fig. 3, Tabelul I): un strat de inteligenta agentica deasupra orchestrarii 3GPP existente (CSMF/NSMF/NSSMF, controllere RAN, SDN, 6G-SBA), cu:
  - un sistem de coordonare agentica (exemple de unelte: LangGraph, CrewAI, NeMo Guardrails, Temporal, Ray);
  - DAS-uri globale: IM-DAS (intent), SO-DAS (orchestrarea serviciilor), NO-DAS (orchestrarea retelei);
  - DAS-uri specializate: RAN-DAS, 6GC-DAS, TN-DAS, Sec-DAS;
  - un strat de unelte si cunostinte (federated/continual learning, knowledge graphs si ontologii conforme ETSI NFV/TMF, baze vectoriale si RAG, modele GenAI fine-tuned).
- Deciziile sunt executate prin entitati conforme 3GPP; AGILE-6G nu inlocuieste functiile 3GPP.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Nu exista implementare evaluata. Doua cazuri de utilizare sunt descrise calitativ (V, Fig. 4-5):
  - robotica conectata: un brat robotic cu procesare 3D offload-ata la edge, cu intentul "set up the 3D reconstruction service with X-ms latency", in faze de pregatire, punere in functiune si operare;
  - supraveghere rezilienta: camere IoT si inferenta AI, cu self-healing la suprasarcina edge, congestie de transport sau defect al modulelor de inferenta.

## Experimente si metrici
- Nedeclarat (fara evaluare cantitativa).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Fara cifre. Beneficiile sunt descrise calitativ, fata de orchestrarea centralizata sau cu un singur agent (V):
  - timp de setup mai mic, prin planificare paralela intre DAS-uri;
  - reactie mai timpurie la presiunea pe resurse;
  - izolarea mai devreme a defectelor si remediere locala, cu escaladare SO-DAS -> NO-DAS doar cand masurile locale esueaza;
  - mai putine puncte unice de defect.
- In cazul 2, actiunile sunt verificate de IM-DAS fata de intentul original si stocate in stratul de cunostinte; validarea umana este invocata cand actiunile depasesc pragurile politicilor sau sunt critice pentru siguranta.

## Limitari declarate de autori
- Sunt necesare mecanisme robuste de fallback, protectii impotriva erorilor de rationament ale LLM si verificarea comportamentului agentilor fata de politici, pentru deployment-uri mari (VI).
- Rezultatele sunt calitative; nu exista evaluare experimentala.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - arhitectura conceptuala; 6GC-DAS interactioneaza conceptual cu functiile core prin interfete standard (IV).
- UE reale sau emulate?: nedeclarat - in cazul 1 bratul robotic este UE-ul conceptual (V.A).
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: partial - planurile sunt validate fata de politici si resurse inainte de executie (III.A, IV); nu exista evaluare predictiva a efectului.
- executa actiuni automat (bucla inchisa)?: da (conceptual) - bucle de adaptare cu telemetrie si remediere locala sau escaladata, cu om in bucla pentru actiunile critice (IV, V.B).
- multi-site / geo-redundanta / failover de baza de date?: partial (conceptual) - continuum edge-cloud cu clustere distribuite; migrarea serviciilor de inferenta in cazul 2 (IV, V.B).
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu.
- observa traficul la SCP / proxy?: nu.
