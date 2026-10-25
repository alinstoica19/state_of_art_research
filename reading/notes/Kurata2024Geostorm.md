# Signaling Storm Mitigation by Geographically Distributed C-plane NF Placement and Routing (2024)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Kurata2024Geostorm . DOI/link: https://doi.org/10.1109/netsoft60951.2024.10588904 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: B

## Problema (cum o formuleaza autorii)
In retelele mobile, un signaling storm (congestie a planului de control cauzata de mesaje de signaling excesive) poate degrada sever performanta. Autorii identifica drept cauze congestia legaturilor inter-site si supraincarcarea unei instante NF anume.

## Ce propun (metoda, pe scurt)
Un algoritm combinat de placement si routing. Algoritmii de placement, impreuna, realizeaza plasarea geografic distribuita a instantelor NF din planul de control, in functie de tiparele de mobilitate fluctuante ale fiecarui UE. Algoritmul de routing alege instanta NF care gestioneaza fiecare UE, luand in considerare rata de utilizare si numarul de contexte al fiecarei instante.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Evaluari extensive prin simulare. Scara, unelte si date: nedeclarat in rezumat.

## Experimente si metrici
Comparatie cu scenarii existente de placement. Metrici mentionate: numarul de mesaje de signaling inter-site si dispersia ratei de utilizare a instantelor NF.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Rezumatul nu contine cifre si nu trimite la tabel sau figura. Afirma ca metodele propuse reduc semnificativ mesajele de signaling inter-site fata de scenariile existente si ca dispersia ratei de utilizare a instantelor NF scade.

## Limitari declarate de autori
nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - (rezumat); rezumatul vorbeste despre retele mobile in general si nu mentioneaza 5G
- UE reale sau emulate?: nedeclarat - (rezumat); evaluarea este prin simulare, dar nu se spune cum sunt modelate UE
- digital twin al retelei?: nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: nedeclarat - (rezumat)
- multi-site / geo-redundanta / failover de baza de date?: da - (rezumat); plasarea NF este geografic distribuita si se analizeaza legaturile inter-site; failover nu este mentionat
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat); routing-ul este per UE, dar metricile sunt la nivel de mesaje si instante NF
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
