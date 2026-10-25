# Proactive and AoI-Aware Failure Recovery for Stateful NFV-Enabled Zero-Touch 6G Networks: Model-Free DRL Approach (2022)
Cheie: Shaghaghi2022Ztpfr . DOI/link: https://doi.org/10.1109/tnsm.2021.3113054 . Sursa textului: integral: arXiv 2103.03817v4
Sectiunea din plan: C . Tema: recuperare proactiva la defecte / DRL / zero-touch
Autori: Amirhossein Shaghaghi, Abolfazl Zakeri, Nader Mokari, Mohammad Reza Javan, Mohammad Behdadfar, Eduard Axel Jorswieck (IRIB University; Tarbiat Modares University; Shahrood University of Technology; TU Braunschweig). IEEE Transactions on Network and Service Management (online 2021). Codul este publicat pe GitHub.

## Problema (cum o formuleaza autorii)
- VNF-urile sunt vulnerabile la defecte de nod fizic si de software. Pentru VNF-urile stateful (de exemplu NAT), instanta de backup trebuie sincronizata cu starea celei active (I.A).
- Recuperarea are trei etape: lansarea backup-ului si migrarea imaginii, reconfigurarea fluxului, sincronizarea starii ("statelets"). Varianta reactiva le executa pe toate dupa defect, cu intrerupere mare si incalcari de SLA. Varianta proactiva (PFR) executa primele doua inainte de defect, pe baza predictiei, iar intarzierea ramane doar sincronizarea (I.A, III.D).
- Un orchestrator uman nu poate anticipa defectele si actiona optim intr-un spatiu de stari mare (I.A).

## Ce propun (metoda, pe scurt)
- **ZT-PFR:** problema de optimizare care minimizeaza un cost ponderat (costul resurselor plus penalitatea deciziilor gresite), cu constrangeri de resurse si timp maxim tolerabil de intrerupere (IV).
- **Mecanism active-standby dinamic:** backup-urile pot fi plasate si eliminate in fiecare nod NFV; o legatura logica de sincronizare are latime de banda mica in starea normala, iar intarzierea de sincronizare trebuie sa fie sub limita de intrerupere a SFC-ului (III.E).
- **Model de "impending failure"** (III.C, Tabelul II): fiecare VNF trece prin starile normal, warning si critical (inspirat de alarmele ITU X.733 si ETSI), cu probabilitati de tranzitie.
- **Monitorizare constienta de AoI:** combinatie de monitorizare declansata de evenimente si programata, pentru prospetimea informatiei (III.C).
- **Agenti DRL model-free** (V): PPO si SAC cu straturi LSTM (LSTM-PPO, LSTM-SAC); baseline PPO fara LSTM (NLSTM-PPO). Actiuni: plasarea backup-ului (BP), sincronizarea starii (SS), PFR.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Simulare (VI.A): 3 SFC-uri x 3 VNF-uri = 9 VNF-uri pe 5 noduri NFV complet conectate (NetworkX), cu trei resurse (CPU, stocare, memorie) si cereri de resurse aleatoare.
- Antrenare paralela: 32 de medii pentru PPO si 16 pentru SAC; politica tinta este evaluata la fiecare 500 de iteratii intr-un mediu nou, cu parametri aleatori (Tabelele III-VI).
- Teste si pe o retea de dimensiune mai mare (Fig. 9).

## Experimente si metrici
- Acuratetea detectiei starii critice (CSA) (Fig. 4) si a starii de warning (WSA) (Fig. 5).
- Comportamentul in starea normala, adica evitarea costurilor inutile (Fig. 6).
- Acuratetea PFR vs. RFR pe iteratii; efectul factorului de discount (Fig. 7-8).
- Efectul dimensiunii retelei (Fig. 9).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Politicile esantionate ating CSA de aproximativ 99,7% (LSTM-PPO) si 96,6% (LSTM-SAC) intr-un mediu nou (VI.B, Fig. 4).
- La prima intrare in warning, agentii aleg BP in aproximativ 45% (LSTM-PPO) si 65% (LSTM-SAC) din cazuri. Daca VNF-ul ramane in warning mai mult de doi pasi, BP este ales in peste 97% din cazuri (Fig. 5).
- LSTM-SAC (fara discount) converge dupa aproximativ 5 x 10^4 iteratii si executa PFR aproape mereu pe starile critice detectate. NLSTM-PPO nu invata PFR nici dupa 3 x 10^5 iteratii (Fig. 7-8).
- PPO converge in aproximativ jumatate din timpul SAC, dar ramane intr-un optim local (VI.B.4).
- Pe retele mai mari performanta scade, iar in starea normala se folosesc mai multe resurse decat necesar (Fig. 9).

## Limitari declarate de autori
- Mediile NFV se schimba continuu; ar fi nevoie de invatare online, cu antrenare rapida si eficienta mare a esantioanelor (VII).
- Performanta scade la dimensiuni mai mari ale retelei (VI.B).
- Lucrari viitoare: testare in medii de retea practice, medii NFV dinamice, retele mai mari (VII).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - retea NFV simulata cu SFC-uri generice (VI.A).
- UE reale sau emulate?: nu se aplica - trafic modelat prin rate de pachete (III).
- digital twin al retelei?: nu - mediu de simulare pentru antrenarea agentilor.
- prezice efectul unei actiuni inainte de a o aplica?: nu - agentul anticipeaza defectul din starile warning si critical, dar nu estimeaza efectul actiunilor inainte de executie.
- executa actiuni automat (bucla inchisa)?: da (in simulare) - agentul DRL este orchestratorul care plaseaza backup-uri, sincronizeaza starea si executa PFR (III, V).
- multi-site / geo-redundanta / failover de baza de date?: partial - failover active-standby al VNF-urilor stateful intre noduri NFV, in simulare (III.E); multi-site si failover de baza de date nu sunt tratate.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu - acuratetea deciziilor si costul resurselor.
- observa traficul la SCP / proxy?: nu.
