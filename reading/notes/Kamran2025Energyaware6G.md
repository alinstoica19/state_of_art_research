# Energy-Aware 6G Network Design: A Survey (2025)
Cheie: Kamran2025Energyaware6G . DOI/link: https://arxiv.org/abs/2509.11289 . Sursa textului: integral: arXiv 2509.11289v1 (14 septembrie 2025)
Sectiunea din plan: C . Tema: energie (6G energy-aware, survey)
Autori: Rashmi Kamran, Mahesh Ganesh Bhat, Pranav Jha, Shana Moothedath, Manjesh Hanawal, Prasanna Chaporkar (IIT Bombay; Iowa State University). Preprint arXiv.

## Problema (cum o formuleaza autorii)
6G va suporta capabilitati noi si aplicatii centrate pe date pentru un numar foarte mare de utilizatori, cu preocupari de eficienta energetica si sustenabilitate. Cercetarea si standardizarea se concentreaza pe monitorizarea si expunerea informatiei de energie, pe surse regenerabile si pe AI/ML. Designul energy-aware aduce provocari noi: overhead-ul colectarii si expunerii informatiei de energie si gestionarea consimtamantului utilizatorului (Rezumat).

## Structura si taxonomia propusa
- **Sectiunea I.A, Tabelul I:** diferentele fata de survey-urile existente.
- **Sectiunea II, motivatii:** economie de energie; eficienta energetica ca parametru QoS; surse regenerabile; compromisul energie consumata vs. economisita pentru AI/ML; "green user satisfaction"; conectivitate in zone cu energie limitata.
- **Sectiunea III, principii de design** pentru retele mobile energy-aware:
  - tehnici de economisire;
  - expunerea informatiei de energie (Tabelul IV): monitorizare granulara per serviciu, flux si utilizator, cu tipul sursei (regenerabila sau nu), colectata prin OAM;
  - clasificarea serviciilor energy-aware;
  - managementul informatiei de energie;
  - ajustarea QoS pe baza informatiei de energie;
  - modele si parametri de energie;
  - optimizare comuna performanta-resurse-energie.
- **Sectiunea IV, exemple:**
  - alocarea resurselor in core bazata pe ML, constienta de energie, cu QoS garantat: minimizarea numarului de NF-uri active si trecerea celorlalte in sleep; de exemplu UPF-uri incarcate complet si celelalte oprite sau in power-saving (Fig. 4);
  - RAN energy-aware condus de ML;
  - mecanism de securitate adaptiv in functie de serviciu.
- **Sectiunea V:** beneficii, inclusiv multicast energy-aware.
- **Sectiunea VI, standardizare** (3GPP, ITU, IEEE; Tabelele V-VIII):
  - in SA1/SA2, lucrarile Rel-19 si studiile Rel-20 urmaresc colectarea informatiei de energie de la NF-uri, expunerea ei catre utilizatori si terti si ajustarea QoS dupa energie;
  - TS 22.261 clauza 6.15;
  - o functie noua, Energy Information Function (EIF), inclusa in arhitectura 5G [80].

## Lucrari/sisteme acoperite (cu numar)
Tabelul III rezuma referintele; numarul total nu a fost numarat aici.

## Directii deschise declarate
Sectiunea VII:
- obtinerea in timp real a informatiei despre consumul din surse regenerabile si predictia lui;
- proceduri de monitorizare si expunere cu overhead minim;
- analiza overhead-ului energetic al colectarii si analizei datelor de energie;
- solutii AI/ML pentru compromisul economie de energie vs. overhead-ul energetic al AI/ML;
- metode de asigurare a consimtamantului utilizatorului pentru ajustarea QoS pe baza energiei.

Provocarea non-tehnica principala este coordonarea si consimtamantul tuturor actorilor.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu (survey); exemplul cu UPF este conceptual (IV.A).
- UE reale sau emulate?: nu.
- digital twin al retelei?: nedeclarat.
- prezice efectul unei actiuni inainte de a o aplica?: nu.
- executa actiuni automat (bucla inchisa)?: discutat conceptual (ML in controlerul core-ului pentru alocarea resurselor, IV.A).
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu (discuta informatia de energie per utilizator si "green user satisfaction" conceptual).
- observa traficul la SCP / proxy?: nu.
