# 🧪 YASS — API Test Automation Framework

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/pytest-Automation-0A9EDC?logo=pytest&logoColor=white" alt="pytest">
  <img src="https://img.shields.io/badge/HTTP-Requests-green" alt="Requests">
  <img src="https://img.shields.io/badge/Status-In%20Progress-orange" alt="In progress">
</p>

<p align="center">
  **Framework d'automatisation QA pour les API de YASS Parfums**
  
  Tests fonctionnels · Validation JSON · Contrôle d'accès · Rapports HTML
</p>

---

## 📌 1. Présentation

**YASS API Test Automation** est un framework de tests automatisés développé en Python pour vérifier la qualité et la fiabilité des API de la boutique YASS Parfums.

| Élément | Description |
|---|---|
| 🌐 Site web | [yassparfums.com](https://yassparfums.com/) |
| 🔐 Administration | [yassparfums.com/admin](https://yassparfums.com/admin) |
| 🐍 Langage | Python |
| 🧪 Framework de test | pytest |
| 🔌 Client HTTP | requests |
| 💻 IDE | PyCharm |
| 📊 Rapports | pytest-html |
| 🎯 Périmètre actuel | Tests API sur environnement déployé |

Le framework est indépendant du backend : les tests communiquent directement avec les endpoints HTTP de l'application.

## 🎯 2. Objectifs QA

- ✅ Vérifier la disponibilité des endpoints.
- ✅ Contrôler les statuts HTTP et les réponses JSON.
- ✅ Valider les données et les types de champs.
- ✅ Tester la pagination et les filtres.
- ✅ Vérifier la gestion des identifiants inexistants.
- ✅ Contrôler l'accès aux endpoints administratifs.
- 📊 Générer des rapports d'exécution HTML.
- 🚀 Préparer l'automatisation E2E Web et Mobile.

## 🏗️ 3. Architecture du projet

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
├── data/
├── mobile/
├── reports/
├── web/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

### 🔧 Rôle des composants

| Composant | Responsabilité |
|---|---|
| `api/client.py` | Client HTTP commun |
| `api/config.py` | URL de base et timeout |
| `api/endpoints.py` | Centralisation des chemins API |
| `api/discovery/` | Documentation et découverte des endpoints |
| `api/tests/` | Scénarios automatisés |
| `config/` | Configuration des environnements |
| `data/` | Données de test |
| `reports/` | Rapports d'exécution |
| `web/` | Futurs tests E2E Web |
| `mobile/` | Futurs tests E2E Mobile |
| `conftest.py` | Fixtures pytest partagées |

## ⚙️ 4. Installation et configuration

### Prérequis

- Python installé.
- PyCharm.
- Accès réseau à l'application YASS.
- Git pour la gestion du code source.

### Installer les dépendances

```bash
python -m pip install -r requirements.txt
```

Si nécessaire, installer le générateur de rapports :

```bash
python -m pip install pytest-html
```

### Configurer l'environnement

L'URL de base est centralisée dans `api/config.py`.

```python
import os

BASE_URL = os.getenv(
    "YASS_API_BASE_URL",
    "https://yassparfums.com"
)

TIMEOUT = 20
```

La variable `YASS_API_BASE_URL` permet de changer d'environnement sans modifier les tests.

> 🔒 **Sécurité :** ne jamais publier de mots de passe, de tokens, de clés API ou le fichier `.env`.

## 🧪 5. Stratégie de test API

### Niveau 1 — Disponibilité

Vérifier que les endpoints répondent et retournent les statuts attendus.

### Niveau 2 — Tests fonctionnels

Valider la structure JSON, les champs obligatoires, les types de données et la cohérence des identifiants.

### Niveau 3 — Tests négatifs

Tester les identifiants inexistants, les paramètres invalides et les erreurs de validation.

### Niveau 4 — Règles métier

Vérifier la pagination, la recherche, les filtres et la cohérence des données retournées.

### Niveau 5 — Sécurité

Vérifier les accès sans token, puis compléter les tests avec des comptes de test autorisés.

## 📚 6. Couverture API

| Domaine | Endpoint principal | Couverture actuelle |
|---|---|---|
| ❤️ Santé | `/api/health` | Tests de disponibilité |
| 🛍️ Produits | `/api/products` | Liste, détail, pagination et filtres |
| 🗂️ Catégories | `/api/categories` | Liste et détail |
| ⚙️ Paramètres | `/api/settings` | Récupération des paramètres |
| 🔐 Dashboard | `/api/dashboard` | Contrôle d'accès sans token |
| 👤 Authentification | `/api/auth/me` | Contrôle d'accès sans token |
| 📦 Commandes | `/api/admin/orders` | Contrôle d'accès sans token |

*La couverture indiquée correspond aux scénarios présents dans le projet. Les endpoints et leurs contrats doivent être confirmés à partir des réponses réelles.*

## ▶️ 7. Exécuter les tests

### Lancer toute la suite

```bash
python -m pytest -v
```

### Lancer un fichier spécifique

```bash
python -m pytest -v api/tests/test_products.py
```

### Afficher les réponses de diagnostic

```bash
python -m pytest -v -s api/tests/test_api_exploration.py
```

### Générer le rapport HTML

```bash
python -m pytest -v --html=reports/api-test-report.html --self-contained-html
```

Le rapport est enregistré dans :

```text
reports/api-test-report.html
```

Ouvrir ce fichier dans Chrome pour consulter les résultats, les erreurs et les traces d'échec.

## 📊 8. Dernier bilan d'exécution connu

<p align="center">
  <img src="https://img.shields.io/badge/Tests-17-blue" alt="17 tests">
  <img src="https://img.shields.io/badge/Passed-16-success" alt="16 réussis">
  <img src="https://img.shields.io/badge/Failed-1-critical" alt="1 échoué">
</p>

| Indicateur | Résultat |
|---|---:|
| Tests exécutés | 17 |
| Tests réussis | 16 |
| Tests échoués | 1 |

### 🐞 Anomalie connue

**Filtrage des produits par catégorie**

- Endpoint : `GET /api/products`
- Paramètre testé : `categorie=7`
- Statut observé : `500 Internal Server Error`
- Statut attendu par le test : `200 OK`

Cette anomalie reste à investiguer. Le test conserve le comportement attendu afin de détecter une éventuelle régression ou correction.

> ℹ️ Ces chiffres correspondent à la dernière campagne communiquée. Ils ne sont pas actualisés automatiquement par GitHub.

## 🚦 9. Priorités QA

| Priorité | Objectif |
|---|---|
| 🔴 P0 | Stabiliser les endpoints essentiels et les tests de régression |
| 🟠 P1 | Compléter les filtres, la pagination et les tests négatifs |
| 🟡 P1 | Étendre les tests d'authentification et d'autorisation |
| 🔵 P2 | Ajouter des rapports enrichis et des contrôles de schéma |
| ⚪ P2 | Préparer l'intégration CI/CD |

## 🗺️ 10. Roadmap

- [x] Créer le framework pytest + requests.
- [x] Centraliser la configuration et les endpoints.
- [x] Développer les premiers tests produits et catégories.
- [x] Ajouter les contrôles d'accès sans token.
- [x] Générer un rapport HTML.
- [ ] Investiguer le filtre de catégorie en erreur.
- [ ] Compléter les tests API authentifiés.
- [ ] Ajouter des données de test réutilisables.
- [ ] Mettre en place une intégration CI/CD.
- [ ] Développer les tests E2E Web avec Selenium.
- [ ] Développer les tests Mobile avec Appium pour Android et iOS.

## 📏 11. Bonnes pratiques

1. Utiliser `api_client` pour les appels HTTP.
2. Centraliser les chemins dans `api/endpoints.py`.
3. Garder les scénarios simples et indépendants.
4. Ne pas masquer les anomalies en modifiant arbitrairement les assertions.
5. Documenter les résultats et les défauts constatés.
6. Ne pas exposer de secrets dans le dépôt.
7. Limiter les requêtes sur la production.
8. Réserver les opérations d'écriture aux environnements et comptes de test autorisés.

## 👨‍💻 12. Contribution et maintenance

Avant de committer des modifications :

```bash
python -m pytest -v
git status
```

Vérifier les résultats, les fichiers modifiés et l'absence de secrets avant le commit et le push.

---

<p align="center">
  **YASS API Test Automation**
  
  *Construire une couverture QA fiable, progressive et maintenable.*
</p>
