# 🧪 E2ETestYaas
### QA Automation Framework — YASS Parfums

![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC?logo=pytest&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-Web_Automation-43B02A?logo=selenium&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-API_Testing-orange)
![Status](https://img.shields.io/badge/Status-In_Progress-yellow)

> **Un framework de tests automatisés pour contrôler la qualité des API et de l'interface web de YASS Parfums.**

🌐 **Application :** [yassparfums.com](https://yassparfums.com/)  
🔐 **Administration :** [yassparfums.com/admin](https://yassparfums.com/admin)  
🛠️ **IDE :** PyCharm

---

## 📌 01 — Présentation du projet

**E2ETestYaas** est un framework QA développé en Python pour automatiser les tests de l'application YASS Parfums.

Le projet suit une approche progressive : commencer par les tests API, mettre en place les tests web avec Selenium, puis étendre la couverture aux parcours end-to-end et aux applications mobiles.

### 🎯 Objectifs

- ✅ Vérifier les réponses et la structure des API.
- ✅ Tester les produits, catégories et filtres.
- ✅ Contrôler les accès aux endpoints protégés.
- ✅ Vérifier le chargement des pages et la navigation web.
- 🔄 Automatiser les fiches produits et les parcours d'achat.
- 📊 Produire des rapports de test HTML.
- 📱 Préparer les tests mobiles avec Appium.

---

## 🧰 02 — Stack technique

| Technologie | Rôle |
|:--|:--|
| 🐍 Python | Langage du framework |
| 🧪 Pytest | Exécution des tests |
| 🌐 Requests | Tests API HTTP |
| 🖥️ Selenium WebDriver | Automatisation web |
| 🌍 Chrome | Navigateur de test |
| 📊 pytest-html | Rapports HTML |
| 💻 PyCharm | Environnement de développement |

---

## 🏗️ 03 — Architecture du projet

```text
E2ETestYaas/
│
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
│
├── config/
│   └── environments.py
│
├── web/
│   ├── pages/
│   │   ├── base_page.py
│   │   ├── home_page.py
│   │   └── catalogue_page.py
│   └── tests/
│       ├── test_home.py
│       ├── test_navigation.py
│       └── test_catalogue.py
│
├── mobile/
├── data/
├── reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

> **Architecture retenue :** séparation des tests API, des pages web, des scénarios de test et de la configuration commune.

---

## 🔌 04 — Stratégie de tests API

### Objectif

Valider les réponses HTTP, les données retournées, les paramètres de requête et les contrôles d'accès, sans accès direct au backend.

### Couverture fonctionnelle

| Domaine | Contrôles |
|:--|:--|
| Health check | Disponibilité de l'API |
| Produits | Liste, données et pagination |
| Détail produit | Produit existant et identifiant inexistant |
| Catégories | Liste et détail |
| Filtres | Recherche, prix et catégorie |
| Paramètres | Structure de la réponse |
| Administration | Accès sans authentification |
| Exploration | Paramètres invalides et réponses d'erreur |

### Bonnes pratiques

- Centraliser les requêtes dans `api/client.py`.
- Centraliser les chemins dans `api/endpoints.py`.
- Garder la configuration dans `api/config.py`.
- Tester les cas nominaux et les cas négatifs.
- Utiliser des assertions explicites.
- Documenter les anomalies sans affaiblir les assertions pour faire artificiellement passer les tests.

---

## 🖥️ 05 — Stratégie de tests Web Selenium

### Objectif

Vérifier le comportement visible de l'application dans Chrome et automatiser progressivement les interactions essentielles des utilisateurs.

### 🧱 Design Pattern : Page Object Model (POM)

Le framework utilise le **Page Object Model** pour séparer la logique des pages des scénarios de test.

| Fichier | Responsabilité |
|:--|:--|
| `config/environments.py` | URL, délai d'attente et dimensions du navigateur |
| `conftest.py` | Création et fermeture du navigateur |
| `web/pages/base_page.py` | Méthodes Selenium communes |
| `web/pages/home_page.py` | Actions de la page d'accueil |
| `web/pages/catalogue_page.py` | Navigation et accès au catalogue |
| `web/tests/` | Scénarios et assertions |

**Avantages :** moins de duplication, sélecteurs centralisés, tests plus lisibles et maintenance facilitée.

### ✅ Scénarios web actuellement validés

| ID | Scénario | Résultat communiqué |
|:--|:--|:--:|
| WEB-001 | Chargement de la page d'accueil | ✅ PASS |
| WEB-002 | Navigation avec « Découvrir la boutique » | ✅ PASS |
| WEB-003 | Affichage de la section « Nos produits » | ✅ PASS |
| WEB-004 | Présence d'éléments dans la grille produits | ✅ PASS |

*Les cartes produits, les prix et les fiches produits doivent encore faire l'objet de vérifications détaillées.*

### 🚀 Prochains scénarios

1. Vérifier le nom et le prix de chaque produit affiché.
2. Ouvrir une fiche produit et vérifier ses informations.
3. Tester les filtres et la recherche depuis l'interface.
4. Vérifier les restrictions d'accès à l'administration.
5. Construire des parcours end-to-end complets.

---

## ⚙️ 06 — Configuration centralisée

Le fichier `config/environments.py` centralise les paramètres communs :

- `BASE_URL` — adresse de l'application.
- `DEFAULT_TIMEOUT` — délai d'attente Selenium.
- `BROWSER_WINDOW_SIZE` — dimensions initiales de Chrome.

L'adresse peut être remplacée par la variable d'environnement `YASS_BASE_URL`.

La configuration API reste dans `api/config.py`, qui réutilise l'URL commune tout en conservant son délai d'attente spécifique.

🔒 **Sécurité :** ne jamais publier les mots de passe, jetons ou valeurs confidentielles du fichier `.env`.

---

## 📦 07 — Installation

### Étape 1 — Créer l'environnement virtuel

Sous Windows :

```bash
python -m venv .venv
```

### Étape 2 — Activer l'environnement

```bash
.venv\Scripts\activate
```

### Étape 3 — Installer les dépendances

```bash
python -m pip install -r requirements.txt
```

### Étape 4 — Vérifier l'environnement

Vérifiez que Chrome est installé. Avec une version récente de Selenium, Selenium Manager peut gérer automatiquement le pilote du navigateur.

---

## ▶️ 08 — Exécution des tests

### Tous les tests

```bash
python -m pytest -v
```

### Tests API uniquement

```bash
python -m pytest -v api/tests
```

### Tests Web uniquement

```bash
python -m pytest -v web/tests
```

### Test de la page d'accueil

```bash
python -m pytest -v web/tests/test_home.py
```

### Générer un rapport HTML

```bash
python -m pytest -v --html=reports/api-test-report.html --self-contained-html
```

📁 Le rapport est enregistré dans `reports/`. Le nom `api-test-report.html` est historique ; un nom plus général pourra être utilisé lorsque les campagnes API et web seront consolidées.

---

## 🐛 09 — Anomalie API connue

<details>
<summary><strong>API — Filtrage des produits par catégorie (HTTP 500)</strong></summary>

**Test concerné :** `test_filter_products_by_category`

**Requête :** `GET /api/products?categorie=7`

| Élément | Résultat |
|:--|:--|
| Résultat attendu | HTTP 200 |
| Résultat observé | HTTP 500 |
| Statut | 🔎 À investiguer |

Lors de la dernière campagne API communiquée :

- **16 tests réussis**
- **1 test échoué**

L'anomalie reste documentée. L'assertion ne doit pas être modifiée uniquement pour obtenir un résultat positif.

</details>

---

## 🗺️ 10 — Roadmap QA

- [x] Structuration des tests API
- [x] Création du client HTTP commun
- [x] Centralisation des endpoints
- [x] Configuration partagée
- [x] Mise en place de Selenium
- [x] Création de `BasePage`
- [x] Création des premiers Page Objects
- [x] Premiers tests web de navigation et du catalogue
- [ ] Validation détaillée des noms et prix des produits
- [ ] Tests des fiches produits
- [ ] Tests des filtres web
- [ ] Tests d'accès à l'administration
- [ ] Parcours end-to-end complets
- [ ] Tests mobiles Android et iOS avec Appium
- [ ] Intégration continue et rapports consolidés

---

## 🔐 11 — Qualité et maintenance

- Ne jamais committer `.env`, les mots de passe ou les jetons.
- Exclure `.venv/`, `__pycache__/` et `.pytest_cache/` de Git.
- Utiliser des attentes explicites dans Selenium.
- Garder les scénarios indépendants et lisibles.
- Séparer les anomalies de l'application des défauts du framework.
- Mettre à jour la documentation lorsque la couverture évolue.

---

<div align="center">

### 🚀 E2ETestYaas

**Quality • Automation • Reliability**

*Framework QA en cours de développement pour YASS Parfums.*

</div>
