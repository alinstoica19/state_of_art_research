# RECAP 5GC: Resilience and CAP aware 5G Core for Consistent and High Availability Service (2024)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Sovitkar2024Recap . DOI/link: https://doi.org/10.1109/noms59830.2024.10575767 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Autorii descriu arhitectura bazata pe servicii (SBA) a 5G Core (5GC), care este stateless si distribuita. Mentioneaza ca teorema CAP (Consistency, Availability, Partition tolerance) impune alegerea intre consistenta si disponibilitate atunci cand apare o partitionare, ceea ce face necesara alegerea intre consistenta starii utilizatorilor si disponibilitatea serviciului in fata defectelor bruste.

## Ce propun (metoda, pe scurt)
Prezinta RECAP 5GC, un 5GC conștient de rezilienta si de teorema CAP, care mentine High Availability (HA) prin rezilienta si consistenta in timpul defectelor bruste ale functiilor stateless. Solutia este implementata integral pe planul de control 3GPP-compliant al unui testbed 5GC, intre Access and Mobility Management Function (AMF) si Unstructured Data Storage Function (UDSF).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Testbed 5GC, conform 3GPP, cu AMF si UDSF. Configuratia experimentala: cluster minimal active/active cu doua noduri. Testbed real sau emulare: nedeclarat in rezumat. Datele: nedeclarate in rezumat.

## Experimente si metrici
Experimente pe configuratia de cluster cu doua noduri active/active, comparand RECAP 5GC cu modul CP si cu modul AP. Metrici mentionate: numarul de cereri ale utilizatorilor abandonate, disponibilitatea si consistenta starii utilizatorului.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- abandoneaza cu 47% mai putine cereri ale utilizatorilor decat modul CP
- abandoneaza cu 86% mai putine cereri ale utilizatorilor decat modul AP
- este cu 1.6% mai disponibil decat modul CP
- ramane consistent in privinta starii si informatiilor utilizatorului
Trimitere la tabel/figura: nedeclarata in rezumat.

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - (rezumat): implementat integral pe planul de control 3GPP-compliant al testbed-ului 5GC
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: nedeclarat - (rezumat)
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat): cluster cu doua noduri active/active; multi-site nedeclarat
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: da - (rezumat): cereri ale utilizatorilor abandonate si starea utilizatorului
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
