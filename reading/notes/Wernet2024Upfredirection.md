# Resilient User Plane Traffic Redirection in Cellular Networks (2024)
NOTA: nota scrisa doar din rezumat; textul integral nu este disponibil din surse libere legale.
Cheie: Wernet2024Upfredirection . DOI/link: https://doi.org/10.1109/nfv-sdn61811.2024.10807476 . Sursa textului: DOAR REZUMAT (OpenAlex)
Sectiunea din plan: C . Tema: rezilienta user plane / redundanta UPF
Autori: Lisa Wernet, Laura-Marie Spang, Fridolin Siegmund, Tobias Meuser. IEEE NFV-SDN 2024.

## Problema (cum o formuleaza autorii)
Folosirea crescanda a retelelor celulare ridica cerintele de disponibilitate si fiabilitate. Un defect pe calea de date duce inevitabil la pierderea conectivitatii. Procedurile standardizate de restaurare, precum si mecanismele de continuitate a sesiunii sau de redundanta pe calea de date, fie au overhead mare in control plane, fie dubleaza tot traficul utilizatorilor (rezumat).

## Ce propun (metoda, pe scurt)
Mecanism de management al sesiunilor eficient ca resurse, care oglindeste proactiv starea sesiunilor din UPF intr-o alta instanta. Designul este independent de implementarea UPF si gNB si transparent pentru dispozitive. Dupa detectarea unui defect UPF, traficul de date este redirectionat catre UPF-ul redundant (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Implementare prototip (rezumat). Core-ul, UPF-ul si scara sunt nedeclarate in rezumat.

## Experimente si metrici
Fezabilitatea, scalabilitatea si performanta designului; timpii de recuperare ai user plane-ului (rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Oglindirea proactiva a sesiunilor reduce timpii de recuperare ai user plane-ului (rezumat; fara cifre).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - prototip; implementarea core/UPF nu este numita in rezumat.
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nu - nementionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: da - redirectionarea automata a traficului catre UPF-ul redundant dupa detectarea defectului (rezumat).
- multi-site / geo-redundanta / failover de baza de date?: da - redundanta UPF cu oglindirea starii sesiunilor si failover (rezumat); geo-distributia nu este precizata.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: partial - recuperarea user plane-ului pentru sesiunile utilizatorilor (rezumat); metricile exacte nu sunt date.
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
