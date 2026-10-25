# Intent-driven Closed Loops for Autonomous Networks (2021)
Cheie: Gomes2021Intentloops . DOI/link: https://doi.org/10.13052/jicts2245-800x.929 . Sursa textului: integral: PDF editor (River Publishers, open access "diamond")
Sectiunea din plan: C . Tema: intent / bucle inchise ZSM / standarde
Autori: Pedro Henrique Gomes, Magnus Buhrgard, Janos Harmatos, Swarup Kumar Mohalik, Dinand Roeland, Jorg Niemoller (Ericsson Research). Journal of ICT Standardization, vol. 9, nr. 2, 2021 (primit noiembrie 2020, publicat iunie 2021). Autorii o numesc "position paper".

## Problema (cum o formuleaza autorii)
- ETSI ZSM ofera componente standardizate pentru crearea, executia si guvernanta mai multor bucle inchise (CL) intre domenii de management (MD). Specificatia ZSM009-1 acopera guvernanta instantelor de bucla, dar instantierea si operarea coordonata si optima a mai multor bucle, inclusiv comunicarea dintre ele, sunt lasate implementarii (Rezumat, 1).
- Solutiile de automatizare bazate pe politici nu sunt suficient de flexibile pentru complexitatea 5G (slicing, cloud-native, multi-domeniu) (1).
- Coordonarea mai multor bucle este o problema deschisa in telecom; sistemele sunt stocastice si greu de modelat pentru control sau teoria jocurilor (6).

## Ce propun (metoda, pe scurt)
- **Intentiile ca mecanism universal de comunicare** intre nivelurile de management si intre MD-uri, pentru coordonarea ierarhiilor de bucle inchise (5).
- **Specificarea formala a intentiilor** (4.3-4.5): RDF/RDFS/OWL, serializare Turtle. O clasa Intent, cu asteptari (Expectation) formate din tinte (ManagedEntities) si parametri. Exemplu pentru un serviciu URLLC dupa GSMA NEST: disponibilitate 99,999, viteza dispozitivului 2, throughput DL/UL per UE 100.000, QoS-ul slice-ului 82, densitate de 1000 UE.
- **Functia de tratare a intentiilor** (4.6, Fig. 5-6): inchide diferenta dintre starea retelei si starea dorita, cu decizie, optimizare si rezolvarea conflictelor; ierarhica, per nivel si per domeniu; raporteaza progresul catre sursa intentiei.
- **Trei operatii de ciclu de viata** (4.7):
  - delegare: descompunerea si trimiterea intentiei catre MD-uri, care o pot accepta sau respinge;
  - raportare: catre handler-ul care a delegat;
  - escaladare: cand MD-ul nu poate indeplini intentia (resurse sau cunostinte insuficiente) sau are nevoie de o judecata intre mai multe solutii; urmeaza decizii in handler-ul superior.
- **In ZSM** (5): functia de tratare a intentiilor ca producator si consumator al unui nou "intent handling MnS" in E2E MD si in toate MD-urile, conectata la buclele inchise prin CL Governance MnS (ZSM009-1). Intentiile sunt stocate cu Data services.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Nu exista implementare sau evaluare. Exemplul este ilustrativ (5, Fig. 8): trei MD-uri (RAN, transport, core) si trei niveluri de bucle. Intentia URLLC E2E este descompusa in intentii de resurse per MD. De exemplu, intentia pentru transport adauga un buget de intarziere a pachetelor de 5 si o rata de eroare a pachetelor; transportul re-deleaga catre doua bucle de nivel inferior.

## Experimente si metrici
- Nedeclarat (lucrare de pozitie).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Fara rezultate cantitative. Autorii sustin (conjectura) ca intentiile, impreuna cu cele trei operatii (delegare, escaladare, raportare), sunt suficiente pentru interactiunile dintre MD-urile autonome si pot creste autonomia (5). Conceptele se pot aplica si la fulfilment si fault management.

## Limitari declarate de autori
- Implementarea solutiei si interoperabilitatea bazata pe meta-modele de intentie si functii standardizate de tratare a intentiilor raman de investigat (7).
- Capabilitatile propuse sunt candidate pentru standardizare viitoare in ETSI ZSM sau alte grupuri (7).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - lucrare conceptuala; core-ul apare ca MD in exemplu (5).
- UE reale sau emulate?: nedeclarat.
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu.
- executa actiuni automat (bucla inchisa)?: da (conceptual) - bucle inchise conduse de intentii, cu delegare, raportare si escaladare (4.7, 5); nu este implementat.
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu.
- observa traficul la SCP / proxy?: nu.
