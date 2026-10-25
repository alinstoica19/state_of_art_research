# A Survey on Cloud-Based 6G Deployments: Current Solutions, Future Directions and Open Challenges (2026)
Cheie: Atalay2026Cloudsurvey . DOI/link: https://arxiv.org/abs/2603.09894 . Sursa textului: integral: arXiv v1 (10 martie 2026)
Sectiunea din plan: C . Tema: SBA/selectie NF (cloud-native core, survey)
Autori: Tolga O. Atalay, Alireza Famili, Amirreza Ghafoori, Angelos Stavrou (A2 Labs LLC; Virginia Tech; WayWave Inc.). Preprint arXiv [eess.SY]; 403 referinte.

## Problema (cum o formuleaza autorii)
Operatorii de telecomunicatii (TSP) colaboreaza cu furnizori de cloud public (AWS, Azure, GCP) pentru a desfasura retele 5G si ulterioare. Are loc trecerea de la functii fizice (PNF) la functii containerizate, cloud-native, gestionate cu Kubernetes. Autorii spun ca aceasta tranzitie aduce provocari tehnice si operationale care trebuie intelese inaintea deployment-urilor la scara mare. Mai spun ca survey-urile anterioare nu analizeaza domeniile din perspectiva cloud-native si a deployment-ului in cloud public (Sectiunea I, Tabelul I).

## Structura si taxonomia propusa
- **Sectiunea II, fundal:**
  - evolutia PNF -> VNF -> CNF;
  - RAN si core 5G, cu un exemplu proof-of-concept de deployment distribuit in cloud;
  - elemente de design cloud-native si framework-uri de orchestrare din industrie.
- **Sectiunea III, taxonomia spatiului de design**, cu cinci subsectiuni:
  - A. Deployment Architecture;
  - B. Resource Management and Orchestration;
  - C. Multi-Tenancy & Isolation;
  - D. Cloud Role and Control;
  - E. Economic & Ownership Models.
  - Rezumatul vorbeste de patru dimensiuni (deployment, resource management/orchestration, multi-tenancy/isolation, economic/ownership).
- **Sectiunea IV:** strategiile AWS, Microsoft Azure si Google Cloud Platform. Exemple date de autori: core 5G SA al Telefonica pe AWS; OpenRAN NTT DOCOMO pe AWS; DISH; Azure Private 5G Core; T-Mobile cu GCP (I, IV).
- **Sectiunea V, arii de investigatie:**
  - A. Security, Trust, and Compliance;
  - B. Performance, Latency, and Reliability;
  - C. Scalability, Elasticity, and Resource Efficiency;
  - D. Orchestration and Automation.
  - Rezumatul enumera sase arii: security/privacy, scalability/elasticity, performance/latency, cost optimization, resilience/fault management, compliance/sovereignty.
- Autorii separa explicit taxonomia (Sectiunea III, clasificare declarativa) de analiza tehnica (Sectiunea V) (Box 1).

## Lucrari/sisteme acoperite (cu numar)
- 403 referinte.
- Tabelul I compara 8 survey-uri existente ([25]-[32]) cu lucrarea curenta, pe dimensiuni tehnice si de deployment, cu marcajele acoperit / partial / neacoperit.

## Directii deschise declarate
Sectiunea VI, Fig. 22:
- A. operatiuni de retea cloud conduse de AI: ZSM, federated learning, network digital twins pentru antrenare si optimizare predictiva, LLM pentru management autonom;
- B. securitate post-cuantica pentru 5G/6G in cloud: PQC pe interfetele SBA prin TLS 1.3, KEMTLS, SUCI/AKA cu CRYSTALS-Kyber;
- C. intent-based networking: interfete in limbaj natural, abordari centrate pe LLM;
- D. semantic networking si Named Data Networking.

Rezumatul mai mentioneaza orchestrarea condusa de AI si serverless networking pentru 6G.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)?: nu (survey) - Sectiunea II descrie un proof-of-concept de deployment distribuit, fara evaluare experimentala in textul consultat.
- UE reale sau emulate?: nedeclarat.
- digital twin al retelei?: mentionat doar ca directie viitoare (VI.A).
- prezice efectul unei actiuni inainte de a o aplica?: nedeclarat.
- executa actiuni automat (bucla inchisa)?: discutat ca directie (ZSM, VI.A); nu este implementat.
- multi-site / geo-redundanta / failover de baza de date?: tratat la nivel de survey in V.B (performanta, latenta, fiabilitate) si in deployment-ul distribuit (II.C).
- evaluare prospectiva (predictie fixata inainte de experiment)?: nu.
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)?: nu.
- observa traficul la SCP / proxy?: nedeclarat.
