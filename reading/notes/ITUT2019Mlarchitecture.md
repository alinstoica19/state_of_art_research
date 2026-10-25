# Architectural framework for machine learning in future networks including IMT-2020 (ITU-T Y.3172) (2019)
Cheie: ITUT2019Mlarchitecture . DOI/link: https://www.itu.int/rec/T-REC-Y.3172 (Recomandarea ITU-T Y.3172, editia 1.0, aprobata 2019-06-22, Study Group 13) . Sursa textului: integral, PDF-ul Recomandarii Y.3172 (06/2019) de pe itu.int (34 pagini)
Sectiunea din plan: Standarde . Tema: arhitectura ML in retele (IMT-2020)

## Problema (cum o formuleaza autorii)
Cl. 1 si 6: Recomandarea specifica un cadru arhitectural pentru machine learning (ML) in retele viitoare, inclusiv IMT-2020. Cl. 6 enumera provocari ale integrarii ML: (A) natura eterogena a functionalitatilor ML si cerinte variate; (B) foi de parcurs de evolutie nealiniate intre ML si retea; (C) costul integrarii in termeni de impact arhitectural; (D) mecanisme de management diferite pentru functionalitati ML si pentru network functions (NF), ceea ce ar perturba operarea. Domeniul declarat: un set de cerinte arhitecturale, componentele necesare, cadrul de integrare si ghiduri pentru aplicare pe retele-suport specifice tehnologiei.

## Ce propun (metoda, pe scurt)
- Cl. 7: cerinte de nivel inalt grupate in cinci seturi: corelare a datelor intre niveluri (REQ-ML-COR-001..003), deployment (REQ-ML-DEP-001..004), interfete (REQ-ML-INT-001..004), specificatii declarative (REQ-ML-SPEC-001..004), management (REQ-ML-MNG-001..005).
- Cl. 8.1: trei componente arhitecturale: ML pipeline, ML function orchestrator (MLFO), ML sandbox.
- Cl. 8.2: arhitectura de nivel inalt cu trei subsisteme (management, ML pipeline, ML sandbox) si puncte de referinta numerotate 1-9 (Fig. 4).
- Cl. 8.3: ghiduri de realizare pe retele-suport; Apendicele I: exemplu de realizare pe o retea IMT-2020; Apendicele II: maparea componentelor pe cerinte.

