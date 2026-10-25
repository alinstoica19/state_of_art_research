# Making cellular networks crisis-proof: Towards island-ready, resilient-by-design 6G communication networks (2026)
Cheie: Janzen2026Islandready . DOI/link: https://doi.org/10.1016/j.comcom.2025.108407 . Sursa textului: integral: arXiv 2512.04346 v1 (4 dec 2025)
Sectiunea din plan: C . Tema: nedeclarata

Lucrare conceptuala / de viziune (analiza calitativa, fara experimente).

## Problema (cum o formuleaza autorii)
Retelele 5G si 5G-Advanced sunt vulnerabile la intreruperi regionale cauzate de dezastre sau atacuri tintite, deoarece majoritatea cazurilor de utilizare depind de un core central, gazduit in putine locatii (fenomenul "path inflation"). O regiune izolata de core si de Internet devine o "insula" (island), unde apelurile de urgenta, cell broadcast, mesageria si aplicatiile de stiri nu mai functioneaza. Autorii citeaza exemple: inundatiile din 2021 din vestul Europei (valea Ahr), cutremurul din Japonia 2011, caderea de curent din Peninsula Iberica 2025 (Sec. 1). Intrebarile de cercetare: RQ1 (ce actori trebuie sa colaboreze), RQ2 (in ce masura sunt 5G/5G-A "island-ready"), RQ3 (ce provocari deschise raman).

## Ce propun (metoda, pe scurt)
Un cadru conceptual pentru "island-ready, resilient-by-design 6G": definitii pentru retea de comunicatii, insula, island connectivity, reziliența (adaptata dupa Khaloopour et al.) si island readiness (Sec. 2); identificarea a cinci categorii de actori (utilizatori, operatori, dezvoltatori, furnizori cloud/edge, autoritati) si a cazurilor lor de utilizare (Sec. 3, Fig. 2); evaluarea calitativa, pe baza specificatiilor 3GPP (Rel. 15-17 = 5G, Rel. 18-19 = 5G-A), a sistemelor din lant (Internet, aplicatii, 5GC, IMS, acces si transport; Sec. 4, Fig. 3, Tabelul 1); o foaie de parcurs a provocarilor deschise (Sec. 5). Se compara patru strategii de desfasurare a aplicatiilor: centralizata, high-availability, distribuita, descentralizata (Fig. 4).

## Structura si taxonomia propusa
- Definitii: island operation vs. normal operation; retea "resilient" vs "island-ready" (un sistem care necesita activarea manuala a replicilor standby este rezilient, dar nu island-ready; Sec. 2.3-2.4).
- Actori si cazuri de utilizare: utilizator, operator, dezvoltator, furnizor, autoritati (Sec. 3).
- Sisteme evaluate: Internet, aplicatii, 5G core (plan de utilizator, plan de control SBA, functii stateful: UDM, PCF, NEF, NRF; EASDF pentru descoperirea serverelor edge), IMS, RAN si transport (Sec. 4).
- Strategii de desfasurare a aplicatiilor (Fig. 4): centralizata (nu e island-ready), high-availability multi-cloud (nu), distribuita cu replica standby (disponibila doar dupa tranzitie manuala), descentralizata cu sincronizare (island-ready, tranzitie fara downtime).

## Lucrari/sisteme acoperite (cu numar)
Nu este un survey sistematic; lista de referinte are 59 de intrari (specificatii 3GPP, studii de dezastre, lucrari despre edge/cloud). Singurul sistem evaluat explicit este arhitectura 5G/5G-A ca "sistem de sisteme". Concluzii din Sec. 4: Internetul, reteaua de acces si cea de transport sunt pregatite pentru island connectivity; aplicatiile de azi, 5G/5G-A si IMS nu sunt. Tabelul 1 listeaza 18 cazuri de utilizare (utilizator 3, operator 5, dezvoltator 4, furnizor 3, autoritati 3) cu implicarea CP/UP/IMS/edge; in majoritatea randurilor 5G si 5G-A sunt marcate "nu sunt island-ready", iar 5G-A este marcat "partial" pentru apeluri de urgenta, tranzitia furnizorului la operarea pe insula si coordonarea fortelor de urgenta (simbolurile tabelului sunt degradate in textul extras, deci aceasta lectura este aproximativa).

## Directii deschise declarate
Descentralizarea planului de control 6G si a IMS fara compromiterea securitatii/confidentialitatii (sincronizarea functiilor stateful); aplicatii local-first; capacitate edge regionala; actiuni manuale pentru activarea operarii pe insula; reglementari si acorduri compatibile cu island readiness; implicatii asupra securitatii si vietii private; cuantificarea rezilientei (stress test, exercitii reale); perspectiva utilizatorului si comunicarea M2M (Sec. 5-6). Lucrarea afirma ca rezolvarea acestor provocari depaseste scopul articolului si propune o abordare "all-society".

## Limitari declarate de autori
Colectia de actori si cazuri de utilizare este declarata non-exhaustiva si necesita expertiza aprofundata pentru rafinare (Sec. 3). Provocarile deschise sunt "selectate si schitate", nu rezolvate (Sec. 5, 6.5). Lucrari viitoare: analize aprofundate pe actori (operator, dezvoltator, furnizor, autoritati).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu - lucrare conceptuala, fara implementare (Sec. 4-5)
- UE reale sau emulate? nu - fara experimente (Sec. 4)
- digital twin al retelei? nedeclarat
- prezice efectul unei actiuni inainte de a o aplica? nu - nedeclarat; lucrare conceptuala
- executa actiuni automat (bucla inchisa)? nu - mentioneaza doar necesitatea "mecanismelor automate" de detectare si tranzitie in operarea pe insula (Sec. 6.4), fara a propune unul
- multi-site / geo-redundanta / failover de baza de date? da (ca tema discutata, nu implementata) - Sec. 4.2, 5, 6.4, Fig. 4: geo-redundanta a aplicatiilor si replici regionale de baze de date; Sec. 4.4: IMS cu geo-redundanta redusa
- evaluare prospectiva (predictie fixata inainte de experiment)? nu - fara experimente
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - Sec. 6.1 citeaza doar un studiu anterior de tip sondaj al perspectivei utilizatorilor
- observa traficul la SCP / proxy? nedeclarat (SCP nu este mentionat)
