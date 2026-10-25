# Fault Diagnosis Using Hybrid Transfer Learning for VNF-based 5G Core Networks (2024)
NOTA: nota scrisa doar din rezumat; textul integral indisponibil.
Cheie: Zhu2024Transferlearning . DOI/link: https://doi.org/10.1109/nfv-sdn61811.2024.10807503 . Sursa textului: DOAR REZUMAT
Sectiunea din plan: B

## Problema (cum o formuleaza autorii)
Autorii spun ca diagnosticul defectelor in 5GC a fost investigat pe larg cu ML, dar solutiile ML intampina dificultati precum disponibilitatea limitata a datelor despre defecte si adaptabilitatea scazuta la schimbarile de mediu.

## Ce propun (metoda, pe scurt)
O abordare hibrida de transfer learning (TL) pentru diagnosticul defectelor de retea in 5GC, care combina model-based TL, instance-based TL si feature-based TL. Autorii spun ca, spre deosebire de TL-ul traditional bazat pe un singur model, metoda lor foloseste cunostintele inerente din datele 5GC si previne transferul negativ ("negative transfer") in caracteristici si in instantele de date.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Autorii construiesc un "scale-out 5G testbed" pentru a genera suficiente date din domeniul sursa, si colecteaza o cantitate mica de date din domeniul tinta dintr-un "real 5GC network setting" (mediu real de retea 5GC). Sarcina: clasificarea defectelor de retea intre diferite functii de retea virtualizate (VNF) din 5GC. Unelte si scara exacta: nedeclarate in rezumat.

## Experimente si metrici
Comparatie cu metode fara TL si cu TL conventional bazat pe model. Metrica mentionata: scorul F1.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Hybrid TL ofera o acuratete "significantly higher" in termeni de scor F1, fata de metodele fara TL si fata de TL conventional bazat pe model.
- Pentru fiecare eticheta de retea, 70 % dintre etichete au un scor F1 mai mare de 0.9.
Trimitere la tabel/figura: nedeclarat in rezumat.

## Limitari declarate de autori
nedeclarat in rezumat

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nedeclarat - (rezumat): se mentioneaza un testbed 5G scalabil si un "real 5GC network setting", fara detalii despre implementarea core-ului.
- UE reale sau emulate? nedeclarat - (rezumat): nu se specifica.
- digital twin al retelei? nedeclarat - (rezumat): nu se mentioneaza.
- prezice efectul unei actiuni inainte de a o aplica? nu - (rezumat): lucrarea descrie clasificarea defectelor, nu predictia efectului unei actiuni.
- executa actiuni automat (bucla inchisa)? nedeclarat - (rezumat): nu se mentioneaza.
- multi-site / geo-redundanta / failover de baza de date? nedeclarat - (rezumat): nu se mentioneaza.
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat - (rezumat): nu se mentioneaza.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nedeclarat - (rezumat): clasificarea se face intre VNF-uri; rezumatul nu spune la ce nivel sunt masurate rezultatele.
- observa traficul la SCP / proxy? nedeclarat - (rezumat): nu se mentioneaza.
