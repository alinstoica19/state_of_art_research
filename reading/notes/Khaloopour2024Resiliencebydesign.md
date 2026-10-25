# Resilience-by-Design in 6G Networks: Literature Review and Novel Enabling Concepts (2024)
Cheie: Khaloopour2024Resiliencebydesign . DOI/link: https://doi.org/10.1109/access.2024.3480275 . Sursa textului: integral: arXiv 2405.17480v2 (23 septembrie 2024; versiunea publicata este IEEE Access, CC BY)
Sectiunea din plan: C . Tema: rezilienta (6G resilience-by-design, review)
Autori: Ladan Khaloopour, Yanpeng Su, Florian Raskob, Tobias Meuser, Roland Bless, Leon Janzen, Kamyar Abedi, Marko Andjelkovic, Hekma Chaari, Pousali Chakraborty, Michael Kreutzer, Matthias Hollick, Thorsten Strufe, Norman Franchi, Vahid Jamali (TU Darmstadt, FAU, KIT, IHP, Fraunhofer FOKUS, Fraunhofer SIT; proiectul Open6GHub). IEEE Access, 2024; 164 de referinte.

## Problema (cum o formuleaza autorii)
Dependenta societatii de infrastructura 6G creste. Intreruperile, fie din erori umane sau tehnice, dezastre naturale sau terorism, ar afecta grav viata zilnica. De aceea, 6G trebuie sa fie rezilient pentru a mentine serviciile esentiale in fata unor provocari posibil necunoscute, nu doar performant (Rezumat, I).

## Structura si taxonomia propusa
- **Sectiunea I.C, Tabelul 1:** lucrari inrudite despre rezilienta si comparatia scopului lor.
- **Sectiunea II:** definitii ale rezilientei (proprietatile resistance, absorption, recovery), enablers (protection, detection, recovery) si diferentierea fata de termeni inruditi (dependability, security etc.).
- **Sectiunea III, conceptul Resilience-by-Design (RBD):**
  - end-to-end resilience pe tot ciclul de viata (III.A);
  - trei principii holistice (III.B): P1 masuri de design protective, P2 capabilitati de self-awareness, P3 capabilitati de reconfigurare;
  - aplicarea pe straturi/perspective (III.C, Tabelul 2): electronica, canal fizic, componente si functii de retea, retele (RAN, core, backbone), servicii;
  - aspecte cross-layer si cross-infrastructure, inclusiv interactiunea cu alte infrastructuri critice (III.D);
  - compromisuri de design: complexitate, eficienta, rezilienta (III.E).
- **Sectiunea IV, cazuri de utilizare:** retea de monitorizare distribuita bazata pe cloud, condus autonom, linie de productie automatizata, VR/AR.

## Lucrari/sisteme acoperite (cu numar)
164 de referinte in arXiv v2. Tabelul 1 compara lucrari inrudite; numarul exact de randuri nu a fost numarat aici.

## Directii deschise declarate
Sectiunea V:
- implementarea principiilor P1-P3: protectie din faza de design, retele self-aware (de exemplu un cadru de monitorizare 6G), moduri multiple de operare activate in functie de starea sistemului;
- reconfigurarea depinde de o infrastructura de control functionala; este nevoie de management autonom si configurare zero-touch sau automatizata pentru a evita erorile umane, precum si de un control plane zero-touch rezilient si securizat (provizionarea certificatelor nu se poate automatiza complet);
- compromisuri: monitorizarea pentru self-awareness adauga overhead si dependente;
- unelte CAD pentru electronica rezilienta si alte provocari specifice straturilor.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu (review conceptual).
- UE reale sau emulate?: nu.
- digital twin al retelei?: nedeclarat in sectiunile citite.
- prezice efectul unei actiuni inainte de a o aplica?: nu; "prediction" apare ca o capabilitate de rezilienta (III.B).
- executa actiuni automat (bucla inchisa)?: propus - reconfigurare (P3), management autonom si zero-touch (V); neimplementat.
- multi-site / geo-redundanta / failover de baza de date?: discutat conceptual (redundanta, interdependente cross-infrastructure).
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu.
- observa traficul la SCP / proxy?: nu.
