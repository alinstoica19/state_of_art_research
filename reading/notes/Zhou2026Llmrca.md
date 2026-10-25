# Large Language Models (LLMs) for Telecom Root Cause Analysis (RCA): A Structured Reasoning Framework for Evidence-Grounded Diagnosis (2026)
Cheie: Zhou2026Llmrca . DOI/link: https://doi.org/10.1109/mwc.2026.3734923 . Sursa textului: integral: arXiv 2609.02805v1 (2 septembrie 2026; acceptat in IEEE Wireless Communications Magazine)
Sectiunea din plan: C . Tema: anomalii/RCA / LLM
Autori: Hao Zhou, Mandar Kulkarni, Hao Chen, Yan Xin, Charlie (Jianzhong) Zhang. Afilierea nu apare in textul extras.

## Problema (cum o formuleaza autorii)
- Defectele si degradarile din retelele 5G-Advanced/6G au consecinte mari. Autorii dau ca exemple intreruperile Rogers (2022), Optus (2023) si AT&T (2024) (I).
- RCA a evoluat de la sisteme expert cu reguli (transparente, dar greu de scalat) la ML (mapare intrare-eticheta, fara explicarea legaturii dintre dovezi si cauze) si apoi la LLM (II).
- LLM-urile aplicate direct produc halucinatii, rationament instabil si o aliniere slaba cu dovezile structurate din retea: speculeaza cauze fara a se baza pe KPI, topologie sau configuratie (I, II).

## Ce propun (metoda, pe scurt)
- **Trecere in revista a paradigmelor LLM pentru RCA** (III, Fig. 2):
  - CoT: verificari pe etape (PHY, MAC/RLC, RRC/handover);
  - RAG: specificatii 3GPP, manuale, incidente istorice;
  - orchestrare agentica: unelte, de exemplu simulare ns-3 pentru impactul unei schimbari de configuratie, sau mai multi agenti specializati;
  - RLVR: recompense verificabile dintr-un simulator sau DT, pe baza imbunatatirii KPI-urilor dupa actiunea propusa.
- **SEKA-FT** (Structured Evidence- and Knowledge-Aligned Fine-Tuning) (IV, Fig. 4):
  1. structurarea canonica a contextului: intrarile eterogene sunt organizate in blocuri fixe (Bottleneck Snapshot, UE Global State, Trajectory-Level Events, parametrii de inginerie ai celulei);
  2. controlul caii de decizie prin CoT: verificari intermediare (viteza, RB-uri insuficiente, handover-uri, distanta) care elimina ipotezele nesustinute;
  3. explicatii ancorate in dovezi si cunostinte, folosite ca tinta de supervizare in doua straturi: verificari, apoi rafinarea ipotezelor.
- Tintele de explicatie sunt generate automat din eticheta reala, verificarile deterministe si sabloane de reguli de domeniu. Antrenarea foloseste loss de modelare cauzala a limbajului, cu tokenii de prompt mascati (IV.D, V.B).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Doua seturi de date (V):
  - TeleLogs [8]: benchmark asociat initiativei GSMA LLM; drive-test cu KPI user-plane, mobilitate, parametri de inginerie ai celulei; 8 clase de cauze (exemplul din Fig. 3 are 7 optiuni M1-M7);
  - TelecomTS [15]: dataset de observabilitate 5G dintr-un testbed de laborator, cu KPI de inalta rezolutie de la statia de baza si de la dispozitiv, sub trafic real de aplicatii.
- Model de baza: Qwen2.5-1.5B-Instruct. Pentru scalare: Qwen2.5-7B-Instruct si Qwen3-32B (ICL). LoRA pe ultimele patru blocuri Transformer, AdamW (lr 1e-5), 12 epoci, batch 2, secventa maxima 2048, bf16, GPU RTX 6000 Ada.
- Zece rulari cu seed-uri diferite, IC 95% (t-Student). McNemar exact pentru acuratete, test de permutare pareat pentru Macro-F1, corectie Holm-Bonferroni.

## Experimente si metrici
- Accuracy si Macro-F1 pentru: ICL (1,5B/7B/32B), LSTM, Vanilla SFT, SFT + Structured Input, SFT + Explanation, SEKA-FT (Tabelul I, Fig. 5a).
- Convergenta pe epoci (Fig. 5b), scalarea ICL (Fig. 5c), consistenta caii de decizie pe verificari (Fig. 5d), acuratete per cauza (Fig. 5e), reducerea spatiului de candidati (Fig. 5f).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Tabelul I (Accuracy / Macro-F1, medie ± IC):

| Metoda | TeleLogs Acc | TeleLogs F1 | TelecomTS Acc | TelecomTS F1 |
|---|---|---|---|---|
| ICL 1.5B | 0,021 ± 0,004 | 0,018 ± 0,003 | 0,033 ± 0,006 | 0,031 ± 0,005 |
| ICL 7B | 0,053 ± 0,006 | 0,043 ± 0,005 | 0,041 ± 0,005 | 0,028 ± 0,003 |
| ICL 32B | 0,126 ± 0,010 | 0,109 ± 0,009 | 0,061 ± 0,005 | 0,053 ± 0,004 |
| LSTM | 0,132 ± 0,012 | 0,090 ± 0,011 | 0,115 ± 0,010 | 0,080 ± 0,010 |
| Vanilla SFT | 0,007 ± 0,003 | 0,013 ± 0,004 | 0,050 ± 0,021 | 0,052 ± 0,016 |
| SFT + Struct Input | 0,256 ± 0,018 | 0,234 ± 0,016 | 0,132 ± 0,009 | 0,138 ± 0,009 |
| SFT + Explanation | 0,030 ± 0,005 | 0,020 ± 0,004 | 0,047 ± 0,008 | 0,041 ± 0,008 |
| SEKA-FT | 0,942 ± 0,006 | 0,937 ± 0,007 | 0,647 ± 0,004 | 0,615 ± 0,005 |

- SEKA-FT are consistenta aproape perfecta a caii de decizie pe verificarile evaluate (Fig. 5d).
- Erorile ramase sunt concentrate intre clasele legate de acoperire si celule vecine (Fig. 5e).
- Cu o distributie uniforma a cauzelor, marimea medie a setului de candidati scade de la 8 la 6,25, 4,75, 3,5 si 2,5 dupa cele patru verificari (Fig. 5f).
- Pe TelecomTS, SEKA-FT imbunatateste Accuracy cu 0,515 si Macro-F1 cu 0,477 fata de SFT + Structured Input (V.C).

## Limitari declarate de autori
- Lucrari viitoare: scenarii RCA mai diverse si realiste, inclusiv defecte de core si de transport, si incidente reale de operator nevazute anterior (VI).
- Verificarile intermediare sunt definite din definitiile RCA ale benchmark-ului (de exemplu viteza peste 40 km/h, RB-uri programate sub 160), nu ajustate pe test (V.B).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - seturi de date RAN (drive-test si testbed); defectele de core sunt lucrare viitoare (V, VI).
- UE reale sau emulate?: reale in datele sursa - drive-test (TeleLogs) si dispozitiv in testbed (TelecomTS); lucrarea foloseste doar seturile de date (V).
- digital twin al retelei?: nu - DT/simulatorul este mentionat doar ca sursa de feedback in paradigma RLVR (III.D).
- prezice efectul unei actiuni inainte de a o aplica?: nu.
- executa actiuni automat (bucla inchisa)?: nu - diagnostic offline.
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu - evaluare pe seturi de date existente, cu 10 seed-uri.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu - metricile sunt de clasificare (Accuracy, Macro-F1).
- observa traficul la SCP / proxy?: nu.
