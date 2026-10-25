# Digital Twin For 5G Networks and Beyond: Domain Transfer and Network Behavior Classification for 6G Readiness (2025)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Petrik2025Dtdomaintransfer . DOI/link: https://doi.org/10.1109/elmar66948.2025.11193997 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Autorii arata ca retelele 5G sustin aplicatii cu cerinte stricte de latenta si fiabilitate, ceea ce ridica provocari pentru monitorizarea in timp real si optimizarea traficului. Vad tehnologia Digital Twin (DT) ca o abordare pentru simularea si clasificarea comportamentului retelei.

## Ce propun (metoda, pe scurt)
Prezinta un sistem DT pentru 5G care analizeaza metrici ale core-ului de retea in timp real si clasifica traficul cu retele neuronale Long Short Term Memory (LSTM). Sistemul combina un mediu de simulare cu un model de clasificare antrenat pe date sintetice. Sistemul suporta fine-tuning online al modelului.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Sistemul este construit integral cu instrumente open source, in mod specific Open5GS si UERANSIM. Modelul de clasificare este antrenat pe date sintetice. Scara: nedeclarata in rezumat.

## Experimente si metrici
Modelul este evaluat pe trafic simulat si pe trafic real de retea. Metrica mentionata: acuratetea modelului de clasificare.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Autorii raporteaza operare cu succes in timp real a DT si suport pentru fine-tuning online. Raporteaza ca acuratetea modelului scade semnificativ pe date din lumea reala. Cifre: nedeclarate in rezumat. Trimitere la tabel/figura: nedeclarata in rezumat.

## Limitari declarate de autori
Adaptarea de domeniu (domain adaptation) este indicata ca provocare critica. Autorii conchid ca sunt necesare strategii de domain transfer mai robuste.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - (rezumat): Open5GS si UERANSIM, instrumente open source
- UE reale sau emulate?: nedeclarat - (rezumat): UERANSIM este mentionat, fara detalii despre UE; trafic real de retea este evaluat
- digital twin al retelei?: da - (rezumat): sistem DT pentru 5G
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: nedeclarat - (rezumat)
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
