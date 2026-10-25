# Next generation of microservices for the 5G Service-Based Architecture (2020)
NOTA: nota scrisa doar din rezumat; versiunea submitted din Repositorio Aberto (Universidade Aberta, handle 10400.2/14095) este accesibila doar prin 'request a copy' (acces restrictionat); textul integral nu a fost obtinut.
Cheie: Moreira2020Http3Sbi . DOI/link: https://doi.org/10.1002/nem.2132 . Sursa textului: DOAR REZUMAT (OpenAlex)
Sectiunea din plan: C . Tema: SBA / HTTP/3 pe SBI / Kubernetes
Autori: Joao Bourbon Moreira, Henrique Sao Mamede, Vasco Pereira, Bruno Sousa. International Journal of Network Management (Wiley), vol. 30, nr. 6, 2020.

## Problema (cum o formuleaza autorii)
SBA-ul core 5G foloseste HTTP/2 peste TCP pe SBI. Familia HTTP evolueaza spre protocoale bazate pe UDP, securizate cu TLS. Autorii spun ca generatia urmatoare de microservicii trebuie sa fie mai sigura, mai performanta si mai usor de gestionat, iar HTTP/3 si platformele de orchestrare a containerelor (Kubernetes) pot contribui la asta (rezumat).

## Ce propun (metoda, pe scurt)
Evaluarea modelelor de deployment pentru serviciile 5G SBA: NF-uri in arhitectura traditionala (toate functiile intr-un VM) versus arhitecturi serverless (functii distribuite in containere). Este evaluata si performanta microserviciilor in Kubernetes, cu diferite versiuni HTTP pe SBI (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Nedeclarat in rezumat (implementarea NF-urilor si generatorul de cereri nu sunt numite).

## Experimente si metrici
Performanta pe diferite versiuni HTTP, inclusiv in retele cu pierderi sau intarzieri; deployment VM versus containere/Kubernetes (rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
HTTP/3 (pe QUIC) aduce beneficii de performanta in retele cu pierderi sau intarzieri. Autorii avertizeaza ca deployment-ul in retele 5G trebuie sa ia in calcul mecanismele de connection tracking pentru volume mari de cereri (rezumat; fara cifre).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - servicii conforme SBA evaluate; implementarea nu este numita in rezumat.
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nu - nementionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: nu - evaluare de deployment (rezumat).
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nu - comunicare SBI intre NF-uri; SCP nu este mentionat (rezumat).
