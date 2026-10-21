# E2ETestYaas — QA Automation Framework

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Test_Automation-green?logo=pytest&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-API_Testing-orange)
![Selenium](https://img.shields.io/badge/Selenium-Web_Automation-brightgreen?logo=selenium&logoColor=white)
![CI/CD](https://img.shields.io/badge/CI%2FCD-In_Progress-yellow)

> **Construire un dispositif de validation fiable, maintenable et orienté risque pour sécuriser les évolutions de YASS Parfums.**

## 1. Introduction & vision stratégique

### Objectif

**E2ETestYaas** est un framework d'automatisation QA développé en Python pour valider les API REST et les parcours utilisateurs de l'application YASS Parfums.

L'objectif dépasse la simple exécution de scripts de test : il s'agit de construire progressivement un dispositif de contrôle qualité qui fournit un feedback rapide, détecte les régressions et améliore la confiance dans les livraisons.

Application cible : [https://yassparfums.com/](https://yassparfums.com/)

Interface d'administration : [https://yassparfums.com/admin](https://yassparfums.com/admin)

### Principes directeurs

- **Risk-based testing :** prioriser les contrôles selon l'impact métier, la probabilité de défaillance et la criticité des fonctionnalités.
- **Fast feedback :** exécuter les tests les plus rapides et les plus déterministes en premier afin d'identifier rapidement les régressions.
- **Testabilité et maintenabilité :** centraliser la configuration, les clients techniques, les fixtures et les composants réutilisables.
- **Traçabilité :** relier les scénarios, les résultats d'exécution, les anomalies et les rapports aux fonctionnalités concernées.
- **Détection précoce :** déplacer les contrôles pertinents vers les Pull Requests et les pipelines d'intégration continue.
- **Amélioration continue :** mesurer la stabilité des tests, analyser les échecs et faire évoluer la couverture en fonction des risques observés.

### Périmètre fonctionnel

Le framework cible progressivement les domaines suivants :

1. Tests de contrats et de comportements des API REST.
2. Contrôles d'accès et scénarios négatifs.
3. Tests web et validation des parcours utilisateur.
4. Vérification de la persistance des données en base SQL, lorsque l'accès est disponible.
5. Tests end-to-end transverses couvrant plusieurs composants.
6. Industrialisation de l'exécution et du reporting via CI/CD.

---

## 2. État actuel vs trajectoire cible

La distinction entre l'existant et la cible est essentielle : les fonctionnalités planifiées ne sont pas considérées comme implémentées tant qu'elles ne sont pas développées et vérifiées.

| Domaine | État actuel | Trajectoire cible |
|---|---|---|
| Tests API REST | Python, Pytest et `requests` | Couverture structurée par risque métier et criticité |
| Validation HTTP | Vérification des codes de statut et des réponses | Assertions métier et contrats de réponse plus complets |
| Données de réponse | Vérifications de structures et champs utiles | Schémas de validation et jeux de données maîtrisés |
| Gestion des appels | Client API commun et endpoints centralisés | Gestion homogène des erreurs, authentification et configuration par environnement |
| Tests web | Premiers tests Selenium avec Pytest et Page Object Model | Parcours métier de bout en bout et couverture des cas critiques |
| Données SQL | Contrôles SQL non encore intégrés au framework | Vérification de la persistance et de la cohérence des données, avec accès autorisé à la base |
| CI/CD | Workflow GitHub Actions prévu ou en cours de mise en place | Exécution automatisée sur Pull Request, push et planification |
| Reporting | Rapports HTML Pytest disponibles localement | Rapports centralisés, historiques d'exécution et suivi des tendances |
| Observabilité | Analyse des résultats et anomalies identifiées | Diagnostics structurés, logs exploitables et classification des échecs |
| IA / LLMs | Usage assisté envisageable | Assistance encadrée à la conception, à l'analyse et à la maintenance des tests |

### État d'avancement connu

**Tests API**
- Client HTTP commun avec `requests`.
- Centralisation des endpoints et de la configuration.
- Tests couvrant notamment les produits, les catégories, les filtres, les paramètres et certains contrôles d'accès.
- Exécution avec Pytest et génération de rapports HTML.

**Tests web**
- Selenium WebDriver intégré à Pytest.
- Configuration commune de l'application et du navigateur.
- Premiers Page Objects : `BasePage`, `HomePage` et `CataloguePage`.
- Premiers scénarios validés pour le chargement de l'accueil, la navigation et la présence de la section produits.

**Limites connues**
- Une anomalie de filtrage par catégorie a été observée : l'API renvoie HTTP 500 pour une requête attendue en HTTP 200.
- La couverture complète des fiches produits et des parcours end-to-end reste à développer.
- Les contrôles SQL et l'intégration CI/CD doivent être considérés comme des objectifs tant que leur exécution effective n'est pas confirmée.

---

## 3. Architecture technique

### Stack technologique

| Technologie | Responsabilité |
|---|---|
| Python | Langage du framework |
| Pytest | Organisation, fixtures et exécution des tests |
| Requests | Appels HTTP et tests API |
| Selenium WebDriver | Automatisation du navigateur |
| pytest-html | Génération de rapports HTML |
| Git / GitHub | Versionnement et collaboration |
| GitHub Actions | Cible d'industrialisation CI/CD |
| PyCharm | Environnement de développement |

### Organisation du code

```text
E2ETestYaas/
├── api/
│   ├── discovery/
│   ├── tests/
│   │   ├── test_admin_access.py
│   │   ├── test_api_exploration.py
│   │   ├── test_auth.py
│   │   ├── test_categories.py
│   │   ├── test_categories_detail.py
│   │   ├── test_health.py
│   │   ├── test_orders.py
│   │   ├── test_product_detail.py
│   │   ├── test_product_filters.py
│   │   ├── test_products.py
│   │   └── test_settings.py
│   ├── client.py
│   ├── config.py
│   └── endpoints.py
├── config/
│   └── environments.py
├── web/
│   ├── pages/
│   │   ├── base_page.py
│   │   ├── home_page.py
│   │   └── catalogue_page.py
│   └── tests/
│       ├── test_home.py
│       ├── test_navigation.py
│       └── test_catalogue.py
├── data/
├── mobile/
├── reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

Cette arborescence décrit l'organisation de référence actuelle. Les fichiers présents peuvent évoluer avec l'implémentation.

### Responsabilités architecturales

- `api/client.py` : centraliser les requêtes HTTP et le cycle de vie de la session.
- `api/endpoints.py` : regrouper les chemins des endpoints.
- `api/config.py` : porter les paramètres propres aux appels API.
- `config/environments.py` : centraliser les paramètres partagés de l'application.
- `conftest.py` : fournir les fixtures communes Pytest, notamment les clients et le navigateur.
- `api/tests/` : isoler les scénarios API.
- `web/pages/` : encapsuler les sélecteurs et les actions Selenium avec le Page Object Model.
- `web/tests/` : décrire les scénarios web et leurs assertions.
- `data/` : accueillir les jeux de données réutilisables.
- `reports/` : recevoir les rapports générés.

### Fixtures Pytest et isolation

Les fixtures Pytest permettent de contrôler la création, la portée et le nettoyage des ressources.

Bonnes pratiques cibles :

- Réutiliser un client API via une fixture adaptée à sa durée de vie.
- Créer et fermer le navigateur proprement après chaque scénario web.
- Éviter les dépendances implicites entre tests.
- Ne pas faire dépendre l'ordre d'exécution de la réussite des tests précédents.
- Garder les données de test séparées de la logique d'assertion.
- Prévoir un nettoyage explicite pour les tests qui créent ou modifient des données.

### Gestion des environnements et des données

La configuration doit être externalisée : URL de base, délais d'attente et paramètres d'environnement ne doivent pas être dispersés dans les tests.

La trajectoire cible prévoit :
- des environnements de test clairement identifiés ;
- des jeux de données déterministes et réutilisables ;
- une séparation entre données de test, configuration et secrets ;
- une stratégie de nettoyage lorsque des données persistantes sont créées ;
- l'utilisation de variables d'environnement ou de mécanismes sécurisés pour les paramètres sensibles.

---

## 4. CI/CD & industrialisation

### Objectif

Industrialiser l'exécution pour rendre le résultat des tests disponible au bon moment, notamment avant la fusion d'une Pull Request ou lors d'une campagne planifiée.

### Pipeline cible

```text
Pull Request / Push / Exécution planifiée
                    |
                    v
          Préparation de l'environnement
                    |
                    v
          Installation des dépendances
                    |
                    v
           Tests API rapides et critiques
                    |
                    v
              Tests Web Selenium
                    |
                    v
        Collecte des rapports et diagnostics
                    |
                    v
        Décision selon les critères qualité
```

### Déclencheurs recommandés

| Déclencheur | Objectif |
|---|---|
| Pull Request | Détecter les régressions avant fusion |
| Push sur branche partagée | Vérifier la cohérence après intégration |
| Exécution planifiée | Détecter les régressions indépendantes des changements récents |
| Lancement manuel | Investiguer un incident ou exécuter une campagne ciblée |

### Stratégie d'exécution

**Niveau 1 — Feedback rapide**
- Tests API critiques et déterministes.
- Contrôles de disponibilité.
- Vérification des contrats et des accès.

**Niveau 2 — Validation fonctionnelle**
- Tests API complets.
- Tests web Selenium.
- Scénarios de recherche, filtres et consultation des produits.

**Niveau 3 — Campagnes approfondies**
- Parcours end-to-end transverses.
- Contrôles SQL de persistance, si un accès autorisé est disponible.
- Tests plus longs, exécutés de préférence sur un environnement adapté.

### Critères de qualité

Les seuils doivent être définis à partir de la criticité métier et de la stabilité réelle des campagnes.

Critères recommandés :
- Aucun échec inexpliqué sur les scénarios critiques.
- Aucun défaut bloquant ouvert sans décision explicite.
- Rapports disponibles pour chaque campagne.
- Tests indépendants et reproductibles.
- Secrets absents des logs et des artefacts.
- Échecs classifiés entre défaut applicatif, problème d'environnement et défaut du test.

Une anomalie connue ne doit pas être masquée en affaiblissant une assertion. Elle doit être documentée, suivie et faire l'objet d'une décision explicite dans la politique de qualité.

### Indicateurs de suivi

| Indicateur | Utilité |
|---|---|
| Taux de réussite | Suivre la stabilité de la campagne |
| Taux de tests instables (flaky) | Identifier les tests non déterministes |
| Durée du pipeline | Mesurer le délai de feedback |
| Couverture des risques critiques | Vérifier que les fonctions prioritaires sont testées |
| Défauts détectés avant production | Mesurer l'efficacité préventive |
| Répartition des échecs | Distinguer application, environnement et framework |
| Ancienneté des anomalies | Suivre la dette qualité |

La couverture de code, si elle est introduite, ne doit pas être considérée comme un substitut à la couverture des risques métier.

### Déploiement continu : étape ultérieure

Le framework cible d'abord la validation continue. Le déploiement automatique devra être envisagé après la mise en place d'un environnement de staging, de critères de promotion, d'une gestion sécurisée des secrets et d'une stratégie de retour arrière.

Les tests contre la production doivent rester non destructifs et ne doivent jamais modifier des données réelles sans autorisation explicite.

---

## 5. Usage pragmatique de l'IA et des LLMs

### Positionnement

Les assistants IA peuvent accélérer certaines activités QA, mais ne remplacent ni l'analyse du risque, ni la validation humaine, ni l'exécution réelle des tests.

### Cas d'usage pertinents

**Conception des tests**
- Proposer des cas nominaux, limites et négatifs à partir d'une spécification.
- Identifier les risques oubliés dans une stratégie de test.
- Générer une première version de scénarios Pytest.
- Suggérer des jeux de données et des assertions.

**Analyse des échecs**
- Résumer des traces d'erreur et des logs.
- Comparer une réponse attendue à une réponse observée.
- Proposer des hypothèses à vérifier lors d'une investigation.
- Aider à distinguer une anomalie applicative d'un problème potentiel de configuration.

**Maintenance**
- Repérer les duplications dans les tests.
- Proposer des refactorisations.
- Améliorer la lisibilité des noms, messages d'erreur et rapports.
- Aider à documenter les scénarios et les anomalies.

### Garde-fous obligatoires

1. **Confidentialité :** ne pas transmettre de mots de passe, jetons, données personnelles ou secrets de production à un assistant non autorisé.
2. **Validation humaine :** tout code généré doit être relu, compris et exécuté avant intégration.
3. **Vérification factuelle :** ne pas accepter un endpoint, un sélecteur ou un comportement inventé par le modèle sans preuve.
4. **Traçabilité :** documenter les décisions importantes et conserver les résultats réels des tests.
5. **Sécurité :** ne jamais autoriser une action destructive ou un déploiement sur la seule base d'une suggestion générée.
6. **Qualité des assertions :** ne pas affaiblir les contrôles pour faire passer une campagne en vert.
7. **Non-régression :** vérifier que les refactorisations proposées conservent le comportement attendu.

### Principe directeur

> **L'IA accélère la production et l'analyse ; la responsabilité de la décision qualité reste humaine.**

---

## 6. Gestion des anomalies et traçabilité

Une anomalie détectée doit être décrite de façon reproductible et exploitable.

Chaque défaut devrait contenir :
- l'identifiant du scénario ;
- l'environnement et le contexte d'exécution ;
- les préconditions et données utilisées ;
- la requête ou l'action exécutée ;
- le résultat attendu et le résultat observé ;
- les logs ou extraits de rapport utiles, expurgés de toute donnée sensible ;
- l'impact métier, la sévérité et la priorité ;
- le statut de l'investigation et la décision de résolution.

### Anomalie connue

Le test de filtrage des produits par catégorie a précédemment révélé une réponse HTTP 500 alors qu'une réponse HTTP 200 était attendue.

Cette anomalie doit être réévaluée lors des campagnes suivantes. Son statut ne doit être déclaré résolu qu'après une vérification effective.

---

## 7. Installation et exécution locale

### Pré-requis

- Python compatible avec les dépendances du projet.
- Git.
- Chrome pour les tests web.
- Dépendances listées dans `requirements.txt`.

### Installation

```bash
python -m venv .venv
```

Sous Windows :

```bash
.venv\Scripts\activate
```

Installer les dépendances :

```bash
python -m pip install -r requirements.txt
```

### Lancer les tests API

```bash
python -m pytest -v api/tests
```

### Lancer les tests Web

```bash
python -m pytest -v web/tests
```

### Lancer l'ensemble des tests

```bash
python -m pytest -v
```

### Générer un rapport HTML

```bash
python -m pytest -v --html=reports/test-report.html --self-contained-html
```

Le rapport est généré localement dans `reports/`. La génération du rapport ne garantit pas que tous les tests passent : le statut de sortie de Pytest reste la référence pour déterminer le résultat de la campagne.

---

## 8. Roadmap d'industrialisation

- [x] Structuration initiale des tests API.
- [x] Client HTTP commun et centralisation des endpoints.
- [x] Configuration commune de l'application.
- [x] Premiers tests web avec Selenium et Pytest.
- [x] Introduction du Page Object Model.
- [ ] Consolidation des conventions et des jeux de données de test.
- [ ] Stabilisation des scénarios API critiques.
- [ ] Couverture détaillée des fiches produits et des parcours web.
- [ ] Mise en place et validation du pipeline GitHub Actions.
- [ ] Conservation et consultation centralisée des rapports.
- [ ] Contrôles SQL de persistance, si l'accès est autorisé.
- [ ] Scénarios end-to-end transverses.
- [ ] Suivi des indicateurs qualité.
- [ ] Extension mobile avec Appium.
- [ ] Évaluation encadrée des cas d'usage IA/LLM.

---

## 9. Sécurité et maintenance du dépôt

- Ne jamais versionner `.env`, les jetons ou les mots de passe.
- Exclure `.venv/`, `__pycache__/` et `.pytest_cache/` de Git.
- Définir une politique claire pour les rapports générés.
- Ne pas stocker de données personnelles ou réelles dans les jeux de données de test.
- Utiliser des environnements adaptés aux tests qui modifient des données.
- Revoir périodiquement les dépendances et versions des actions CI utilisées.

---

## Conclusion

**E2ETestYaas évolue d'une suite de tests API vers un dispositif de validation QA industrialisé.**

La priorité est de garantir des contrôles fiables, traçables et orientés risque, puis de les intégrer progressivement aux workflows de développement. L'objectif final n'est pas seulement d'augmenter le nombre de tests, mais d'améliorer la rapidité du feedback, la détection précoce des défauts et la confiance dans chaque livraison.

*Projet : E2ETestYaas — QA Automation Framework*  
*Application cible : YASS Parfums*  
*Statut : développement et industrialisation progressifs*
