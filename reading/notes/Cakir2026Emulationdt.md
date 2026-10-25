# Emulation Digital Twin Framework: Case Study on NGAP Attacks in 5G Control Plane (2026)
Cheie: Cakir2026Emulationdt . DOI/link: https://doi.org/10.1109/iccworkshops63917.2026.11586630 . Sursa textului: integral: PDF urcat de autor (Emulation_Digital_Twin_Framework_Case_Study_on_NGAP_Attacks_in_5G_Control_Plane.pdf)
Sectiunea din plan: A . Tema: digital twin
Autori: Lal Verda Cakir, Arsen Duzgun, Kubra Duran, Mehmet Ali Erturk, Berk Canberk (Edinburgh Napier University; Erturk si Istanbul University), Mehmet Ozdem (Turk Telekom). ICC 2026 Workshops; 6 pagini.

## Problema (cum o formuleaza autorii)
Autorii formuleaza trei provocari (Sectiunea I.A):
- Protocoalele de semnalizare din control plane-ul 5G, de exemplu NGAP, pot fi exploatate pentru DoS. Un DoS pe un NF afecteaza NF-urile co-localizate si se propaga.
- Mecanismele de detectie sunt evaluate mai ales pentru acuratete, offline, si nu la nivel de deployment, unde conteaza overhead-ul si latenta.
- Cadrele de emulare 5G cer multa interventie manuala, ceea ce impiedica analiza what-if iterativa si la scara.

Autorii mai observa ca DT-urile sunt folosite in principal ca metode predictive. Simularea ofera doar performanta teoretica, fara stivele software ale nodurilor (II).

## Ce propun (metoda, pe scurt)
Emulation Digital Twin (EDT) Framework, cu trei straturi (Fig. 1):
- **Emulation Layer:**
  - Containerlab gestioneaza NF-urile containerizate, UERANSIM emuleaza UE si gNB la nivel de protocol, iar core-ul este Open5GS extins.
  - Extensia Open5GS consta in "signalling hooks" modulare pe etapele de procesare a mesajelor: Message Parsing, State Machine Decision, Context Update (Fig. 2). Hook-urile trimit alarme catre DT.
- **Digital Twin Layer:**
  - reprezentare graf sincronizata, implementata cu networkx si expusa prin FastAPI. Campurile sunt Property, State, Alarm, Telemetry si Relationship.
  - detectie si mitigare in trei pasi:
    1. detectie pe semnaturi (praguri de frecventa, secvente), care declanseaza packet capture pe interfetele identificate;
    2. clasificare ML a pachetelor (benign/malitios);
    3. executarea mitigarii prin signalling hooks (III.B).
- **Orchestration Layer:**
  - Scenario Engine (teste in mai multe faze: baseline, injectie de atac, activarea mitigarii, post-analiza);
  - Twin Manager;
  - Topology Generator (YAML Containerlab, cu impairment-uri de latenta, jitter, pierderi);
  - Traffic Generator, Attack Generator, Experiment Manager (III.C).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Emulare cu Containerlab, UERANSIM si Open5GS extins, pe o masina AMD Ryzen 9 7900X cu 12 nuclee (IV).
- Atacul: DoS NGAP prin N2, catre AMF, cu volum mare de pachete cu UE-NGAP-ID corupt in timpul procedurii de inregistrare.
- Detectia ML foloseste metoda din [3]: retea hibrida TCN pentru secventa de fluxuri plus MLP pentru caracteristicile semantice ale IE-urilor.
- Numarul de UE si de NF nu este declarat.

## Experimente si metrici
- Patru configuratii: fara DT cu trafic benign; fara DT cu atac; cu DT cu trafic benign; cu DT cu atac.
- Metrici: throughput si latenta in data plane (Fig. 3); CPU si RAM; linii de cod necesare pentru experimente.
- Comparatie intre Open5GS pur, Open5GS + Containerlab si Open5GS + Containerlab + EDT (Fig. 4).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Atacul porneste la 15 s si scade throughput-ul si creste latenta utilizatorilor benigni (Fig. 3).
- Cu EDT, hook-urile declanseaza detectia, DT-ul valideaza semnatura pe o captura scurta de pachete, iar atacatorul este pus pe blacklist. Latenta si throughput-ul revin, dar nu complet la nivelul anterior: atacatorul continua sa genereze trafic si consuma resurse inainte de drop (IV).
- Numarul de linii de cod pentru experimente scade cu 81% (Fig. 4; Rezumat).
- Overhead-ul computational este de 0,42% (contributii, Sectiunea I.B). CPU-ul ramane relativ constant intre configuratii (Fig. 4).

## Limitari declarate de autori
Nu sunt declarate limitari explicite. Securitatea la nivel fizic este in afara scopului, de unde emularea la nivel de protocol cu UERANSIM (III.A). Lucrari viitoare: emulare distribuita si generare de scenarii cu AI (V).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - Open5GS extins cu signalling hooks (III.A).
- UE reale sau emulate?: emulate - UERANSIM (III.A).
- digital twin al retelei?: da - DT Layer cu reprezentare graf sincronizata cu emularea (III.B).
- prezice efectul unei actiuni inainte de a o aplica?: nu in sensul predictiei - EDT este un mediu what-if emulat in care se testeaza detectia si mitigarea fara reteaua live (III); nu se prezice efectul unei actiuni inainte de aplicarea ei in EDT.
- executa actiuni automat (bucla inchisa)?: da (in emulare) - blacklisting automat al atacatorului prin signalling hooks (III.B, IV).
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: da - throughput si latenta data plane pentru utilizatorii benigni (Fig. 3).
- observa traficul la SCP / proxy?: nu - observatia se face prin hook-uri in NF-urile Open5GS si capturi pe interfete (N2).
