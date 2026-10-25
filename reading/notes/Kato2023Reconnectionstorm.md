# Congestion Control by Mobile Core and RAN Coordination in 5G Mobile Network (2023)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Kato2023Reconnectionstorm . DOI/link: https://doi.org/10.1109/vtc2023-spring57618.2023.10199592 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Autorii arata ca defectele la scara larga din retelele mobile provoaca congestie, din cauza reconectarii echipamentelor utilizator (UE). Desi 3GPP defineste functii de control al congestiei in Network Functions (NF), precum AMF, parametrii de control urmeaza sa fie calculati in AMF, care are resurse computationale epuizate in conditii de congestie.

## Ce propun (metoda, pe scurt)
Propun o schema de control al congestiei bazata pe coordonarea intre Radio Access Network (RAN) si reteaua core. Platforma de orchestrare calculeaza rata de reducere a traficului la statiile de baza, pe baza statisticilor din RAN si din core, in locul AMF-ului, in timpul congestiei.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Rezultatele sunt raportate din simulare. Testbed real sau emulare, unelte si scara: nedeclarate in rezumat.

## Experimente si metrici
Metrica mentionata: timpul pana la convergenta, comparat cu limita teoretica.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Schema creste timpul pana la convergenta cu doar 8.9 procente fata de limita teoretica. Trimitere la tabel/figura: nedeclarata in rezumat.

## Limitari declarate de autori
Nedeclarat in rezumat. Rezumatul spune doar ca lucrarea discuta aspecte de avut in vedere in specificatiile 3GPP si O-RAN pentru implementarea propunerii.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - (rezumat)
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: nedeclarat - (rezumat)
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
