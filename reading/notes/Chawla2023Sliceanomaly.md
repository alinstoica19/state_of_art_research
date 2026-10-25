# Graph-based Interpretable Anomaly Detection Framework for Network Slice Management in Beyond 5G Networks (2023)
Cheie: Chawla2023Sliceanomaly . DOI/link: https://doi.org/10.1109/noms56928.2023.10154357 . Sursa textului: DOAR REZUMAT
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Sectiunea din plan: B
## Problema (cum o formuleaza autorii)
Sistemele 5G si Beyond 5G au complexitate tehnologica crescuta, comportament dinamic si variabilitate a accesului la retea. Autorii considera automatizarea o cerinta majora de management si sustin ca este necesara automatizarea proactiva end-to-end.
## Ce propun (metoda, pe scurt)
G5IAD (Graph-based Interpretable Anomaly Detection), un framework care combina Graph Convolutional Neural Networks cu corelatii intre KPI-urile multivariate ale slice-urilor de retea, si prezice serii temporale individuale cu Recurrent Neural Networks/GRU. Arhitectura include un mecanism de detectie a anomaliilor bazat pe clasificare probabilista. Abordarea este nesupervizata si are scopul de a ajuta operatorii sa identifice si sa explice caracteristici ale KPI-urilor, pentru root cause analysis mai rapida si slice-uri auto-gestionate.
## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Modelul a fost testat intr-o "realistic 5G simulation". Unelte, scara si date: nedeclarat in rezumat.
## Experimente si metrici
Comparatia dintre un model cu Graph CNN si Recurrent Neural Network si un model GRU. Metrica mentionata: acuratetea. Alte detalii: nedeclarat in rezumat.
## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
"45.9% better accuracy when trained with a Graph CNN and Recurrent Neural Network compared to the GRU model." Tabel/figura: nedeclarat in rezumat.
## Limitari declarate de autori
Nedeclarat in rezumat.
## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - (rezumat: se mentioneaza o simulare 5G; nu se precizeaza daca core-ul este implementat)
- UE reale sau emulate?: nu - (rezumat: testarea este descrisa ca "realistic 5G simulation", nu ca testbed cu UE reale)
- digital twin al retelei?: nedeclarat - (rezumat: nu mentioneaza)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat: se prognozeaza serii temporale de KPI, nu efectul unei actiuni)
- executa actiuni automat (bucla inchisa)?: nedeclarat - (rezumat: mentioneaza "self-managed network slices" ca scop, dar nu descrie o bucla inchisa implementata)
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat: nu mentioneaza)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat: nu mentioneaza)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat: se analizeaza KPI-uri ale slice-urilor de retea)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat: nu mentioneaza SCP sau proxy)
