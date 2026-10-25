# Enhanced Open-Source NWDAF for Event-Driven Analytics in 5G Networks (2026)
Cheie: Daniel2026Opennwdaf . DOI/link: arXiv:2601.01838 . Sursa textului: integral, arXiv v1 (5 ian 2026): https://arxiv.org/pdf/2601.01838 (lucrare cu copyright IFIP 2025, IFIP Networking)
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Implementarile NWDAF existente sunt in mare parte proprietare, iar cele open-source nu ofera suport complet pentru subscriptie si notificare de evenimente end-to-end (rezumat). In Free5GC, desi exista unele interfete de event exposure, lipseste un mecanism complet de notificare in timp real, iar AMF si SMF nu suporta nativ subscriptii la evenimente (Sec. I). Implementarile NWDAF open-source sunt descrise ca limitate, adesea la colectare pasiva de metrici. Datele operationale reale raman in sisteme proprietare, iar simularea comportamentului real (analitica si mobilitate) este o provocare (Sec. I).

## Ce propun (metoda, pe scurt)
Un NWDAF open-source integrat in Free5GC (Sec. III):
- Extinde AMF si SMF cu event exposure (Namf_EventExposure, Nsmf_EventExposure) si cu un handler propriu de notificare, "SendEventNotification()", care potriveste evenimentul cu subscriptiile active si trimite raportul la URI-ul abonatului. AMF: inregistrare/dezinregistrare UE, handover, stare de conectivitate, raportare locatie, prezenta in zona, reachability. SMF: stabilire/eliberare sesiune PDU, rapoarte de volum de trafic, schimbari QoS, schimbari de cale UP.
- NWDAF se inregistreaza la NRF, citeste dintr-un fisier YAML lista de evenimente, se aboneaza prin modulul consumer, stocheaza in baza de date si anuleaza abonarea la oprire. Construit pe implementarea NWDAF pentru Free5GC a lui Kim et al. (Sec. III-B); contributia: modulul "service", mecanismul de colectare si modelele de predictie.
- Model de mobilitate bazat pe activitati (ABMM) in UERANSIM: locatii (coordonate, timp de stationare ~ N(mu, sigma^2)), cinci categorii de timp ale zilei (dimineata, pranz, dupa-amiaza, seara, noapte), esantionare a tipului de activitate cu penalizare a activitatii curente, viteza v0 ~ U(vmin, vmax) (Sec. III-C).
- Modul ML (Python) care prezice celula gNB tinta a urmatorului handover, din istoricul UE.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Free5GC (core), UERANSIM (gNB si UE simulate), NWDAF propriu in Go cu modul ML Python si baza de date (Fig. 1, 2). Testbed emulat/simulat, fara RAN sau UE fizice.
- Desfasurare de doua saptamani: 4 gNB virtuale (TAC distinct, formatie patrata, raza de acoperire simulata 120 unitati, prag semnal -120 dBm, implicit UERANSIM), 4 UE virtuale: trei se ataseaza/detaseaza dinamic, unul ramane conectat continuu (Sec. IV, Fig. 4).
- Date: generate de modelul de mobilitate propriu; dataset si cod publicate (https://github.com/HenokDanielbfg/5g-testbed-conference).
- Predictie: set de date impartit 70% antrenare / 30% test; caracteristici: SUPI, ultimele doua celule vizitate, perioada zilei, coordonatele (x, y) ale celulei curente, frecventa vizitarii celulei in acea perioada (Sec. IV-B).

## Experimente si metrici
- Comportament de inregistrare, tranzitii de stare si handover pe doua saptamani: durate in stare activa/inactiva, numar UE active pe zi, timp mediu pana la handover pe celula, rute de handover (Fig. 5a-c).
- Latenta de subscriptie si de notificare, utilizare CPU si memorie a NWDAF.
- Compararea a patru clasificatori pentru celula urmatorului handover: Random Forest, Gradient Boosting, K-Nearest Neighbors, Decision Tree; metrica: acuratete (Sec. IV-B).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Toate incercarile de inregistrare si dezinregistrare au reusit (Sec. IV-A).
- Stare activa in medie 100-102 minute; stare inactiva tipic 37-40 minute (Sec. IV-A). Sesiunea continua cea mai lunga: 9000 s (2.5 ore).
- Activitate ridicata in jurul orei 11:00 si intre 14:00 si 17:00; handover-urile cele mai frecvente la mijlocul zilei si la inceputul serii (Sec. IV-A, Fig. 5a). Un gNB apare ca punct dominant de trafic.
- Subscriptiile NWDAF confirmate de AMF si SMF in aprox. 10 ms; notificarile primite si procesate in aprox. 109 ms dupa eveniment (Sec. IV-A).
- NWDAF: 0.06% din CPU si 0.17% din memoria sistemului (27 MB RAM) (Sec. IV-A).
- Acuratete predictie handover: Gradient Boosting 80.65% (n_estimators=100, max_depth=9, learning_rate=0.05), Random Forest 80.24%, Decision Tree 80.11%, KNN 79.03% (Sec. IV-B).
- Valorile din Fig. 5b-c (timp mediu pana la handover, numar de handover-uri pe ruta) sunt doar in figura.

## Limitari declarate de autori
- Setup-ul simuleaza un tipar de mobilitate controlat; modele mai realiste pot fi adaugate de altii pentru stress-test (Sec. IV-A).
- NWDAF suporta momentan subscriptii doar la evenimente AMF si SMF (Sec. III-B).
- Directii viitoare declarate: mai multe categorii de evenimente, aplicatii peste NWDAF (predictie de trafic, detectie de anomalii), interfete de intentie cu NLP, integrare in platforme precum SLICES-RI pentru scenarii distribuite geografic (Sec. V).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? da - Free5GC extins cu event exposure AMF/SMF si NWDAF (Sec. III-A, III-B)
- UE reale sau emulate? emulate - UE virtuale in UERANSIM cu model de mobilitate propriu (Sec. III-C, IV)
- digital twin al retelei? nu - nu este mentionat
- prezice efectul unei actiuni inainte de a o aplica? nu - prezice celula urmatorului handover, nu efectul unei actiuni; nu se aplica actiuni (Sec. IV-B)
- executa actiuni automat (bucla inchisa)? nu - NWDAF colecteaza, stocheaza si prezice; nicio actiune de control descrisa; se afirma doar ca predictia poate informa alocarea proactiva (Sec. III-B, IV)
- multi-site / geo-redundanta / failover de baza de date? nu - un singur testbed; SLICES-RI mentionat doar ca directie viitoare (Sec. V)
- evaluare prospectiva (predictie fixata inainte de experiment)? nu - predictia e evaluata offline pe un split 70/30 al datasetului colectat (Sec. IV-B)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? da - inregistrari/dezinregistrari reusite, durate de stare, handover-uri per UE (Sec. IV-A)
- observa traficul la SCP / proxy? nu - NWDAF primeste notificari direct de la AMF/SMF prin event exposure (Sec. III-B); SCP nu este mentionat
