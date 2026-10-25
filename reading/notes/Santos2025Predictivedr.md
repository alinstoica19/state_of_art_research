# Predictive Disaster Recovery for Multi-Redundant Operations and Maintenance 5G Network Systems (2025)
NOTA: nota scrisa doar din rezumat; textul integral nu este disponibil din surse libere legale.
Cheie: Santos2025Predictivedr . DOI/link: https://doi.org/10.1109/iwcmc65282.2025.11059520 . Sursa textului: DOAR REZUMAT (OpenAlex)
Sectiunea din plan: C . Tema: disaster recovery / failover predictiv
Autori: Charles F. Santos, Augusto Neto, Ramon R. Fontes, Roger Immich, Vicente A. de Sousa, Helber W. Da Silva. IWCMC 2025.

## Problema (cum o formuleaza autorii)
Evolutia rapida a retelelor 5G aduce provocari in mentinerea continuitatii serviciului, mai ales in verticala critica eHealth. Abordarile traditionale sunt reactive, cu logica de switchover binara (rezumat).

## Ce propun (metoda, pe scurt)
PDRS (Proactive Disaster Recovery System), sistem de disaster recovery condus de ML pentru sistemele de operare si mentenanta (OMS) 5G din verticale eHealth critice. Permite failover proactiv prin: (1) monitorizarea continua a starii OMS prin KPI; (2) predictia dezastrelor prin analitica in timp real; (3) alegerea instantei OMS de backup optime dintre mai multi candidati redundanti, pe baza estimarilor costului de migrare (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Evaluare proof-of-concept (rezumat). Testbed-ul, modelul ML si scara sunt nedeclarate in rezumat.

## Experimente si metrici
Mentinerea continuitatii serviciului fata de metode de referinta, pentru aplicatii eHealth cu latenta mica care cer disponibilitate 99,999% (rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
PDRS este superior metodelor de referinta in mentinerea continuitatii serviciului, mai ales pentru aplicatiile eHealth cu latenta mica (rezumat; fara cifre).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - OMS 5G; implementarea nu este precizata in rezumat.
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nu - nementionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica?: partial - estimeaza costul de migrare pentru instantele de backup candidate inainte de alegere (rezumat).
- executa actiuni automat (bucla inchisa)?: da - failover proactiv declansat de predictia dezastrelor (rezumat).
- multi-site / geo-redundanta / failover de baza de date?: da - instante OMS de backup multi-redundante, cu failover proactiv (rezumat); geo-distributia nu este precizata.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - continuitatea serviciului; metrica exacta nu este precizata in rezumat.
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
