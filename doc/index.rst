=====================
Documentation d'Orange County Lettings Website
=====================

Bienvenue dans la documentation de OC Lettings website.

Orange County Lettings est une start-up dans le secteur de la location de biens immobiliers.

L'objectif de cette documentation est de présenter le site web de la start-up et de décrire les fonctionnalités de ce dernier.
Tout en donnant les clés pour une meilleur compréhension des différentes fonctionnalités du site et des choix de développement.

Sommaire :
----------------

.. _ma-section-cible:




Installation du projet en local
----------------


- Clonez ce dépôt de code à l’aide de la commande (vous pouvez également télécharger le code en tant qu’archive zip) :
   .. code-block::

       $ git clone https://github.com/EdwinLRT/P13-OCLettings-V2




- Rendez vous depuis un terminal à la racine du répertoire oc-cg-p13 avec la commande :
   .. code-block::

       $ cd P13-OCLettings

- Créez un environnement virtuel pour le projet avec :

  - sous Windows :

    .. code-block::

        $ python -m venv env

  - sous OsX ou Linux :

    .. code-block::

        $ python3 -m venv env



- Activez l’environnement virtuel avec :
   - sous Windows
      .. code-block::

          $ env\Scripts\activate
   - sous MacOS ou Linux
      .. code-block::

          $ source env/bin/activate

- Installez les dépendances du projet avec :
   .. code-block::

       $ pip install -r requirements.txt


Démarrez le serveur
----------------

Après avoir réalisé les étapes d’installation, démarrez le serveur avec :
   .. code-block::

       $ python manage.py runserver


Dans votre navigateur web, rendez vous à l’adresse suivante : http://localhost:8000/

Vous devriez être en mesure d'accéder et de naviguer sur le site de manière locale.
Vous retrouverez les fonctionnalités du site web de la start-up Orange County Lettings,
les profils des utilisateurs et les différentes locations.

Technologies utilisées
----------------

 - **Python 3.11**


 - **Django**: C'est un framework web haut niveau en Python qui encourage le développement rapide et une conception propre et pragmatique. Django est utilisé comme le principal framework web pour la construction de votre application.


 - **gunicorn**: Il s'agit d'un serveur HTTP WSGI pour UNIX. gunicorn est un serveur très performant et léger qui s'intègre bien avec les applications Django, permettant de gérer les requêtes HTTP.


 - **pytest** et **pytest-django**: Ce sont des frameworks de test pour Python. pytest fournit un ensemble riche de fonctionnalités pour écrire des tests, tandis que pytest-django est spécifiquement conçu pour tester les applications Django.


 - **coverage** et **pytest-cov**: Ces outils sont utilisés pour mesurer la couverture de code de vos tests. Ils aident à identifier les parties du code qui ne sont pas couvertes par vos tests.


 - **flake8**: Cet outil est utilisés pour l'analyse statique du code. Il aide à maintenir la qualité du code en vérifiant la conformité avec les conventions de codage et en détectant les erreurs potentielles.


 - **Sentry-sdk**: Sentry est un outil de suivi des erreurs qui aide les développeurs à surveiller et à corriger les crashs en temps réel. L'intégration de Sentry dans votre projet Django peut aider à identifier et résoudre rapidement les problèmes.


 - **whitenoise**: WhiteNoise permet à votre application web de servir ses propres fichiers statiques, rendant votre application plus autonome et réduisant la dépendance à des services externes pour la distribution de contenu statique.


 - **python-dotenv**: Utilisé pour gérer les variables d'environnement. Il permet de charger les variables d'environnement à partir d'un fichier .env, ce qui est utile pour configurer des paramètres qui ne doivent pas être codés en dur dans l'application.


 - **Circle CI**: CircleCI est un service d'intégration et de déploiement continu qui automatise le processus de test et de déploiement de votre code. Il offre une configuration facile, une intégration avec divers outils et services, et prend en charge de nombreux langages de programmation et frameworks.


 - **Heroku**: Heroku est une plateforme cloud qui permet le déploiement, la gestion et le dimensionnement d'applications. Elle est connue pour sa facilité d'utilisation et sa capacité à simplifier les processus de déploiement d'applications web.

 - **SQlite3**: SQLite3 est un système de gestion de base de données relationnelle léger, qui est intégré dans l'application. Il est très apprécié pour sa simplicité, sa fiabilité et son indépendance, ne nécessitant pas de serveur de base de données séparé.