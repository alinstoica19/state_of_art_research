# A Survey on 5G Radio Access Network Energy Efficiency: Massive MIMO, Lean Carrier Design, Sleep Modes, and Machine Learning (2022)
Cheie: LopezPerez2022Ranenergy . DOI/link: 10.1109/comst.2022.3142532 (arXiv:2101.11246) . Sursa textului: integral, arXiv v2 (7 oct. 2021): https://arxiv.org/pdf/2101.11246v2 (107 pagini; citite rezumatul, introducerea, Sec. II si IX-X in detaliu; Sec. III-VIII doar ca structura)
Sectiunea din plan: D . Tema: eficienta energetica RAN (survey)

## Problema (cum o formuleaza autorii)
5G ar permite un grad ridicat de automatizare, iar specificatia 3GPP NR ofera instrumente pentru reducerea consumului de energie si a emisiilor (rezumat). Sec. I-B: RAN, in special statiile de baza (BS), consuma cea mai mare parte a energiei retelei (aprox. 57% din consumul total al retelei pentru BS, conform [24]; 50.6% pentru RAN in 2025 conform [25], Fig. 3); echipamentul RF reprezinta aprox. 65% din energia unei BS, urmat de racire (17.5%), procesare digitala/baseband (10%) si convertoare AC-DC (7.5%). Sec. I-B citeaza un studiu [23] conform caruia o retea 5G fara orientare spre eficienta energetica ar putea consuma peste 140% mai multa energie decat una 4G cu acoperire similara, si apelul 3GPP pentru reducerea cu 90% a consumului NR fata de LTE [22]. Sec. I-C compara cu sondaje anterioare (Tabelul I) si afirma ca niciunul nu trateaza specificul 3GPP NR.

## Ce propun (metoda, pe scurt)
Survey al tehnologiilor prin care un RAN 5G (sub 6 GHz) isi poate creste eficienta energetica (Sec. I-D): categorisirea modelelor de consum si a metricilor de eficienta energetica (Sec. III-IV); patru tehnologii-cheie: massive MIMO (Sec. V, abordare teoretica, single-cell si multi-cell), lean carrier design si sleep modes pe trei domenii - timp/symbol shutdown (Sec. VI), carrier shutdown (Sec. VII: intra-BS, inter-BS, inter-RAT), antena/channel shutdown (Sec. VIII) - si machine learning (Sec. IX); directii de cercetare (Sec. X). Textul precizeaza explicit: "5G core networks aspects are not covered in this survey" (Sec. I-D).

## Setup experimental
Nu exista experimente proprii; lucrare de sinteza a literaturii (nedeclarat un setup propriu).

## Experimente si metrici
Nu se aplica experimente. Sec. IV prezinta metrici de eficienta energetica (pentru retele limitate de interferenta si de zgomot, eficienta energetica a E2E network slicing, metrici link-aware); Sec. III prezinta modele de consum pentru RAN distribuit si centralizat (cu figuri de impact al componentelor).

## Rezultate raportate (cifre exacte, cu trimitere la sectiune)
Cifre preluate de autori din literatura, Sec. IX-B (ML pentru optimizarea eficientei energetice):
- Q-learning pentru sleep mode time-domain [141]: sleep mode-ul nu ar trebui activat la incarcare de celula peste 30% daca intarzierea e critica; la incarcari foarte mici, pana la 55% economie de energie.
- Fuzzy Q-learning pentru DTX celule si backhaul [192]: pana la 38% economie fata de un DTX de baza fara buffering.
- Actor-critic DRL (DDPG) pentru (de)activarea small cells [198]: pana la 30% castig fata de Q-learning.
- Sec. II-B/C: lean carrier in 3GPP NR permite perioade de sleep de pana la 160 ms (micro-sleeps).
- Tabelul XIII sintetizeaza contributiile din Sec. IX.
Sec. IX-A (ML pentru predictia traficului) este despre prognoza traficului; detaliile nu au fost citite integral.

## Limitari declarate de autori
Sec. I-D: nu sunt acoperite aspectele de core 5G; accent pe deployment-uri sub 6 GHz. Nota 1 (Sec. I-D): pentru massive MIMO se trateaza aspecte teoretice consacrate, deoarece munca practica este limitata (simulari de sistem si masuratori). Sec. X (directii deschise): modelare teoretica multi-cell, instrumente de planificare orientate pe eficienta energetica, analiza multi-carrier si retele eterogene, optimizare data-driven (masuratori influentate de punctul de observatie, lipsa intelegerii efectului erorilor de predictie asupra economiilor de energie, lipsa framework-urilor end-to-end care combina supervised learning si RL, dificultatea achizitiei de seturi mari de date in RAN), Green AI.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu - lucrare de sinteza; core-ul nu este acoperit (Sec. I-D).
- UE reale sau emulate? nu se aplica.
- digital twin al retelei? nedeclarat in sectiunile citite.
- prezice efectul unei actiuni inainte de a o aplica? nedeclarat ca metoda proprie; Sec. IX discuta predictia traficului si RL, din literatura.
- executa actiuni automat (bucla inchisa)? nu este metoda proprie; Sec. IX prezinta din literatura agenti RL care comanda starea BS (sleep, activare/dezactivare).
- multi-site / geo-redundanta / failover de baza de date? nu - nu se aplica.
- evaluare prospectiva? nu se aplica.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu se aplica (cifrele sunt citate din alte lucrari, pe energie si QoS).
- observa traficul la SCP / proxy? nu - SCP nu apare; core-ul e exclus (Sec. I-D).
