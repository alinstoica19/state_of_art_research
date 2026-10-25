# Scaling UPF Instances in 5G/6G Core With Deep Reinforcement Learning (2021)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Nguyen2021Upfscaling . DOI/link: https://doi.org/10.1109/access.2021.3135315 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: B

## Problema (cum o formuleaza autorii)
UPF (User Plane Function) transporta datele abonatilor in sesiuni PDU. Numarul instantelor UPF pornite ar trebui sa depinda de numarul de sesiuni PDU necesare, pentru a economisi resursele consumate; aceasta este controlata de un algoritm de scalare.

## Ce propun (metoda, pe scurt)
Aplicarea Deep Reinforcement Learning (DRL) pentru scalarea instantelor UPF impachetate in containere in Kubernetes. Autorii propun o functie de recompensa bazata pe prag si adapteaza algoritmul proximal policy optimization (PPO). Un clasificator support vector machine (SVM) este folosit pentru a trata actiunile nedorite propuse de agent din cauza politicii stochastice.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Rezultate numerice extinse; tipul de mediu (testbed, emulare sau simulare) nu este precizat. Unelte: Kubernetes, PPO, SVM. Scara si date: nedeclarat in rezumat.

## Experimente si metrici
Comparatie cu Horizontal Pod Autoscaler (HPA) din Kubernetes. Metrica mentionata: numarul mediu de Pod-uri economisit.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
metoda DRL economiseste 2.7–3.8% din numarul mediu de Pod-uri, iar SVM 0.7–4.5% fata de HPA. Trimitere la tabel/figura: nedeclarat in rezumat.

## Limitari declarate de autori
nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - (rezumat); UPF in containere in Kubernetes este descris, dar nu se precizeaza daca core-ul este implementat sau modelat
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: nedeclarat - (rezumat); agentul DRL "sugereaza" actiuni de scalare, dar rezumatul nu spune daca sunt aplicate automat
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
