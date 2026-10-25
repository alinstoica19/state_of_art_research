# Digital Twin-Assisted Handover Scheme for Mobile Networks Using Generative AI (2026)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Cakir2026Dthandover . DOI/link: https://doi.org/10.1109/tnsm.2026.3690572 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Autorii descriu managementul handover-ului in retelele mobile ca fiind afectat de latenta mare si fiabilitate redusa in deployment-uri dense si in conditii de mobilitate. Spun ca schemele existente imbunatatesc initierea handover-ului prin optimizarea candidatului la momentul deciziei, dar sunt aplicate dupa o intarziere neneglijabila, cauzata de signalizarea din planul de control; in acel interval, candidatul poate deveni invalid sau degrada performanta.

## Ce propun (metoda, pe scurt)
Propun o schema de handover asistata de Digital Twin (DT), care realizeaza validare predictiva la momentul executiei, inainte de pregatirea handover-ului bazat pe NG. Componenta DT-What-If Generator (DT-WIG) este un model generativ spatiotemporal pe graf, cu variational latent sampling, care emuleaza stari de retea pe un orizont scurt, sub incertitudine, si genereaza trasee contrafactuale post-handover pentru decizia candidatului. AMF estimeaza riscurile de esec si QoS asociate candidatului si aproba sau respinge handover-ul prin signalizare conforma standardului. Mecanismul este declarat agnostic fata de politica si ruleaza peste politica de handover existenta.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Generarea de trace-uri se face in simulare cu ns-3/5G-LENA; evaluarea se face prin analiza de replay pe politici. Evaluarea signalizarii se face cu OpenAirInterface. Testbed real: nedeclarat in rezumat. Scara si datele folosite: nedeclarate in rezumat.

## Experimente si metrici
Experimente: generare de trace-uri ns-3/5G-LENA, analiza de replay bazata pe politici si evaluare a signalizarii cu OpenAirInterface. Metrici mentionate: rata de esec a handover-ului, timpul de intrerupere a handover-ului, latenta, jitter, throughput si packet loss.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Rezumatul arata ca metoda reduce rata de esec a handover-ului si timpul de intrerupere a handover-ului, si imbunatateste latenta, jitter-ul, throughput-ul si packet loss-ul. Cifre: nedeclarate in rezumat. Trimitere la tabel/figura: nedeclarata in rezumat.

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - (rezumat)
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: da - (rezumat): Digital Twin (DT)-assisted handover scheme, cu DT-WIG care emuleaza stari viitoare ale retelei
- prezice efectul unei actiuni inainte de a o aplica?: da - (rezumat): validare predictiva a candidatului de handover inainte de pregatirea acestuia, prin trasee post-handover generate
- executa actiuni automat (bucla inchisa)?: da - (rezumat): AMF aproba sau respinge candidatul de handover prin signalizare conforma standardului
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
