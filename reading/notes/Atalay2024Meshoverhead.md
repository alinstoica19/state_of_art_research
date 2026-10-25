# Evaluating 5G Core Service Mesh Encapsulations in Cloud Deployments (2024)
NOTA: nota scrisa doar din rezumat; textul integral nu este disponibil din surse libere legale.
Cheie: Atalay2024Meshoverhead . DOI/link: https://doi.org/10.1109/nfv-sdn61811.2024.10807506 . Sursa textului: DOAR REZUMAT (OpenAlex)
Sectiunea din plan: C . Tema: SBA / service mesh / observabilitate
Autori: Tolga Atalay, Alireza Famili, Angelos Stavrou. IEEE NFV-SDN 2024.

## Problema (cum o formuleaza autorii)
Core-ul 5G trece la VNF-uri pe hardware COTS si catre infrastructuri de cloud public precum AWS. Pe masura ce MVNO-urile investesc in core-uri bazate pe cloud, autorii spun ca trebuie intelese implicatiile acestei tranzitii, inclusiv mecanismele de management si comunicare intre VNF-uri (rezumat).

## Ce propun (metoda, pe scurt)
5G-NECTAR (5G Network Encapsulation and Control Telemetry Augmentation Resource): cadru de masurare care incapsuleaza VNF-urile core 5G intr-un service mesh custom, cu proxy-uri side-car, folosind OpenTelemetry si Jaeger. Permite evaluarea deployment-urilor in cloud pe diferite versiuni HTTP (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Evaluari in AWS (rezumat). Core-ul folosit, generatorul de UE si scara sunt nedeclarate in rezumat.

## Experimente si metrici
Overhead-ul de control plane si costurile incapsularii in service mesh, pe diferite versiuni HTTP (rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Nedeclarat in rezumat (nu sunt raportate cifre).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - VNF-uri core 5G in AWS; implementarea nu este numita in rezumat.
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nu - nementionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: nu - cadru de masurare (rezumat).
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - deployment in cloud public; multi-site nementionat (rezumat).
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: partial - traficul SBI este observat prin proxy-uri side-car de service mesh (OpenTelemetry/Jaeger); nu este SCP 3GPP (rezumat).
