# Dynamic Network Slice Scaling Assisted by Attention-Based Prediction in 5G Core Network (2022)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Nhu2022Slicescaling . DOI/link: https://doi.org/10.1109/access.2022.3190640 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: B

## Problema (cum o formuleaza autorii)
Managementul resurselor si scalarea network slice-urilor sunt dificile. Operatorii trebuie sa asigure cerintele SLA pentru latenta, banda si resurse, folosind eficient resursele limitate. Abordarile reactive (prag) si cele proactive (predictie) au un compromis intre asigurarea SLA si eficienta: prag mai jos sau predictie mai prudenta pot garanta mai bine cerintele, dar pot duce la risipa de resurse.

## Ce propun (metoda, pe scurt)
Un algoritm proactiv de prognoza a resurselor, bazat pe un model encoder-decoder cu atentie (attention-based), pentru prognoza unor serii de timp multivariate. Un mecanism automat de configurare a resurselor monitorizeaza resursele si adauga sau elimina automat instante VNF ale slice-urilor de retea.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Nedeclarat in rezumat (se mentioneaza doar "comprehensive experiments"). Testbed, emulare sau simulare, unelte, scara si date: nedeclarat in rezumat.

## Experimente si metrici
Experimente comparative cu alte solutii, pentru acuratetea predictiei pe termen scurt si lung. Metrici mentionate: costul incalcarilor SLA, supra-alocarea de resurse si calitatea de intarziere (delay) a slice-urilor.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Rezumatul nu contine cifre si nu trimite la tabel sau figura. Afirma ca solutia propusa depaseste alte solutii in predictia pe termen scurt si lung, reducand costul incalcarilor SLA si al supra-alocarii si imbunatatind calitatea de intarziere.

## Limitari declarate de autori
nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - (rezumat); titlul mentioneaza 5G Core, dar rezumatul nu spune daca sistemul este implementat sau modelat
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat); predictia vizeaza utilizarea viitoare a resurselor, nu efectul actiunilor
- executa actiuni automat (bucla inchisa)?: da - (rezumat); mecanismul adauga sau elimina automat instante VNF
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
