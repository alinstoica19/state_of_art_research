# Design of Resilient Mobile Core Network Architecture Inspired by Soft Guarantee Behavior (2025)
NOTA: nota scrisa doar din rezumat; textul integral nu este disponibil din surse libere legale.
Cheie: Kurata2025Softguarantee . DOI/link: https://doi.org/10.23919/cnsm67658.2025.11297448 . Sursa textului: DOAR REZUMAT (OpenAlex)
Sectiunea din plan: C . Tema: rezilienta core / degradare gratioasa
Autori: Masayuki Kurata, Ryu Watanabe, Masaki Suzuki. CNSM 2025.

## Problema (cum o formuleaza autorii)
Pentru a incepe comunicarea, dispozitivele trebuie sa treaca prin autentificare, autorizare si stabilirea sesiunii, toate gestionate de core (MCN). O intrerupere a core-ului poate perturba critic aceste proceduri si degrada QoE (rezumat).

## Ce propun (metoda, pe scurt)
SG-MCN (soft guarantee MCN), arhitectura inspirata de comportamentul "soft guarantee" din sistemele web cu trei niveluri: raspunsuri rapide care ocolesc procesarea din nivelul de date, predispus la bottleneck, folosind informatii din nivelurile de aplicatie si prezentare. SG-MCN respecta standardele de securitate 3GPP: verifica dispozitivele intr-o functie echivalenta nivelului de prezentare, folosind un identificator criptat pe dispozitiv si un identificator precalculat din nivelul de date; autentificarea mutuala foloseste un vector de autentificare precalculat; autorizarea si stabilirea sesiunii sunt facute speculativ, pe baza contextelor per dispozitiv obtinute in procedurile anterioare (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Emulare (rezumat). Implementarea core-ului, UE-urile si scara sunt nedeclarate in rezumat.

## Experimente si metrici
Scoruri QoE in conditii normale si in conditii de intrerupere, cand functiile din nivelul de date sunt indisponibile (rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
SG-MCN mentine scoruri QoE apropiate de cele ale MCN in conditii normale, atat in conditii normale cu overhead de procesare suplimentar, cat si in conditii de intrerupere cu nivelul de date indisponibil (rezumat; fara cifre).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - evaluare prin emulare; implementarea nu este numita in rezumat.
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nu - nementionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: partial - autorizarea si stabilirea sesiunii sunt facute speculativ, automat, cand nivelul de date este indisponibil (rezumat).
- multi-site / geo-redundanta / failover de baza de date?: partial - indisponibilitatea functiilor din nivelul de date (UDM/UDR, conform descrierii cu trei niveluri) este tratata prin ocolire, nu prin failover (rezumat).
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: da - QoE la nivel de utilizator, cu proceduri de autentificare, autorizare si sesiune (rezumat).
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
