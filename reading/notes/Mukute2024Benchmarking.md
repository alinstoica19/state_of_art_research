# Control Plane Performance Benchmarking and Feature Analysis of Popular Open-Source 5G Core Networks: OpenAirInterface, Open5GS, and free5GC (2024)
Cheie: Mukute2024Benchmarking . DOI/link: https://doi.org/10.1109/access.2024.3441725 . Sursa textului: integral: PDF editor, IEEE Access (open access, licenta CC conform Crossref)
Sectiunea din plan: C . Tema: core open-source / benchmarking control plane
Autori: Tariro Mukute, Lusani Mamushiane, Albert A. Lysko, Elena-Ramona Modroiu, Thomas Magedanz, Joyce Mwangama (University of Cape Town; CSIR; TU Berlin). IEEE Access, vol. 12, 2024, pp. 113336 si urmatoarele. Artefacte (Ansible, generator de trafic, notebook-uri) publicate pe GitHub.

## Problema (cum o formuleaza autorii)
Exista mai multe implementari 5GC open-source compatibile 3GPP (OAI, free5GC, Open5GS, Open5GCore), care ruleaza pe diverse NFVI (containere, pod-uri, VM-uri). Un VNF ruleaza peste kernel-ul Linux, ceea ce ii degradeaza performanta fata de un NF hardware (V). Autorii vor sa compare maturitatea (suportul pentru operatiile NF si procedurile 5G) si performanta la runtime a control plane-ului, si sa explice diferentele prin arhitectura software (I, II).

## Ce propun (metoda, pe scurt)
- **Evaluare bazata pe functionalitati:** un cadru care coreleaza operatiile de serviciu ale NF-urilor cu procedurile 5G din Release 17, pentru a evalua cat de complet este suportata fiecare procedura (Tabelul 3, Anexa A, Fig. 14-16). Comunitatea si adoptia (Tabelul 1), cerintele hardware si licentele (Tabelul 2). Rezultatele detaliate sunt publicate pe un site.
- **Macro-benchmarking:** timpul in care un numar dat de UE finalizeaza inregistrarea si de-inregistrarea; RTT-ul asocierii SCTP (I, VII.A).
- **Micro-benchmarking:** latenta si frecventa apelurilor de sistem facute de 5GC si procesele care le genereaza, masurate cu BCC (BPF Compiler Collection), plus profiling si tracing (I, VII.B).
- Pe baza corelatiei macro/micro, autorii formuleaza recomandari de arhitectura software pentru fiecare core (VII.B, VIII).
- **Generator de trafic propriu**, pentru ca UERANSIM da segmentation fault la 200 de UE, my5G-RANTester nu suporta sesiuni simultane, iar niciunul nu raporteaza metrici de performanta (VI.B).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- 5GC si generatorul de trafic ruleaza in VM-uri pe OpenStack (stable/zed), pe un PC cu i7 2,5 GHz, 16 GB RAM, 8 nuclee si HDD de 200 GB. VM-urile au Ubuntu 20.04, kernel 5.4, cu resursele minime recomandate pentru fiecare core. Legatura dintre VM-uri trece printr-un VPN, despre care autorii spun ca poate afecta performanta (VI.B).
- Inregistrari de UE trimise in rafala. Rezultatele sunt aratate pana la 300 de UE, maximul suportat de free5GC. OAI cadea initial la sarcina mare din cauza log-urilor NAS care nu puteau fi oprite; problema a fost raportata si rezolvata de echipa OAI (tag-ul 2023.w12) (VII).
- Setup-ul este automatizat cu Ansible pentru reproducere (VI.B).

## Experimente si metrici
- Timpul total si mediu per UE pentru inregistrare si de-inregistrare, in functie de numarul de UE (Fig. 3).
- Apeluri de sistem pe categorii (Fig. 4); multiplexare I/O (select, poll, epoll_wait; Tabelele 5-6); futex; socket send; sched_yield (Fig. 8-12).
- Sinteza tiparelor de utilizare: numarul cumulat de apeluri versus rata de crestere cu numarul de UE, cu latenta ca raza a bulei (Fig. 13).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Macro: Open5GS are cea mai buna performanta, urmat de free5GC si apoi OAI (VII.A, Fig. 3; valorile absolute sunt doar in figura). In limitele studiului, timpul de inregistrare creste liniar cu numarul de UE (IX).
- Micro:
  - toate cele trei core-uri au latenta considerabila in apelurile futex (VII.B.1);
  - Open5GS si OAI folosesc select, iar free5GC foloseste epoll_wait si poll (VII);
  - free5GC foloseste sched_yield, pe care autorii il considera posibil inutil pe Linux sau un semn de software legacy (IX);
  - Open5GS are apelurile si procesele concentrate in cadranul de jos-stanga al Fig. 13 (crestere proportionala sau mai mica a resurselor cu numarul de UE);
  - OAI face apeluri read blocante de doua ori mai des decat free5GC face apelurile din cadranele din dreapta, diferenta pe care autorii o leaga de diferenta de performanta (VIII).
- Recomandari: optimizarea multiplexarii I/O (de exemplu epoll in mod edge-triggered), apeluri non-blocante, reducerea contentiei pe memorie partajata si pe lock-uri (VII.B, IX).
- Tabelele 1-3 (adoptie, hardware si licente, numarul de operatii suportate) sunt imagini in PDF; valorile lor nu sunt disponibile in textul extras.

## Limitari declarate de autori
- Este evaluata doar inregistrarea si de-inregistrarea; alte proceduri de control plane raman lucrare viitoare (IX).
- VM-uri in loc de hardware dedicat, din lipsa de hardware; VPN-ul dintre VM-uri poate influenta testele (VI.B).
- Scara este limitata la 300 de UE de capacitatea free5GC (VII).
- Lucrari viitoare: benchmarking in pipeline-uri CI, aliniere cu specificatia ETSI NFV de benchmarking a NFVI, comparatie cu Open5GCore (IX).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - OAI, free5GC si Open5GS in VM-uri OpenStack (VI.B).
- UE reale sau emulate?: emulate - generator de trafic propriu, cu UE si gNB emulate (VI.B).
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu.
- executa actiuni automat (bucla inchisa)?: nu.
- multi-site / geo-redundanta / failover de baza de date?: nu.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: da - timpul de inregistrare si de-inregistrare pentru pana la 300 de UE emulate (Fig. 3).
- observa traficul la SCP / proxy?: nu - observatia se face la nivel de apeluri de sistem pe VM-ul core-ului.
