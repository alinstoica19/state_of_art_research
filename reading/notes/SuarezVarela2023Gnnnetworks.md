# Graph Neural Networks for Communication Networks: Context, Use Cases and Opportunities (2023)
Cheie: SuarezVarela2023Gnnnetworks . DOI/link: https://doi.org/10.1109/mnet.123.2100773 . Sursa textului: integral: arXiv 2112.14792v2 (27 iulie 2022; acceptat in IEEE Network)
Sectiunea din plan: C . Tema: modele de retea (GNN, pozitie/tutorial)
Autori: Jose Suarez-Varela, Paul Almasan, Miquel Ferriol-Galmes, Albert Cabellos-Aparicio, Pere Barlet-Ros (UPC / Barcelona Neural Networking Center), Krzysztof Rusek (AGH), Fabien Geyer (TUM), Xiangle Cheng, Xiang Shi, Shihan Xiao (Huawei), Franco Scarselli (Univ. Siena). IEEE Network, 2023.

## Problema (cum o formuleaza autorii)
- Modelarea retelei permite predictia KPI-urilor (latenta, jitter, pierderi) pentru configuratii noi si, cuplata cu un optimizator, controlul autonom.
- Modelele analitice (fluide, teoria cozilor) reproduc limitat retelele reale. Simulatoarele pe evenimente discrete (ns-3, OMNeT++) nu scaleaza si sunt prea lente pentru optimizare online.
- Retelele neuronale clasice (fully-connected, CNN, autoencoders) nu generalizeaza pe date relationale de retea. Lucrarea de pozitie propune GNN-urile ca instrument fundamental (Introducere).

## Ce propun (metoda, pe scurt)
- Tutorial despre arhitectura GNN in nomenclatura MPNN, in trei faze (Fig. 1):
  1. initializarea starilor nodurilor;
  2. message passing (message, aggregation, update);
  3. readout.
- O arhitectura generica de optimizare SDN cu model GNN, in mod open-loop (cu operator) sau closed-loop (Fig. 3).
- Doua exemple implementate cu IGNNITION:
  - RouteNet pentru retele cu fir;
  - WCGCN pentru managementul resurselor radio.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- **RouteNet:**
  - intrari: topologia, matricea de trafic si configuratia de rutare; iesiri: KPI per flux;
  - antrenat pe 177.500 de esantioane simulate (OMNeT++) in NSFNET (14 noduri) si Germany50 (50 de noduri);
  - testat pe 40.000 de esantioane din NSFNET, Germany50 si o topologie nevazuta, GBN (17 noduri).
- **WCGCN:** controlul puterii; antrenat pe 1.000 de esantioane cu 50 de link-uri si evaluat pe retele cu 50-400 de link-uri, fata de WMMSE (100 de iteratii).

## Experimente si metrici
- RouteNet: Mean Relative Error (MRE) pentru intarzierea per flux, fata de etichetele OMNeT++, comparat cu un NN fully-connected (Fig. 4).
- WCGCN: suma ratelor normalizata fata de WMMSE (Fig. 5).
- Pentru ambele: timpul de executie.

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- RouteNet: MRE sub 3% pe toate seturile de test, inclusiv GBN, topologie nevazuta la antrenare. NN-ul fully-connected are erori mai mari, cu MRE de aproximativ 35% pe GBN (Fig. 4).
- RouteNet evalueaza un esantion Germany50 in 65 ms in medie; OMNeT++ are nevoie de peste 10 minute per esantion.
- WCGCN: performanta similara cu WMMSE pana la 400 de link-uri (aproximativ +4%) (Fig. 5); 16 ms in medie la 400 de link-uri, fata de peste 10 s pentru WMMSE.

## Limitari declarate de autori
- GNN-urile sunt la un nivel scazut de maturitate tehnologica.
- Generalizarea la retele reale mari (sute sau mii de noduri) este limitata, de exemplu de over-smoothing in agregare.
- Incertitudinea modelelor probabilistice este o problema pentru infrastructuri critice. Solutii propuse: explicabilitate, NN bayesiene, teste care sa determine intervalele de operare sigure inainte de deployment, cu certificare.
- Fiecare caz de utilizare cere un design GNN specific (sectiunea Opportunities and Open Challenges).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu - retele cu fir simulate in OMNeT++ si retele wireless modelate.
- UE reale sau emulate?: nu.
- digital twin al retelei?: nu folosesc termenul; RouteNet este prezentat ca model de retea pentru analiza what-if (Example Use-Cases).
- prezice efectul unei actiuni inainte de a o aplica?: da (capabilitate) - RouteNet estimeaza KPI-urile pentru configuratii alternative (what-if); experimentele masoara acuratetea predictiei, nu decizii aplicate.
- executa actiuni automat (bucla inchisa)?: propus - arhitectura de optimizare closed-loop (Fig. 3); nu este evaluata in lucrare.
- multi-site / geo-redundanta / failover de baza de date?: nu (recuperarea rapida la caderea unui link este mentionata ca use case din [1]).
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu - intarzierea per flux, din simulare.
- observa traficul la SCP / proxy?: nu.
