# YASS — API Test Automation

## 1. Présentation du projet

Ce projet a pour objectif de mettre en place une stratégie d'automatisation des tests API pour l'application web **YASS Parfums**.

- **Application testée :** https://yassparfums.com/
- **Administration :** https://yassparfums.com/admin
- **Environnement actuel :** application déployée, testée à distance
- **IDE :** PyCharm
- **Langage :** Python
- **Framework de test :** pytest
- **Client HTTP :** requests

Le projet QA est indépendant du backend. Les tests sont exécutés à partir de requêtes HTTP envoyées à l'application déployée. L'accès au code source backend n'est pas nécessaire.

## 2. Objectifs QA

Les objectifs sont les suivants :

- Vérifier la disponibilité des endpoints API.
- Contrôler les codes de réponse HTTP.
- Vérifier la structure des réponses JSON.
- Valider les données retournées par les API.
- Tester les paramètres de recherche et de pagination.
- Vérifier les réponses aux requêtes invalides.
- Contrôler les mécanismes d'authentification et d'autorisation.
- Identifier et documenter les anomalies.
- Préparer une base réutilisable pour les futurs tests E2E Web et Mobile.

## 3. Périmètre fonctionnel

### 3.1 Produits

Endpoint principal : `/api/products`

Tests prévus et commencés :

- Récupération de la liste des produits.
- Vérification de la structure JSON.
- Vérification des champs principaux.
- Contrôle de la pagination.
- Consultation d'un produit par son identifiant.
- Gestion d'un identifiant inexistant.
- Filtrage par recherche.
- Filtrage par catégorie.
- Filtrage par prix.
- Validation des paramètres invalides.

### 3.2 Catégories

Endpoint principal : `/api/categories`

Tests prévus et commencés :

- Récupération de la liste des catégories.
- Vérification de la structure de la réponse.
- Consultation d'une catégorie existante.
- Gestion d'une catégorie inexistante.

### 3.3 Paramètres de la boutique

Endpoint : `/api/settings`

Tests prévus et commencés :

- Vérification du code HTTP.
- Vérification du format JSON.
- Vérification de la présence de l'objet `data`.

### 3.4 Santé de l'API

Endpoint : `/api/health`

Tests prévus et commencés :

- Vérification de la disponibilité de l'API.
- Vérification du statut HTTP.
- Vérification de la réponse JSON.

### 3.5 Administration et sécurité

Endpoints :

- `/api/dashboard`
- `/api/auth/me`
- `/api/admin/orders`

Tests prévus et commencés :

- Vérification du refus d'accès sans token.
- Vérification des réponses HTTP 401 ou 403.
- Préparation des tests authentifiés avec un compte de test autorisé.

### 3.6 Documentation API

Les endpoints suivants ont été identifiés dans la cartographie initiale et restent à vérifier en exécution si nécessaire :

- `/api/docs`
- `/api/docs/`
- `/api/docs/openapi.json`

## 4. Architecture du projet

Structure actuelle recommandée :

```text
E2ETestYaas/
│
├── api/
│   ├── __init__.py
│   ├── config.py
│   ├── client.py
│   ├── endpoints.py
│   │
│   └── tests/
│       ├── test_health.py
│       ├── test_products.py
│       ├── test_product_detail.py
│       ├── test_product_filters.py
│       ├── test_categories.py
│       ├── test_category_detail.py
│       ├── test_settings.py
│       ├── test_admin_access.py
│       └── test_api_exploration.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

### Rôle des principaux fichiers

| Fichier | Responsabilité |
|---|---|
| `api/config.py` | Configuration de l'URL de base et du timeout |
| `api/client.py` | Client HTTP commun basé sur `requests.Session` |
| `api/endpoints.py` | Centralisation des chemins API |
| `conftest.py` | Fixture pytest `api_client` |
| `api/tests/` | Scénarios automatisés |
| `pytest.ini` | Configuration de pytest |
| `requirements.txt` | Dépendances Python |

## 5. Configuration

### 5.1 Dépendances

Installation des dépendances :

```bash
python -m pip install pytest requests
```

Les dépendances du projet sont déclarées dans `requirements.txt`.

### 5.2 URL de base

La configuration est centralisée dans `api/config.py`.

```python
import os

