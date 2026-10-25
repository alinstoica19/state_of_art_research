# Practice on fifth-generation core (5GC) network fault self-recovery based on a Digital Twin (2022)
Cheie: Zheng2022Dtselfrecovery . DOI/link: 10.12688/digitaltwin.17692.1 . Sursa textului: integral, PDF publicat, versiunea 1 (Digital Twin 2022, 2:18; include rapoartele de peer review): https://digitaltwin1.org/articles/2-18/v1
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Operatorul China Mobile Zhejiang are o retea complexa (2G-5G, mai multi furnizori); remedierea manuala a defectelor depinde de experienta personalului, iar sistemele inteligente existente se confrunta cu standardizare scazuta a datelor, esantioane insuficiente de defecte, costuri mari de testare, capabilitati end-to-end slabe, coordonare complexa si adaptabilitate/scalabilitate slaba. Se urmareste auto-recuperarea defectelor din 5GC (obiectivul China Mobile de autonomie L4 pana in 2025).

## Ce propun (metoda, pe scurt)
- Cadru de network digital twin cu straturi: retea fizica, twin, aplicatii, sistem de operare/management, securitate end-to-end.
- Modele de date dupa DAMA (data governance) pentru 5GC: model de echipament (static prin FTP, dinamic prin Kafka: alarme, performanta, loguri), model de serviciu, model de link.
- Vizualizare topologica: topologie pe straturi (Fig. 4) si topologie de eveniment pentru un scenariu de defect (Fig. 5, ex. pool de UPF).
- Capabilitati KaaS (knowledge-as-a-service): operatii atomice de O&M si mapare serviciu/sub-proces; simulare de testare prin apelare (dial test) cu elemente de retea twin construite pe modulul Open5GS (interfete N2/N3 gNodeB, N8/N15 AMF, N7/N10 SMF; Tabel 1), cu teste de conectivitate 7*24h prin acces punctual catre 5GC fizic; graf de cunostinte (Fig. 8) pentru inferenta lantului de propagare a defectului si cauza radacina (Fig. 9); evaluarea fezabilitatii disaster recovery din trafic si capacitate (Fig. 10).
- Bucla inchisa in patru etape: perception, analysis, decision-making, execution (Fig. 11), cu reparare "one-click" a elementului defect.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Aplicat pe reteaua 5GC a operatorului (retea fizica de productie, conform descrierii); twin-ul include elemente simulate bazate pe Open5GS (licenta AGPLv3). Date: inregistrari istorice ale defectelor 5GC pe 3 luni (Tabel 2, 10 incidente, martie-mai 2022); date si cod disponibile pe Zenodo (10.5281/zenodo.7052603 si 10.5281/zenodo.7003078). Numarul de UE, NF sau noduri nu este specificat.

## Experimente si metrici
Metrici: durata de descoperire, analiza, decizie, executie si durata totala a defectului (minute), pe 10 incidente inregistrate pe 3 luni (Tabel 2).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Medii pe 10 incidente (Tabel 2): descoperire 0.63 min; analiza 1.48 min; decizie 15.18 min; executie 3.21 min; durata totala a defectului 20.50 min. Textul reia: 0.63, 1.48, 15.18 si 3.21 minute pe etape.
- Rezumat/concluzii: detectie in 1 min, delimitare in 20 min, recuperare in 5 min; metoda "poate trata 98%" din defectele 5GC (Abstract, Conclusions).
- Legenda Fig. 11: cauza radacina localizata in 20 min; recuperare sau reparare one-click in 5 min.
- Statut peer review (pagina publicata): 1 aprobat cu rezerve, 1 neaprobat. Raportul neaprobat noteaza lipsa unei justificari pentru cifra de 98% si a tipurilor de defecte; raportul aprobat cu rezerve cere clarificari ale figurilor si exemple suplimentare.

## Limitari declarate de autori
Lucru viitor: explorarea mecanismului elementelor/echipamentelor de retea digitale, extinderea capabilitatilor de configurare si control la mai multe elemente, imbunatatirea detectiei in timp real, a fuziunii si delimitarii defectelor, si a procesarii non-destructive a defectelor (Conclusions).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? da partial - elemente twin AMF/SMF/UPF simulate pe baza Open5GS, testate contra 5GC fizic al operatorului (Applications, Tabel 1)
- UE reale sau emulate? nedeclarat; apelarile de test sunt generate de elementele twin (Fig. 7)
- digital twin al retelei? da - cadru de network digital twin (System framework)
- prezice efectul unei actiuni inainte de a o aplica? da, partial - fezabilitatea disaster recovery evaluata din trafic/capacitate inainte de executie (Fig. 10, 11); metoda de validare nedetaliata
- executa actiuni automat (bucla inchisa)? da - declarat "closed-loop self-recovery", reparare one-click in etapa de executie (Abstract, Fig. 11); gradul de automatizare per incident nedetaliat
- multi-site / geo-redundanta / failover de baza de date? nedeclarat; apare disaster recovery pe elemente de retea/pool UPF (Fig. 5, 10)
- evaluare prospectiva (predictie fixata inainte de experiment)? nu - evaluare pe inregistrari istorice pe 3 luni (Tabel 2)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - metrici la nivel de incident/retea (Tabel 2)
- observa traficul la SCP / proxy? nedeclarat; testele de apelare acopera interfete SBI (Tabel 1), fara SCP mentionat
