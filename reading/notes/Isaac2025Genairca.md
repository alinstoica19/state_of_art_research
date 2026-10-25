# 5G Core Fault Detection and Root Cause Analysis using Machine Learning and Generative AI (2025)
Cheie: Isaac2025Genairca . DOI/link: arXiv:2508.09152 . Sursa textului: integral, arXiv (versiune nespecificata in text): https://arxiv.org/pdf/2508.09152
Sectiunea din plan: B

## Problema (cum o formuleaza autorii)
Analiza fisierelor PCAP si de log din testarea unui packet core 5G cere multe ore-om pentru a sorta rezultatele si a gasi defectele; verificarea manuala este lenta si predispusa la erori (rezumat, Introducere). In sesiuni de test nocturne cu multe executii simultane, testerii trebuie sa revizuiasca manual loguri si PCAP-uri a doua zi (Related Works). Lucrari existente pe PCAP detecteaza anomalii dar nu le explica, de exemplu LLMcap detecteaza fara explicatie.

## Ce propun (metoda, pe scurt)
5G Core Fault Analysis (FA) Engine, cu trei componente (Fig. 1):
- Golden Flow: graf de cunostinte construit din PCAP-urile testelor reusite; cadrele sunt noduri, legate prin muchii orientate cu urmatorul cadru. La inferenta, un cadru care iese din graf este marcat ca anomalie, impreuna cu pasii asteptati (Fig. 2).
- AI Engine: clasificator NLP pe cadre individuale: preprocesare text, vectorizare Bag-of-words, clasificator Support Vector Machine (Fig. 3). Cadrele din PCAP-urile reusite sunt corecte; cadrele din PCAP-urile esuate care nu apar in cele reusite sunt considerate defecte, fara etichetare manuala.
- Agent de depanare LLM: MistralAI cu RAG construit din documente 3GPP, specificatii si coduri de cauza Packet Core Controller (PCC) si un document al testerilor cu probleme frecvente; promptul include cadrul defect si cadrul anterior.
Extragerea datelor din PCAP se face cu biblioteci Wireshark, in JSON.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- 198 fisiere PCAP: 58 din teste 5G core reusite si 140 din teste esuate; testele acopera inregistrare UE, stabilire sesiune PDU si deregistrare. Fisierele au fost create intr-un mediu de laborator simulat (Rezultate).
- Split 80/20 antrenare/test.
- Unelte: Wireshark (extragere), SVM, retea neuronala, Random Forest, clasificator Bayes (comparatie), MistralAI + RAG. Nume de core open-source (Open5GS, free5GC): nedeclarate. Scara (numar UE, NF, noduri): nedeclarat.
- Date: PCAP-uri sintetice/de laborator.

## Experimente si metrici
- Golden Flow: acuratete de detectie.
- AI Engine: comparatie a patru clasificatori cu accuracy si F1 (Tabel 1, toate protocoalele impreuna).
- Tabel 2: SVM pe tipuri de protocol (accuracy, precision negativ, recall negativ, F1).
- Test calitativ al LLM-ului pe un fisier cu eroare in fluxul de inregistrare (Registration Reject cu Congestion).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Golden Flow: acuratete de detectie 100% pe fisierele de test.
- Tabel 1 (accuracy / F1): SVM 86% / 84%; Neural Network 81% / 80%; Random Forest 83% / 81%; Bayes 79% / 76%.
- Tabel 2 (accuracy / precision(-ve) / recall(-ve) / F1): All protocols together 86% / 90% / 79% / 84%; HTTP2 99% / 80% / 80% / 89%; HTTP2/JSON 99% / 100% / 80% / 89%; HTTP2/JSON/NAS-5GC 100% / 100% / 100% / 100%; NAS-5GC 100% / 100% / 100% / 100%.
- Exemplu LLM: cadrul suspect Registration reject (Congestion) la frame 23; mesaje asteptate InitialContextSetupRequest -> InitialContextSetupResponse; cauze posibile: raspunsuri 504 Gateway Time-out la cadrele 20 si 22. LLM-ul a oferit o procedura de remediere cu trimiteri la documente. Nu sunt raportate metrici cantitative pentru LLM.

## Limitari declarate de autori
Nu exista sectiune dedicata. Concluzia afirma ca sistemul merge bine cand sunt furnizate suficiente date pentru fiecare caz limita. Textul observa ca modelul combinat pe toate protocoalele reduce recall-ul. Directii viitoare: alte forme de intrare (loguri, fisiere de configurare), LLM-uri multimodale, trafic 4G.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nedeclarat - PCAP-urile provin dintr-un mediu de laborator simulat pentru teste pe packet core (documentatie PCC), fara descrierea implementarii (Rezultate).
- UE reale sau emulate? nedeclarat - sunt mentionate teste de inregistrare/PDU/deregistrare, fara a preciza tipul UE (Rezultate).
- digital twin al retelei? nu - nu este mentionat.
- prezice efectul unei actiuni inainte de a o aplica? nu - detecteaza defecte in capturi si sugereaza remedieri (Metodologie).
- executa actiuni automat (bucla inchisa)? nu - motorul indica defectul si pasii de remediere utilizatorului (Introducere, Metodologie).
- multi-site / geo-redundanta / failover de baza de date? nedeclarat.
- evaluare prospectiva (predictie fixata inainte de experiment)? nu - evaluare pe split 80/20 din fisiere existente (Rezultate).
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - metricile sunt pe cadre/fisiere PCAP; scenariile includ inregistrare si PDU, dar nu sunt raportate rate de succes ale utilizatorilor (Rezultate).
- observa traficul la SCP / proxy? nedeclarat - se analizeaza PCAP-uri cu cadre NAS si HTTP2/JSON; SCP nu este mentionat (Rezultate).
