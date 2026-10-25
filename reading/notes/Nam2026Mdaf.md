# MDAF-Based Explainable Failure Prediction for Network Functions in 5G/6G (2026)
Cheie: Nam2026Mdaf . DOI/link: https://doi.org/10.1109/noms69089.2026.11668370 . Sursa textului: integral: PDF urcat de autor (MDAF-Based_Explainable_Failure_Prediction_for_Network_Functions_in_5G_6G.pdf)
Sectiunea din plan: B . Tema: anomalii/RCA
Autori: Sukhyun Nam, Wonseok Choi, James Won-Ki Hong (POSTECH). NOMS 2026, full paper; 9 pagini. Cod publicat pe GitHub (obiwan96/FP_with_LLM).

## Problema (cum o formuleaza autorii)
- Un defect intr-o instanta de NF se poate propaga intre domenii, pana la intreruperi la nivel de retea.
- Cauza unui defect al unui NF poate fi in alt NF sau in alt domeniu: overload local, defecte ale functiilor co-localizate, cereri eronate, erori de baza de date.
- Sistemele existente de predictie a defectelor urmaresc acuratetea si dau rezultate greu de interpretat de operatori. XAI este putin explorat in detectia anomaliilor de retea.
- MDAF (3GPP, introdus in Rel-16) este discutat in literatura mai ales conceptual. Autorii prezinta lucrarea ca una dintre primele implementari ale MDAF (Sectiunile I, II.A).

## Ce propun (metoda, pe scurt)
Cadru MDAF cu trei module (Fig. 1):
1. **MDAF-Collector** colecteaza metrici din RAN, Core si Application, ghidat de TS 28.552 si TS 28.554 (Tabelul I).
   - Metrici per pod: CPU, memorie, trafic transmis, scrieri pe disc.
   - Metrici de context definite de autori, extrase din loguri:
     - RRC State Count (din logurile gNB) si UE Fail State Count;
     - SLO Violation Count, masurat de un UE dedicat care genereaza periodic trafic catre un server de aplicatie;
     - PDU Session Delay (corelare loguri AMF-SMF), AMF Registration Rate, UPF Userplane Throughput, SMF Session Drop Count;
     - Known Error Count (erori ne-critice).
   - Reprezentari ale datelor: Raw, Diff, Var; transformare log pentru metricile cu skewness peste 20; standardizare.
2. **Failure Prediction Module:**
   - sliding window; eticheta 1 daca defectul apare la orizontul h;
   - soft labeling liniar inainte de defect: y = 1 - dist/s;
   - modele: LSTM, GRU, GRU-Attn, CNV-GRU (Conv1D inainte de GRU);
   - Focal Loss, hiperparametri optimizati cu Optuna, evaluare 2-fold cronologica.
3. **Root Cause Analysis Module:**
   - SHAP identifica NF-ul cauzal; fiecarei caracteristici de context ii sunt asociate dinainte NF-urile relevante;
   - cele mai importante caracteristici si fragmente de log sunt trimise ca prompt unui LLM, care da explicatia si actiunea sugerata (de exemplu scale out al pod-ului oai-amf).
   - LLM-uri prin Ollama: GPT-OSS:20B, Gemma3:27B, DeepSeek-r1-Llama3:14B.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Kubernetes, cu RAN, Core si Application pe noduri separate (Fig. 3):
  - core: OAI;
  - RAN: UERANSIM (gNB si UE emulate);
  - server de aplicatie: NGINX;
  - colectare: Prometheus, Loki, Grafana;
  - analiza: InfluxDB si un motor ML Python pe un server extern; doua noduri GPU (RTX 5000, A6000), unul pentru predictie si unul pentru LLM.
- Suprasarcina este indusa intentionat: aproximativ la fiecare 10 s se creeaza si se sterg un numar aleator de UE. Traficul de fond si de suprasarcina catre server este generat cu K6 si h2load.
- Datele acopera 10 zile de trafic, cu 51 de caracteristici per pas de timp si pas de esantionare de 3 minute.
- Au fost observate 13 defecte (Tabelul II):

| NF | Restart | Defect complet | Total |
|---|---|---|---|
| gNB | 3 | 2 | 5 |
| SMF | 1 | 2 | 3 |
| AMF | 1 | 1 | 2 |
| UDR | 1 | 1 | 2 |
| nod Kubernetes | 0 | 1 | 1 |
| Total | 6 | 7 | 13 |

