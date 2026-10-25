# Evaluating CAP Theorem on a Stateless 5G Core (2024)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Sovitkar2024Capstateless . DOI/link: https://doi.org/10.1109/ccnc51664.2024.10454811 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Autorii descriu arhitectura bazata pe servicii (SBA) a 5G Core, construita stateless, scalabila si robusta, cu mai multe Network Functions (NF) participante. Mentioneaza ca studiul teoremei CAP devine necesar pentru a evalua impactul asupra SBA-ului bazat pe servicii, in contextul cerintelor de rezilienta din 6G.

## Ce propun (metoda, pe scurt)
Evalueaza teorema CAP pe un 5GC stateless, conform 3GPP si non-roaming, si arata compromisul intre modul Consistency si Partition tolerance (CP) si modul Availability si Partition tolerance (AP).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
5GC stateless, conform 3GPP, non-roaming. Modul de implementare, testbed real sau emulare: nedeclarat in rezumat. Scara si datele: nedeclarate in rezumat.

## Experimente si metrici
Experimente care compara modul CP cu modul AP. Metrici mentionate: numarul de cereri de sesiune PDU servite si disponibilitatea.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Modul CP al 5GC serveste mai multe cereri de sesiune PDU, dar este mai putin disponibil decat modul AP. Cifre: nedeclarate in rezumat. Trimitere la tabel/figura: nedeclarata in rezumat.

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - (rezumat): se evalueaza un 5GC 3GPP-compliant, fara detalii despre implementare
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: nedeclarat - (rezumat)
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: da - (rezumat): numar de cereri de sesiune PDU servite
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
