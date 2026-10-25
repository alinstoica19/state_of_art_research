# Dynamic AI-Based UPF Switching: Adapting for Performance/Energy-Efficiency in 5G Networks (2025)
Cheie: Christakis2025Upfswitching . DOI/link: 10.1109/globecom59602.2025.11432027 . Sursa textului: DOAR REZUMAT (OpenAlex, rezumat: https://doi.org/10.1109/globecom59602.2025.11432027; textul integral nu a fost obtinut)
Sectiunea din plan: B . Tema: energy-efficient UPF / AI-based switching

## Problema (cum o formuleaza autorii)
Retelele 5G si ulterioare urmaresc viteze, latenta si densitate mai bune; implementari software ale UPF (SPGW-U, VPP) se bazeaza pe software pentru forwarding si trafic. SPGW-U ofera throughput limitat dar consum de energie rezonabil, iar VPP ofera throughput semnificativ mai mare cu un consum mult mai mare.

## Ce propun (metoda, pe scurt)
Un mecanism proactiv de comutare dinamica intre doua implementari software ale UPF (SPGW-U si VPP), pe baza throughput-ului si a consumului de energie; un model LSTM integrat prezice proactiv valorile de throughput, iar pe baza predictiilor mecanismul decide cand comuta intre implementari.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
nedeclarat (doar rezumat).

## Experimente si metrici
nedeclarat (doar rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
nedeclarat (doar rezumat).

## Limitari declarate de autori
nedeclarat (doar rezumat).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nedeclarat (doar rezumat); sunt mentionate implementari de UPF (SPGW-U, VPP).
- UE reale sau emulate? nedeclarat (doar rezumat).
- digital twin al retelei? nedeclarat (doar rezumat).
- prezice efectul unei actiuni inainte de a o aplica? da, la nivel de rezumat - LSTM prezice throughput-ul (nu efectul actiunii de comutare) inainte de decizie.
- executa actiuni automat (bucla inchisa)? nedeclarat (doar rezumat); mecanismul "determina cand sa comute".
- multi-site / geo-redundanta / failover de baza de date? nedeclarat (doar rezumat).
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat (doar rezumat).
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nedeclarat (doar rezumat).
- observa traficul la SCP / proxy? nedeclarat (doar rezumat).
