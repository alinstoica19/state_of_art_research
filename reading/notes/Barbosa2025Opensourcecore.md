# Open-Source 5G Core Platforms: A Low-Cost Solution and Performance Evaluation (2025)
Cheie: Barbosa2025Opensourcecore . DOI/link: https://doi.org/10.1109/icoin63865.2025.10992769 . Sursa textului: integral: arXiv 2412.21162v1 (30 decembrie 2024)
Sectiunea din plan: C . Tema: core open-source / benchmarking
Autori: Maria Barbosa, Marcelo Silva, Ednelson Cavalcanti, Kelvin Dias (Universidade Federal de Pernambuco, Brazilia). ICOIN 2025.

## Problema (cum o formuleaza autorii)
Platformele 5GC open-source (Free5GC, OpenAirInterface, Open5GS, SD-Core) urmeaza specificatiile 3GPP, dar in stadii diferite de release si cu modele de implementare diferite, deci pot avea performante diferite pe control plane si data plane. Dupa autori, nicio lucrare anterioara nu a analizat calitativ toate cele patru platforme si nu le-a comparat performanta intr-un singur studiu experimental; lucrarile anterioare au folosit doar simulare (I, IV, Tabelul II).

## Ce propun (metoda, pe scurt)
- **Analiza calitativa** a celor patru platforme (III, Tabelul I): release 3GPP, modelul de comunicare intre NF-uri, dificultatea de instalare si de configurare (scala 1-4, definita de autori), limbaj, infrastructura de virtualizare si functii suportate (MEC, NEF, DPDK, P4, WebUI, monitorizare, VoNR, dispozitive non-3GPP).
- **Prototip low-cost 5G SA** pentru evaluarea cantitativa a Free5GC, Open5GS si OAI (V). SD-Core este exclus din evaluarea de performanta pentru ca suporta doar pod-uri Kubernetes, iar celelalte ruleaza in Docker.

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
- Testbed real (V, Fig. 4, Tabelul III):
  - gNodeB OAI in container, pe placa SDR Ettus B210 (USB 3.0) cu antena Ettus Log Periodic;
  - server Intel Xeon Gold 5215, 96 GB RAM, Ubuntu 20.04.6, Docker 24.0.5, Docker Compose 2.20.2;
  - UE real: telefon Motorola Edge 20 cu SIM Sysmocom.
- Data plane: iperf3 (download/upload), ping (latenta) si o aplicatie video (server Flask conectat la UPF prin N6; client Android care descarca Big Buck Bunny 4K 60 fps) (VI.B).
- 30 de esantioane pentru fiecare test CP si UP si 50 pentru consumul de resurse, pentru interval de incredere 95% (VI).

## Experimente si metrici
- Control plane: timpul de inregistrare a UE (deltaTr, AMF) si timpul de stabilire a sesiunii PDU (deltaTs, SMF) (Fig. 5-6).
- Data plane: throughput, latenta, timp de incarcare video (Tabelul IV, Fig. 7-8).
- CPU si RAM medii pentru CP si UP (Fig. 9).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- **Tabelul I** (calitativ):

| Parametru | Free5GC | OAI | Open5GS | SD-Core |
|---|---|---|---|---|
| Release 3GPP | Rel-15 | Rel-16 | Rel-17 | Rel-16 |
| Comunicare NF | Model B | Model B | Model C | Model B |
| Dificultate instalare (1-4) | 1 | 3 | 2 | 4 |
| Dificultate configurare (1-4) | 2 | 4 | 1 | 3 |
| Limbaj | Go | C++ | C | Go |

- Niciuna dintre platforme nu ofera NWDAF (III).
- **Control plane** (Fig. 5-6): Open5GS are cei mai mici deltaTr si deltaTs. deltaTr este cu aproximativ 13% mai mare la Free5GC si cu 40% mai mare la OAI. deltaTs este cu aproximativ 11% mai mare la Free5GC si cu 17% mai mare la OAI (valorile absolute sunt doar in figuri).
- **Tabelul IV** (medie / deviatie standard):

| Platforma | Download (Mbps) | Upload (Mbps) | Latenta (ms) |
|---|---|---|---|
| Free5GC | 66,5 / 9,53 | 3,11 / 0,35 | 14,14 / 3,77 |
| OAI | 100,1 / 11,3 | 4,8 / 0,4 | 12,7 / 3,02 |
| Open5GS | 86,8 / 6,75 | 4,7 / 0,26 | 13,6 / 3,32 |

- Video: Free5GC are throughput cu aproximativ 23% mai mic si timp de incarcare cu 30% mai mare decat OAI (Fig. 7-8).
- **Resurse** (Fig. 9):
  - CPU: OAI are cel mai mare consum pe CP si UP; Open5GS consuma cu 85% (CP) si 45% (UP) mai putin decat OAI; Free5GC cu aproximativ 97% mai putin decat OAI;
  - RAM UP: Free5GC cel mai mic, OAI +28,97%, Open5GS +165,42% fata de Free5GC; RAM CP: Open5GS +121,61% fata de OAI.

## Limitari declarate de autori
- Analiza de performanta este descrisa ca preliminara (VII).
- Un singur UE; lucrarile viitoare vor creste numarul de utilizatori, vor automatiza instantierea NF-urilor si vor evalua infrastructura Kubernetes si SD-Core (VII).

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: da - Free5GC, Open5GS si OAI in Docker (V).
- UE reale sau emulate?: reale - Motorola Edge 20 prin gNodeB OAI pe SDR B210 (V, Tabelul III).
- digital twin al retelei?: nu.
- prezice efectul unei actiuni inainte de a o aplica?: nu.
- executa actiuni automat (bucla inchisa)?: nu.
- multi-site / geo-redundanta / failover de baza de date?: nu - un singur server.
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: da - timpi de inregistrare si de stabilire a sesiunii PDU, throughput si timp de incarcare video pe UE (Fig. 5-8).
- observa traficul la SCP / proxy?: nu - SCP este mentionat doar la modelele de comunicare (Model C pentru Open5GS) (II, Tabelul I).
