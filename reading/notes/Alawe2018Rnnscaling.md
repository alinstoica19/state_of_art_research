# Smart Scaling of the 5G Core Network: An RNN-Based Approach (2018)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Alawe2018Rnnscaling . DOI/link: https://doi.org/10.1109/glocom.2018.8647590 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: B

## Problema (cum o formuleaza autorii)
Core-ul mobil bazat pe functii de retea virtualizate (VNF) se confrunta cu cresterea traficului de date pe planurile de date si de control, din cauza numarului crescut de dispozitive si a serviciilor 5G. Sunt necesare tehnici dinamice si precise de scalare, iar strategia (cand si cat sa scalezi) ramane complexa.

## Ce propun (metoda, pe scurt)
Tehnici de scalare bazate pe retele neuronale, care prognozeaza incarcarea viitoare. Provizionarea resurselor este programata astfel incat resursele necesare sa fie active cand incarcarea creste, iar resursele nefolosite sunt eliminate cand traficul scade.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Simulare cu evenimente discrete (discrete event simulation). Traficul de test provine dintr-un set de date de trafic furnizat de un operator de retea. Unelte suplimentare si scara: nedeclarat in rezumat.

## Experimente si metrici
Simulari comparative cu o tehnica de scalare bazata pe praguri. Metrici: nedeclarat in rezumat.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Rezumatul nu contine cifre si nu trimite la tabel sau figura. Afirma ca propunerea este mai robusta decat tehnica bazata pe praguri.

## Limitari declarate de autori
nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - (rezumat); evaluarea este facuta prin simulare cu evenimente discrete
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat); predictia vizeaza incarcarea viitoare, nu efectul actiunilor
- executa actiuni automat (bucla inchisa)?: nedeclarat - (rezumat)
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
