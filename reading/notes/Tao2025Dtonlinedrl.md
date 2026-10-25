# Digital Twin-Accelerated Online Deep Reinforcement Learning for Admission Control in Sliced Communication Networks (2025)
Cheie: Tao2025Dtonlinedrl . DOI/link: https://doi.org/10.1109/tcomm.2024.3476430 . Sursa textului: integral: arXiv 2310.09299v3 (21 noiembrie 2023, versiune submitted, titlu diferit: "Digital Twin Assisted Deep Reinforcement Learning for Online Admission Control in Sliced Network")
Sectiunea din plan: C . Tema: digital twin / DRL / admission control slicing
Autori: Zhenyu Tao, Wei Xu, Xiaohu You (Southeast University, Nanjing; Purple Mountain Laboratories). IEEE Transactions on Communications (online 2024).
ATENTIE: versiunea citita este preprint-ul arXiv v3. Rezumatul versiunii publicate (OpenAlex) raporteaza alte cifre (de exemplu imbunatatire de pana la 26,39% a utilizarii resurselor fata de modelul DRL de referinta) si mentioneaza behavior cloning si mentinerea veniturilor pe termen lung. Cifrele de mai jos sunt cele din preprint.

## Problema (cum o formuleaza autorii)
- Admission control decide ce cereri de servicii sunt acceptate in slice-uri care partajeaza resurse limitate. Metodele conventionale (cautare, euristici) devin ineficiente, iar DRL este folosit pentru eficienta si flexibilitate (I).
- Modelele DRL antrenate intr-un simulator imprecis pot functiona prost in reteaua reala. Antrenarea online direct pe reteaua reala perturba operarea si reduce utilizarea resurselor, din cauza actiunilor stocastice ale modelului initializat aleator (I).

## Ce propun (metoda, pe scurt)
- **Model** (III): trei parti (utilizatori, tenanti, InP), K = 4 slice-uri (mMTC, eMBB, URLLC, other); sosiri Poisson, timpi de servire exponentiali, timp maxim de asteptare in coada; resurse combinate radio, calcul, stocare. Procesul de decizie este formulat ca SMDP, apoi simplificat intr-un MDP in timp discret echivalent.
- **DT la nivel de politica** (IV): o retea neuronala (FFN) cu strat de iesire customizat pentru cererile din coada, antrenata supervizat pe perechi stare-actiune colectate de la politica de admitere implicita existenta. Autorii spun ca colectarea nu perturba operarea retelei.
- **DRL asistat de DT** (Algoritmul 2, A2C modificat):
  1. antrenarea DT-ului;
  2. actorul este initializat ca o copie a DT-ului, iar criticul este antrenat singur;
  3. actorul si criticul sunt antrenati impreuna, online.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Simulare in Python 3.9, PyTorch 1.10, CUDA 11.3; PC cu i7-12700KF, 32 GB RAM, RTX 3080 (V.A).
- Parametrii slice-urilor sunt in Tabelul I. De exemplu URLLC are timpul mediu de servire 1/mu3 = 1,6 si hold time T3 = 0,2.
- FFN cu 3 straturi de 64 de noduri pentru DT, actor si critic.
- Trei politici implicite: PRIO (euristica cu prioritate si echitate), ILP (maximizeaza utilizarea radio) si Greedy. Baseline DRL: Dueling-DQN cu (nmax+1)^K = 256 de iesiri.
- Obiectiv: maximizarea veniturilor din taxarea stocarii (vectorul de taxare c = [0, 0, 100]).
- Patru rulari cu seed-uri diferite; date inregistrate la fiecare 200 de epoci de decizie.

## Experimente si metrici
- Acuratetea DT-ului in functie de marimea setului de antrenare (Fig. 3).
- Utilizarea resurselor si rata de acceptare pentru politicile implicite, DRL antrenat direct si DRL asistat de DT (Fig. 4-6).
- Utilizarea resurselor in primele 20.000 de epoci, agregata pe intervale de 4.000 (Fig. 7).
- Recompensa cumulata in 400 de epoci de decizie dupa antrenare (Fig. 8).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Cu 100.000 de esantioane, DT-ul reproduce politica implicita cu acuratete peste 99% pentru toate cele trei politici (V.B.1, Fig. 3).
- Antrenarea a durat 6.000 de epoci pentru pasul 2 si 50.000 pentru pasul 3. Modelul propus antrenat direct converge dupa aproximativ 20.000 de epoci de decizie; Dueling-DQN are dificultati de convergenta (Fig. 5).
- In primele 4.000 de epoci, DRL asistat de DT are utilizare a resurselor cu pana la 41,75% mai mare decat Dueling-DQN si cu pana la 22,36% mai mare decat acelasi model antrenat direct. Diferentele scad pe masura ce modelele converg (Fig. 7).
- Toate modelele DRL depasesc politicile implicite la recompensa cumulata. Varianta bazata pe ILP are rezultate mai slabe decat DRL antrenat direct; autorii pun asta pe seama numarului limitat de esantioane de antrenare (Fig. 8).

## Limitari declarate de autori
- Performanta depinde intr-o anumita masura de politica implicita (de exemplu varianta bazata pe ILP) (V.B.2).
- Daca politica implicita este prea complexa pentru a fi replicata, autorii sugereaza o politica simpla de substitutie (Greedy) (V.B.2).
- Evaluarea este exclusiv in simulare.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - sistem de cozi simulat cu resurse abstracte (III, V).
- UE reale sau emulate?: simulate - cereri generate stocastic (Poisson) (III).
- digital twin al retelei?: partial - "DT" este o replica neuronala a politicii de admitere (policy-level), nu a starii retelei (IV).
- prezice efectul unei actiuni inainte de a o aplica?: nu - DT-ul imita decizii; nu estimeaza efectul lor.
- executa actiuni automat (bucla inchisa)?: da (in simulare) - agentul DRL ia decizii de admitere online (IV, V).
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: partial - rata de acceptare a cererilor de servicii per slice (Fig. 4-6).
- observa traficul la SCP / proxy?: nu.
