# A Reliable AMF Scaling and Load Balancing Framework for 5G Core Networks (2023)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Chouman2023Amfscaling . DOI/link: https://doi.org/10.1109/iwcmc58020.2023.10182447 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: B

## Problema (cum o formuleaza autorii)
Retelele 5G trebuie sa sustina un numar crescut de dispozitive conectate; strategiile si solutiile folosite trebuie sa tina cont de optimizarea resurselor de retea disponibile. Lucrarea vizeaza scalarea AMF si balansarea incarcarii in acest context.

## Ce propun (metoda, pe scurt)
Un framework de scalare AMF si de load balancing. Framework-ul foloseste distributii ale claselor de trafic si ponderi pentru a determina numarul minim de instante AMF necesare pentru cererea estimata si capacitatea relativa a instantelor AMF, pentru balansarea incarcarii. Reziliența solutiei este controlata prin formularea problemei de optimizare.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Un prototip de 5G core construit cu software open-source de emulare. Numele software-ului, scara si datele: nedeclarat in rezumat.

## Experimente si metrici
Nedeclarat in rezumat. Rezumatul mentioneaza doar ca modulul de load balancing a fost evaluat pe un set de instante AMF.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Rezumatul nu contine cifre si nu trimite la tabel sau figura. Afirma ca reziliența depinde de formularea problemei de optimizare si ca modulul de load balancing echilibreaza incarcarea intre toate instantele AMF din set.

## Limitari declarate de autori
nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - (rezumat); lucrarea descrie un prototip de 5G core, construit cu software open-source de emulare
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: nedeclarat - (rezumat); nu se spune daca numarul de instante AMF este aplicat automat
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
