# A Survey of AIOps in the Era of Large Language Models (2025)
Cheie: Zhang2025Llmaiops . DOI/link: https://doi.org/10.1145/3746635 . Sursa textului: integral: arXiv v1 (23 Jun 2025, format ACM J. ACM)
Sectiunea din plan: C . Tema: nedeclarata

## Problema (cum o formuleaza autorii)
Sistemele software distribuite la scara mare trebuie sa functioneze 24/7, iar esecurile sunt inevitabile si greu de detectat, localizat si diagnosticat (Sec. 1). Abordarile AIOps bazate pe ML/DL clasic sunt descrise ca avand cinci limitari: nevoia de feature engineering complex, lipsa generalitatii intre platforme, lipsa flexibilitatii intre sarcini, adaptabilitate limitata la schimbari ale sistemului si niveluri restranse de automatizare (Sec. 1.1). Autorii sustin ca o intelegere cuprinzatoare a impactului, potentialului si limitelor LLM-urilor in AIOps este inca incipienta si ca lipseste un survey care sa acopere intregul proces AIOps in era LLM (Tabelul 1 compara cu cinci survey-uri anterioare). Scopul este restrans la AIOps pentru esecuri software la runtime in sisteme distribuite; Ops for AI si securitatea retelei sunt in afara scopului.

## Ce propun (metoda, pe scurt)
Systematic review organizat in jurul a patru research questions: RQ1 surse de date si preprocesare, RQ2 evolutia sarcinilor AIOps, RQ3 metode bazate pe LLM, RQ4 metodologii de evaluare. Protocol (Sec. 2): cautare in cinci baze (Scopus, Web of Science, IEEE Xplore, ACM DL, arXiv), publicatii dupa 2020; criterii de includere IC1-IC4 si de excludere EC1-EC5 (printre ele: modele sub 1 miliard de parametri, nelegate de software, fara experimente). Fluxul din Fig. 4: 761 de lucrari identificate (221 ACM, 238 Scopus, 81 WoS, 110 IEEE, 111 arXiv), 614 unice, 333 excluse la screening, 395 citite integral, 232 eliminate, 163 studii noi incluse. Rezumatul indica 183 de lucrari analizate, ianuarie 2020 - decembrie 2024; textul nu explica diferenta fata de cifra 163.

## Structura si taxonomia propusa
- RQ1 (Sec. 3): date traditionale generate de sistem (metrics, logs, traces) cu preprocesare LLM (imputare de metrici, generare de trace-uri, log parsing prin abordari empirice, prompt-based si fine-tuning); surse noi generate de oameni (Fig. 6): Software Information (documentatie, config, arhitectura), Source Code, Question & Answer, Incident Reports.
- RQ2 (Sec. 4, Fig. 7): trei etape. Failure Perception (failure prevention, failure prediction, anomaly detection), Root Cause Analysis (failure localization, failure category classification, root cause report generation - nou), Assisted Remediation, ordonata dupa nivelul de automatizare (Fig. 9): assisted questioning, mitigation solution generation, command recommendation, script generation, automatic execution (ultimele patru marcate ca sarcini noi, cu exceptia mitigation solution generation, care exista si inainte).
- RQ3 (Sec. 5): foundation model, fine-tuning, embedding-based, prompt-based, knowledge-based (RAG si similare).
- RQ4 (Sec. 6, Fig. 11): metrici de clasificare (performance si error), de generare (lexicale: BLEU, ROUGE, METEOR; semantice: BERTScore, BLEURT, NUBIA), de executie (task-level: Functional Correctness, Average Correctness; execution success rate, correct refactorings) si evaluare manuala (calitativa, preferinte umane); seturi de date noi (LogEval cu 4.000 intrari de log si 15 prompturi per sarcina; OpsEval cu 7.184 intrebari cu variante multiple si 1.736 QA; OWL-bench; KubePlaybook cu 130 prompturi; AIOpsLab, benchmark pentru intregul ciclu cu injectare de esecuri).

## Lucrari/sisteme acoperite (cu numar)
163 de studii noi incluse conform Fig. 4 (rezumatul spune 183 de lucrari). Lucrarile sunt discutate pe sarcini; textul observa ca failure prevention are un singur studiu (FAIL), failure prediction putine studii cu scop restrans, anomaly detection este cel mai bine reprezentata, iar automatic execution are putine lucrari ("related work is limited") ale caror eficacitate practica ramane de verificat. Fig. 1 prezinta tendinta de crestere a publicatiilor pe trimestre.

## Directii deschise declarate
Sec. 7: (7.1) eficienta temporala si costul LLM-urilor, critice pentru failure perception care ruleaza continuu (exemplu: fereastra de detectie de 10 s necesita inferenta sub 1 s); (7.2) utilizarea mai profunda a surselor de date, in special traces, pentru care nu exista lucrari LLM adecvate, si declansarea RCA pe baza datelor generate de sistem in loc de incident reports scrise de oameni; (7.3) generalizabilitate si adaptabilitate la evolutia software, cu validare empirica sistematica; (7.4) integrarea cu toolchain-uri AIOps existente (modele mici, Ansible, Kubernetes operators). Probleme generale ale LLM (halucinatii, context) sunt declarate in afara scopului.

## Limitari declarate de autori
Sunt excluse studiile cu modele sub 1 miliard de parametri (inclusiv BERT) si cele fara rezultate experimentale (EC1, EC5); scopul exclude Ops for AI si securitatea retelei (Sec. 1). Nu exista o sectiune separata de "threats to validity" in textul citit.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu - Survey despre AIOps pentru sisteme software; nu este vorba de core 5G
- UE reale sau emulate? nu - fara experimente proprii
- digital twin al retelei? nu - nu este tratat
- prezice efectul unei actiuni inainte de a o aplica? nedeclarat - Sec. 4.1 acopera failure prediction (prezicerea esecurilor), nu efectul unei actiuni
- executa actiuni automat (bucla inchisa)? nu - survey; Sec. 4.3 trateaza automatic execution ca sarcina cu putine lucrari
- multi-site / geo-redundanta / failover de baza de date? nedeclarat
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - fara experimente proprii
- observa traficul la SCP / proxy? nedeclarat
