# Intent-Based Networking - Concepts and Definitions (RFC 9315) (2022)
Cheie: IRTFNMRG2022Intentrfc . DOI/link: https://datatracker.ietf.org/doc/rfc9315/ (10.17487/RFC9315) . Sursa textului: integral, RFC 9315 (octombrie 2022, IRTF, Informational), text de pe rfc-editor.org
Sectiunea din plan: Standarde . Tema: Intent / closed-loop

## Problema (cum o formuleaza autorii)
Termenii legati de Intent-Based Networking sunt folositi adesea vag si inconsecvent, uneori suprapusi sau confundati cu "policy". Documentul clarifica conceptul de "intent" si ofera o privire de ansamblu asupra functionalitatii asociate, ca baza comuna pentru definirea ulterioara a problemelor de cercetare si inginerie (Abstract, Sec. 1). Articularea problemelor de cercetare IBN este declarata in afara scopului (Sec. 1).

## Ce propun (metoda, pe scurt)
Document de concepte si definitii al IRTF NMRG, publicat informativ (nu Standards Track). Defineste intent, il diferentiaza de service model si policy, enumera principii si descrie functiile IBN impartite in Intent Fulfillment si Intent Assurance, cu un ciclu de viata al intentiei.

## Clauze relevante (numar clauza - ce defineste)
- 2 - definitii: Intent ("a set of operational goals ... and outcomes ... defined in a declarative manner without specifying how"), IBN, IBS, IBA (Intent-Based Analytics), Policy, Service Model, SSoT, Statement of Intent, User (operator/administrator, nu end user).
- 3.1 - intent si Intent-Based Management; exemple de ce este si ce nu este intent (de ex. regula "alerta cand utilizarea interfetei depaseste un prag" nu este intent); discutie despre implementare centralizata vs distribuita si evitarea single points of failure.
- 3.2.1-3.2.3 - service models, policy si PBNM (event-condition-action), diferentele dintre intent, policy si service model.
- 4 - principii: (1) Single Source of Truth si Single Version of Truth, cu detectarea derivei intre starea dorita si cea operationala; (2) "One touch but not one shot"; (3) Autonomy and Supervision; (4) Learning; (5) Capability exposure; (6) Abstract and outcome-driven; plus aspecte suplimentare (explainability, rezolvarea intentiilor conflictuale, trust).
- 5.1 - Intent Fulfillment: 5.1.1 ingestion si interactiune cu utilizatorii, 5.1.2 intent translation, 5.1.3 intent orchestration.
- 5.2 - Intent Assurance: 5.2.1 monitoring, 5.2.2 intent compliance assessment (inclusiv verificarea ca actiunile au avut efectul dorit si detectarea "intent drift"), 5.2.3 intent compliance actions (actiuni corective sau raportare catre operatori), 5.2.4 abstraction/aggregation/reporting.
- 6 - ciclul de viata al intentiei (Fig. 1): doua planuri (fulfillment, assurance) si trei spatii (User Space, Translation/IBS Space, Network Operations Space).
- 7 - consideratii suplimentare: subcategorii de intent (Operational Intent, Rule Intent, Service Intent, Flow Intent) si "intent-washing".
- 9 - securitate: securizarea IBS, atenuarea efectelor intentiilor eronate sau compromise (detectie automata de comportament anormal, rollback/fallback la o stare "safe", prevenirea amplificarii erorilor, niveluri dinamice de supervizare), exprimarea politicilor de securitate ca intent.

## Entitati, servicii si parametri definiti
Entitati conceptuale: IBS, IBN, SSoT/SVoT, statement of intent, functiile de fulfillment si assurance, spatiile User / Translation(IBS) / Network Operations. Nu defineste protocoale, parametri numerici sau interfete concrete. Exemple de intentii formulate in limbaj natural includ unul despre slice-uri dedicate si redundante pentru trafic de control al semafoarelor intr-un smart city (Sec. 3.1).

## Limitari declarate de autori
Nu este specificatie Standards Track; consideratiile de securitate raman la nivel inalt, detaliile urmand a fi in documentele de arhitectura si functionalitate (Sec. 9); un set complet de clasificari ale conceptelor de intent urmeaza sa fie descris intr-un document separat (Sec. 7); problemele de cercetare IBN sunt in afara scopului (Sec. 1).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu se aplica - document conceptual.
- UE reale sau emulate? nu se aplica.
- digital twin al retelei? nedeclarat.
- prezice efectul unei actiuni inainte de a o aplica? nedeclarat ca cerinta; principiile mentioneaza ca un IBS echipat cu mijloace de predictie a starilor poate anticipa si planifica (Sec. 4, principiul 1) si capacitati de planning pentru a prevedea raspunsul la schimbari (principiul 4).
- executa actiuni automat (bucla inchisa)? descris conceptual: fulfillment + assurance cu actiuni corective la intent drift (Sec. 5.2.3, Fig. 1); nu e implementare.
- multi-site / geo-redundanta / failover de baza de date? nedeclarat; se mentioneaza doar evitarea single points of failure prin hosting distribuit al functiilor (Sec. 3.1).
- evaluare prospectiva (predictie fixata inainte de experiment)? nu se aplica.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu se aplica.
- observa traficul la SCP / proxy? nu - nu este mentionat.
