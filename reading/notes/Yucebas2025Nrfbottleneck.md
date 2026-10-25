# Performance and Viability Analysis of Deploying Cloud-native 5G Autoscaling Platforms (2025)
NOTA: nota scrisa doar din rezumat; lucrarea este open access (licenta CC conform Crossref), dar PDF-ul din ACM Digital Library este in spatele unui bot check Cloudflare, care nu a fost ocolit.
Cheie: Yucebas2025Nrfbottleneck . DOI/link: https://doi.org/10.1145/3733814.3765490 . Sursa textului: DOAR REZUMAT (OpenAlex)
Sectiunea din plan: C . Tema: autoscaling / cloud-native core
Autori: Amber Yucebas, Ruoting Xiong, Yi Cheng Ren, Xu Zhang, Gerard P. Parr. Publicatie ACM (2025; venue nedeclarat in metadatele OpenAlex).

## Problema (cum o formuleaza autorii)
Autoscaling-ul in 5G inseamna alocarea si eliminarea dinamica a functiilor de retea dupa cererea in timp real: ofera capacitate pentru utilizatori noi si evita costurile excesive (rezumat).

## Ce propun (metoda, pe scurt)
Comparatie intre doua platforme 5G stateless cu autoscaling, CoreKube si free5GC-helm, plus analiza bottleneck-ului si a problemei de autoscaling a free5GC-helm, cu indicatii pentru deployment real (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Ambele platforme sunt desfasurate pe Hetzner Cloud. Sarcina mare este generata cu PacketRusher, iar metricile sunt colectate pentru analiza (rezumat). Scara (numar de UE, noduri) este nedeclarata in rezumat.

## Experimente si metrici
Evaluarea autoscaling-ului sub sarcina mare si analiza bottleneck-ului free5GC-helm (rezumat). Metricile exacte sunt nedeclarate in rezumat.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Mecanismul de scalare al free5GC-helm atinge rapid bottleneck-uri, in principal din cauza deciziilor luate in NRF (rezumat; fara cifre).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - CoreKube si free5GC-helm desfasurate pe Hetzner Cloud (rezumat).
- UE reale sau emulate?: emulate - PacketRusher (rezumat).
- digital twin al retelei?: nu - nementionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: partial - autoscaling-ul platformelor (mecanisme existente) este evaluat; nu este propus un controller nou (rezumat).
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nu - bottleneck-ul este atribuit NRF; SCP nu este mentionat (rezumat).
