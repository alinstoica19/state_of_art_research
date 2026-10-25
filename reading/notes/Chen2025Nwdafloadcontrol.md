# A Machine Learning-Driven NWDAF Architecture For Intelligent 5G Core Networks (2025)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Chen2025Nwdafloadcontrol . DOI/link: https://doi.org/10.1145/3733814.3765498 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Lipsa controlului inteligent si dinamic in core-urile 5G open-source duce la blocaje de performanta care necesita interventie manuala.

## Ce propun (metoda, pe scurt)
Un framework ML-driven centrat pe un NWDAF conform 3GPP, integrat cu proiectul free5GC. Arhitectura este decuplata: Model Training Logical Function (MTLF) este separata, pentru deployment flexibil si eficient. NWDAF colecteaza date de retea in timp real pentru a antrena modele dedicate, care prezic incarcarea fiecarei functii de retea (NF). Use case demonstrat: predictiile sunt folosite pentru a ajusta dinamic pragul URR (Usage Reporting Rule), un parametru critic in sistemul de taxare.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Integrare cu free5GC. Validare cu un "custom-built UE-Testbed" pentru simulare realista de trafic. Rezumatul nu precizeaza daca UE sunt reale sau emulate. Scara: nedeclarata in rezumat.

## Experimente si metrici
Comparatie intre sistemul dinamic propus si configuratia statica implicita a free5GC. Metrici exacte: nedeclarate in rezumat.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Autorii afirma ca sistemul dinamic previne supraincarcarea NF-urilor si imbunatateste semnificativ stabilitatea retelei, comparativ cu configuratia statica implicita free5GC. Rezumatul nu contine cifre si nu trimite la tabele sau figuri.

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - (rezumat: integrare cu free5GC)
- UE reale sau emulate?: nedeclarat - (rezumat: "custom-built UE-Testbed for realistic traffic simulation"; nu e precizat daca UE sunt reale sau emulate)
- digital twin al retelei?: nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat: se prezice incarcarea NF-urilor; nu efectul unei actiuni inainte de aplicare)
- executa actiuni automat (bucla inchisa)?: da - (rezumat: pragul URR este ajustat dinamic pe baza predictiilor)
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
