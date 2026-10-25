# The Cost of Stateless Network Functions in 5G (2021)
NOTA: nota scrisa doar din rezumat; lucrarea este open access in ACM DL (licenta CC conform Crossref), dar PDF-ul este in spatele unui bot check Cloudflare (HTTP 403), care nu a fost ocolit.
Cheie: Kulkarni2021Statelesscost . DOI/link: https://doi.org/10.1145/3493425.3502749 . Sursa textului: DOAR REZUMAT (OpenAlex)
Sectiunea din plan: C . Tema: core stateless / costul managementului starii
Autori: Umakant P. Kulkarni, Amit Sheoran, Sonia Fahmy. ACM (ANCS 2021, conform DOI; venue nedeclarat in metadatele OpenAlex).

## Problema (cum o formuleaza autorii)
Arhitectura cloud-native a facilitat deployment-ul si actualizarea rapida a serviciilor celulare 5G, iar o parte importanta este implementarea stateless a functiilor. Statelessness, cu serializarea, deserializarea si interactiunea cu baza de date, creste semnificativ latenta. Autorii fac primii pasi spre cuantificarea costului statelessness intr-un sistem 5G cloud-native (rezumat).

## Ce propun (metoda, pe scurt)
Compararea costului mai multor paradigme de management al starii si mai multe optimizari: partajarea starii utilizatorului intre functiile 5G, apeluri non-blocante si API-uri custom pentru baza de date (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Experimente cu 100 pana la 1000 de cereri simultane (rezumat). Core-ul si baza de date folosite sunt nedeclarate in rezumat.

## Experimente si metrici
Costul (latenta) paradigmelor de management al starii si efectul optimizarilor (rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Partajarea starii utilizatorului intre functiile 5G reduce costul total in medie cu 10% in experimentele cu 100-1000 de cereri simultane. Apelurile non-blocante si API-urile custom pentru baza de date reduc si ele costul, dar mai putin. Rezultatele sunt descrise ca preliminare (rezumat).

## Limitari declarate de autori
Rezultatele sunt descrise ca preliminare (rezumat).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - sistem 5G cloud-native; implementarea nu este numita in rezumat.
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nu - nementionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: nu - (rezumat)
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: partial - latenta cererilor (100-1000 simultane); procedurile nu sunt numite in rezumat.
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
