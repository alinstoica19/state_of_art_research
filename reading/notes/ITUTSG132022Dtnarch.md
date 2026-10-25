# Digital twin network - Requirements and architecture (ITU-T Y.3090) (2022)
Cheie: ITUTSG132022Dtnarch . DOI/link: https://www.itu.int/rec/T-REC-Y.3090-202202-I/en (PDF Y.3090 (02/2022), 26 pagini) . Sursa textului: integral, ITU-T Y.3090 (02/2022), PDF descarcat de la itu.int
Sectiunea din plan: Standarde . Tema: Network Digital Twin

## Problema (cum o formuleaza autorii)
Recomandarea defineste digital twin network (DTN) ca reprezentare virtuala a unei retele fizice, utila pentru analiza, diagnosticare, emulare si control al retelei fizice pe baza de date, model si interfata, cu mapare interactiva in timp real intre reteaua fizica si reteaua virtuala (Sec. 1, 3.2.1, 6). Scopul include cerinte functionale, cerinte de serviciu, arhitectura si consideratii de securitate pentru DTN (Sec. 1). Textul afirma ca nu exista (la data redactarii) o arhitectura de referinta sau un standard de arhitectura pentru digital twin networks in domeniul retelelor (Sec. 8).

## Ce propun (metoda, pe scurt)
- Sec. 6: patru caracteristici cheie ale unui DTN: date, mapare (real-time interactive mapping, descrisa ca trasatura care distinge DTN de un sistem de simulare a retelei), model, interfata standardizata (sudica si nordica).
- Sec. 7: cerinte functionale (colectare de date, unified data repository, unified data models, interfete sudice/nordice deschise, management DTN) si cerinte de serviciu (compatibilitate, scalabilitate, fiabilitate, securitate, confidentialitate, flexibilitate, vizualizare, sincronizare).
- Sec. 8: arhitectura de referinta "three-layer, three-domain, double closed-loop".
- Apendice I (informativ): cazuri de utilizare.

## Clauze relevante (numar clauza - ce defineste)
- 3.2.1 - definitia digital twin network.
- 6 - cele patru caracteristici (date, mapare, model, interfata); DTN poate sprijini "low-cost trial, intelligent decision-making, efficient innovation and predictive maintenance" prin AI/ML, big data, cloud.
- 7.1.1 - colectare eficienta de date (date complete, instrumente diverse precum SNMP, NetConf, telemetry, INT; instrumente usoare, fara afectarea operarii retelei).
- 7.1.2 - unified data repository (ETL, stocare heterogena, acces in timp real, snapshot istoric si rollback, backup si recovery pentru disponibilitate ridicata).
- 7.1.3 - unified data models: modele de elemente de retea si topologie; modele functionale (network optimization, traffic scheduling, load balancing, fault prediction); domenii unice sau multiple (inclusiv core network); interfata pentru a livra change requests catre elementele fizice; capacitate de emulare si optimizare iterativa a aplicatiilor de retea.
- 7.1.4 - interfete sudice (colectare pasiva/activa/subscription/on-demand, optiuni de viteza de la nivel de minut la real-time, livrarea de semnalizare de control si schimbari de configuratie) si nordice (livrarea cerintelor aplicatiei catre modele; "recomandat" interfata bazata pe intent; raportarea rezultatelor; interfata restful).
- 7.1.5 - managementul DTN (date, topologie, model, securitate; management automat).
- 7.2.1-7.2.8 - compatibilitate (RAN, transport, core network, data centre, campus), scalabilitate, fiabilitate (recomandat 99.99%, adica cel mult 52 de minute de indisponibilitate pe an; backup, restaurare la checkpoint-uri, disaster recovery), securitate, confidentialitate, flexibilitate, vizualizare, sincronizare (reprezentarea starii reale in timp real, in limita unei intarzieri acceptabile, si sincronizarea executiei informatiei de control de la entitatea virtuala la cea fizica).
- 8 - arhitectura de referinta (Fig. 8-1): trei straturi (physical network layer, network digital twin layer, network application layer), trei domenii in stratul twin (data domain = unified data repository, model domain = unified data models, management domain = digital twin entity management), doua bucle ("inner closed loop" de emulare si optimizare pe modelele unificate; "outer closed loop" de control, feedback si optimizare a aplicatiei de retea).
- 9 - consideratii de securitate (adresate prin cerintele din Sec. 7).
- Apendice I - cazuri de utilizare: operatiune si mentenanta complexa, eficientizarea optimizarii retelei, accelerarea inovatiei in retea (si altele in continuarea apendicelui).

## Entitati, servicii si parametri definiti
- Straturi: physical network layer, network digital twin layer, network application layer (Sec. 8).
- Subsisteme in network digital twin layer: unified data repository (data collection, data storage, data service, data management), unified data models (basic models: network element model si network topology model; functional models: analiza, emulare, diagnoza, predictie, asigurare), digital twin entity management (topology management, model management, security management) (Sec. 8).
- Interfete: southbound (retea fizica - twin) si northbound (twin - aplicatii) (Sec. 7.1.4).
- Termeni: digital twin network, domain (Sec. 3.2).
- Parametri numerici: disponibilitate recomandata 99.99% / maxim 52 minute indisponibilitate pe an (Sec. 7.2.3); niveluri de viteza ale interfetei sudice: minute, 10 secunde, secunda (near real-time), real-time (Sec. 7.1.4.1).
- Text normativ: "is required" / "is recommended" definite in Sec. 5.

## Limitari declarate de autori
Textul precizeaza ca pentru domeniul retelelor nu exista o arhitectura sau un standard de referinta pentru DTN (Sec. 8) si ca arhitectura propusa e derivata prin analogie cu cadrul ISO 23247 din manufacturing. Recomandarea nu specifica protocoale sau implementari concrete pentru modele; securitatea e tratata prin cerintele din Sec. 7 (Sec. 9). Nu defineste 5G Core NF-uri specifice; mentioneaza core network si "user plane function elements in the core network" ca exemplu de infrastructura-obiect (Sec. 8).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu se aplica - recomandare de cerinte si arhitectura, fara implementare.
- UE reale sau emulate? nedeclarat.
- digital twin al retelei? da - obiectul recomandarii (Sec. 1, 6, 8).
- prezice efectul unei actiuni inainte de a o aplica? da, ca cerinta/functie de arhitectura: modelele emuleaza si verifica schimbarile de control si optimizare inainte de distribuirea lor in reteaua fizica (Sec. 8, 2b; Sec. 7.1.3).
- executa actiuni automat (bucla inchisa)? da, ca arhitectura: "double closed-loop", cu trimiterea actualizarilor de control catre reteaua fizica prin interfata sudica dupa verificare (Sec. 8); nu e o implementare.
- multi-site / geo-redundanta / failover de baza de date? nedeclarat ca atare; cerinte de backup, restaurare la checkpoint, disaster recovery si backup/recovery al repository-ului (Sec. 7.1.2, 7.2.3).
- evaluare prospectiva (predictie fixata inainte de experiment)? nu se aplica.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu se aplica.
- observa traficul la SCP / proxy? nu - SCP nu este mentionat.
