# Deep Learning-Based Modeling of 5G Core Control Plane for 5G Network Digital Twin (2024)
Cheie: Tao2024Corecontrolplane . DOI/link: 10.1109/tccn.2023.3324634 . Sursa textului: arXiv v2 (19 Oct 2023), https://arxiv.org/pdf/2302.06980 (versiunea arXiv poate diferi de cea publicata; antetul indica IEEE TCCN vol. 15 no. 1, august 2023)
Sectiunea din plan: A
## Problema (cum o formuleaza autorii)
Digital twin-urile 5G existente sunt in mare parte pentru optimizare si planificare de resurse; putine modeleaza functiile core, iar acelea se bazeaza direct pe proiecte open source (ex. Free5GC), care difera de retelele fizice (versiuni de protocol, configuratii) si cer dezvoltare suplimentara. Replicarea prin programare a unei retele fizice heterogene este spusa a fi lenta si laborioasa. Autorii cauta o abordare data-driven compatibila cu retele fizice diferite, concentrata pe control plane (user plane doar transporta traficul datorita CUPS).
## Ce propun (metoda, pe scurt)
- Analogie cu sisteme de dialog NLP: semnalizarea intre user plane si control plane (interfetele N1, N2, N4) vazuta ca dialog; modelul primeste mesajul de semnalizare uplink si genereaza autoregresiv raspunsul (mesajele downlink) pana la un token de sfarsit.
- Doua arhitecturi: state-based (stare ascunsa h actualizata dupa fiecare interactiune, Ec. 2-3) implementata ca 5GC-Seq2Seq (encoder-decoder LSTM), si signaling-based (raspuns pe baza mesajelor anterioare, Ec. 4) implementata ca 5GC-former (decoder Transformer cu masked multi-head attention).
- Conversie reversibila mesaj de semnalizare <-> vector de lungime limitata: decodare cu Wireshark, tabel cu o coloana per information element (IE), dictionare per coloana, iar IE-urile cu domeniu larg de valori (type II: ID-uri, IE de autentificare) sunt inlocuite cu valori relative (cel mult n_max, aici 8) printr-o lista de mapare (Alg. 1, 2). IE-urile care cer cunostinte din afara retelei neuronale (autentificare, alocare ID, verificare IMSI de catre UDM) sunt alocate/calculate dupa reguli prestabilite la refacerea mesajului.
- Loss si metrici redefinite pentru clasificare multi-clasa multi-label pe IE-uri (Ec. 20-24).
## Setup experimental (testbed real / emulare / simulare; unelte: Open5GS, free5GC, OAI, UERANSIM, ns-3, Kubernetes...; scara: nr. UE, NF, noduri; date: trafic real, trace-uri, sintetice)
- Semnalizare 5GC capturata (pcap) pe interfetele N1, N2, N4 cu un tester de retea Spirent C50 care genereaza comportamente UE si proceduri (registration, deregistration, authentication, handover, PDU session establishment/modification/release); numarul si intervalul sesiunilor per utilizator urmeaza o distributie Poisson; monitorizarea e pasiva (Sec. III.A). Nu sunt mentionate Open5GS/free5GC/UERANSIM/OAI ca baza experimentala (apar doar in related work).
- Set de date: 90.766 mesaje de semnalizare: 20,18% registration, 14,98% deregistration, 41,32% PDU session, 5,93% handover intra-AMF, 11,34% handover inter-AMF, 5,24% authentication; n_IE = 676; proceduri intercalate artificial (inclusiv mai multi utilizatori concurenti) (Sec. V.A). Impartire train/val/test 3:1:1, fara amestecare in interiorul secventelor (Sec. III.C).
- Hardware/software: PC i7-12700KF, 32 GB RAM, GPU RTX 3080, Python 3.9, PyTorch 1.10 (Sec. V.A). Hiperparametri in Tabel I: dimensiune model 200, 6 sublayers, 4 capete, FFN 400, Adam (0.9, 0.99, 1e-8), batch 8, dropout 0.1, learning rate 0.0001, early stopping cu patience 20.
## Experimente si metrici
- Precision, recall, F1 la nivel de IE (valoarea 0 = IE absent = esantion negativ), medii peste mesajele valide; si separat pe IE-uri type II (Tabel II, scenariu UE unic).
- F1 in functie de numarul de UE concurente, 1 la 5 (Tabel III).
- Curbe de loss (Fig. 13, 14), timp de antrenare, exemplu de predictie pe o procedura de handover (Tabel IV, Fig. 15) si hartile de atentie (Fig. 16).
## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Tabel II (UE unic), Overall: 5GC-Seq2Seq precision 99.99705%, recall 99.99732%, F1 99.99719%; 5GC-Former 99.99917% / 99.99917% / 99.99917%. Type II: Seq2Seq 99.95568% / 99.95976% / 99.95771%; Former 99.98785% pentru toate trei.
- Tabel III, F1 (S = Seq2Seq, F = Former), concurenta 1/2/3/4/5: S Overall 99.997% / 99.65% / 99.59% / 99.34% / 99.18%; F Overall 99.999% / 99.89% / 99.81% / 99.72% / 99.57%; S Type II 99.958% / 96.16% / 95.27% / 91.91% / 89.43%; F Type II 99.988% / 99.10% / 98.10% / 97.04% / 95.33%.
- Timpul de antrenare al 5GC-former este 1/12 din cel al 5GC-Seq2Seq pe aceleasi date (Sec. V.C).
- Exemplu (Tabel IV): dupa registration si 3 sesiuni PDU, un handover request declanseaza 4 iteratii de predictie pana la tokenul de sfarsit (Fig. 15).
## Limitari declarate de autori
- 5GC-Seq2Seq: performanta slaba cu UE concurente si nevoie de timp mare de antrenare (lipsa paralelismului). 5GC-former: trebuie pastrate mesajele anterioare si are complexitate computationala mare, deci nepotrivit pentru scenarii cu raspuns extrem de rapid (Sec. V.D).
- Schema curenta cere etichetare/reguli pentru IE-uri cu cunostinte a priori (autentificare, alocare ID); lucru viitor: legaturi intre modelele DL si bazele de date din 5G core, transfer learning intre retele fizice, structuri mai rapide si mai precise (Sec. VI).
## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu - core-ul este modelat de retele neuronale antrenate pe semnalizare capturata; ce core a produs capturile nu este precizat (Sec. III.A, V.A)
- UE reale sau emulate? emulate - tester Spirent C50 genereaza comportamentul UE (Sec. III.A)
- digital twin al retelei? da - tinta declarata: modelarea control plane-ului 5G core pentru un 5G network DT; nu e prezentat un twin complet (Sec. I, II)
- prezice efectul unei actiuni inainte de a o aplica? nu - modelul prezice raspunsul de semnalizare al core-ului la un mesaj uplink, nu efectul unei actiuni de management (Sec. II)
- executa actiuni automat (bucla inchisa)? nu - nedescris; modelul doar raspunde cu semnalizare predicta (Sec. IV-V)
- multi-site / geo-redundanta / failover de baza de date? nu - nu este abordat; lucru viitor: conectarea modelelor la baze de date ale core-ului (Sec. VI)
- evaluare prospectiva (predictie fixata inainte de experiment)? nu - evaluare pe set de test separat din aceeasi captura (3:1:1), nu predictie fixata dinainte (Sec. III.C, V.D)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - metrici la nivel de IE din mesaje; F1 e raportat si pe numar de UE concurente (Sec. V.B, V.D, Tabel III)
- observa traficul la SCP / proxy? nu - captura pe interfetele N1, N2, N4, nu SBI/SCP (Sec. III.A)
