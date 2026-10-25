# Assurance and Conflict Detection in Intent-Based Networking: A Comprehensive Survey and Insights on Standards and Open-Source Tools (2026)
Cheie: Gharbaoui2026Intentconflictsurvey . DOI/link: https://doi.org/10.1109/tnsm.2026.3651896 . Sursa textului: integral: versiunea publicata (IEEE TNSM vol. 23, 2026, pp. 1891-; licenta CC per Crossref; https://ieeexplore.ieee.org/ielx8/4275028/11319294/11334180.pdf)
Sectiunea din plan: C . Tema: bucle inchise (IBN assurance, survey)
Autori: Molka Gharbaoui, Filippo Sciarrone, Mattia Fontana, Piero Castoldi, Barbara Martini. IEEE Transactions on Network and Service Management, 2026.

## Problema (cum o formuleaza autorii)
Pe masura ce deployment-urile IBN cresc in scara, heterogenitate si dinamism, devine esential si tot mai greu sa asiguri alinierea continua intre comportamentul retelei si obiectivele utilizatorului. Lucrarea analizeaza tehnicile de asigurare (assurance) si de detectie a conflictelor in IBN (Rezumat).

## Structura si taxonomia propusa
- **Sectiunea II, fundal:**
  - fulfillment si verificare pentru rezolvarea conflictelor;
  - assurance la runtime, intent drift si conformitate;
  - verificarea intentiei (inainte de deployment) vs. validarea ei (la runtime) (Tabelul I).
- **Sectiunea III, metodologie PRISMA:**
  - textul mentioneaza 217 lucrari regasite, apoi "222 articole", din care 10 excluse, rezultand 212 analizate;
  - 94 de lucrari incluse final (Tabelul II, clasificate pe interogari).
- **Sectiunea IV:** survey-uri IBN existente.
- **Sectiunea V, intent assurance:** colectarea si analiza datelor, verificarea conformitatii intentiei, tehnici AI/ML, automatizare in bucla inchisa.
- **Sectiunea VI, detectia conflictelor:**
  - conflicte semantice (statice): inconsistente de sens sau scop intre intentii sau politici, detectate prin analiza statica la ingestie sau verificare;
  - conflicte operationale: obiective de performanta sau resurse incompatibile; unele detectate prin verificari de fezabilitate, altele la runtime, rezolvate prin optimizare sau adaptare in bucla inchisa;
  - abordari de detectie si rezolvare, rezumate in Tabelele III-V.
- **Sectiunea VII:**
  - standarde: IETF (YANG, NETCONF/RESTCONF, arhitectura SAIN pentru service assurance), ETSI (NFV MANO, ZSM, network slicing);
  - unelte open-source (ONAP s.a.), ordonate dupa maturitate.

## Lucrari/sisteme acoperite (cu numar)
94 de lucrari incluse dupa PRISMA (III.C).

## Directii deschise declarate
Sectiunea VIII:
- A. traducerea intentiilor;
- B. integrarea AI/ML (Tabelul VI);
- C. generalizare;
- D. stabilitatea buclelor de control: raspunsurile prea agresive pot produce oscilatii sau ajustari conflictuale, iar feedback-ul intarziat lasa incalcarile nedetectate;
- E. performanta: tehnicile de assurance sunt la inceput si nu ofera robustete;
- F. scalabilitate;
- G. interoperabilitate multi-domeniu;
- H. securitate si confidentialitate;
- I. standardizare: nu exista un limbaj de intentii acceptat universal. ETSI si IETF nu au standarde unificate pentru validarea si verificarea continua a intentiilor si pentru detectia conflictelor (VII.A).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu (survey).
- UE reale sau emulate?: nu.
- digital twin al retelei?: nedeclarat in sectiunile citite.
- prezice efectul unei actiuni inainte de a o aplica?: tema survey-ului - verificarea intentiei si a fezabilitatii inainte de deployment (II.C, VI).
- executa actiuni automat (bucla inchisa)?: tema survey-ului - automatizare in bucla inchisa (V.D) si stabilitatea ei (VIII.D).
- multi-site / geo-redundanta / failover de baza de date?: nu; interoperabilitatea multi-domeniu este o provocare (VIII.G).
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu.
- observa traficul la SCP / proxy?: nu.
