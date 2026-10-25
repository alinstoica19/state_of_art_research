# Orchestrating Cross-Layer Anomaly Detection and Mitigation to Address Gray Failures in Large-Scale Cloud Infrastructure (2025)
NOTA: nota scrisa doar din rezumat; textul integral nu este disponibil din surse libere legale.
Cheie: Li2025Panacea . DOI/link: https://doi.org/10.1109/aiops66738.2025.00008 . Sursa textului: DOAR REZUMAT (OpenAlex)
Sectiunea din plan: C . Tema: anomalii/RCA / gray failures cloud
Autori: Ze Li, Chang Lou, Vignatha Yenugutala, Vivek Ramamurthy, Eion Blanchard, Minghua Ma, Murali Chintalapati. AIOps 2025 (conform DOI).

## Problema (cum o formuleaza autorii)
Infrastructura cloud de productie are permanent gray failures: o stare degradata, nedetectata de mecanismele sistemului, care afecteaza totusi utilizatorii finali. Tratarea anomaliilor de pe nodurile gazda este esentiala. Doua limitari ale abordarilor curente: detectia foloseste doar semnale dintr-o singura dimensiune a gazdei, cu viziune partinitoare din cauza observabilitatii diferentiale; mitigarea consta mai ales in operatii la nivel de gazda (reboot), iar majoritatea problemelor de productie raman pentru interventie manuala (rezumat).

## Ce propun (metoda, pe scurt)
Panacea: cadru holistic care detecteaza si mitigheaza automat anomaliile gazdelor. Agrega si coreleaza informatii din VM-uri si din nivelul aplicatiilor, pentru a acoperi golul de detectie, si orchestreaza mitigari fine si sigure pe toate nivelurile. Este proiectat pentru o gama larga de anomalii (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Desfasurat in productie pe milioane de gazde (rezumat). Furnizorul de cloud nu este numit in rezumat.

## Experimente si metrici
Nedeclarat in rezumat.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
Nedeclarat in rezumat (nu sunt raportate cifre, in afara scarii de deployment).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - infrastructura cloud generica, nu core 5G (rezumat).
- UE reale sau emulate?: nu se aplica - utilizatori de cloud (rezumat).
- digital twin al retelei?: nu - nementionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: da - detectie si mitigare automate, orchestrate pe mai multe niveluri, in productie (rezumat).
- multi-site / geo-redundanta / failover de baza de date?: nedeclarat - milioane de gazde; multi-site si failover nementionate explicit (rezumat).
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nedeclarat - rezumatul vorbeste de impactul gray failures asupra utilizatorilor, fara metrici.
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
