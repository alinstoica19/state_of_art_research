# AICOM: A Novel LLM-based Autonomous Configuration Management in Cloud-Native 5GC (2026)
Cheie: Veronese2026Aicom . DOI/link: https://doi.org/10.23919/ifipnetworking70592.2026.11579155 . Sursa textului: DOAR REZUMAT
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Sectiunea din plan: B
## Problema (cum o formuleaza autorii)
Trecerea la retele 5GC nativ cloud introduce provocari noi pentru managementul configuratiei, care cer mai multa automatizare, flexibilitate si fiabilitate.
## Ce propun (metoda, pe scurt)
O arhitectura unificata pentru managementul automat si inteligent al configuratiei 5GC cloud-native (AICOM), care integreaza framework-uri de automatizare deterministe, orchestrare bazata pe Kubernetes si agenti cu LLM. Arhitectura separa intelegerea din Intelligence Layer de executia din Network Automation Layer. Se folosesc GitOps si procesarea intentiilor cu AI, iar orchestrarea taskurilor este hibrida (deterministic plus agentic), pentru a reduce dependenta de agenti.
## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Evaluare pe un "real testbed". Scara si volumul: nedeclarat in rezumat. Unelte: Kubernetes, GitOps, agenti cu LLM (ca parti ale arhitecturii).
## Experimente si metrici
Evaluare a solutiei pe testbed-ul real, pe diverse intentii ale operatorilor (operator intents), inclusiv mecanisme de recuperare (recovery). Metrici cantitative: nedeclarat in rezumat.
## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Autorii raporteaza "reliable automation", "strong performance across diverse operator intents" si "robust recovery mechanisms" (formulari calitative). Cifre: nedeclarat in rezumat. Autorii mentioneaza ca rezultatele arata limitari actuale ale inteligentei si adaptabilitatii LLM pentru cerinte noi.
## Limitari declarate de autori
Limitari actuale ale LLM in privinta inteligentei si adaptabilitatii pentru cerinte noi; este nevoie de progrese in arhitecturile LLM si in standardizare. Modelul hibrid echilibreaza fiabilitatea deterministica cu flexibilitatea agentica.
## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - (rezumat: se vorbeste despre 5GC cloud-native, fara detalii despre implementarea core-ului)
- UE reale sau emulate?: nedeclarat - (rezumat: nu mentioneaza)
- digital twin al retelei?: nedeclarat - (rezumat: nu mentioneaza)
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat: nu mentioneaza)
- executa actiuni automat (bucla inchisa)?: da - (rezumat: automatizeaza fluxurile de configurare prin GitOps si procesarea intentiilor cu AI, executate de Network Automation Layer)
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - (rezumat: mentioneaza "robust recovery mechanisms", fara detalii despre multi-site sau failover de baza de date)
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat: nu mentioneaza)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - (rezumat: nu mentioneaza)
- observa traficul la SCP / proxy?: nedeclarat - (rezumat: nu mentioneaza)
