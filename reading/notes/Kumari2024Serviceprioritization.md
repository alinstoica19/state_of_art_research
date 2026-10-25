# Resource-Aware Service Prioritization in a Slice-Supportive 5G Core Control Plane for Improved Resilience and Sustenance (2024)
NOTA: nota scrisa doar din rezumat; textul integral nu este disponibil din surse libere legale.
Cheie: Kumari2024Serviceprioritization . DOI/link: https://doi.org/10.1109/ccnc51664.2024.10454708 . Sursa textului: DOAR REZUMAT (OpenAlex)
Sectiunea din plan: C . Tema: rezilienta control plane / prioritizare slice
Autori: Supriya Kumari, Shwetha Vittal, A. Antony Franklin. IEEE CCNC 2024.

## Problema (cum o formuleaza autorii)
Serviciul rezilient si sustinut este dificil in SBA-ul unui core 5G distribuit, unde mai multe NF-uri servesc cererile de serviciu ale utilizatorilor (USR) din control plane. Este nevoie de monitorizarea continua a NF-urilor intr-o bucla de automatizare inchisa (CLA). Defectele, suprasarcinile sau congestia NF-urilor pot duce la pierderea inutila a USR-urilor critice (rezumat).

## Ce propun (metoda, pe scurt)
Monitorizarea proactiva a NF-urilor din control plane, folosita pentru programarea USR-urilor si prioritizarea cererilor critice ale slice-urilor. Algoritmul Ford-Fulkerson (max-flow) evalueaza proactiv performanta si disponibilitatea NF-urilor si serveste cererile critice in situatii de defect si suprasarcina (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Testbed 5G conform 3GPP (rezumat). Core-ul folosit, generatorul de UE si scara sunt nedeclarate in rezumat.

## Experimente si metrici
Numarul de USR servite la varf de trafic, pentru core-ul nativ si pentru cel cu slice-uri (mMTC, uRLLC) (rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Core-ul nativ serveste cu 20% mai multe USR predominante. Core-ul cu slice-uri serveste cu 33% mai multe USR mMTC si cu 47% mai multe USR uRLLC, fiecare la traficul de varf respectiv (rezumat).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - testbed 5G conform 3GPP; implementarea nu este numita in rezumat.
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nu - nementionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica?: partial - evaluarea proactiva a capacitatii NF-urilor prin max-flow inainte de servirea cererilor (rezumat).
- executa actiuni automat (bucla inchisa)?: da - programarea si prioritizarea cererilor pe baza monitorizarii, in bucla inchisa (CLA) (rezumat).
- multi-site / geo-redundanta / failover de baza de date?: partial - defecte si suprasarcini de NF tratate prin prioritizare; failover nu este mentionat (rezumat).
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: da - numarul de cereri de serviciu ale utilizatorilor servite (rezumat).
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
