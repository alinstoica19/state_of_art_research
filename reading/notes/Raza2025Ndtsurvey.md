# A comprehensive survey of Network Digital Twin architecture, capabilities, challenges, and requirements for Edge-Cloud Continuum (2025)
Cheie: Raza2025Ndtsurvey . DOI/link: https://doi.org/10.1016/j.comcom.2025.108144 . Sursa textului: integral: versiunea autorilor pe HAL (hal-04986834v1, depusa la 11 martie 2025; preprint "submitted to Elsevier")
Sectiunea din plan: C . Tema: digital twin (NDT, survey)
Autori: Syed Mohsan Raza, Roberto Minerva, Noel Crespi, Maira Alvi, Manoj Herath, Hrishikesh Dutta (SAMOVAR, Telecom SudParis, Institut Polytechnique de Paris). Computer Communications, vol. 236, 2025, art. 108144.
Nota de proces: la prima incercare din aceasta rulare, pagina HAL era protejata de o verificare anti-bot si nota a fost scrisa doar din rezumat. La o reincercare ulterioara, PDF-ul HAL a fost servit direct, iar nota a fost rescrisa din textul integral.

## Problema (cum o formuleaza autorii)
- NDT colecteaza date din componente fizice, virtuale si software si sustine analiza performantei in timp real, emularea si controlul inteligent al retelei fizice. Definitiile IRTF NMRG si ITU sunt citate (1).
- In Edge-Cloud Continuum (ECC) exista mai multi actori: Service Providers, CSP, Platform Providers, operatori de retea (NO), clienti. Toti au nevoie de monitorizare pe mai multe niveluri (infrastructura, virtualizare, software) pentru KPI, SLA si SLO (1.4).
- Specificatiile NDT nu arata cum ar beneficia alti actori decat NO si nu contextualizeaza ECC. In particular, ignora principiile cloud-native (containerizare, MSA) (1.4, Rezumat).

## Structura si taxonomia propusa
- **Metodologie** (1.4): cautare in IEEE Xplore, ScienceDirect, ACM, SpringerLink, Wiley, MDPI, cu termeni precum "Digital Twin Networks", "Network Digital Twin", "DT Modeling", "IRTF Digital Twin Network", "NDT Optimization". Sunt excluse lucrarile care trateaza DT generic, fara perspectiva de retea (de exemplu Industry 4.0/5.0).
- **Sectiunea 1:** beneficiile NDT, contextul ECC, survey-uri existente (Tabelul 1), motivatie si contributii.
- **Sectiunea 2, perspectiva operatorului:** componentele si arhitectura NDT (2.1); integrarea modelelor de invatare (2.2, Fig. 8); NDT in 5G si dupa (2.3, cu tabele de studii, de exemplu Tabelele 3-4 pe SDN); NDT optic (2.4); simulare pentru scenarii what-if (2.5, Tabelul 8).
- **Sectiunea 3:** beneficiile NDT pentru verticale.
- **Sectiunea 4, provocari si propuneri de atenuare** (Fig. 12):
  - colectarea si procesarea datelor (inclusiv date generate prin simulare sau GenAI, care trebuie validate);
  - securitate (acces neautorizat, politici falsificate, blockchain si FL, de exemplu FedTwin, DTPF);
  - alegerea modelului de invatare;
  - complexitatea ECC;
  - deployment-ul NDT.
- **Sectiunea 5, tendinte:** calcul si comunicatii, MSA, evaluarea abordarilor de virtualizare, orchestrarea resurselor, servicii constiente de consumul de energie.
- **Sectiunea 6:** ontologii si modele de date. Ontologiile existente (de exemplu OEG si Huawei Research Ireland) nu sunt direct integrabile pentru ECC.
- **Sectiunea 7:** perspectiva altor actori in ECC. Autorii propun un model de date cu trasaturi descriptive si prescriptive si o vedere pe straturi a ECC (Fig. 15).

## Lucrari/sisteme acoperite (cu numar)
- Lista de referinte are 248 de intrari (ultima numerotata [248]).
- Tabelul 1 compara survey-urile existente despre NDT.
- Proiecte citate in concluzie: 3D-Twin, HyPer-5G, 6G-TWIN, B5GEMINI, descrise de autori ca fiind in faza de design si arhitectura (8).

## Directii deschise declarate
Sectiunea 8:
- Interpretarea si folosirea modelelor de invatare in literatura difera de recomandarile ITU si IRTF. Unele lucrari reduc NDT la suportul unui model anume (de exemplu FL). Rolul, pozitia si scopul modelelor trebuie clarificate.
- Literatura trateaza marginal validarea de catre administratori (acceptare sau respingere) a politicilor produse de modele inainte de aplicarea lor; este nevoie de human-in-the-loop.
- SDN integrat cu NDT creste riscurile de securitate si overhead-ul de control; ECC cere un control plane SDN distribuit.
- Simularea pentru validarea politicilor cere un mediu distribuit (NDT local si global). Scalabilitatea pentru mii de configuratii este tratata marginal.
- Autorii nu au gasit produse NDT disponibile pentru managementul ECC. Majoritatea contributiilor sunt propuneri descriptive.
- Lucrari viitoare: implementarea modelului de date dupa NGSI-LD si FIWARE, cu context broker Stellio; overhead-ul deployment-ului NDT in segmente distribuite; testare intr-un cluster real.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu (survey) - Sectiunea 2.3 descrie arhitectura 5G ca fundal.
- UE reale sau emulate?: nedeclarat.
- digital twin al retelei?: da (subiectul survey-ului) - NDT conform IRTF/ITU, plus modelul de date propus pentru ECC (2, 7).
- prezice efectul unei actiuni inainte de a o aplica?: discutat - simularea what-if pentru validarea politicilor si a rezultatelor modelelor (2.5, 8); nu este implementat in lucrare.
- executa actiuni automat (bucla inchisa)?: discutat - integrarea modelelor de invatare pentru management in bucla inchisa (1.4, 2.2); autorii cer human-in-the-loop (8).
- multi-site / geo-redundanta / failover de baza de date?: partial (la nivel de survey) - instante NDT locale si globale in segmente ECC distribuite geografic (4.1, 8); failover de baza de date nementionat.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu.
- observa traficul la SCP / proxy?: nu.
