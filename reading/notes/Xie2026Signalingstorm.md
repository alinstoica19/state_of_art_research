# Open the Floodgates in a Digital Twin: Experiences of Building Spillway for 100M+-User Signaling Storms in Cellular Core Network (2026)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Xie2026Signalingstorm . DOI/link: https://doi.org/10.1145/3789240.3829205 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Rezumatul spune ca furtunile de semnalizare (signaling storms) amenintă nucleele de retea celulara, cand reconectari sincronizate ale unui numar mare de dispozitive produc supraincarcari in cascada. Apararile existente folosesc configurari manuale si statice ale controalelor locale de supraincarcare, care ignora dependentele seriale dintre elementele de retea heterogene.

## Ce propun (metoda, pe scurt)
Spillway, un sistem bazat pe digital twin, care automatizeaza mitigarea globala a inundatiilor de semnalizare. Sistemul are o arhitectura ierarhica de aparare care impune "altruistic throttling", astfel incat nodurile din amonte elimina din trafic inainte ca blocajele din aval sa cedeze. Pentru evaluarea configuratiilor candidate se foloseste CN-DES, un simulator cu evenimente discrete specific domeniului, cu nucleu vectorizat, care agrega utilizatorii ce impart stari de protocol. Optimizarea parametrilor se face cu heteroscedastic evolutionary Bayesian optimization.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Tip de testbed (real, emulat sau simulat): simulare (CN-DES) si deployment de cinci ani intr-o retea 5G Standalone, "the world's largest", cu incidente reale.
Unelte: CN-DES, heteroscedastic evolutionary Bayesian optimization.
Scara: simulari regionale cu zeci de milioane de utilizatori; deployment in "the world's largest 5G Standalone network".
Date: incidente reale din retea, inclusiv anomalii ale aplicatiilor si defecte RAN; analiza post-incident.

## Experimente si metrici
Simularea furtunilor de semnalizare cu CN-DES; compararea timpului de simulare cu simularea traditionala; compararea numarului de "user fallbacks" intre configuratiile optimizate de Spillway si cele legacy, pe incidente reale; verificarea post-incident ca elementele de retea au ramas in limite sigure de functionare.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- CN-DES: "60× speedup over traditional simulation" si simularea storm-urilor cu "tens of millions of users in minutes".
- In incidente reale, retelele cu configuratii optimizate de Spillway au avut "substantially fewer user fallbacks than predicted under legacy configurations"; nu este dat un numar.
- Parametrii pre-deployed au mentinut "all network elements within safe operating bounds" (analiza post-incident).
Rezumatul nu contine trimitere la tabel/figura.

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? da - (rezumat): deployment de cinci ani in retea 5G Standalone reala; CN-DES este un simulator (model) folosit pentru evaluarea configuratiilor.
- UE reale sau emulate? nedeclarat - (rezumat): simularile folosesc zeci de milioane de utilizatori agregati; in deployment, statutul UE nu este detaliat.
- digital twin al retelei? da - (rezumat): Spillway este descris ca "digital-twin-driven system".
- prezice efectul unei actiuni inainte de a o aplica? da - (rezumat): configuratiile candidate sunt evaluate prin CN-DES inainte de implementare; rezumatul mentioneaza si fallback-uri "predicted" de catre configuratiile legacy.
- executa actiuni automat (bucla inchisa)? da - (rezumat): sistemul "automates global signaling-flood mitigation"; nu este descrisa explicit o bucla inchisa in timp real.
- multi-site / geo-redundanta / failover de baza de date? nedeclarat - (rezumat): "regional-scale storms" nu sunt descrise ca multi-site sau failover.
- evaluare prospectiva (predictie fixata inainte de experiment)? da - (rezumat): fallback-urile reale din incidente sunt comparate cu cele "predicted" de simulare, folosind parametrii pre-deployed; rezumatul nu spune explicit ca predictia a fost inregistrata inainte de fiecare incident.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? da - (rezumat): metrica "user fallbacks" (utilizatori care cad pe o cale de rezerva); nu sunt mentionate inregistrari sau sesiuni.
- observa traficul la SCP / proxy? nedeclarat - (rezumat): nu se mentioneaza SCP sau proxy.
