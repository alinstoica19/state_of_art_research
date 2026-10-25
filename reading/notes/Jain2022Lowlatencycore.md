# L25GC: A Low Latency 5G Core Network based on High-Performance NFV Platforms (2022)
NOTA: nota scrisa doar din rezumat; lucrarea este open access in ACM DL (licenta CC conform Crossref), dar PDF-ul este in spatele unui bot check Cloudflare (HTTP 403), care nu a fost ocolit. Semantic Scholar a raspuns 429.
Cheie: Jain2022Lowlatencycore . DOI/link: https://doi.org/10.1145/3544216.3544267 . Sursa textului: DOAR REZUMAT (OpenAlex)
Sectiunea din plan: C . Tema: core cu latenta mica / NFV de inalta performanta / rezilienta
Autori: Vivek Jain, Hao-Tse Chu, Shixiong Qi, Chia-An Lee, Hung-Cheng Chang, Cheng-Ying Hsieh, K. K. Ramakrishnan, Jyh-Cheng Chen. ACM SIGCOMM 2022.

## Problema (cum o formuleaza autorii)
Procedurile de control ale retelei celulare (mobilitate, tranzitia idle-activ pentru economisirea energiei) influenteaza direct comportamentul planului de date si intarzierea percepută de utilizator. Pornind de la aceasta interdependenta control-date, core-ul 5G este re-arhitecturat pentru a reduce latenta operatiilor de control si impactul lor asupra planului de date (rezumat).

## Ce propun (metoda, pe scurt)
L25GC, bazat pe free5GC: (1) memorie partajata, care elimina serializarea mesajelor si overhead-ul HTTP, pastrand conformitatea cu standardele 3GPP; (2) planul de date este refactorizat pentru a evita interferenta control-date, cu clasificatoare de pachete scalabile la nivel de flux pentru lookup-ul regulilor de forwarding; (3) buffere in core pentru paging si o schema de handover care evita rutarea hairpin din 3GPP si pierderile cauzate de buffer-ele limitate din statiile de baza; (4) rezilienta integrata la defecte, care recupereaza transparent dupa defectele NF-urilor software si ale hardware-ului mai repede decat procedura 3GPP de re-atasare (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Implementare pe baza free5GC (rezumat). Testbed-ul si generatorul de UE sunt nedeclarate in rezumat.

## Experimente si metrici
Timpul de finalizare a evenimentelor de control si latenta pachetelor de date in timpul paging-ului si handover-ului, comparate cu free5GC; recuperarea dupa defecte (rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Timpul de finalizare a mai multor evenimente de control scade cu aproximativ 50%, iar latenta pachetelor de date se imbunatateste de aproximativ 2x in timpul paging-ului si handover-ului, fata de free5GC (rezumat).

## Limitari declarate de autori
Implementarea curenta suporta un numar limitat de sesiuni de utilizator (rezumat).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - pe baza free5GC (rezumat).
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nu - nementionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: da - recuperare automata, transparenta, dupa defecte de NF software si hardware (rezumat).
- multi-site / geo-redundanta / failover de baza de date?: partial - recuperare la defecte de NF si hardware; multi-site si failover de baza de date nu sunt mentionate (rezumat).
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: da - timpul de finalizare a evenimentelor de control si latenta pachetelor utilizatorilor (rezumat).
- observa traficul la SCP / proxy?: nu - comunicarea prin memorie partajata inlocuieste HTTP/SBI; SCP nu este mentionat (rezumat).
