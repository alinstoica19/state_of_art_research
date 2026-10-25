# Power Consumption-Aware 5G Edge UPF Selection using Deep Reinforcement Learning (2024)
Cheie: Bellin2024Upfselection . DOI/link: 10.1109/nfv-sdn61811.2024.10807472 . Sursa textului: DOAR REZUMAT (OpenAlex, rezumat: https://doi.org/10.1109/nfv-sdn61811.2024.10807472; singura copie gasita (IEEE Xplore stamp) nu a fost accesata; textul integral nu a fost obtinut)
Sectiunea din plan: B . Tema: energy-aware UPF selection / DRL

## Problema (cum o formuleaza autorii)
Orchestrarea unui deployment 5G core edge-cloud cu mai multe instante UPF distribuite; selectia UPF la stabilirea unei noi conexiuni a utilizatorului catre data network.

## Ce propun (metoda, pe scurt)
Un algoritm Deep Reinforcement Learning (agent DRL) care furnizeaza o politica pentru procedura de selectie a UPF; alegerea se bazeaza pe metrici de consum de putere in timp real de la gazdele edge si cloud, plus cerintele de latenta si latime de banda ale utilizatorilor. Obiectiv: minimizarea consumului de putere al sistemului cu respectarea QoS dorit.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
nedeclarat (doar rezumat).

## Experimente si metrici
nedeclarat (doar rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Conform rezumatului, algoritmul obtine rezultate mai bune decat alte euristici (consum mai mic de putere si mai putine erori la cerintele de latenta) si se arata avantajul folosirii datelor de putere in locul metricilor de utilizare CPU. Cifre: nedeclarat (doar rezumat).

## Limitari declarate de autori
nedeclarat (doar rezumat).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nedeclarat (doar rezumat); se mentioneaza un "5G core network deployment" edge-cloud.
- UE reale sau emulate? nedeclarat (doar rezumat).
- digital twin al retelei? nedeclarat (doar rezumat).
- prezice efectul unei actiuni inainte de a o aplica? nedeclarat (doar rezumat).
- executa actiuni automat (bucla inchisa)? nedeclarat (doar rezumat); agentul DRL furnizeaza politica de selectie UPF.
- multi-site / geo-redundanta / failover de baza de date? nedeclarat (doar rezumat).
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat (doar rezumat).
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nedeclarat (doar rezumat).
- observa traficul la SCP / proxy? nedeclarat (doar rezumat).
