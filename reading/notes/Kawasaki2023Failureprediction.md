# Failure Prediction in Cloud Native 5G Core With eBPF-based Observability (2023)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Kawasaki2023Failureprediction . DOI/link: https://doi.org/10.1109/vtc2023-spring57618.2023.10200028 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Autorii arata ca functiile de retea cloud-native (CNF) ofera scalabilitate si flexibilitate, dar arhitectura lor de microservicii ridica o provocare operationala prin numarul mare de compozitii si schimbarile dinamice de topologie. Predictia defectelor este descrisa ca un factor cheie pentru operarea proactiva, iar datele folosite pentru antrenarea ML trebuie sa aiba granularitate fina.

## Ce propun (metoda, pe scurt)
Folosesc extended Berkeley Packet Filter (eBPF) pentru a colecta informatii fin granulare din infrastructura virtuala in care ruleaza CNF-urile. Antreneaza un model Long Short-Term Memory (LSTM) pe datele colectate, pentru a prezice tranzitia viitoare a indicatorilor de performanta (KPI) intr-un 5G core (5GC) cloud-native.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Experimentul este realizat intr-un mediu de laborator. Unelte: eBPF si LSTM. Datele: informatii fin granulare colectate cu eBPF din infrastructura virtuala. Scara: nedeclarata in rezumat.

## Experimente si metrici
Compararea modelului antrenat pe date eBPF cu modele antrenate fara aceste date. Metrici: nedeclarate explicit in rezumat.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Modelul de predictie antrenat pe date eBPF depaseste (outperforms) celelalte modele antrenate fara date eBPF. Cifre: nedeclarate in rezumat. Trimitere la tabel/figura: nedeclarata in rezumat.

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - (rezumat): se mentioneaza un 5GC cloud-native, fara detalii despre implementare
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat): modelul prezice KPI-uri viitoare, fara o actiune asociata
- executa actiuni automat (bucla inchisa)?: nedeclarat - (rezumat)
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