- Defectele au fost identificate manual: caderi bruste de trafic plus verificarea logurilor. Auto-restart-urile de pod-uri sunt tratate ca defecte (IV.A).
- Exemple de erori cunoscute:
  - UDR: "No data available for AccessAndMobilitySubscriptionData";
  - AMF: "Could not find Nsmf PDUSession URI" (cand nu obtine URI-ul SMF de la NRF) (III.B).

## Experimente si metrici
- F1 in functie de fereastra (15/30/45 min) si orizont (0/3/6/9/15 min) pentru reprezentarile Raw, Diff si Var (Tabelul III).
- Ablatie pe arhitectura modelului si pe componente (Tabelul IV).
- Efectul cross-domain si al metricilor din loguri (Tabelul V).
- Explicabilitate (Tabelul VI): acuratetea identificarii NF-ului cauzal de catre SHAP si acuratetea cauzei date de LLM.
- In afara Tabelului III, setarea implicita este fereastra 30 min, orizont 6 min, reprezentare Diff.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- **Tabelul III** (CNV-GRU, fereastra 30 min):
  - detectie (orizont 0): Raw 72,1 / Diff 78,6 / Var 76,7;
  - orizont 3 min: 63,6 / 72,3 / 73,0;
  - orizont 6 min: 57,8 / 71,3 / 71,1;
  - orizont 15 min: 48,1 / 62,3 / 61,9.
  - Fereastra de 30 min este in general cea mai buna; Raw este constant inferior.
- **Tabelul IV** (F1):

| Model / componenta | F1 |
|---|---|
| LSTM | 64,3 |
| GRU | 65,5 |
| GRU-Att | 67,6 |
| CNV-GRU | 68,4 |
| + Focal Loss | 69,5 |
| + Soft Labeling | 71,3 |

- **Tabelul V** (F1):

| Domeniu | Doar resurse | Resurse + context |
|---|---|---|
| RAN | 63,7 | 68,7 |
| Core | 65,8 | 69,1 |
| Multi-domain | 66,3 | 71,3 |

- **Explicabilitate:**
  - SHAP identifica NF-ul cauzal in 77,8% din cazuri, in medie pe patru modele. La fereastra 30 min si orizont 6 min sunt detectate corect 9 defecte, iar SHAP gaseste NF-ul cauzal in 7. In erori, SHAP acorda importanta mare memoriei (IV.D, Tabelul VI).
  - LLM pe 12 defecte, cu loguri de nivel warning sau mai mare din cele 30 de minute anterioare plus rezultatele SHAP:
    - cu prompt nerestrictionat, peste 80% din raspunsuri contin cauza corecta;
    - cu un singur raspuns: GPT-OSS 66,7%, Gemma3 50%, DeepSeek-r1-Llama3 41,7%;
    - instruite sa se concentreze pe loguri, toate trei depasesc 65%; cu pana la doua raspunsuri, depasesc 75%;
    - medii in Tabelul VI: un raspuns 69,5%, doua raspunsuri 77,7%.

## Limitari declarate de autori
- Numarul de defecte este mic. Nu exista o metrica bine definita pentru calitatea explicatiilor generate de LLM (IV.D).
- Testbed de laborator, sub control administrativ unic al domeniilor RAN, Core si Service. Autorii afirma ca defectele observate corespund celor mai frecvente defecte raportate in retele reale (V).
- 3GPP nu specifica metrici concrete pentru MDAF, deci metricile de context sunt definite de autori. Domeniul de transport nu este considerat (III.B).
- Lucrari viitoare: o bucla inchisa care sa incorporeze automat rezultatele RCA, modelarea corelatiilor multi-domeniu, RAG si fine-tuning pentru LLM (V).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - OpenAirInterface 5G Core pe Kubernetes (III.E).
- UE reale sau emulate?: emulate - UERANSIM (III.E).
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu - prezice defecte; LLM-ul sugereaza actiuni fara evaluarea efectului lor.
- executa actiuni automat (bucla inchisa)?: nu - bucla inchisa este lucrare viitoare (V).
- multi-site / geo-redundanta / failover de baza de date?: nu - unele defecte sunt atribuite suprasarcinii bazei de date (UDR), dar nu exista failover sau multi-site.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu - evaluare 2-fold cronologica pe date colectate.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: partial - SLO Violation Count masurat de un UE dedicat si metrici de sesiune ca intrari; metrica de evaluare este F1 pentru predictia defectelor.
- observa traficul la SCP / proxy?: nu.
