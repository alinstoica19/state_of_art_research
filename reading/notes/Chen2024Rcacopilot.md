# Automatic Root Cause Analysis via Large Language Models for Cloud Incidents (2024)
Cheie: Chen2024Rcacopilot . DOI/link: https://doi.org/10.1145/3627703.3629553 . Sursa textului: integral: arXiv 2305.15778v4 (13 noiembrie 2023; versiunea EuroSys '24)
Sectiunea din plan: C . Tema: anomalii/RCA / LLM in operatiuni cloud
Autori: Yinfang Chen, Huaibing Xie, Minghua Ma, Yu Kang, Xin Gao, Liu Shi, Yunjie Cao, Xuedong Gao, Hao Fan, Ming Wen, Jun Zeng, Supriyo Ghosh, Xuchao Zhang, Chaoyun Zhang, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Tianyin Xu (Microsoft; UIUC; Peking University; HUST; NUS). EuroSys 2024, Atena.

## Problema (cum o formuleaza autorii)
- Ciclul de viata al unui incident are patru etape: detectie, triere, diagnostic, mitigare. RCA manual (loguri, metrici, trace-uri, tichete) este laborios si predispus la erori. Autorii descriu un "spectru informational": RCA e dificil atat cand informatia lipseste, cat si cand este in exces (1).
- Ghidurile de troubleshooting (TSG) cer integrare manuala a datelor, se invechesc si au detalii si acoperire insuficiente (2.2.3).
- Fine-tuning-ul unui LLM doar pe titlul si rezumatul incidentului [1] ignora alte surse, este costisitor si greu de actualizat (1).
- Trei observatii dintr-un studiu pe un an de incidente ale serviciului de email Microsoft (3):
  - cauza este greu de determinat dintr-o singura sursa de date;
  - incidentele cu aceeasi cauza revin in scurt timp: 93,80% dintre incidentele recurente reapar in 20 de zile;
  - incidentele cu cauze noi sunt frecvente: 24,96% (163 din 653).

## Ce propun (metoda, pe scurt)
- **RCACopilot**, sistem on-call in doua etape (4, Fig. 4):
  1. **Colectarea informatiei de diagnostic:** incidentul este asociat, dupa tipul alertei, unui "incident handler" construit de inginerii on-call (OCE). Handler-ul este un workflow de tip arbore de decizie, cu actiuni reutilizabile si versionate: scope switching (de exemplu de la nivel "forest" la nivel de masina), query si mitigation. Datele sunt colectate din loguri, stack trace-uri si metrici (de exemplu metrici de socket) (4.1).
  2. **Predictia categoriei de cauza:**
     - embedding FastText antrenat pe incidentele istorice;
     - cautarea celor mai apropiate incidente cu o similaritate care combina distanta euclidiana si distanta temporala (alpha = 0,3);
     - selectarea a K = 5 incidente din categorii diferite ca exemple;
     - rezumarea informatiei de diagnostic cu GPT (120-140 de cuvinte);
     - prompt CoT cu optiunea "Unseen incident" si cerinta de explicatie (4.2).
- Implementare: 58.286 de linii de cod (56.129 C# si 2.157 Python) si o aplicatie web pentru construirea handler-elor (4.3).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Sistemul tinta este Transport, serviciul global de email al Microsoft (SMTP, IMAP, POP3).
- 653 de incidente dintr-un an, etichetate manual de OCE cu categoria de cauza; impartire 75% antrenare / 25% test (5.1).
- LLM: GPT-3.5-turbo si GPT-4 (8K), cu GPT-4 implicit. Baseline-uri: FastText, XGBoost, GPT fine-tuned [1], GPT-4 Prompt (fara exemple), GPT-4 Embedding.
- Server cu i7-9700, 32 GB RAM, Windows 11. Trei runde de experimente (5).

## Experimente si metrici
- Micro-F1 si Macro-F1 pentru predictia categoriei de cauza; timpul de antrenare si de inferenta (Tabelul 2).
- Ablatie pe sursele de context din prompt: AlertInfo, DiagnosticInfo (brut sau rezumat), ActionOutput (Tabelul 3); numarul de exemple CoT si alpha (Fig. 12).
- Utilizare in productie: timpul mediu de executie al handler-elor si numarul de handler-e per echipa (Tabelul 4).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- **Tabelul 2** (Micro-F1 / Macro-F1 / timp de inferenta in secunde):

| Metoda | Micro-F1 | Macro-F1 | Inferenta (s) |
|---|---|---|---|
| FastText | 0,076 | 0,004 | 0,524 |
| XGBoost | 0,022 | 0,009 | 1,211 |
| GPT fine-tuned [1] | 0,103 | 0,144 | 4,262 |
| GPT-4 Prompt | 0,026 | 0,004 | 3,251 |
| GPT-4 Embedding | 0,257 | 0,122 | 3,522 |
| RCACopilot (GPT-3.5) | 0,761 | 0,505 | 4,221 |
| RCACopilot (GPT-4) | 0,766 | 0,533 | 4,205 |

- **Tabelul 3:** informatia de diagnostic rezumata da cel mai bun rezultat (0,766 / 0,533), cu 0,077 / 0,023 peste informatia nerezumata (0,689 / 0,510). Adaugarea altor surse (AlertInfo, ActionOutput) scade performanta; cu toate trei sursele se obtine 0,440 / 0,349.
- Cea mai buna combinatie este K = 5 si alpha = 0,3; mai multe exemple nu imbunatatesc intotdeauna rezultatul (Fig. 12).
- In trei runde, Micro-F1 este constant peste 0,70 si Macro-F1 peste 0,50 (5.6).
- **Productie:** colectarea informatiei de diagnostic este folosita de peste 30 de echipe Microsoft de peste patru ani. Timpul mediu per incident este intre 15 si 841 de secunde; Tabelul 4 arata 10 echipe, cu 18 pana la 213 handler-e activate. Modulul de predictie a fost lansat in serviciul Transport, iar feedback-ul OCE colectat prin email-urile de notificare este descris ca in majoritate pozitiv (5.5).

## Limitari declarate de autori
- Eficacitatea depinde de LLM; este integrat doar cu modelele GPT de la OpenAI (6).
- Rezultatele depind de calitatea etichetelor puse manual de OCE (6).
- Daca monitoarele nu detecteaza incidentul sau nu exista un handler pentru acel tip de alerta, sistemul nu se aplica (6).
- Handler-ele nu ofera mitigari pentru toate situatiile; de exemplu regresiile de cod sunt greu de tratat (4.1.2).
- Instabilitatea ocazionala a LLM poate produce variatii intre runde (6).
- Lucrare viitoare: evaluarea pe alte servicii, pentru generalizabilitate (6).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - serviciu de email cloud (Microsoft Transport) (5.1).
- UE reale sau emulate?: nu se aplica - incidente reale de productie (5.1).
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu.
- executa actiuni automat (bucla inchisa)?: partial - handler-ele colecteaza automat date si pot contine actiuni de mitigare predefinite; predictia cauzei este prezentata OCE spre revizuire (4, 4.1.2).
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - serviciul este descris ca distribuit global, dar lucrarea nu trateaza failover (5.1).
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu - impartire 75/25 a incidentelor istorice; deployment-ul in productie nu are o evaluare prospectiva cuantificata.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu - metrici de clasificare.
- observa traficul la SCP / proxy?: nu - nu este o retea 5G. Un incident descris implica servere proxy front-door SMTP (3).