## Clauze relevante (numar clauza - ce defineste)
- 3.2: termeni definiti: machine learning, MLFO, ML model, ML overlay (model de deployment slab cuplat, cu integrare si management standardizate), ML pipeline, ML sandbox (mediu in care modelele ML pot fi antrenate, testate si efectele lor asupra retelei evaluate), ML underlay network.
- 7.1 (REQ-ML-COR-001..003): corelarea datelor din surse multiple (ex. UE, AN, CN, AF); suport pentru mai multe tehnologii si interfatare cu entitati non-IMT-2020; instantiere distribuita a functionalitatilor ML pe mai multe niveluri.
- 7.2 (REQ-ML-DEP-001..004): puncte de interactiune intre functii ML si NF-urile retelei-suport, independent de aplicatia ML; deployment impartit sau combinat; plasare flexibila coordonata cu management and orchestration; incarcare de modele/configurari intr-un mediu ML in rulare. Nota la DEP-001: iesirea ML poate fi politici sau configurari, a caror aplicare poate fi controlata de politicile operatorului.
- 7.3 (REQ-ML-INT-001..004): transfer de modele, date si antrenare/testare intre niveluri; interfete catre NF-uri specifice; partajare distribuita a datelor intre niveluri.
- 7.4 (REQ-ML-SPEC-001..004): specificatii declarative ale aplicatiilor ML traductibile in functionalitati ML, cu constrangeri de timp si de resurse; specificare de catre terti.
- 7.5 (REQ-ML-MNG-001..005): selectia modelului ML la set-up; antrenare si actualizare fara impact asupra retelei; monitorizarea efectului ML asupra retelei si actualizarea modelelor/politicilor fara impact (nota: exemplu de imbunatatire continua a fluxurilor de fault recovery automat, cu root cause analysis); orchestrare a tuturor functionalitatilor ML, cu reconfigurare cand performanta scade sub un prag predefinit; chaining flexibil.
- 8.1: noduri ale unui ML pipeline: SRC (sursa de date, ex. UE, SMF, AF), C (collector), PP (preprocessor), M (model), P (policy), D (distributor), SINK (tinta iesirii ML). Nodul P aplica politici asupra iesirii modelului, de exemplu pentru a minimiza impactul aplicarii in reteaua live (nota 5: ex. upgrade-uri majore doar noaptea sau la trafic scazut). MLFO gestioneaza si orchestreaza nodurile pipeline-ului pe baza unui "ML Intent" si/sau a conditiilor dinamice din retea; selecteaza si reselecteaza modelul ML dupa performanta; raspunde de plasare si chaining. ML Intent este o descriere declarativa a unei aplicatii ML, fara NF-uri specifice tehnologiei. ML sandbox este un domeniu izolat in care pipeline-uri sunt antrenate, testate si evaluate inainte de deployment in reteaua live, cu date din retele-suport simulate si/sau live.
- 8.1 (aspecte de suport): Service-based architecture (SBA, cu referire la ETSI TS 129 500) poate fi folosita pentru interfatarea functionalitatilor ML cu retelele-suport (reale sau simulate) si intre nodurile pipeline-ului; pentru NF-uri fara SBA se folosesc protocoale specifice.
- 8.2: subsistem de management (MLFO si functii de management si orchestrare, ex. Y.3111); subsistem ML pipeline (suprapus peste infrastructura existenta, poate fi distribuit pe UE, AN, CN); subsistem ML sandbox (permite operatorilor sa studieze efectul iesirilor ML inainte de a le aplica pe retele live; primeste feedback de la functiile de management).
- 8.3: ghiduri: instantierea nodurilor de catre MLFO, interfatare prin SRC si SINK, management, antrenare si evaluare in sandbox.
- 9: securitate: se aplica cerintele generale de securitate IP; este obligatorie prevenirea accesului neautorizat si a scurgerilor de date dintr-un ML pipeline.
- Apendice I: exemple de pipeline-uri pe o retea IMT-2020, inclusiv decizii de tip SON sau closed loop pentru alocarea resurselor (Fig. I.1); Apendice II: mapare componente - cerinte.

## Entitati, servicii si parametri definiti
Entitati: ML pipeline (noduri SRC, C, PP, M, P, D, SINK), MLFO, ML sandbox, ML Intent, ML overlay/underlay, puncte de referinta 1-9 (1,2 intre retele-suport simulate si pipeline din sandbox; 3 sandbox-pipeline; 4 pipeline-retea-suport; 5,6 management-pipeline/sandbox; 7 MLFO-alte functii de management; 8,9 intre noduri pipeline de pe niveluri diferite). Nu sunt definiti parametri numerici; cerintele sunt formulate cu "is required to" / "is recommended" / "can optionally" (cl. 5).

## Limitari declarate de autori
Cl. 8.2 nota 2: punctele de referinta dintre functiile de management si NF-urile retelei-suport sunt in afara domeniului Recomandarii. Apendicele I si II sunt marcate ca informative. Recomandarea este voluntara (Foreword).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din document)
- core 5G implementat (nu model)? nu se aplica - specificatie arhitecturala, fara implementare.
- UE reale sau emulate? nedeclarat.
- digital twin al retelei? nu este folosit termenul; ML sandbox foloseste "simulated ML underlay networks" (cl. 8.1, 8.2).
- prezice efectul unei actiuni inainte de a o aplica? sandbox-ul permite studierea efectului iesirilor ML inainte de aplicarea pe retele live (cl. 8.2).
- executa actiuni automat (bucla inchisa)? nodul SINK actioneaza asupra iesirii ML; Apendice I mentioneaza "closed loop decisions" privind alocarea resurselor; aplicarea poate fi controlata prin nodul P (cl. 8.1, App. I).
- multi-site / geo-redundanta / failover de baza de date? nedeclarat; pipeline distribuit pe mai multe niveluri UE/AN/CN (cl. 7.1, 8.2).
- evaluare prospectiva? nu se aplica.
- rezultat masurat la nivel de utilizator? nu se aplica.
- observa traficul la SCP / proxy? nedeclarat; SCP nu este mentionat in text (UPF si SMF apar ca exemple de surse/puncte de integrare).
