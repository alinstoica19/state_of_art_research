# Fault Tolerance in Service Function Chains: A Taxonomy, Survey and Future Directions (2025)
Cheie: Shahab2025Sfcfaulttolerance . DOI/link: https://doi.org/10.1007/s10922-025-09955-8 . Sursa textului: integral: preprint Research Square rs-4913807/v1 (https://doi.org/10.21203/rs.3.rs-4913807/v1; marcat ca acceptedVersion de Unpaywall)
Sectiunea din plan: C . Tema: rezilienta (SFC fault tolerance, survey sistematic)
Autori: Muhammad Hamza Shahab, Yogesh Sharma (University of Regina). Journal of Network and Systems Management, 2025.

## Problema (cum o formuleaza autorii)
Deployment-ul virtualizat al SFC-urilor le face mai susceptibile la defecte decat cel fizic. Autorii afirma ca survey-urile existente despre toleranta la defecte in SFC sunt putine si nesistematice, fara taxonomie specifica si fara analiza critica. Singurul survey sistematic comparabil (Ly et al. [26]) nu ofera taxonomie, analiza critica si identificarea golurilor (Sectiunea 3).

## Structura si taxonomia propusa
- **Metodologie dupa Kitchenham** (Sectiunea 4):
  - patru intrebari de cercetare (Tabelul 2): tipuri de defecte, tipare de aparitie, mecanisme de management, metrici de evaluare;
  - surse: Google Scholar, IEEE Xplore, ACM DL, ScienceDirect, SpringerLink, arXiv, MDPI, Wiley;
  - perioada 2015-2024, plus snowballing;
  - selectie: 4600 de rezultate -> 150 dupa titlu -> 146 dupa rezumat si concluzii -> 87 de articole analizate critic (Tabelul 9).
- **Taxonomia in patru parti** (Sectiunea 5, Fig. 5):
  1. tipuri de defecte: software (logica aplicatiei, configurare), hardware, virtualizare;
  2. tipare de aparitie: defecte independente sau corelate;
  3. mecanisme de management: proactive, reactive, hibride;
  4. metrici: fiabilitate, disponibilitate, performanta.
- **Cadru conceptual** (Sectiunea 7, Fig. 7): extinde arhitectura ETSI NFV cu un strat de monitorizare (senzori de performanta VNF, hardware, virtualizare), un strat de analiza inteligenta a defectelor si un strat de control adaptiv bazat pe AI/ML.

## Lucrari/sisteme acoperite (cu numar)
87 de articole, analizate critic in Tabelul 9 (puncte tari si slabe).

## Directii deschise declarate
Concluzii (Sectiunea 8):
- explorarea mai profunda a defectelor software si de virtualizare, nu doar hardware;
- renuntarea la presupunerea de defecte independente in favoarea defectelor corelate si in cascada;
- combinarea mecanismelor proactive si reactive;
- integrarea AI/ML pentru predictia defectelor, detectia anomaliilor in timp real si recuperare automata.

Sectiunea 6 discuta si golurile de cercetare.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu (survey; SFC/NFV general).
- UE reale sau emulate?: nu.
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu.
- executa actiuni automat (bucla inchisa)?: propus conceptual (stratul de control adaptiv, Sectiunea 7); neimplementat.
- multi-site / geo-redundanta / failover de baza de date?: tema generala (mecanisme reactive de recuperare); fara evaluare proprie.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu.
- observa traficul la SCP / proxy?: nu.
