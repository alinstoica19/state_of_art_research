# Mobility Prediction for 5G Core Networks (2021)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Jeong2021Mobilityprediction . DOI/link: https://doi.org/10.1109/mcomstd.001.2000046 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: A

## Problema (cum o formuleaza autorii)
Rezumatul spune ca mobilitatea este un factor esential in nucleul 5G. Daca planul de control poate prezice mobilitatea, operarea poate deveni mai eficienta, cu decizii proactive. Modelele de mobilitate au fost studiate pe seturi de date din retele celulare, iar 3GPP a initiat specificarea unei arhitecturi de nucleu pentru analiza datelor si ML.

## Ce propun (metoda, pe scurt)
O taxonomie a cadrelor de predictie a mobilitatii in nucleele 5G, de la colectarea datelor pana la servirea modelelor, tinand cont de arhitectura si interfetele 3GPP. Sunt introduse doua cazuri de utilizare cheie in nucleele 5G. Una dintre metodele propuse este paging adaptiv asistat de ML.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Tip de testbed (real, emulat sau simulat): date din "live networks" (retele in functiune).
Unelte: nedeclarate in rezumat.
Scara: nedeclarata in rezumat.
Date: seturi de date din retele live.

## Experimente si metrici
Evaluarea castigurilor din predictia mobilitatii pe seturi de date din retele live, pentru cele doua cazuri de utilizare. Metrica explicit mentionata este overhead-ul de semnalizare.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Metoda de paging adaptiv asistat de ML "reduces signaling overhead by up to 75 percent". Rezumatul nu contine trimitere la tabel/figura.

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nedeclarat - (rezumat): taxonomie a cadrelor in nucleele 5G; nu este precizat ce nucleu sau implementare s-a folosit.
- UE reale sau emulate? nedeclarat - (rezumat)
- digital twin al retelei? nedeclarat - (rezumat)
- prezice efectul unei actiuni inainte de a o aplica? nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)? nedeclarat - (rezumat): sunt mentionate decizii proactive, fara bucla inchisa explicita.
- multi-site / geo-redundanta / failover de baza de date? nedeclarat - (rezumat)
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nedeclarat - (rezumat): metrica raportata este overhead-ul de semnalizare; inregistrarile sau sesiunile nu sunt mentionate.
- observa traficul la SCP / proxy? nedeclarat - (rezumat)
