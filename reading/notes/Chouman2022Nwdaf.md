# Towards Supporting Intelligence in 5G/6G Core Networks: NWDAF Implementation and Initial Analysis (2022)
Cheie: Chouman2022Nwdaf . DOI/link: 10.1109/iwcmc55113.2022.9824403 . Sursa textului: integral, arXiv v1 (30 mai 2022; "Accepted: IWCMC 2022"): https://arxiv.org/pdf/2205.15121
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Retelele 5G si ulterioare trebuie sa sustina conexiuni numeroase cu cerinte de rate, latenta si fiabilitate; AI este folosit pentru a le atinge. O provocare majora a AI este disponibilitatea datelor de calitate, ceea ce cere interfete de colectare in retea; NWDAF este propus de 3GPP ca solutie (Sec. I). Lucrarea trateaza dezvoltarea practica a NWDAF si integrarea lui intr-un core 5G operational open-source.

## Ce propun (metoda, pe scurt)
Contributii declarate (Sec. I): analiza initiala a tipurilor de date de functii de core pe care NWDAF le poate colecta; prezentarea unor insight-uri din datele colectate; discutie despre influenta NWDAF asupra activitatilor MANO (de exemplu plasarea functiilor de core); perspectiva asupra limitarilor 5G ca motivatie pentru 6G.
Studiu de caz (Sec. III): NWDAF atasat unui core Open5GS (SA, SBA, CUPS) cu UERANSIM; NWDAF colecteaza prin SBA date despre celelalte NF autorizate. Se analizeaza pachetele de control-plane generate la instantierea core-ului: numar si dimensiune per protocol, apoi interactiunea BSF-NRF, pe baza careia se formuleaza o recomandare privind plasarea BSF fata de NRF. Partea de background (Sec. II) descrie NF-urile de core, serviciile NWDAF (AnalyticsSubscription, AnalyticsInfo, DataManagement, MLModelProvision, MLModelInfo) si consumatorii PCF/NSSF.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Open5GS (5G SA, SBA, CUPS) + UERANSIM (UE si RAN) (Sec. III, Fig. 1). Datele includ doar semnalizarea de control-plane intre NF, fara trafic GTP de la UE si RAN.
- Colectare de 138 de minute; datele sunt publice: https://github.com/Western-OC2-Lab/5G-Core-Networks-Datasets.
- Numarul de UE, de gNB si de noduri nu este specificat in aceasta lucrare. Mecanismul de captura nu este detaliat aici (este detaliat in lucrarea Manias2022Signaling).

## Experimente si metrici
- Numar de pachete per protocol (Fig. 2); statistici de lungime a pachetelor per protocol: maxim si medie (Fig. 3).
- Pentru perechea BSF-NRF: octeti pe secunda schimbati (Fig. 4); lungimea pachetelor BSF->NRF in timp (Fig. 5) si NRF->BSF (Fig. 6), cu adnotari ale evenimentelor (inregistrare, heartbeat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Cele mai multe pachete sunt TCP (HTTP/2 peste REST), apoi alte protocoale; PFCP este rar, dar prezent pe N4 (Fig. 2, Sec. III). Cele mai mari pachete sunt SSL, dar infrecvente (Fig. 3). Valorile exacte sunt doar in figuri (scala logaritmica).
- Interactiunea BSF-NRF: varf de dimensiune la inceput (inregistrarea BSF la NRF), apoi dimensiune constanta (Fig. 4, 5). Heartbeat-ul BSF are loc la fiecare 10 secunde, prin cerere PATCH; apar doua dimensiuni de pachet (cerere heartbeat si confirmare) (Fig. 5).
- Raspunsul NRF: varf la inregistrare (NF REGISTERED, profil creat), apoi confirmari mici; raspunsul mai mare apare daca statusul se schimba semnificativ (de exemplu NF_DEREGISTERED) (Fig. 6).
- Concluzia studiului de caz: schimbul de informatie de control BSF-NRF e limitat, deci co-locarea nu este probabil necesara; interactiunea BSF-PCF ramane pentru lucrari viitoare (Sec. III).
- Nu se raporteaza numarul total de pachete in aceasta lucrare (cifra 171,821 apare in Manias2022Signaling).

## Limitari declarate de autori
- Lucrare viitoare: impactul NWDAF asupra retelelor 5G, explorarea datelor generate de NF-urile de core, studiul interactiunii BSF-PCF, dezvoltarea de modele de analitica avansate pentru management proactiv si forecasting (Sec. III, V).
- Analiza se limiteaza la control-plane (Sec. III). Nu sunt declarate alte limitari explicite ale metodei.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? da - Open5GS operational cu UERANSIM (Sec. I, III)
- UE reale sau emulate? emulate - UERANSIM (Sec. III)
- digital twin al retelei? nu - nu este mentionat
- prezice efectul unei actiuni inainte de a o aplica? nu - analiza descriptiva a traficului; recomandarea de plasare BSF e argumentata din date, fara predictie (Sec. III)
- executa actiuni automat (bucla inchisa)? nu - doar analiza si o recomandare; closed-loop apare doar in background despre NWDAF industriale (Sec. II-B, III)
- multi-site / geo-redundanta / failover de baza de date? nu - un singur sistem; nedeclarat altceva (Sec. III)
- evaluare prospectiva (predictie fixata inainte de experiment)? nu - nu exista predictii (Sec. III)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - masuratorile sunt pe pachete de control intre NF; trafic GTP exclus (Sec. III)
- observa traficul la SCP / proxy? nu - SCP nu e mentionat; datele sunt pachete de control-plane intre NF, capturate de NWDAF (Sec. III)
