# HARNESS: High Availability Supportive Self Reliant Network Slicing in 5G Networks (2022)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Vittal2022Harness . DOI/link: https://doi.org/10.1109/tnsm.2022.3157888 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Operatorii (MNO) ofera slice-uri izolate (eMBB, uRLLC, mMTC), dar se confrunta cu supraincarcare, congestie si scalare la sosirea neasteptata de cereri de serviciu ale utilizatorilor (USR) in plan de control; rezultatul sunt USR-uri pierdute si afectarea High Availability (HA) a slice-ului (rezumat).

## Ce propun (metoda, pe scurt)
- Sistemul HARNESS pentru 5G Core, bazat pe paradigma SON (rezumat).
- Algoritmi care programeaza si servesc o parte semnificativa a USR-urilor de plan de control, pentru slice-uri tolerante la intarziere si sensibile la intarziere (rezumat).
- Framework dezvoltat intr-un 5G test-bed system cu XDP si eBPF, pentru functionarea end-to-end (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Framework dezvoltat intr-un "5G test-bed system" (rezumat); detalii despre testbed nedeclarate.
- Unelte: XDP, eBPF (rezumat).
- Configuratie: cluster minimal cu doua noduri active/active (rezumat).
- Scara si date: nedeclarate in rezumat.

## Experimente si metrici
- Comparatie cu metodele tradionale de provizionare HA (rezumat).
- Metrici: numarul de USR-uri critice de plan de control impiedicate (occluded); timpul mediu de raspuns al USR-urilor; HA-ul serviciului de slice (rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Prevenirea ocluziei USR-urilor critice de plan de control: cu 60% (rezumat; fara trimitere la tabel/figura).
- Reducerea timpului mediu de raspuns pentru aceste USR-uri: cu 50% (rezumat).
- HA-ul serviciului de slice in configuratia cu doua noduri active/active: cu 3.2% mai bun (rezumat).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nedeclarat - rezumatul spune ca framework-ul este dezvoltat intr-un 5G test-bed system, fara detalii despre nucleu (rezumat).
- UE reale sau emulate? nedeclarat (rezumat).
- digital twin al retelei? nu - nu este mentionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica? nedeclarat (rezumat).
- executa actiuni automat (bucla inchisa)? nedeclarat - rezumatul descrie algoritmi de programare a USR-urilor si un sistem autonom, fara o bucla masurare-actiune descrisa (rezumat).
- multi-site / geo-redundanta / failover de baza de date? nedeclarat - se mentioneaza configuratia cu doua noduri active/active, fara geo-redundanta sau failover de baza de date (rezumat).
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat (rezumat).
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? da - metrici pe USR-uri (cereri de serviciu ale utilizatorilor) si timpul lor de raspuns (rezumat).
- observa traficul la SCP / proxy? nedeclarat (rezumat).
