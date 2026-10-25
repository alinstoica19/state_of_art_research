# Safe RL for Core Network autoscaling (2024)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Long2024Saferl . DOI/link: https://doi.org/10.23919/cnsm62983.2024.10814355 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: B

## Problema (cum o formuleaza autorii)
Autoscaling-ul core network este o provocare critica de scalabilitate. Metodele traditionale si abordarile RL avansate ignora adesea aspectele de siguranta, ducand la explorarea unor actiuni nesigure in timpul antrenarii.

## Ce propun (metoda, pe scurt)
Autoscaling-ul este formulat ca o problema de Safe RL, cu constrangeri de siguranta incluse. Metodologiile de autoscaling sunt dezvoltate prin optimizarea algoritmilor Safe RL, prin design atent al functiilor si reglarea hiperparametrilor.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Evaluare pe un mediu de simulare bazat pe Gym si pe platforma open-source Magma Core Network. Daca platforma Magma este reala sau emulata, scara si datele: nedeclarat in rezumat.

## Experimente si metrici
Modelele Safe RL sunt evaluate in mediul Gym si pe platforma Magma. Metrici: nedeclarat in rezumat (se mentioneaza doar comportamentul in timpul explorarii).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Rezumatul nu contine cifre si nu trimite la tabel sau figura. Afirma ca modelele Safe RL au un comportament mai sigur in timpul explorarii si pot ajuta aplicabilitatea RL in lumea reala.

## Limitari declarate de autori
nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - (rezumat); se mentioneaza platforma Magma, dar nu generatia (5G) si nu este precizat daca evaluarea este pe core real sau emulat
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nedeclarat - (rezumat); mediul Gym este un simulator, termenul digital twin nu apare
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: nedeclarat - (rezumat)
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
