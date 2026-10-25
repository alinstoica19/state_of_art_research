# Energy-Efficient Softwarized Networks: A Survey (2025)
Cheie: Setiawan2025Softwarized . DOI/link: https://doi.org/10.1109/tnsm.2025.3599919 . Sursa textului: integral: arXiv 2307.11301v1 (21 iulie 2023; "Version 1.0"; versiunea publicata in IEEE TNSM 2025 poate diferi)
Sectiunea din plan: C . Tema: energie (SDN/NFV/NS, survey)
Autori: Iwan Setiawan, Binayak Kar, Shan-Hsiang Shen. IEEE Transactions on Network and Service Management, 2025; 159 de referinte in versiunea arXiv v1.

## Problema (cum o formuleaza autorii)
Softwarizarea retelei este enabler-ul evolutiei retelelor (programabilitate, flexibilitate, management agil). Satisfacerea cerintelor serviciilor nu trebuie sa ignore energia, din motive de sustenabilitate a mediului si a afacerii (Rezumat). Lucrarea pune SDN, NFV si network slicing (NS) intr-un context orientat pe energie.

## Structura si taxonomia propusa
- **Metodologie** (I.D, Fig. 2):
  - doua parti: un survey al survey-urilor (eficienta energetica, softwarizare, intersectia lor) si survey-ul pe fiecare tehnologie;
  - IEEE Xplore ca baza primara, plus Google Scholar (ACM, Elsevier, Springer, Hindawi, Wiley, IEICE, arXiv);
  - lucrarile sunt clasificate dupa scenariul de retea, stratul control/MANO, strategia de eficienta energetica si atributele solutiei (abordare, metoda de evaluare, criteriu, metrica).
- **Sectiunea II:**
  - contributorii la consumul de energie si modelele de consum;
  - taxonomia strategiilor (Tabelul II): imbunatatiri hardware, adaptare dinamica, moduri sleep, heterogenitatea retelei, heterogenitatea energiei, machine learning.
- **Sectiunea III:** SDN, NFV, NS si MANO ca enablers, cu accent pe straturile control si MANO.
- **Sectiunea IV:** survey pe SDN eficient energetic (Tabelul III), NFV (Tabelul IV) si NS (Tabelul V).

## Lucrari/sisteme acoperite (cu numar)
159 de referinte in arXiv v1; Fig. 3 arata numarul de publicatii pe an. Numarul exact de lucrari clasificate in Tabelele III-V nu a fost numarat aici.

## Directii deschise declarate
Sectiunea V, zece preocupari:
- A. hardware programabil verde si software verde;
- B. consumul de energie al straturilor control si MANO insesi (de la un server cu controller SDN la mai multe masini pentru scalabilitate, securitate sau fiabilitate);
- C. reconfigurarea si partajarea retelei;
- D. economii de energie la edge;
- urmatoarele directii:
  - F. heterogenitatea retelei;
  - G. heterogenitatea energiei (surse regenerabile, energy harvesting);
  - H. abordari de optimizare traditionale vs. ML;
  - I. metrici si masuratori (de exemplu RESDN, ECPUB: energie pe bit util in loc de bit transmis).
- Rezumatul mentioneaza zece preocupari esentiale; textul extras listeaza explicit sectiunile A-I.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu (survey).
- UE reale sau emulate?: nu.
- digital twin al retelei?: nedeclarat in sectiunile citite.
- prezice efectul unei actiuni inainte de a o aplica?: nu.
- executa actiuni automat (bucla inchisa)?: nu (survey); politicile de eficienta energetica sunt aplicate prin MANO (VI).
- multi-site / geo-redundanta / failover de baza de date?: nu; mentioneaza replicarea controllerului SDN ca sursa de consum (V.B).
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu.
- observa traficul la SCP / proxy?: nu.
