# Adaptive and Latency-aware Load Balancing for Control Plane Traffic in the 4G/5G Core (2021)
NOTA: nota scrisa doar din rezumat; textul integral nu este disponibil din surse libere legale.
Cheie: Nguyen2021Cploadbalancing . DOI/link: https://doi.org/10.1109/eucnc/6gsummit51104.2021.9482513 . Sursa textului: DOAR REZUMAT (OpenAlex)
Sectiunea din plan: C . Tema: control plane / load balancing
Autori: Van-Giang Nguyen, Karl-Johan Grinnemo, Javid Taheri, Anna Brunstrom (Karlstad University, conform afilierii cunoscute a autorilor; nedeclarat in metadate). EuCNC/6G Summit 2021.

## Problema (cum o formuleaza autorii)
Proliferarea dispozitivelor si aplicatiilor mobile genereaza o crestere a traficului de semnalizare in control plane-ul core-ului, care poate deveni bottleneck. Lucrarea se concentreaza pe load balancing-ul unui MME virtualizat si distribuit (vMME), elementul de control plane central in core-urile 4G si 5G non-standalone. Majoritatea lucrarilor existente folosesc abordari statice simple (round-robin, consistent hashing), care nu functioneaza bine intr-un mediu eterogen (rezumat).

## Ce propun (metoda, pe scurt)
Trei algoritmi adaptivi de load balancing, ale caror decizii tin cont de dinamica sistemului: sarcina vMME, timpul de finalizare a unei cereri servite de un vMME si numarul de cereri in asteptare la un vMME (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Testbed Open5GCore (rezumat). Scara si generatorul de trafic sunt nedeclarate in rezumat.

## Experimente si metrici
Timpul de finalizare a cererilor de semnalizare, comparat cu scheme statice si dinamice, inclusiv cu intarzieri de legatura diferite intre load balancer si vMME-uri (rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Schema latency-aware scurteaza timpul de finalizare a cererilor de semnalizare de pana la cinci ori fata de schemele statice si dinamice, in cazurile in care intarzierile de legatura dintre load balancer si vMME-uri difera semnificativ (rezumat).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: partial - Open5GCore, cu vMME (core 4G / 5G NSA); nu core 5G SA (rezumat).
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nu - nementionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: da - load balancer-ul ia automat decizii de distribuire pe baza starii vMME (rezumat).
- multi-site / geo-redundanta / failover de baza de date?: partial - vMME distribuite cu intarzieri de legatura diferite; failover nementionat (rezumat).
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: partial - timpul de finalizare a cererilor de semnalizare (rezumat).
- observa traficul la SCP / proxy?: nu - load balancer pentru vMME (4G); SCP nu este mentionat (rezumat).
