# A Protocol-Based Framework for AIaaS Lifecycle Management in 6G via NWDAF (2025)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Oliveira2025Aiaas . DOI/link: https://doi.org/10.23919/cnsm67658.2025.11297508 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Autorii considera ca 6G va fi AI-native. Dupa ei, NWDAF din 5G a introdus automatizare bazata pe analytics, dar nu are suport standardizat pentru: controlul ciclului de viata al modelelor, Data Analytics as a Service (DAaaS), feedback in bucla inchisa si interoperabilitate la scara larga.

## Ce propun (metoda, pe scurt)
Un framework bazat pe protocol pentru managementul AI-as-a-Service (AIaaS) in 6G, centrat pe un NWDAF extins cu patru componente: Model Lifecycle Orchestrator, Model Registry & Validator, Distributed Execution Engine si Feedback Aggregator. Introduce doua interfete service-based usoare: Model Training and Creation Protocol (MTCP), pentru antrenarea si publicarea modelelor bazate pe intentie, si Model Execution Protocol (MEP), pentru inferenta on-box si feedback de metrici.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Validare prin verificare formala sub pierderi de mesaje, folosind un model TLA+ reproductibil cu trei NF-uri si doua versiuni de model. Specificatia TLA+ publica este configurata pentru 3 NF-uri. Modelarea complexitatii este descrisa ca teoretica. Testbed real: nedeclarat in rezumat.

## Experimente si metrici
Verificare formala (TLA+) a framework-ului sub pierderi de mesaje, si modelare a complexitatii. Metrici: nedeclarate in rezumat.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Autorii afirma ca rezultatele arata ca NWDAF poate evolua intr-un manager fezabil al ciclului de viata AI, permitand deployment-uri AI-native scalabile si stabile in 6G. Din modelarea complexitatii: "linear resource scaling up to 128 network functions (theoretical)". Specificatia TLA+ publica este configurata pentru 3 NFs. Rezumatul nu trimite la tabele sau figuri.

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - (rezumat: NWDAF extins in 6G; nu e precizat daca exista o implementare)
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: nedeclarat - (rezumat: "closed-loop feedback" este indicat ca lipsa; nu e precizat daca bucla e inchisa in evaluare)
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
