# Anomaly Detection and Failure Root Cause Analysis in (Micro) Service-Based Cloud Applications: A Survey (2022)
Cheie: Soldani2022Rcasurvey . DOI/link: https://doi.org/10.1145/3501297 . Sursa textului: integral: arXiv 2105.12378v1 (26 mai 2021; preprint al articolului din ACM Computing Surveys)
Sectiunea din plan: C . Tema: anomalii/RCA (microservicii, survey)
Autori: Jacopo Soldani, Antonio Brogi (University of Pisa). ACM Computing Surveys, 2022.

## Problema (cum o formuleaza autorii)
Aplicatiile multi-serviciu au adesea sute de servicii care interactioneaza. In ele este dificil sa detectezi defectele si sa intelegi daca un serviciu a cazut singur sau in cascada. Tehnicile de detectie a anomaliilor si de RCA sunt raspandite in literatura si tratate de obicei separat, ceea ce ingreuneaza construirea unui pipeline detectie -> RCA de catre operatori (Sectiunea 1).

## Structura si taxonomia propusa
- **Sectiunea 2:** terminologie.
- **Sectiunea 3, detectia anomaliilor**, pe trei clase:
  - log-based;
  - distributed tracing-based;
  - monitoring-based (KPI).
  - Metodele includ invatare nesupervizata, supervizata si verificari de SLO.
- **Sectiunea 4, RCA**, pe aceleasi trei clase:
  - pe loguri: analiza pe causality graph;
  - pe trace-uri: analiza vizuala, analiza directa, analiza pe topology graph;
  - pe monitorizare.
- **Tabelele 1-2** clasifica tehnicile dupa:
  - clasa si metoda;
  - tipul anomaliei (functionala sau de performanta);
  - granularitate (la nivel de aplicatie sau de serviciu);
  - artefactele de intrare (setup cost);
  - integrarea in pipeline;
  - tipul cauzei identificate (servicii, evenimente, KPI-uri) si daca cauzele sunt ordonate.
- **Discutie** (3.4, 4.4): compromisul instrumentare/cost; acuratetea, inclusiv false positive/negative la aplicatii care se schimba in timp; explicabilitate si contramasuri.
- **Constatare din 4.4.1:** cea mai frecventa abordare RCA reconstruieste un causality graph din loguri sau KPI-uri. Cu exceptia LOUD, aceasta se face aplicand algoritmul PC pe serii de timp.

## Lucrari/sisteme acoperite (cu numar)
97 de referinte in versiunea arXiv v1. Tehnicile sunt grupate in Tabelele 1 si 2; numarul exact de randuri nu a fost numarat aici.

## Directii deschise declarate
Sectiunea 6:
- comparatie cantitativa a tehnicilor pe aceleasi aplicatii de referinta si medii de rulare, in maniera lui Arya et al.;
- tehnici care functioneaza sub schimbari continue (release-uri continue, migrari de servicii), de exemplu prin continual learning, in locul re-antrenarii sau al actualizarilor manuale;
- tehnici "explainable by design";
- recomandarea de contramasuri, de exemplu circuit breakers, bulkheads sau scalare preventiva pe baza predictiei degradarii.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu (survey despre aplicatii cloud multi-serviciu, nu telecom).
- UE reale sau emulate?: nu.
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu.
- executa actiuni automat (bucla inchisa)?: nu - contramasurile automate sunt identificate ca problema deschisa (4.4.4, 6).
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu.
- observa traficul la SCP / proxy?: nu (unele tehnici folosesc interactiunile monitorizate dintre servicii sau distributed tracing).
