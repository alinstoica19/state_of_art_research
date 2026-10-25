# NFVAgent: A Retrieval-Augmented LLM Agent for Resilient NFV Failure Recovery (2025)
NOTA: nota scrisa doar din rezumat; textul integral nu este disponibil din surse libere legale.
Cheie: Woo2025Nfvagent . DOI/link: https://doi.org/10.23919/cnsm67658.2025.11297536 . Sursa textului: DOAR REZUMAT (OpenAlex)
Sectiunea din plan: C . Tema: recuperare defecte / agenti LLM / NFV
Autori: Yeunjin Woo, Honguk Woo. CNSM 2025.

## Problema (cum o formuleaza autorii)
Sistemele traditionale de management NFV se bazeaza pe politici statice si interventii manuale si nu raspund eficient conditiilor dinamice, ceea ce duce la recuperari intarziate sau suboptimale. Diversitatea deployment-urilor (configuratii, tenanti, standarde operationale) limiteaza solutiile bazate pe politici. LLM-urile nu au expunere explicita la caracteristicile mediilor NFV, deci generalizeaza si sunt fiabile limitat (rezumat).

## Ce propun (metoda, pe scurt)
NFVAgent: cadru de recuperare NFV condus de LLM, bazat pe RAG. Baza de cunostinte este actualizata continuu cu experiente din testbed si din mediile de deployment; cunostintele validate sunt integrate in bucla de decizie a agentului pentru generarea actiunilor de recuperare (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Set de date de alarme cu peste 500 de evenimente de defect, in medii NFV diverse configurate dupa standarde industriale (ONAP, ETSI, O-RAN) (rezumat). LLM-ul folosit este nedeclarat in rezumat.

## Experimente si metrici
Acuratetea recuperarii comparata cu metode existente bazate pe politici, inclusiv in medii multi-tenant (rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Acuratete de recuperare de pana la 99,8%; depaseste metodele bazate pe politici cu o marja medie de 37,7% in medii multi-tenant (rezumat).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - medii NFV generice (ONAP/ETSI/O-RAN); core 5G nementionat (rezumat).
- UE reale sau emulate?: nu se aplica - (rezumat)
- digital twin al retelei?: nu - nementionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: partial - agentul genereaza actiuni de recuperare; executarea lor automata pe infrastructura nu este precizata in rezumat.
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu - evaluare pe un set de date de alarme (rezumat).
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu - acuratetea recuperarii (rezumat).
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
