# Enabling simulation services for digital twins of 5G/B5G mobile networks (2024)
Cheie: Nardini2024Simu5Gdt . DOI/link: https://doi.org/10.1016/j.comcom.2023.10.017 . Sursa textului: integral: PDF din repository-ul institutional ARPI (Universita di Pisa); Unpaywall o eticheteaza submittedVersion, dar fisierul are paginatia revistei (Computer Communications 213 (2024) 33-48)
Sectiunea din plan: C . Tema: digital twin / simulare what-if
Autori: Giovanni Nardini, Giovanni Stea (Universita di Pisa). Computer Communications, vol. 213, 2024, pp. 33-48.

## Problema (cum o formuleaza autorii)
- DT-urile retelelor mobile (DTMN) pentru 5G si dupa trebuie sa sustina reconfigurarea dinamica si anticiparea defectelor. Autorii sustin ca simulatoarele de retea cu evenimente discrete trebuie integrate in DTMN ca servicii: ofera analiza what-if si rezultate interpretabile fara antrenare, inclusiv in scenarii putin probabile sau netestate. Pot rula si in timp real (emulare) sau mai repede decat timpul real (I).
- Simularea si ML sunt prezentate ca complementare: simulatorul poate genera date de antrenare pentru conditii ipotetice, iar modelele ML pot accelera simularea subsistemelor mari (I).
- Provocari specifice DTMN (Sectiunea 3):
  - scara spatiala (un DT per gNB sau per cluster; retea de DT-uri cu probleme de sincronizare);
  - ce primeste DTMN-ul ca intrare: la un capat toata starea masinilor de stare, la celalalt doar intrarile externe cu modele interne, cu checkpointing intre ele;
  - interfete standardizate fizic-digital si overhead-ul transmiterii datelor;
  - securitate: interfata de control catre reteaua fizica poate deveni un backdoor, iar informatia din DTMN poate fi folosita pentru pregatirea atacurilor;
  - gazduire: MEC este propus pentru latenta mica si control de catre operator.

## Ce propun (metoda, pe scurt)
- **Doua tipuri de analiza what-if** (4.2, Fig. 5):
  - Lockstep (LWI): o singura simulare evalueaza simultan politicile alternative la fiecare perioada, pe intrarile reale. Poate rula in timp real, dar rezultatul politicilor nu influenteaza starea simulata, deci nu poate evalua metrici cu durata in timp (fairness, intarziere medie);
  - Branching (BWI): starea curenta este copiata in instante separate, una per politica, care evolueaza independent pana la un checkpoint. Cere mai mult calcul, dar permite metrici temporale si replici independente pentru intervale de incredere.
- **DTMN Simulation Service (DTMN-SS)** (4.3, Fig. 6-7), compatibil cu arhitectura DTN discutata in IETF [10]:
  - expune un API RESTful cu resursele: mediul de simulare, topologia retelei, parametrii retelei, metricile de iesire si campania de simulare;
  - parametrizarea poate folosi date in timp real, date istorice, date date de client sau o combinatie;
  - verifica la managementul DTMN daca exista resurse de calcul inainte de a crea un model.
- **Proof-of-concept** (5.2): server HTTP in C++ (libhttpserver), sesiuni per client prin cookie; genereaza fisiere NED/INI pentru OMNeT++/Simu5G si extrage metricile cu scavetool, raportand media, varianta, deviatia standard si intervalul de incredere 95% in JSON.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Simulare cu OMNeT++ si Simu5G. Nu exista retea reala: autorii spun ca nu au avut o retea mobila reala din care sa extraga date, deci folosesc un data repository cu date pentru o retea "toy" (5.3.1).
- What-if: un gNB observat plus trei gNB interferenti; UE cu trafic downlink de la un server remote prin core; 10 minute si 30 de checkpoint-uri de 20 s; numarul si pozitia UE generate aleator (deplasare 0-50 m intre checkpoint-uri) (5.3.1, Fig. 15-16).
- Orchestrare MEC: un gNB si doua MEC host-uri (500 si 5000 MIPS), cel de-al doilea mai departe, prin mai multe UPF-uri, cu o intarziere suplimentara aleatoare de 5-10 ms (5.3.2, Fig. 19).
- Generare de date: 100 de UE, fiecare cu 200 kB/s, o simulare de 86.400 s (o zi) (5.3.3, Fig. 23-24).

## Experimente si metrici
- What-if BWI pentru carrier aggregation: CA-1CC vs. CA-2CC. Metrici: throughput-ul celulei la MAC si consumul de putere al gNB, cu modelul P = N_CC x P0 + delta_p x Pmax x chi (P0 = 114,5 W, delta_p = 588,1 W, Pmax = 1 W) (Fig. 17-18).
- MEC: RTT estimat pentru fiecare cerere de instantiere pe fiecare host (Fig. 20) si incarcarea host-urilor (Fig. 21).
- Generarea unui set de date sintetic pentru un serviciu de antrenare ML (fara metrici de calitate a modelului).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- CA: in primele 12 checkpoint-uri (4 minute) throughput-ul este acelasi pentru ambele politici, iar CA-2CC consuma mai multa putere. Dupa aproximativ 5 minute, CA-1CC atinge limita de 1,8 Mbps, iar CA-2CC obtine throughput mai mare cu putere usor mai mare. Dupa checkpoint-ul 27, CA-1CC redevine preferabila (5.3.1, Fig. 17-18).
- MEC: la prima cerere, RTT-ul pe MEC Host 1 este aproximativ jumatate din cel pe MEC Host 2. La cererea a sasea, MEC Host 1 devine mai lent, iar aplicatia este plasata pe MEC Host 2. Dupa cererea a noua, MEC Host 2 ofera RTT mai mic pentru toate aplicatiile (5.3.2, Fig. 20).

## Limitari declarate de autori
- Prototipul este evaluat pe date sintetice ale unei retele "toy", fara retea fizica (5.3.1).
- Lucrari viitoare: modele de simulare multi-scala, cu cerinte diferite de viteza si acuratete, si orchestrarea instantelor de simulare pentru folosirea eficienta a resurselor de calcul (6).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - core-ul este modelat in Simu5G (UPF-uri in scenariul MEC); nu exista core real (5.3).
- UE reale sau emulate?: simulate - UE in Simu5G, cu numar si pozitii generate aleator (5.3.1).
- digital twin al retelei?: da (cadru propus) - serviciu de simulare in DTMN; prototipul nu este conectat la o retea fizica (4.3, 5.3.1).
- prezice efectul unei actiuni inainte de a o aplica?: da (in simulare) - analiza BWI compara CA-1CC si CA-2CC, iar orchestratorul MEC estimeaza RTT-ul pe fiecare host inainte de instantiere (5.3.1, 5.3.2).
- executa actiuni automat (bucla inchisa)?: partial - in scenariul MEC, orchestratorul alege automat host-ul pe baza simularii; pentru CA, aplicarea politicii pe reteaua fizica este descrisa ca posibila, nu implementata (5.3).
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: partial - RTT per aplicatie MEC si throughput-ul celulei, in simulare (Fig. 17, 20).
- observa traficul la SCP / proxy?: nu.
