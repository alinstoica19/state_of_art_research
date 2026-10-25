# ML-SLD: A message-level stateless design for cloud-native 5G core network (2023)
NOTA: nota scrisa doar din rezumat; lucrarea este open access (CC BY-NC-ND), dar ScienceDirect a raspuns cu HTTP 403 la cererile automate (PDF si HTML), iar pagina declara rezervare TDM. Nu s-a insistat; textul integral nu a fost obtinut.
Cheie: Du2023Statelesscore . DOI/link: https://doi.org/10.1016/j.dcan.2022.04.026 . Sursa textului: DOAR REZUMAT (OpenAlex)
Sectiunea din plan: C . Tema: core stateless / cloud-native
Autori: Keliang Du, Luhan Wang, Xiangming Wen, Yu Liu, Haiwen Niu, Shaoxin Huang. Digital Communications and Networks (KeAi/Elsevier), online 2022.

## Problema (cum o formuleaza autorii)
Traficul de semnalizare generat de miliarde de dispozitive IoT pune presiune pe control plane-ul core-ului 5G. 3GPP a propus SBA pentru un core cloud-native, flexibil si scalabil. Din cauza cuplarii starilor de protocol cu functiile, raman multe provocari pentru folosirea deplina a beneficiilor cloud si pentru orchestrarea cloud-native a core-ului (rezumat).

## Ce propun (metoda, pe scurt)
ML-SLD (Message-Level StateLess Design), un core 5G cloud-native din punct de vedere arhitectural: (1) un mecanism de servitizare a interfetei N2, care mentine conexiunea dintre RAN si core si evita intreruperile si pierderile pentru volume mari de utilizatori; (2) un algoritm de On-demand Message Forwarding (OMF), care reduce impactul fluctuatiilor din cloud asupra performantei (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Prototip bazat pe OpenAirInterface 5G core, cu toate NF-urile in containere Docker, desfasurate intr-un cloud bazat pe Kubernetes. Experimente cu UERANSIM si Chaosblade (rezumat).

## Experimente si metrici
Viabilitatea si eficienta metodelor propuse (rezumat). Metricile exacte sunt nedeclarate in rezumat.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Nedeclarat in rezumat (nu sunt raportate cifre).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - prototip pe OAI 5G core, in Kubernetes (rezumat).
- UE reale sau emulate?: emulate - UERANSIM (rezumat).
- digital twin al retelei?: nu - nementionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: partial - redirectionarea mesajelor la cerere (OMF) ca raspuns la fluctuatiile din cloud (rezumat).
- multi-site / geo-redundanta / failover de baza de date?: partial - continuitatea conexiunii N2 la intreruperi, testata cu injectare de defecte (Chaosblade) (rezumat); multi-site nementionat.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - rezumatul mentioneaza evitarea intreruperilor pentru volume mari de utilizatori, fara metrici.
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
