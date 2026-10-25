# IntAgent: NWDAF-Based Intent LLM Agent Towards Advanced Next Generation Networks (2026)
Cheie: Soliman2026Intagent . DOI/link: 10.1109/icc59461.2026.11587323 (arXiv:2601.13114) . Sursa textului: integral, arXiv v1 (19 ian. 2026): https://arxiv.org/pdf/2601.13114v1
Sectiunea din plan: B

## Problema (cum o formuleaza autorii)
Managementul traditional al retelei se bazeaza pe procese manuale, lente si predispuse la erori. Retelele bazate pe intentii (IBN) automatizeaza operatiunile, dar lucrarile existente cu LLM pentru intent translation au rar integrare profunda cu functii de analitica precum NWDAF pentru decizii bazate pe date in timp real; sistemele agentice presupun instrumente preexistente si stari abstracte ale retelei si rareori trateaza crearea de unelte pe baza analiticii standardizate sau folosirea dinamica a datelor live (Sec. I).

## Ce propun (metoda, pe scurt)
- IntAgent: agent LLM de intentii integrat cu NWDAF (Sec. I, III).
- Extinderea Event Exposure Service din NWDAF pentru colectare de date de la UPF, PCF si SMF, stocate in MongoDB (Sec. II-B).
- Intent tools engine in motorul de analitica NWDAF, expus printr-un server MCP cu unelte de programare, monitorizare si analitica: Feasibility Checker, KPI Analyzer, Monitoring Manager, Policy Manager, Session Manager (Sec. II-C).
- Patru grupuri de unelte MCP: regasire de date (MongoDB, RAG), intent tools, programare/domeniu (generare cod Python cu DeepSeek-R1, mediu Python) si siguranta (confirmare umana, validare Pydantic) (Fig. 3).
- Bucla agentica (Algoritm 1): plan, act, observe, critical-thinking (blocare presupuneri, urmarirea scopului, validare structurata, poarta de siguranta cu aprobare umana la actiuni critice). Raspunsul LLM e restrans la trei formate: thought, tool call, final answer (Sec. III-B, III-C).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Core 5G Open5GS pe cluster Kubernetes, cu NWDAF actualizat (intent tools) si IntAgent (Sec. IV-A).
- UE/RAN: simulator UERANSIM, 10 UE cu trafic aleator.
- LLM: Meta Llama 3.1 cu 8 miliarde de parametri, rulat cu Ollama, temperatura 0.1; interfata Streamlit; DeepSeek-R1 pentru generare de cod.
- Hardware: i7-13700K, 32 GB RAM, NVIDIA RTX 3050.
- Textul afirma ca s-au monitorizat latenta, throughput si overhead de semnalizare pe mai multe sesiuni sub explozii simulate de trafic si ca operarea a fost stabila, fara cifre.
- Date: trafic simulat si date de utilizare memorie colectate de NWDAF.

## Experimente si metrici
Doua cazuri de utilizare, prezentate calitativ (Sec. IV-B, IV-C):
- Caz 1: intentia "predict memory utilization % for the internet slice based on 500 recent values"; agentul planifica, extrage date, genereaza si ruleaza cod Python, antreneaza un Random Forest Regressor cu fereastra glisanta, produce grafic si raspuns final. Metrica: R-patrat pe antrenare si test (Fig. 4).
- Caz 2: intentia de a creste cu 20% rata de date a slice-ului "streaming" intre 4:27 PM si 4:30 PM in zilele lucratoare; agentul a generat un plan in 7 pasi (listare colectii, cautare config, verificare fezabilitate, calcul rata noua, aplicare cu programare, verificare, raspuns final), a contactat Monitoring Manager pentru a programa schimbarea de AMBR. Rezultat prezentat in Fig. 5 (rate UL/DL in timp).
Nu exista comparatii cu alte metode sau cu alti LLM-uri, nici statistici pe mai multe rulari.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Caz 1 (Fig. 4, raspuns final): model Random Forest Regressor; R-patrat pe setul de test 0.7520 (descris ca nivel moderat de acuratete); legenda figurii: Train R2 = 0.956, Test R2 = 0.752; partitie 80% antrenare / 20% test.
- Caz 2 (Fig. 5): agentul a programat si aplicat cresterea ratei de date pentru slice-ul streaming conform cererii; figura arata rata de date UL/DL in timp in jurul orelor 4:25-4:31 PM. Valori numerice exacte ale ratelor: nu sunt date in text.
- Nu sunt raportate cifre pentru latenta, throughput sau semnalizare, doar afirmatia de operare stabila (Sec. IV-A).

## Limitari declarate de autori
Sec. IV-D: halucinatii ale LLM aparute regulat, atribuite posibil dimensiunii modelului ales; ciclul complex plan-think-act-observe produce multi pasi suplimentari chiar pentru intentii simple. Directii viitoare (Sec. V): fine-tuning pe date de retelistica, prompt imbunatatit, comparatie intre LLM-uri, sistem multi-agent.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? da - Open5GS pe Kubernetes cu NWDAF extins (Sec. II-B, IV-A).
- UE reale sau emulate? emulate - UERANSIM, 10 UE (Sec. IV-A).
- digital twin al retelei? nu - nu este mentionat.
- prezice efectul unei actiuni inainte de a o aplica? nu, cu nuante - Feasibility Checker evalueaza prin constrangeri ce actiuni sunt posibile si planul include verificare de fezabilitate (Sec. II-C, IV-C); predictia din Caz 1 priveste utilizarea memoriei, nu efectul unei actiuni.
- executa actiuni automat (bucla inchisa)? da - agentul apeleaza unelte care aplica modificari (programare AMBR, Caz 2), cu cerere de confirmare umana pentru actiuni critice (Sec. III-C, IV-C); "Closed Loop" apare in Index Terms.
- multi-site / geo-redundanta / failover de baza de date? nu - o singura masina de test, cluster Kubernetes unic (Sec. IV-A).
- evaluare prospectiva (predictie fixata inainte de experiment)? nu - demonstratie pe doua cazuri de utilizare; R-patrat pe split 80/20 (Sec. IV-B).
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - cazurile raporteaza R-patrat si rata de date a slice-ului; fara metrici per inregistrare sau sesiune (Sec. IV).
- observa traficul la SCP / proxy? nu - datele vin prin SBI/Event Exposure de la UPF, PCF, SMF; SCP nu este mentionat (Sec. II-A, II-B).
