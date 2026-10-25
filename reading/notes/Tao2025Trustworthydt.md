# Toward Trustworthy Digital Twins in AI Agent-based Wireless Network Optimization: Challenges, Solutions, and Opportunities (2025)
Cheie: Tao2025Trustworthydt . DOI/link: https://arxiv.org/abs/2511.19961 . Sursa textului: integral: arXiv 2511.19961v2 (5 iunie 2026)
Sectiunea din plan: C . Tema: digital twin / fidelitate / sim-to-real
Autori: Zhenyu Tao, Wei Xu, Xiaohu You (Southeast University; Purple Mountain Laboratories). Articol de tip magazine; antetul preprint-ului indica IEEE Wireless Communications.

## Problema (cum o formuleaza autorii)
- Agentii RL pentru optimizarea retelelor wireless nu pot explora liber pe reteaua reala: costuri, degradare QoS, incalcari de SLA, riscuri de stabilitate. Paradigma RL antrenat in DT depinde insa de fidelitatea DT-ului; un DT inexact produce un decalaj sim-to-real (I).
- Trei provocari declarate (I):
  - lipsesc metode de evaluare holistice: un DT este compus din mai multe modele (UE, canal, core), iar evaluarile existente masoara acuratetea fiecarui model separat;
  - proiectarea si mentenanta DT-ului sunt empirice (ce modele, cate date, cand se actualizeaza);
  - nu exista garantii de performanta pentru o politica antrenata in DT si apoi desfasurata.

## Ce propun (metoda, pe scurt)
- **Fidelitate centrata pe sarcina** (II.B, Fig. 2): reteaua reala si DT-ul sunt abstractizate ca MDP-uri, asa cum le percepe agentul (stare, actiune, probabilitate de tranzitie, recompensa), si este evaluata similaritatea dintre ele. Pasi:
  1. definirea MDP-ului pentru sarcina data;
  2. esantionarea tuplurilor (stare, actiune, recompensa, stare urmatoare) din ambele medii, sub politica operationala existenta, fara explorare suplimentara;
  3. estimarea celor doua MDP-uri din date;
  4. calculul fidelitatii si al garantiei de performanta.
- Pentru agenti bazati pe LLM, prompt-ul este rezumat de LLM intr-un embedding latent compact (II.C).
- **DT-BSM (DT-bisimulation metric)** [13]: un scor scalar bazat pe distanta Wasserstein, care masoara discrepantele pe termen lung in P si R. Complexitatea minima este O(|A||S|²). Stabileste o margine superioara a pierderii de performanta la deployment, ca suma liniara intre pierderea de antrenare a agentului si DT-BSM (II.C).
- **Aplicatii** (III):
  - DT la nivel de MDP: complexitatea de esantionare da un criteriu de oprire pentru colectarea datelor; pentru DT-uri bazate pe retele neuronale, evaluarea poate fi folosita la tuning sau ca regularizare;
  - DT la nivel de sistem: alegerea combinatiei de modele (canal, mobilitate, trafic) si a granularitatii (de exemplu rezolutia hartii radio), ca echilibru intre fidelitate si cost (Fig. 3).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Testbed wireless real (IV, Fig. 4): un gNB si trei UE (camera de supraveghere si laptop de gaming conectate prin 5G-CPE, smartphone de livestreaming), cu trafic uplink cu caracteristici diferite.
- Sarcina: agentul RL aloca resource blocks intre cele trei UE la fiecare pas, pentru a maximiza throughput-ul total ponderat.
- 36 de ore de date operationale colectate de pe testbed. Pe baza lor au fost construite 100 de DT-uri candidate cu setari diferite (latimea si adancimea retelei neuronale, numarul de episoade de antrenare).
- Pentru fiecare DT: DT-BSM si, pentru comparatie, pierderea de predictie one-step a traficului UE (acuratete la nivel de model). Un agent este antrenat pana la convergenta in fiecare DT si apoi desfasurat pe testbed.

## Experimente si metrici
- Corelatia dintre DT-BSM, respectiv pierderea de predictie, si performanta politicii desfasurate (throughput ponderat) (Fig. 5a).
- Pre-filtrarea DT-urilor (top 5% dupa DT-BSM) comparata cu brute-force (toate cele 100) si cu trei baseline-uri de filtrare: aleator, recompensa de antrenare in DT, acuratete la nivel de model. Metrici: costul de antrenare si costul de testare, definit ca pierderea de performanta din folosirea politicilor testate in locul celei optime (Fig. 5b).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Exista o corelatie liniara: un DT-BSM mai mic da o performanta mai buna in cel mai rau caz. Pierderea de predictie are o corelatie vizibil mai slaba; unele DT-uri cu pierdere mica dau politici slabe (Fig. 5a).
- Pre-filtrarea pe top 5% duce la o politica finala comparabila cu optimul gasit prin brute-force. Costul de antrenare scade cu 95%, iar cel de testare cu peste 97%. Baseline-urile de filtrare nu exclud consecvent DT-urile slabe si pot elimina DT-urile cele mai bune (Fig. 5b).

## Limitari declarate de autori
- Marginea de performanta este unilaterala: controleaza pierderea in cel mai rau caz pentru DT-urile cu fidelitate mare, dar nu ce poate produce intamplator un DT cu fidelitate mica (IV).
- Pentru spatii de stare foarte mari este necesara abstractizarea starilor (II.C).
- Directii viitoare (V):
  - sincronizare DT declansata de valoarea de mismatch (evaluation-in-the-loop);
  - predictia transferabilitatii unui DT intre medii (de exemplu SAGIN);
  - antrenare RL care tine cont de mismatch.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nedeclarat - testbed cu gNB si 5G-CPE; core-ul nu este descris (IV).
- UE reale sau emulate?: reale - camera, laptop prin 5G-CPE, smartphone (IV, Fig. 4).
- digital twin al retelei?: da - 100 de DT-uri candidate construite din 36 de ore de date reale; cadru de evaluare a fidelitatii (IV).
- prezice efectul unei actiuni inainte de a o aplica?: da - DT-BSM da o margine pentru pierderea de performanta a unei politici antrenate in DT inainte de deployment (II.C, Fig. 5a).
- executa actiuni automat (bucla inchisa)?: da (pe testbed) - agentii RL desfasurati aloca resource blocks pe testbed-ul real (IV).
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: partial - scorurile DT-BSM sunt calculate inainte de antrenarea si deployment-ul agentilor si apoi comparate cu performanta masurata (IV); nu este declarat un protocol pre-inregistrat.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: partial - throughput ponderat al UE pe testbed (Fig. 5); nu inregistrari sau sesiuni.
- observa traficul la SCP / proxy?: nu.
