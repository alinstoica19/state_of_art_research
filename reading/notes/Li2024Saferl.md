# DT-LNS: Digital-Twin-Based Low-Risk Network Slicing Using Safe Reinforcement Learning (2024)
Cheie: Li2024Saferl . DOI/link: 10.1109/jiot.2024.3445177 . Sursa textului: DOAR REZUMAT (OpenAlex/Crossref, https://doi.org/10.1109/jiot.2024.3445177; fara versiune gratuita gasita prin Unpaywall/OpenAlex)
Sectiunea din plan: B . Tema: nedeclarat

## Problema (cum o formuleaza autorii)
Digital twins (DT) si reinforcement learning (RL) au fost aplicate la managementul dinamic al network slicing, dar majoritatea DT-urilor existente nu pot evalua incertitudinea predictiilor si sunt supraconfidente in medii necunoscute; pentru RL clasic este dificil sa se mentina performanta stabila a slice-urilor in retele dinamice (rezumat).

## Ce propun (metoda, pe scurt)
Cadrul DT-LNS (DT-based low-risk network slicing) cu safe RL: un DT cu retele neuronale profunde si analiza incertitudinii date-model prezice performanta slice-urilor si incertitudinea predictiei; RL selecteaza actiuni de configurare cu risc scazut prin preverificarea riscului de incalcare a SLA pentru actiunile candidate din RL si din subspatiul de actiuni de referinta, prin DT (rezumat).

## Setup experimental
nedeclarat (doar rezumat)

## Experimente si metrici
Din rezumat: comparatie cu sase metode clasice de configurare a slice-urilor (round robin, deep Q network, advantage actor-critic, deep deterministic policy gradient, RL avansat asistat de preantrenare cu DT si predictie de stare); metrici: SLA satisfaction rate (SSR), SSR jitter, delay jitter, data rate jitter, viteza de convergenta. Detalii de setup: nedeclarat (doar rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Rezumat: castig procentual mediu de 7.84%, 93.58%, 65.63%, 84.20% si 90.27% pentru SSR mediu, SSR jitter, delay jitter, data rate jitter si respectiv viteza de convergenta. Tabele/figuri: nedeclarat (doar rezumat).

## Limitari declarate de autori
nedeclarat (doar rezumat)

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nedeclarat (doar rezumat)
- UE reale sau emulate? nedeclarat (doar rezumat)
- digital twin al retelei? da - rezumatul descrie un DT bazat pe retele neuronale pentru predictia performantei slice-urilor
- prezice efectul unei actiuni inainte de a o aplica? da - DT preverifica riscul de incalcare a SLA pentru actiunile candidate (rezumat)
- executa actiuni automat (bucla inchisa)? nedeclarat (doar rezumat)
- multi-site / geo-redundanta / failover de baza de date? nedeclarat (doar rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat (doar rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nedeclarat (doar rezumat)
- observa traficul la SCP / proxy? nedeclarat (doar rezumat)
