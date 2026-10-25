# Investigating Inter-NF Dependencies in Cloud-Native 5G Core Networks (2021)
NOTA: nota scrisa doar din rezumat; exista o versiune submitted in repository-ul institutional mediaTUM (mediatum.ub.tum.de/1620043), dar serverul mediaTUM nu a raspuns din acest mediu (timeout); textul integral nu a fost obtinut.
Cheie: Goshi2021Internf . DOI/link: https://doi.org/10.23919/cnsm52442.2021.9615565 . Sursa textului: DOAR REZUMAT (OpenAlex)
Sectiunea din plan: C . Tema: SBA / dependente intre NF-uri / resurse
Autori: Endri Goshi, Michael Jarschel, Rastin Pries, Mu He, Wolfgang Kellerer. CNSM 2021.

## Problema (cum o formuleaza autorii)
Core-ul 5G este dezvoltat dupa principii cloud-native, cu descompunere functionala mare si deployment distribuit. Asta creeaza dependente intre NF-uri, care trebuie studiate. Lucrarea investigheaza efectul acestor dependente asupra modului in care NF-urile folosesc resursele (rezumat).

## Ce propun (metoda, pe scurt)
Studiu experimental al dependentelor dintre NF-uri. Autorii dezvolta un emulator de gNB si UE pentru a executa diverse proceduri de control plane (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Cloud privat; free5GC desfasurat si orchestrat cu Kubernetes; emulator gNB/UE propriu (rezumat). Scara este nedeclarata in rezumat.

## Experimente si metrici
Utilizarea resurselor de catre NF-uri in timpul diferitelor proceduri de control plane (rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Nedeclarat in rezumat (fara cifre). Concluzia declarata: este important sa se tina cont de dependentele dintre NF-uri pentru o utilizare eficienta a resurselor si pentru a evita deployment-uri in care un singur NF devine bottleneck pentru tot core-ul (rezumat).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - free5GC pe Kubernetes (rezumat).
- UE reale sau emulate?: emulate - emulator gNB si UE dezvoltat de autori (rezumat).
- digital twin al retelei?: nu - nementionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: nu - studiu de masurare (rezumat).
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
