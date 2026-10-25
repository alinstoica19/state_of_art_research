# Failures and Resilience in the IP Era: Navigating the Fragility of Modern Telecommunications Networks - The Sovereign Functions (2025)
Cheie: Owen2025Sovereignfunctions . DOI/link: https://doi.org/10.1109/access.2025.3602054 . Sursa textului: integral: versiunea publicata (IEEE Access, CC BY 4.0; https://ieeexplore.ieee.org/ielx8/6287639/10820123/11136144.pdf)
Sectiunea din plan: C . Tema: rezilienta (defecte la nivel de operator, survey orientat pe defecte)
Autori: Raymond Owen, Adam Bryant, Leigh Finch, Daniel Franklin, Mahrokh Abdollahi, Mehran Abolhasan (University of Technology Sydney; Australian National Telecom Resilience Centre). IEEE Access vol. 13, 2025, pp. 155756-; 182 de referinte.

## Problema (cum o formuleaza autorii)
Pe langa redundanta fizica si izolarea geografica, retelele moderne depind de un set de functii IP interdependente, numite de autori "functii suverane": rutare, adresare si naming, sincronizare de timp. De ele sunt cuplate servicii suport: autentificare si control al accesului, managementul licentelor, configurare si management. Autorii arata ca defectele reale la scara nationala provin adesea din aceste straturi, mai ales din erori de configurare (Rezumat, I). Ei citeaza Uptime Institute 2025: eroarea umana este principala cauza a intreruperilor majore in 2025, in crestere cu 10 puncte procentuale fata de 2024 (IV).

## Structura si taxonomia propusa
- **Sectiunea II:** rolul functiilor IP critice si al configurarii lor.
- **Sectiunea III:**
  - studii de caz ale intreruperilor la scara mare din 2020 pana in prezent (Tabelul 1);
  - impact financiar, de reglementare si social;
  - strategii de mitigare:
    - igiena configurarii: RBAC, training, sabloane, versionare, audituri;
    - management out-of-band independent;
    - automatizarea configurarii, care poate propaga rapid erorile;
    - segmentare si izolare.
- **Sectiunea IV, functii suverane in trei categorii**, fiecare cu riscuri, strategii de rezilienta si incidente reale (Tabelul 2):
  1. rutare si determinarea cailor: BGP, OSPF, MPLS;
  2. adresare si naming: DNS, DHCP;
  3. sincronizare de timp: NTP, PTP, ITU-T G.8275.x.
- **IV.D, functii suport critice**, cu incidente (Tabelul 3).

## Lucrari/sisteme acoperite (cu numar)
- 182 de referinte.
- Tabelul 1 contine intreruperi majore din 2020 pana in prezent; Tabelele 2 si 3 contin incidente cauzate de functiile suverane si de cele suport.
- Exemple din text (III):
  - KDDI (2022): eroare de configurare a unui router in mentenanta, congestie la nodurile VoLTE si baza de date de abonati coplesita de autentificari repetate; aproximativ 22,78 milioane de utilizatori VoLTE si peste 7,65 milioane de utilizatori de date 4G/5G afectati;
  - Rogers (2022): intrerupere nationala de 15 ore; eliminarea unui filtru ACL a provocat un val de actualizari de rutare care a prabusit routerele core; costul a fost de 150 milioane CAD;
  - Optus (8 noiembrie 2023): 12 ore, declansata de un upgrade la furnizorul upstream Singtel; surplusul de informatii de rutare (in special IPv6) a depasit pragurile de autoprotectie lasate la valorile implicite ale vendorului, iar routerele s-au autoizolat. Peste 2.100 de apeluri de urgenta au fost afectate; restaurarea a fost manuala, deoarece s-a pierdut accesul in-band si out-of-band la reteaua O&M;
  - AT&T (2024): 12 ore, peste 125 de milioane de dispozitive;
  - Telefonica (2025): upgrade MPLS.

## Directii deschise declarate
Sectiunea V:
- ghiduri de design pentru functiile suverane, cu segmentarea si izolarea functiilor critice;
- examinarea dependentei IP de aceste functii si a abordarilor descentralizate;
- tehnologii emergente: blockchain pentru BGP, DNS descentralizat, rutare locala la edge, tehnici AI pentru monitorizarea si detectia erorilor de configurare si a atacurilor;
- securitate si monitorizare pentru detectia si remedierea rapida a erorilor de configurare;
- colaborare academie-industrie-reglementatori.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu (survey bazat pe incidente).
- UE reale sau emulate?: nu (sunt date numerele de utilizatori afectati in incidente reale).
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu; ca mitigare sunt propuse audituri si verificari ale configurarii.
- executa actiuni automat (bucla inchisa)?: nu; observa ca automatizarea configurarii poate propaga erorile rapid (III.B).
- multi-site / geo-redundanta / failover de baza de date?: discutat - redundanta fizica si izolarea geografica sunt considerate necesare, dar insuficiente; exemplul KDDI implica baza de date de abonati supraincarcata.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: da (din incidente) - utilizatori afectati, apeluri de urgenta intrerupte.
- observa traficul la SCP / proxy?: nu.
