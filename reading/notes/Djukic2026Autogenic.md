# From Agentic to Autogenic Network Management for AI-Native 6G and Beyond: A Standards Perspective (2026)
Cheie: Djukic2026Autogenic . DOI/link: https://doi.org/10.1109/mnet.2026.3711903 . Sursa textului: integral: arXiv 2607.06786v1 (7 iulie 2026)
Sectiunea din plan: C . Tema: agenti AI / management autonom / standarde
Autori: Petar Djukic, Sudipta Acharya, Takai Eddine Kennouche, Burak Kantarci (Nokia Bell Labs; Nokia Technology Standards; University of Ottawa). IEEE Network (articol de tip magazine).

## Problema (cum o formuleaza autorii)
- In 6G AI-native, ML va fi in toate nivelurile si interfetele. Proliferarea software-ului ML creeaza dependente ascunse: principiul "Changing Anything Changes Everything" (CACE), unde o schimbare minora a unui model poate degrada tot sistemul (I.A, I.C).
- Exemplu folosit in toata lucrarea: consumul excesiv de energie in RAN cauzat de drift-ul modelului ML de scheduling MAC. Ciclul detectie -> diagnostic -> reantrenare -> validare -> deployment -> monitorizare trebuie repetat continuu, iar supravegherea umana nu scaleaza (I.A).
- Autorii sustin ca autonomia la scara cere un plan de management care sa genereze software nou de automatizare, sa-i valideze corectitudinea si sa-si modifice propria structura la runtime (I).

## Ce propun (metoda, pe scurt)
- **Spectrul componentelor AI** (II, Fig. 1-2), aliniat nivelurilor de autonomie L0-L5 (TM Forum):
  - programate (L0-L1);
  - de invatare, adica predictii ML (L2-L3);
  - ghidate: agenti bazati pe Large AI Models (LAM) care se autoprogrameaza, cu om in bucla (L4);
  - recursive: agenti cu autoprogramare si auto-reflectie, care valideaza fara aprobare umana (L5 si peste).
- **Patru capabilitati "autogenice"** (III.B): self-programming, self-reflection, self-orienting (generarea de obiective noi), self-architecting (modificarea structurii la runtime).
- **Arhitectura de referinta cu sapte subsisteme** (III.C, Fig. 3): Execution (sistemul gestionat), Monitoring, Analysis, Planning, Control (bucle AADE), Management (guverneaza evolutia sistemului) si Peering (coordonare externa), pe o platforma suport. Subsistemele sunt separate pe scale de timp.
- **Sase principii de design** (III.E): complexitate minima viabila, management cu scop dublu, reutilizare in loc de reinventare, rezilienta proprie, pregatire pentru fallback, constructie doar din componente.
- **Pentru 6G** (III.F): RAN si core sunt sistemele gestionate.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Nu exista experimente. Demonstratia este conceptuala, pe cele 11 scenarii cu valoare mare ale TM Forum (Tabelul I, Fig. 4) si pe un caz de fault management detaliat (Fig. 5).

## Experimente si metrici
- Nedeclarat (articol de pozitie/arhitectura, fara evaluare cantitativa).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Fara rezultate numerice.
- **Cazul de fault management** (IV.B, Fig. 5): intentia operatorului ("Reduce excessive RAN energy consumption while preserving service quality") este preluata de Planner (Intent Handler). Subsistemul Management creeaza dinamic agentii Analyst (RCA), Executor (remediere, configuratie), Coordinator (change management) si Critic (validarea rezultatului si feedback).
- **Tranzitia de la componente ghidate la recursive** (IV.C) se face prin "solution banking": solutiile validate de oameni sunt stocate intr-un depozit de incredere si refolosite automat pentru defecte recurente; defectele noi cer in continuare supraveghere umana.

## Limitari declarate de autori
- Self-orienting si self-architecting sunt "active research frontier". Prototipurile actuale functioneaza doar in domenii restranse, iar LAM-urile nu au garantii formale de corectitudine (III.D).
- Cazul de fault management este o rezolvare idealizata. Interoperabilitatea dintre furnizori cere standarde pentru interfetele dintre agenti (IV.B).
- Directii (V, VI):
  - digital twins ca medii sigure de evaluare a strategiilor generate autonom, inclusiv o "digital twin factory" (agent care sintetizeaza modele si middleware de colectare a datelor);
  - interfete constranse formal, cu autorizare, validare si rollback;
  - validatori externi si validare la scara mare pe RAN, core si scenarii cross-domain;
  - autoorientarea ridica probleme de aliniere, stabilitate si siguranta.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - arhitectura conceptuala; RAN si CN sunt mentionate ca sisteme gestionate (III.F).
- UE reale sau emulate?: nedeclarat.
- digital twin al retelei?: discutat ca directie - DT ca mediu sigur de evaluare si "digital twin factory" (V.A); nu este implementat.
- prezice efectul unei actiuni inainte de a o aplica?: discutat - evaluarea strategiilor in DT inainte de productie (V.A, VI); nu este implementat.
- executa actiuni automat (bucla inchisa)?: da (conceptual) - bucle AADE si agenti Executor/Critic, cu om in bucla pentru componentele ghidate (III, IV).
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu.
- observa traficul la SCP / proxy?: nu.
