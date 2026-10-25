# PP5GS - An Efficient Procedure-Based and Stateless Architecture for Next-Generation Core Networks (2023)
NOTA: nota scrisa doar din rezumat; exista o versiune submitted in repository-ul institutional mediaTUM (mediatum.ub.tum.de/1695118), dar serverul nu a raspuns (timeout la doua incercari) din acest mediu; textul integral nu a fost obtinut.
Cheie: Goshi2023Pp5Gs . DOI/link: https://doi.org/10.1109/tnsm.2022.3230206 . Sursa textului: DOAR REZUMAT (OpenAlex)
Sectiunea din plan: C . Tema: SBA / arhitectura core stateless
Autori: Endri Goshi, Raffael Stahl, Hasanin Harkous, Mu He, Rastin Pries, Wolfgang Kellerer. IEEE Transactions on Network and Service Management (online 2022).

## Problema (cum o formuleaza autorii)
SBA a schimbat proiectarea si operarea core-ului 5G si este primul pas spre deployment-uri cloud-native. Gradul mare de descompunere functionala din SBA creste traficul de semnalizare intre NF-uri in timpul procedurilor de control plane si complica orchestrarea unui sistem cu dependente stranse intre NF-uri (rezumat).

## Ce propun (metoda, pe scurt)
PP5GS: arhitectura core 5G stateless, cu descompunere functionala pe proceduri. Sunt dezvoltate NF-uri per procedura (Per-Procedure NFs) pentru patru proceduri de control plane (rezumat).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Evaluari intr-un cloud privat orchestrat cu Kubernetes (rezumat). Baseline-uri: un sistem stateful si unul stateless. Generatorul de UE si scara sunt nedeclarate in rezumat.

## Experimente si metrici
Resurse de calcul, trafic de semnalizare, timpul de finalizare a procedurilor, fezabilitatea edge-offloading-ului NF-urilor (rezumat).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
PP5GS foloseste cu pana la 34% mai putine resurse de calcul decat baseline-ul stateful si cu pana la 55% mai putine decat cel stateless. Genereaza cu cel putin 40% mai putin trafic de semnalizare. Procedurile complexe se finalizeaza cu pana la 50% mai repede. Autorii spun ca PP5GS este mai potrivit pentru edge-offloading-ul NF-urilor core (rezumat).

## Limitari declarate de autori
Nedeclarat in rezumat.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - NF-uri per procedura implementate si desfasurate pe Kubernetes (rezumat).
- UE reale sau emulate?: nedeclarat - (rezumat)
- digital twin al retelei?: nu - nementionat in rezumat.
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat - (rezumat)
- executa actiuni automat (bucla inchisa)?: nu - propunere de arhitectura (rezumat).
- multi-site / geo-redundanta / failover de baza de date?: partial - edge-offloading al NF-urilor este evaluat; failover nementionat (rezumat).
- evaluare prospectiva (predictie fixata inainte de experiment)?: nedeclarat - (rezumat)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: partial - timpul de finalizare a procedurilor de control plane (rezumat).
- observa traficul la SCP / proxy?: nedeclarat - (rezumat)
