# Design and Implementation of a Cost-Effective Failover Mechanism for Containerized UPF (2025)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: NguyenTrung2025Upffailover . DOI/link: https://doi.org/10.3390/electronics14152991 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Autorii descriu retelele private 5G cu edge computing, in care UPF (User Plane Function) si aplicatiile sunt containerizate aproape de dispozitive. Spun ca mediile edge au resurse limitate si esecuri neprevazute (intreruperi de retea, defecte hardware), iar strategiile de rezilienta bazate pe redundanta, care mentin instante standby, au costuri substantiale si reduc eficienta resurselor si scalabilitatea.

## Ce propun (metoda, pe scurt)
Propun un design care permite detectia rapida a esecurilor UPF si doua mecanisme de failover pentru restaurarea instantelor UPF esuate: fie in clusterul care gazduieste UPF-ul esuat, fie pe mai multe clustere, in functie de disponibilitatea resurselor si de starea clusterului.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Implementare si evaluare pe un testbed bazat pe Kubernetes. Testbed real sau emulat: nedeclarat in rezumat. Scara si datele: nedeclarate in rezumat.

## Experimente si metrici
Evaluare comparativa cu metode de baza (timpul de redeployment al UPF) si cu metode de failover bazate pe redundanta (costul sistemului), in conditii de cerinte de fiabilitate ridicate.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- timpul de redeployment al UPF este redus cu pana la 37% fata de metodele de baza
- costul sistemului este redus cu pana la 50% sub cerinte de fiabilitate ridicate, fata de metodele de failover bazate pe redundanta
Trimitere la tabel/figura: nedeclarata in rezumat.

## Limitari declarate de autori
Nedeclarat in rezumat. Autorii spun ca abordarea poate fi o solutie complementara strategiilor de rezilienta traditionale.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - (rezumat): UPF containerizat este mentionat, fara detalii despre implementarea UPF
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: da - (rezumat): detectia esecurilor UPF si doua mecanisme de failover care restaureaza instantele esuate
- multi-site / geo-redundanta / failover de baza de date?: da - (rezumat): failover in cadrul aceluiasi cluster sau intre mai multe clustere; failover de baza de date nedeclarat
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
