# Semantic Routing for Enhanced Performance of LLM-Assisted Intent-Based 5G Core Network Management and Orchestration (2024)
Cheie: Manias2024Semanticrouting . DOI/link: 10.1109/globecom52923.2024.10901065 . Sursa textului: integral, arXiv v1 (2404.15869v1, 24 Apr 2024): https://arxiv.org/pdf/2404.15869
Sectiunea din plan: B

## Problema (cum o formuleaza autorii)
Extragerea de intent cu un LLM standalone bazat pe prompting (lucrarea anterioara a autorilor) distinge greu intent-uri similare, nu scaleaza (limita de tokeni pentru exemple suplimentare in prompt) si, dupa o perioada de operare, a prezentat halucinatii (ex. redenumirea categoriilor de intent). Autorii discuta si riscurile LLM-urilor closed-source (transparenta, confidentialitate) si promoveaza modele open-source.

## Ce propun (metoda, pe scurt)
Un framework end-to-end de intent extraction pentru MANO in core-ul 5G cu un semantic router (implementarea open-source Aurelio AI) in fata/alaturi de LLM, cu rutare deterministica. Sunt definite 6 rute statice (intent-urile din 3GPP TS 28.312: Deployment, Modification, Performance Assurance, Intent Report Request, Intent Feasibility Check, Regular Notification Request) plus ruta implicita "None"; fiecare ruta are o utterance de baza din standard (Tabel I). Se foloseste threshold tuning per ruta (prag initial 0.5). Contributii: framework-ul, un dataset divers de prompt-uri pentru intent-urile core 5G (de publicat pe GitHub-ul OC2 Lab), analiza efectului encoderului, cuantizarii si diversitatii lingvistice. Prompt-uri: seed (scrise manual), variability (reformulare cu ChatGPT 3.5) si paraphrased (schimbare de structura cu ChatGPT 3.5).

## Setup experimental (testbed real / emulare / simulare; unelte; scara; date)
Fara core 5G live in aceasta lucrare (rutele dinamice cu function calling pentru integrare cu testbed-ul end-to-end anterior sunt lucru viitor). Date: 30 seed prompts pe ruta = 180 esantioane, 5-fold cross-validation; utterance-urile suplimentare sunt scoase din setul de date. LLM de baza: Mistral-7B-Instruct-v0.2 cuantizat 2-bit (Q2_K), daca nu se specifica altfel. Encodere: Hugging Face all-MiniLM-L6-v2 (open-source, trunchiaza la 256 cuvinte) si OpenAI text-embedding-ada-002 (platit, closed-source).

## Experimente si metrici
Metrica raportata: acuratete (matricile de confuzie si alte metrici derivate au fost calculate dar nu sunt prezentate). Experimente (Sec. IV-F): (1) numar de utterance-uri: 0, 15, 30, 45 in plus fata de cea de baza (5, 10, 15 seed x 3 versiuni), pre/post threshold training, train/test; (2) diversitate de vocabular: (seed, variable, paraphrase) = (5,0,0), (5,5,0), (5,0,5), (5,5,5); (3) encoder HF vs OpenAI; (4) prompting vs routing; (5) cuantizare: Q2_K (2 biti, 3.08 GB), Q4_K_S (4 biti, 4.14 GB), Q6_K (6 biti, 5.94 GB).

## Rezultate raportate (cifre exacte, cu trimitere la tabel/figura)
- Utterance-uri (Fig. 3, encoder HF): performanta creste cu numarul de utterance-uri; threshold tuning imbunatateste performanta post-training fata de pre-training pe train si test; diferenta train-test scade cu mai multe utterance-uri. Valorile exacte sunt doar in grafic.
- Diversitate (Fig. 4): cu 5 seed prompts maximul este de circa 60%; adaugarea de variable prompts creste cu 6%, de paraphrased cu 8%, iar toate trei cu inca 10%.
- Encoder (Fig. 5 vs Fig. 3): encoderul OpenAI depaseste HF in toate incercarile, chiar fara utterance-uri suplimentare; peste 15 utterance-uri threshold tuning nu mai schimba performanta.
- Prompting vs routing (Fig. 6): routerul semantic (encoder OpenAI, post-training) are acuratete mai mare decat prompting-ul (raportat cu si fara halucinatie); eficienta de timp empirica de 50x in favoarea routerului. Valori numerice de acuratete doar in grafic.
- Cuantizare (Sec. V-E): rezultatele au ramas consistente pentru toate nivelurile, modelul cel mai mic la fel de bun ca cele mai mari (fara tabel/figura cu valori).

## Limitari declarate de autori
Rute doar statice (nu dinamice, fara function calling); dataset mic (180 esantioane) construit manual/cu LLM; doar acuratetea e prezentata; compromis encoder OpenAI (performant dar closed-source si platit) vs HF. Viitor: back translation si tone shift, combinatii LLM x cuantizare x encoder, RAG pentru colectii mari de rute, rute dinamice cu integrare in retea live, cereri cu intent-uri multiple.

## Steaguri factuale (da / nu / nedeclarat, cu sectiunea din lucrare)
- core 5G implementat (nu model)? nu - fara core in experiment; testbed anterior doar citat (Sec. IV-C)
- UE reale sau emulate? nu se aplica
- digital twin al retelei? nu
- prezice efectul unei actiuni inainte de a o aplica? nu
- executa actiuni automat (bucla inchisa)? nu - rutele sunt statice; actiuni asupra core-ului sunt lucru viitor (Sec. IV-C)
- multi-site / geo-redundanta / failover de baza de date? nu
- evaluare prospectiva (predictie fixata inainte de experiment)? nedeclarat (cross-validation 5-fold, Sec. IV-E)
- rezultat masurat la nivel de utilizator (inregistrari, sesiuni)? nu - acuratete de clasificare a prompt-urilor (Sec. V)
- observa traficul la SCP / proxy? nu
