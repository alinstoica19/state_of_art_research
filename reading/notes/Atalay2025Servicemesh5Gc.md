# 5G-STREAM: Service Mesh Tailored for Reliable, Efficient and Authorized Microservices in the Cloud (2025)
NOTA: nota scrisa doar din rezumat; textul integral nu este disponibil din surse libere legale.
Cheie: Atalay2025Servicemesh5Gc . DOI/link: https://doi.org/10.1109/dsn64029.2025.00025 . Sursa textului: DOAR REZUMAT (OpenAlex)
Sectiunea din plan: C . Tema: SBA / service mesh / NRF
Autori: Tolga Atalay, Alireza Famili, Sudip Maitra, Dragoslav Stojadinovic, Angelos Stavrou, Haining Wang. IEEE/IFIP DSN 2025.

## Problema (cum o formuleaza autorii)
Mecanismele existente de inregistrare, descoperire si autorizare din control plane-ul core 5G au probleme de scalabilitate si eficienta. La scara mare creste latenta comunicarii intre VNF-uri, ceea ce degradeaza fiabilitatea procedurilor critice (rezumat).

## Ce propun (metoda, pe scurt)
5G-STREAM (Service mesh Tailored for Reliable, Efficient, and Authorized Microservices): optimizeaza traficul de control plane in medii cloud distribuite, pe baza cunoasterii topologiei lanturilor de servicii in ierarhiile de cloud. Pe baza acestei cunoasteri, configureaza dinamic caile de comunicare pentru a reduce semnalizarea de descoperire si autorizare (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Prototip; costul de deployment este estimat pe AWS (rezumat). Core-ul folosit, scara si generatorul de sarcina sunt nedeclarate in rezumat.

## Experimente si metrici
Timpul de finalizare a procedurilor din lanturile de servicii ale core-ului, in functie de latenta VNF-NRF si de lungimea lantului; costul de deployment (rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Timpul de finalizare a procesului scade de pana la 2x raportat la latenta inter VNF-NRF per tranzactie, cu beneficii mai mari pentru lanturi mai lungi. Costul suplimentar este 0,1 USD/ora pe AWS pentru un VNF care proceseaza sustinut 50.000 de cereri pe minut (rezumat).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - prototip, fara precizarea core-ului in rezumat.
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nu - nementionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: partial - configurarea dinamica a cailor de comunicare (rezumat).
- multi-site / geo-redundanta / failover de baza de date?: partial - medii cloud distribuite si ierarhii de cloud (rezumat); failover nementionat.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nedeclarat - service mesh pentru traficul de control plane; SCP nu este numit in rezumat.
