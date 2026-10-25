# A Scalable and Fault-Tolerant 5G Core on Kubernetes (2025)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Paul2025Faulttolerantk8S . DOI/link: https://doi.org/10.1109/comsnets63942.2025.10885628 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Autorii spun ca, odata cu cresterea numarului de dispozitive conectate si a traficului dinamic, core-ul 5G trebuie sa fie scalabil si tolerant la defecte, cerinta amplificata de softwarizarea core-ului de pachete si de deployment-urile cloud. Mentioneaza ca lucrarile anterioare nu exploreaza complet toate alegerile de design sau nu sunt conforme cu standardele 3GPP.

## Ce propun (metoda, pe scurt)
Prezinta o comparatie a alegerilor de design pentru construirea unui 5G core scalabil si tolerant la defecte pe o platforma cloud orchestrata cu Kubernetes. Pornesc de la un 5G core de productie, conform 3GPP, si construiesc mai multe variante de componente 5G core cloud-native. Folosesc failover-ul automat si capabilitatile de auto-scaling ale Kubernetes in moduri diferite.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Core 5G de productie, conform 3GPP (numele nu este declarat in rezumat), pe platforma cloud Kubernetes. Testbed real sau emulare: nedeclarat in rezumat. Scara: nedeclarata in rezumat.

## Experimente si metrici
Experimente extinse pentru evaluarea scalabilitatii si rezilientei variantelor de design si pentru cuantificarea overhead-ului deployment-urilor cloud. Metrici mentionate: scalabilitate, rezilienta si overhead.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Nedeclarat in rezumat: nu sunt raportate cifre. Autorii afirma ca lucrarea expune compromisuri intre performanta si toleranta la defecte. Trimitere la tabel/figura: nedeclarata in rezumat.

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - (rezumat): 5G core de productie, conform 3GPP
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: da - (rezumat): folosesc failover automat si auto-scaling Kubernetes
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat): se mentioneaza failover automat Kubernetes al componentelor, fara referire la multi-site sau la baza de date
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
