# SENTINEL: Self Protecting 5G Core Control Plane from DDoS Attacks for High Availability Service (2023)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Chilukuri2023Sentinel . DOI/link: https://doi.org/10.1109/comsnets56262.2023.10041318 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Inovatiile din network slicing 5G aduc un numar mare de utilizatori si servicii din 5GC, dar deschid usa amenintarilor de securitate care pot afecta functionarea 5GC si utilizatorii legitimi (rezumat). Problema tratata este protejarea plan-ului de control al 5GC de atacuri DDoS ale utilizatorilor malitiosi, pastrand High Availability (HA) pentru utilizatorii legitimi (rezumat).

## Ce propun (metoda, pe scurt)
- SENTINEL: un 5GC autoprotejat in plan de control, bazat pe paradigma Self Organizing Network (SON) (rezumat).
- Framework autonom care protejeaza plan-ul de control de atacuri DDoS (rezumat).
- Implementare ca framework bazat pe Hierarchical Temporal Memory (HTM), impreuna cu un agregator de slice bazat pe XDP si eBPF (rezumat).
- Izoleaza utilizatorii suspecti de 5GC (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Unelte mentionate: HTM, eXpress Data Path (XDP), extended Berkeley Packet Filter (eBPF) (rezumat).
- Testbed, scara si date: nedeclarat in rezumat.

## Experimente si metrici
- Nedeclarat in rezumat, cu exceptia sensibilitatii de izolare a utilizatorilor suspecti (rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Sensibilitatea de izolare a utilizatorilor suspecti: 85.59% (rezumat; fara trimitere la tabel/figura in rezumat).
- Rezumatul afirma ca HA pentru utilizatorii legitimi ramane intact, fara resurse suplimentare; nu sunt date cifre (rezumat).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nedeclarat - rezumatul nu spune daca 5GC este implementat sau modelat (rezumat).
- UE reale sau emulate? nedeclarat (rezumat).
- digital twin al retelei? nu - nu este mentionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica? nedeclarat (rezumat).
- executa actiuni automat (bucla inchisa)? da - framework autonom care izoleaza automat utilizatorii suspecti din 5GC (rezumat).
- multi-site / geo-redundanta / failover de baza de date? nedeclarat (rezumat).
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat (rezumat).
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nedeclarat - rezumatul vorbeste de izolarea utilizatorilor, fara metrici per inregistrare sau sesiune (rezumat).
- observa traficul la SCP / proxy? nedeclarat (rezumat).
