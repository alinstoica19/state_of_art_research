# A Graph Neural Network-Based Digital Twin for Network Slicing Management (2022)
Cheie: Wang2022Slicedt . DOI/link: 10.1109/tii.2020.3047843 . Sursa textului: integral, manuscris de autor depus in depozitul Univ. Bristol/figshare (TII-GNN-DT.pdf, 10 pagini): https://figshare.com/articles/journal_contribution/A_Graph_Neural_Network-based_Digital_Twin_for_Network_Slicing_Management/29776406
Sectiunea din plan: B . Tema: nedeclarat

## Problema (cum o formuleaza autorii)
Network slicing in 5G ridica provocari de management din cauza infrastructurii virtualizate si a cerintelor stricte de QoS; este necesar sa se monitorizeze reteaua si sa se genereze cu acuratete metrici E2E ale slice-urilor (Sec. I). Modelele analitice (teoria cozilor, network calculus) se bazeaza pe ipoteze simplificatoare, iar arhitecturile de invatare uzuale nu invata din structuri de graf non-euclidiene si generalizeaza greu pe topologii dinamice (Sec. I, II).

## Ce propun (metoda, pe scurt)
- Un digital twin (DT) al network slicing-ului bazat pe Graph Neural Network cu cadru inductiv GraphSAGE, care construieste o reprezentare virtuala in graf a retelei substrat si a slice-urilor si prezice latenta E2E per slice (Sec. III-IV).
- Starea unui nod agrega resursele VNF-urilor gazduite (Eq. 2-3); stari agregate pe calea sursa-destinatie a slice-ului dau latenta E2E (Algoritm 1).
- Antrenare cu loss Log-Cosh si optimizator Adam; dropout repetat la inferenta pentru distributie de predictii (Sec. IV).
- Trei utilizari: monitorizarea incalcarii SLA, evaluarea migrarii dupa caderi de legaturi, optimizare greedy a deplasarii (Sec. V-C).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Nu exista core 5G implementat; datele provin din conversia datasetului din [26] (matrici de trafic sursa-destinatie) in scenarii de slicing (Sec. V-A).
- Trei topologii: NSFNET (14 noduri, 42 legaturi, 10 slice-uri), GEANT2 (24 noduri, 74 legaturi, 30 slice-uri), retea sintetica (50 noduri, 276 legaturi, 50 slice-uri) (Sec. V-A).
- Implementare in TensorFlow si Stellargraph; 2000 pasi, mini-batch 64; K = 2; dimensiunea starii 256; dropout 0.3; learning rate initial 0.0005; (E1, E2) = (3,3) NSFNET, (6,4) GEANT2, (9,6) sintetic (Sec. V-A).
- Test de scalabilitate: 500 de grafuri combinate (de ex. GEANT2 cu 12000 noduri si 37000 legaturi); 30% din noduri eliminate la antrenare si reintegrate la evaluare, fara reantrenare (Sec. V-A).
- Etichetele (latente) pastreaza intarzierile de propagare predefinite din datasetul original (Sec. V-A).

## Experimente si metrici
- Acuratetea latentei E2E prezise vs latenta reala pe cele trei scenarii: mediana peste 30 de rulari, bare de eroare 95% (Fig. 4).
- Generalizare pe GEANT2 cu 10-100 slice-uri (pas 10) si 10 algoritmi de rutare nevazuti la antrenare, plus trafic de fundal; 550 perechi predictie-realitate din 10 experimente (Fig. 5).
- Transfer la o metrica noua (jitter) (Fig. 6).
- Aplicatii: monitorizare SLA la utilizare 30%-150% a resurselor (Fig. 7), caderea a 1-5 legaturi cu cai alternative prin shortest path (Fig. 8), optimizare greedy "Latency" vs "Efficiency" (Fig. 9).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Fig. 4: eroare sub 5% si varianta mica pe cele trei scenarii (Sec. V-B).
- Fig. 5: eroarea totala este mica, dar mai vizibila la latente mari (rare in antrenare) (Sec. V-B).
- Fig. 6: modelul de latenta converge in jur de 600 de pasi, metrica jitter in jur de 250 de pasi.
- Fig. 7: la utilizare de 90% latenta Slice 1 incalca SLA-ul; DT poate genera alerta.
- Fig. 8: latentele tuturor celor trei slice-uri cresc odata cu numarul de legaturi cazute (media a 5 experimente per punct).
- Fig. 9: optimizatorul greedy cauta solutii cand SLA-ul este incalcat; valorile numerice exacte nu sunt date in text.

## Limitari declarate de autori
Erorile pe latente mari sunt mai vizibile deoarece acestea sunt rare in antrenare; autorii indica un set de antrenare cu distributie mai larga a latentelor (Sec. V-B). Latentele din etichete pot fi mai mari decat cerintele aplicatiilor 5G (Sec. V-A). O sectiune separata de limitari: nedeclarat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu - date derivate din matrici de trafic ale unor topologii (Sec. V-A).
- UE reale sau emulate? nu se aplica - nu exista UE; trafic din dataset (Sec. V-A).
- digital twin al retelei? da - DT bazat pe GNN pentru slicing (Sec. IV).
- prezice efectul unei actiuni inainte de a o aplica? da - prezice latenta dupa migrarea slice-urilor la caderea de legaturi si evalueaza scenarii what-if (Sec. I, V-C).
- executa actiuni automat (bucla inchisa)? nu - optimizatorul greedy este o demonstratie in DT, fara aplicare pe retea (Sec. V-C).
- multi-site / geo-redundanta / failover de baza de date? nu pentru baze de date; caderi de legaturi si re-rutare simulate (Fig. 8).
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - latenta E2E per slice.
- observa traficul la SCP / proxy? nu - SCP nu este mentionat.
