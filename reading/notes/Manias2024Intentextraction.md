# Towards Intent-Based Network Management: Large Language Models for Intent Extraction in 5G Core Networks (2024)
Cheie: Manias2024Intentextraction . DOI/link: 10.1109/drcn60692.2024.10539172 . Sursa textului: integral, arXiv v2 (2403.02238v2, 22 May 2024): https://arxiv.org/pdf/2403.02238
Sectiunea din plan: B

## Problema (cum o formuleaza autorii)
Integrarea intelegentei in retea (NWDAF in 5G) este vazuta ca limitata pentru cerintele B5G/6G; este nevoie de inteligenta "ubicua" si de automatizare zero-touch (ZSM). Un sistem autonom trebuie sa interpreteze intentiile utilizatorului/operatorului si sa configureze reteaua, reducand interventia umana si erorile. Primul pas este extragerea acurata si consistenta a intent-ului din cererea utilizatorului. Autorii spun ca lucrarile existente nu folosesc potentialul LLM-urilor si ca extragerea de intent specific pentru core-ul 5G nu a fost tratata pana acum.

## Ce propun (metoda, pe scurt)
Un LLM "customizat" prin prompting (ChatGPT 3.5) pentru extragerea intent-urilor din core-ul 5G, ca prim pas dintr-o abordare bottom-up spre IBN end-to-end. Arhitectura generala (Fig. 1): utilizator, interfata, modul de interpretare a cererii (intent extraction, entity extraction, context retrieval, request transformation) si modul de executie; lucrarea acopera doar intent extraction. Cele 6 tipuri de intent din 3GPP TS 28.312 (Rel-18): Deployment, Modification, Performance Assurance, Intent Report Request, Intent Feasibility Check, Regular Notification Request (Tabel I). Prompt cu rol, descrierea sarcinii, context din standard si comportament asteptat (Tabel II); modelul poate returna mai multe intent-uri per cerere, cu justificare (explainability), sau "no intent present"/"unknown intent".

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Nu exista testbed live: LLM-ul (OpenAI ChatGPT 3.5, closed-source) este interogat cu cereri exemplu. Nu exista dataset etichetat; exemplele sunt cereri reprezentative alese de autori (intent unic, multiple, absent). Integrarea cu un testbed 5G live (cu NWDAF Rel-18) este listata ca lucru viitor.

## Experimente si metrici
Evaluare calitativa pe exemple: 2 cereri cu intent unic (Fig. 2, Fig. 3), 2 cu intent multiplu (Fig. 4, Fig. 5), 2 fara intent / intent necunoscut (Fig. 6). Nu sunt definite metrici cantitative (acuratete, F1 etc.).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Nu sunt raportate cifre. Descriere: Fig. 2 - cererea despre starea crearii retelei test123 identificata ca Intent Report Request; Fig. 3 - eliminarea unui link intre noduri identificata ca Modification Intent; Fig. 4 - trei intent-uri identificate (Deployment, Intent Feasibility Check, Regular Notification Request); Fig. 5 - trei intent-uri (Modification, Performance Assurance, Regular Notification Request); Fig. 6 - "Hello, how are you?" returneaza "No intent present", iar o cerere despre payroll returneaza "Unknown intent". Autorii noteaza ca intent-ul de notificare din Fig. 4 ar fi putut fi interpretat si ca Intent Report Request (suprapunere intre tipuri) si ca in Fig. 5 lipseste frecventa notificarilor (ambiguitate).

## Limitari declarate de autori
Modelul ales este closed-source (arhitectura si antrenarea nepublice); se foloseste doar prompting; lipseste clarificarea distinctiei intre tipuri similare de intent; ambiguitati la cereri incomplete; halucinatiile LLM urmeaza a fi analizate (RAG ca mitigare). Viitor: LLM open-source (ex. Llama 2), fine-tuning pe dataset etichetat generat cu augmentari (back translation, paraphrasing etc.), integrare cu testbed 5G live, arhitectura cu mai multe LLM-uri si apeluri API.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu - fara core in experiment; testbed-ul propriu este doar mentionat ca tinta viitoare (Sec. VI)
- UE reale sau emulate? nu se aplica - fara UE (Sec. V)
- digital twin al retelei? nu
- prezice efectul unei actiuni inainte de a o aplica? nu (Intent Feasibility Check apare doar ca tip de intent clasificat, Sec. III)
- executa actiuni automat (bucla inchisa)? nu - doar extragerea intent-ului; executia este viitoare (Sec. IV, VI)
- multi-site / geo-redundanta / failover de baza de date? nu
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - exemple calitative de cereri text (Sec. V)
- observa traficul la SCP / proxy? nu