BASE_URL = os.getenv(
    "YASS_API_BASE_URL",
    "https://yassparfums.com"
)

TIMEOUT = 20
```

L'URL par défaut cible l'application déployée.

Pour changer d'environnement, la variable `YASS_API_BASE_URL` peut être configurée sans modifier les tests.

### 5.3 Client HTTP

Le client commun est défini dans `api/client.py`.

Il centralise :

- La construction des URLs.
- La session HTTP.
- Le timeout des requêtes.
- La préparation à l'ajout de headers et de l'authentification.

Tous les tests doivent utiliser `api_client.get()` pour les requêtes GET, plutôt que d'appeler directement `requests.get()`.

### 5.4 Centralisation des endpoints

Les chemins API sont définis dans `api/endpoints.py`.

Exemple :

```python
PRODUCTS = "/api/products"
PRODUCT_DETAIL = "/api/products/{id}"
CATEGORIES = "/api/categories"
SETTINGS = "/api/settings"
```

Les chemins sont importés dans les tests afin d'éviter leur duplication.

## 6. Stratégie de test API

La stratégie est organisée en plusieurs niveaux.

### Niveau 1 — Tests de disponibilité

Objectif : vérifier que les endpoints sont accessibles.

Contrôles :

- Statut HTTP.
- Temps de réponse observé.
- Présence d'une réponse exploitable.

### Niveau 2 — Tests fonctionnels nominaux

Objectif : vérifier que les API retournent les données attendues.

Contrôles :

- Structure JSON.
- Présence des champs obligatoires.
- Types de données.
- Cohérence des identifiants.
- Format des listes et objets.

### Niveau 3 — Tests négatifs

Objectif : vérifier le comportement face aux entrées invalides.

Contrôles :

- Identifiant inexistant.
- Pagination invalide.
- Paramètres incorrects.
- Ressource absente.
- Accès sans authentification.

### Niveau 4 — Tests métier

Objectif : vérifier la cohérence des données.

Exemples :

- Prix non négatif.
- Identifiant de produit cohérent.
- Pagination respectée.
- Filtres appliqués correctement.
- Données de détail cohérentes avec celles de la liste.

### Niveau 5 — Sécurité

Objectif : contrôler les autorisations.

Exemples :

- Accès au dashboard sans token.
- Accès au profil admin sans token.
- Accès aux commandes sans token.
- Vérification future des rôles et des tokens invalides ou expirés.

Les tests de sécurité plus approfondis seront réalisés avec un compte de test autorisé et dans un environnement adapté.

## 7. Priorisation des tests

| Priorité | Description | Exemples |
|---|---|---|
| P0 | Fonctionnalités essentielles et disponibilité | Santé API, produits, catégories |
| P1 | Validation, filtres et contrôle d'accès | Pagination, recherche, authentification |
| P2 | Cas limites et couverture complémentaire | Paramètres avancés, erreurs supplémentaires |

Les priorités pourront être ajustées selon les risques métier et les résultats observés.

## 8. Exécution des tests

### Lancer toute la suite

Depuis le terminal PyCharm :

```bash
python -m pytest -v
```

### Exécuter un fichier spécifique

```bash
python -m pytest -v api/tests/test_products.py
```

### Afficher les réponses de diagnostic

```bash
python -m pytest -v -s api/tests/test_api_exploration.py
```

### Exécuter plusieurs fichiers

```bash
python -m pytest -v api/tests/test_products.py api/tests/test_product_detail.py
```

### Comprendre les résultats

- `PASSED` : le test a satisfait ses assertions.
- `FAILED` : une assertion ou une opération du test a échoué.
- `SKIPPED` : le test a été volontairement ignoré.
- `ERROR` : le test n'a pas pu être exécuté correctement, par exemple à cause d'une erreur de fixture.

Un test réussi confirme uniquement le comportement vérifié par ses assertions. Il ne garantit pas à lui seul l'absence de défaut dans toute l'API.

## 9. État actuel de la suite

À la dernière exécution complète :

| Indicateur | Résultat |
|---|---:|
| Tests collectés | 17 |
| Tests réussis | 16 |
| Tests échoués | 1 |

### Anomalie connue

**Filtrage des produits par catégorie**

- Endpoint : `GET /api/products`
- Paramètre : `categorie=7`
- Résultat observé : HTTP 500
- Résultat attendu par le test actuel : HTTP 200

Cette anomalie est connue et reste à investiguer.

Elle ne doit pas être masquée en remplaçant arbitrairement le statut attendu par 500. Le test doit continuer à représenter le comportement fonctionnel souhaité, jusqu'à ce que l'analyse confirme la cause et le résultat attendu.

Une fois le problème corrigé ou expliqué, le test devra être réexécuté et le rapport mis à jour.

## 10. Règles de développement des tests

Les règles suivantes s'appliquent au projet :

1. Un fichier de test par domaine fonctionnel ou groupe de scénarios cohérents.
2. Utiliser `api_client` pour toutes les requêtes HTTP.
3. Centraliser les chemins dans `api/endpoints.py`.
4. Ne pas dupliquer l'URL de base dans les tests.
5. Garder des noms de fonctions explicites commençant par `test_`.
6. Écrire des assertions simples et lisibles.
7. Séparer les scénarios nominaux et négatifs lorsque cela améliore la lisibilité.
8. Ne pas ignorer une anomalie sans la documenter.
9. Ne pas exposer de mots de passe, tokens ou autres secrets dans les logs ou le dépôt.
10. Ne pas effectuer de modifications ou suppressions de données en production.

## 11. Limites actuelles

- Les tests ciblent l'application déployée.
- Le code source backend n'est pas accessible au projet QA.
- Les résultats dépendent de la disponibilité du site et de son environnement.
- Certains comportements restent à explorer.
- Les tests administratifs authentifiés ne sont pas encore couverts.
- Les tests d'écriture ne sont pas inclus dans le périmètre actuel.
- Les tests E2E Web et Mobile ne sont pas encore développés.

Les erreurs réseau, les changements de données et les modifications du contrat API peuvent affecter les résultats des tests.

## 12. Roadmap

### Phase 1 — Discovery API

- [x] Identifier les endpoints principaux.
- [x] Tester la liste des produits.
- [x] Tester le détail produit.
- [x] Tester la liste des catégories.
- [x] Tester le détail catégorie.
- [x] Tester les paramètres de la boutique.
- [x] Tester certains accès administratifs sans token.
- [x] Centraliser la configuration HTTP.
- [ ] Documenter tous les endpoints confirmés en exécution.
- [ ] Investiguer le filtre de catégorie qui retourne HTTP 500.

### Phase 2 — Compléter les tests API

- [ ] Finaliser les tests des paramètres de pagination.
- [ ] Vérifier le comportement des filtres.
- [ ] Compléter les tests négatifs.
- [ ] Ajouter les tests authentifiés avec un compte autorisé.
- [ ] Documenter les anomalies et résultats attendus.
- [ ] Produire un bilan d'exécution reproductible.

### Phase 3 — Amélioration du framework

- [ ] Ajouter des données de test réutilisables.
- [ ] Améliorer la configuration des environnements.
- [ ] Ajouter un rapport de test HTML ou Allure.
- [ ] Réduire les doublons entre scénarios.
- [ ] Ajouter des contrôles de schéma JSON lorsque les contrats sont confirmés.

### Phase 4 — Tests E2E Web

- [ ] Installer Selenium.
- [ ] Mettre en place le Page Object Model.
- [ ] Automatiser les parcours client prioritaires.
- [ ] Tester le parcours administratif.

### Phase 5 — Tests Mobile

- [ ] Préparer Appium et Python.
- [ ] Tester le site mobile sous Chrome Android.
- [ ] Tester le site mobile sous Safari iOS.
- [ ] Ajouter les configurations tablette et appareils réels selon les besoins.

### Phase 6 — CI/CD

- [ ] Intégrer les tests dans un pipeline CI.
- [ ] Exécuter automatiquement les tests de régression.
- [ ] Publier les rapports.
- [ ] Définir les règles de validation avant livraison.

## 13. Conclusion

Le projet YASS API Test Automation constitue la base de la stratégie d'automatisation QA.

L'approche actuelle privilégie des tests simples, lisibles et indépendants du backend. Le framework sera enrichi progressivement, en commençant par la fiabilisation des tests API avant d'étendre la couverture aux parcours E2E Web et Mobile.
