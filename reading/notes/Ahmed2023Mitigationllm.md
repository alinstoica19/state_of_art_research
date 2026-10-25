# Recommending Root-Cause and Mitigation Steps for Cloud Incidents using Large Language Models (2023)
Cheie: Ahmed2023Mitigationllm . DOI/link: https://doi.org/10.1109/icse48619.2023.00149 . Sursa textului: integral: arXiv 2301.03797v2 (9 februarie 2023)
Sectiunea din plan: C . Tema: anomalii/RCA / LLM in managementul incidentelor
Autori: Toufique Ahmed, Supriyo Ghosh, Chetan Bansal, Thomas Zimmermann, Xuchao Zhang, Saravan Rajmohan (Microsoft; Microsoft Research; primul autor in timpul unui internship). ICSE 2023.

## Problema (cum o formuleaza autorii)
- Inginerii on-call (OCE) au nevoie de multe cunostinte de domeniu si efort manual ca sa gaseasca cauza si sa mitigheze incidentele de productie. Autorii prezinta lucrarea ca primul studiu la scara mare despre eficacitatea modelelor GPT-3.x pentru aceste sarcini (Rezumat, I).
- Sumarele, cauzele si planurile de mitigare sunt scrise in forma libera, cu tabele, link-uri si imagini. Unele incidente sunt tranzitorii sau mitigate automat (III.A).

## Ce propun (metoda, pe scurt)
- Studiu empiric cu sase intrebari de cercetare (II.D):
  - RQ1-RQ2: GPT-3.x fine-tuned pentru cauza si pentru planul de mitigare;
  - RQ3: castigul fine-tuning-ului fata de zero-shot;
  - RQ4: multi-task learning;
  - RQ5: mitigare cand cauza este data;
  - RQ6: incidente detectate de masini vs. de oameni.
- Intrarea modelului este titlul si sumarul scris la crearea incidentului, pentru a evita scurgerea informatiei din iesire (III.A).
- Modele: GPT-3.x (Curie, Codex-cushman, Davinci, Code-davinci-002/GPT-3.5) fine-tuned; baseline-uri encoder-decoder RoBERTa si CodeBERT (III.B).
- Evaluare umana cu proprietarii reali ai incidentelor (V).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Incidente Microsoft create intre 1 ianuarie 2018 si 15 iulie 2022, cu statut "Resolved" sau "Mitigated" si severitate 0-3. Rezumatul si concluzia vorbesc de peste 40.000 de incidente din peste 1000 de servicii cloud (I).
- Initial 123.953 de cauze si 23.544 de mitigari. Dupa deduplicare: 57.520 de cauze si 8.300 de mitigari. Au fost pastrate cauzele de pana la 100 de tokeni (73% dintre instante) si eliminate cele sub 3 tokeni (III.A).
- Impartire cronologica:
  - cauze: 35.820 antrenare / 3.000 test / 2.000 validare;
  - mitigari: 5.455 / 2.000 / 500;
  - seturile de test au fost filtrate manual la 2.621 de cauze si 1.780 de mitigari.
- Datele nu pot fi publicate (confidentialitate) (nota de subsol din III).
- Evaluare umana (V): 50 de incidente recente (ultimele doua luni); au raspuns 25 de proprietari, interviuri de 20-30 de minute; scoruri 1-5 de corectitudine si lizibilitate, plus un scor general.

## Experimente si metrici
- Metrici lexicale (BLEU-4, ROUGE-L, METEOR) si semantice (BERTScore, BLEURT, NUBIA), Top-1 si Top-5 (Tabelele I-II).
- Zero-shot vs. fine-tuned (Tabelul IV); multi-task (Tabelul V); mitigare cu cauza data (Tabelul VI); detectie de masina vs. de om (Tabelul VII); unicitatea sugestiilor (Tabelul III); evaluare umana (Tabelele VIII-IX).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- **Cauza, Top-1** (Tabelul I): Code-davinci-002 are BLEU-4 4,24, ROUGE-L 11,43, METEOR 10,42, BLEURT 36,77, fata de RoBERTa 4,21 / 12,83 / 9,89 / 35,66. Castigul fata de celelalte modele GPT-3 este +42,16% METEOR Top-1.
- **Mitigare, Top-1** (Tabelul II): Code-davinci-002 are BLEU-4 6,76, ROUGE-L 10,22, METEOR 8,23.
- **Fine-tuning vs. zero-shot** (Tabelul IV): pentru cauza, castig de 49,82% BLEU-4 Top-1 si 87,07% ROUGE-L Top-1.
- **Multi-task learning** nu imbunatateste rezultatele (Tabelul V).
- **Cauza data** (Tabelul VI): imbunatatire medie a celor trei metrici de 9,8% (Curie), 8,3% (Codex), 5,4% (Davinci) si 26% (Code-davinci-002).
- **Masina vs. om** (Tabelul VII; 592 de incidente detectate de masini, 1.188 de oameni): incidentele detectate de masini au scoruri mai mari cu 9,5% (BLEU-4), 20% (ROUGE-L) si 23% (METEOR), Top-1, Code-davinci-002.
- **Evaluare umana:**
  - corectitudine medie: Davinci 2,88 (cauza) / 3,04 (mitigare), Code-davinci-002 2,56 / 3,16; per ansamblu, modelele OpenAI au intre 2,28 si 3,16;
  - lizibilitatea este intre 2,52 si 4,08;
  - folosind scorul maxim dintre modelele OpenAI, corectitudinea si lizibilitatea medie sunt intre 3,52 si 4,64;
  - scor general (Tabelul IX): 5 - 2 proprietari, 4 - 9, 3 - 8, 2 - 6, 1 - 2. Peste 70% dau 3 sau mai mult.
- Corelatia Pearson dintre metricile lexicale si scorurile umane este intre -0,42 si +0,62 (VI.A).

## Limitari declarate de autori
- Prin eliminarea tabelelor si imaginilor din sumare se poate pierde informatie critica (III.A).
- Proprietarii recomanda includerea discutiilor dintre OCE ca intrare; modelele sunt mai slabe pe incidentele rare (V, VI).
- Metricile semantice folosesc modele pre-antrenate generale. Rezultatele provin din serviciile unei singure organizatii. Esantionul uman este mic, deci nu se poate obtine semnificatie statistica (VI.D).
- Lucrari viitoare: fine-tuning pe modele mai mari sau pre-antrenare pe date de incidente (VI).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - incidente din servicii cloud Microsoft.
- UE reale sau emulate?: nu se aplica.
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu - genereaza text de mitigare fara a-i estima efectul.
- executa actiuni automat (bucla inchisa)?: nu.
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: partial - impartire cronologica (antrenare pe date istorice), iar evaluarea umana foloseste incidente recente. Nu exista o evaluare in timp real la crearea incidentelor.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu - metrici de similaritate text si scoruri ale OCE.
- observa traficul la SCP / proxy?: nu.
