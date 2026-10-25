# CoreKube: An Efficient, Autoscaling and Resilient Mobile Core System (2023)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Larrea2023Corekube . DOI/link: https://doi.org/10.1145/3570361.3592522 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Autorii considera ca eficienta, scalabilitatea dinamica cost-eficienta si rezilienta planului de control al mobile core sunt esentiale. Identifica doua provocari: decuplarea starii core-ului de procesare si decuplarea procesarii planului de control de interfata catre RAN.

## Ce propun (metoda, pe scurt)
Propun CoreKube, un design de mobile core orientat pe mesaje si cloud-native, cu workers stateless (unitati de procesare) care interfateaza cu o baza de date comuna, care tine starea core-ului, si cu RAN-ul printr-un frontend. Componentele containerizate sunt orchestrate cu Kubernetes, care ofera autoscaling si self-healing.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Autorii dezvolta implementari CoreKube conforme standardelor 4G si 5G. Evaluarile experimentale sunt realizate pe platforma Powder; tipul exact al testbed-ului (real sau emulat) si scara nu sunt detaliate in rezumat.

## Experimente si metrici
Evaluari experimentale extinse, realizate pe platforma Powder si comparate cu lucrari anterioare (prior art). Aspecte evaluate: procesarea mesajelor planului de control, scalarea dinamica, consumul de resurse de calcul si recuperarea dupa defecte.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Nedeclarat in rezumat: rezultatele sunt descrise calitativ (procesare eficienta a mesajelor, scalare dinamica cu resurse de calcul minime, recuperare dupa defecte), fara cifre. Trimitere la tabel/figura: nedeclarata in rezumat.

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - (rezumat): implementari CoreKube conforme standardului 5G
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: da - (rezumat): Kubernetes asigura autoscaling si self-healing pentru componentele containerizate
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
