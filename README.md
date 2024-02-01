## Résumé

Site web d'Orange County Lettings

Les objetcifs de la V2 de ce projet : 
- Amélioration de l'architecture modulaire de l'application via réorganisation du code, modification de l'arborecence des fichiers et création de modules indépendants
- Amélioration de la sécurité de l'application via l'ajout de tests unitaires et de tests d'intégration
- Réduction des divers problèmes sur le projet : Linting, gestion des erreurs 404 et 500, documentation du code et des fonctions, etc.
- Ajout de fonctionnalités : 
    - Surveillance de l'application via Sentry
    - Mise en place de logs pour l'application
    - Création d'une pipeline CI/CD pour le déploiement de l'application
- 

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Déploiement 
Le processus de déploiement, automatisé par une pipeline CI/CD, active la mise en production du site à chaque validation sur la branche principale du dépôt.
Cette automatisation comprend des étapes cruciales telles que l'installation des dépendances, l'exécution des tests,
la vérification de la couverture des tests, la conteneurisation de l'application et son déploiement sur le serveur de production.

Voici les différentes étapes de la pipeline CI/CD : 
- Reproduction de l'environnement de développement local. (Variables, requirements...)
- Vérification de la conformité syntaxique (Linting).
- Execution des tests implantés.
- Vérification de la couverture de tests (Sur ce projet, la couverture doit être superieure à 80%).
- Conteneurisation de l'application via Docker, l'image crée est pushée sur Docker Hub.
- Mise en production de l'application web chez l'hébergeur (ici AWS).

 
Voici les éléments nécéssaires pour la mise en place correcte de la pipeline :
 - Compte GitHub avec accès en lecture à ce repository.
 - Compte Docker Hub.
 - Compte Sentry avec un projet déjà configuré.
 - Compte AWS avec possibilité de lancer des instances EC2.
