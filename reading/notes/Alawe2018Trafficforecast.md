# Improving Traffic Forecasting for 5G Core Network Scalability: A Machine Learning Approach (2018)
Cheie: Alawe2018Trafficforecast . DOI/link: 10.1109/mnet.2018.1800104 (HAL hal-01933966) . Sursa textului: integral, versiunea de autor depusa pe HAL (v1, 24 nov. 2018): https://inria.hal.science/hal-01933966
Sectiunea din plan: B . Tema: nedeclarat

## Problema (cum o formuleaza autorii)
In arhitectura 5G core bazata pe NFV/SDN, VNF-urile pot fi scalate dinamic, dar solutiile cu prag static reactioneaza la evenimente, iar instantierea unei noi instante poate dura de la un minut la zeci de minute, ceea ce creste durata de attach a UE si duce la respingerea unor cereri (Sec. II-B). AMF este descris ca punct de intrare si gat de sticla al core-ului (Sec. II-B). Studiile anterioare proactive folosesc doar informatie la nivel de sistem (CPU, memorie), nu informatie la nivel de serviciu (Sec. II-B).

## Ce propun (metoda, pe scurt)
- Mecanism de scalare a AMF bazat pe prognoza incarcarii de control plane cu retele neuronale: LSTM (RNN) si DNN comparate (Sec. III-B).
- Datele sunt clasificate in 10 clase de incarcare (clasa corespunde numarului de instante AMF necesare); se prezice clasa incarcarii medii pentru urmatoarea perioada (10 minute) (Sec. III-B).
- NFVO foloseste RNN pentru a deriva numarul de AMF de implementat proactiv, inaintea cresterii de trafic; nu mai este nevoie de monitorizarea performantei VNF prin VNFM (Sec. III-C).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Benchmark al AMF cu OpenAirInterface in varianta emulata OAISIM (UE emulate, un eNodeB); functia rulata a fost MME din OAI EPC, folosita ca proxy pentru AMF; doua configuratii de VM: 1 CPU/1 GB si 2 CPU/2 GB (Sec. III-A).
- Date de antrenare: dataset Telecom Italia Big Data Challenge (SMS, apeluri, CDR la interval de 10 minute, doua luni); autorii presupun ca minim 10% din trafic este control plane si folosesc doar aceasta parte (Sec. III-B1).
- Retele implementate in TensorFlow; impartire 60% antrenare / 40% test (Sec. III-B3).
- Evaluarea mecanismului: simulator cu evenimente discrete in SimPy cu generator de trafic UE, eNodeB cu load balancing, VNF-uri AMF cu capacitate de 20 cereri de attach/s si NFVO; 48 de ore de sosiri; latenta de implementare a unei instante 60 s (Sec. IV).

## Experimente si metrici
- Benchmark AMF: UE acceptate si durata de attach in functie de numarul de cereri de attach pe secunda (Fig. 2).
- Acuratetea prognozei DNN vs LSTM (Fig. 3).
- Comparatie scalare bazata pe prag (scale-out la 80% din capacitate, scale-in sub 10%) vs scalare bazata pe RNN: numar de instante AMF vs trafic (Fig. 4, 6) si cereri de attach blocate (Fig. 5).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Fig. 2: configuratia 1 CPU/1 GB incepe sa respinga attach de la aproximativ 20 UE/s, configuratia 2 CPU/2 GB in jur de 35 UE/s; durata de attach creste exponential de la 20 UE/s (prima) si 40 UE/s (a doua) (Sec. III-A).
- Fig. 3: acuratete aproximativ 90% pentru LSTM si aproximativ 80% pentru DNN (Sec. III-B3).
- Fig. 4-5 (Sec. IV): la sarcina maxima RNN implementeaza pana la 8 instante, pragul pana la 7; la sarcina minima pragul are cel putin 2 instante, RNN cel putin 3; mecanismul bazat pe prag blocheaza mai multe cereri decat cel bazat pe RNN (numere exacte de cereri blocate: nedeclarate in text).

## Limitari declarate de autori
Concluzii: lucrul viitor vizeaza folosirea RNN antrenat pentru estimarea numarului de UPF necesare pentru data plane. Alte limitari explicite: nedeclarat. Textul mentioneaza ca benchmarkul foloseste MME din OAI EPC in locul AMF (Sec. III-A).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu - benchmark cu MME din OAI EPC ca proxy pentru AMF; mecanismul de scalare este evaluat in simulator SimPy (Sec. III-A, IV).
- UE reale sau emulate? emulate - OAISIM in benchmark; in simulator, UE generate dupa dataset (Sec. III-A, IV).
- digital twin al retelei? nu - nu este mentionat.
- prezice efectul unei actiuni inainte de a o aplica? nu - prezice incarcarea viitoare, nu efectul unei actiuni (Sec. III-B).
- executa actiuni automat (bucla inchisa)? da, in simulator - NFVO implementeaza instante AMF pe baza predictiei (Sec. III-C, IV); nu pe sistem real.
- multi-site / geo-redundanta / failover de baza de date? nu.
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat - evaluare pe split 60/40 al datasetului (Sec. III-B3).
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? partial - cereri de attach blocate si durata de attach (Fig. 2, 5); fara date de la UE reale.
- observa traficul la SCP / proxy? nu - SCP nu este mentionat; eNodeB-ul din simulator distribuie cererile intre instantele AMF (Sec. IV).
