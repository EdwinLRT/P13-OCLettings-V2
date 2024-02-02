===============================================
Documentation d'Orange County Lettings Website
===============================================
.. image:: https://readthedocs.org/projects/p13-oclettings-v2/badge/?version=latest
   :target: https://p13-oclettings-v2.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

Bienvenue dans la documentation de OC Lettings website.

Orange County Lettings est une start-up dans le secteur de la location de biens immobiliers.

L'objectif de cette documentation est de présenter le site web de la start-up et de décrire les fonctionnalités de ce dernier.
Tout en donnant les clés pour une meilleur compréhension des différentes fonctionnalités du site et des choix de développement.

.. Table of Contents
.. _sommaire:

Sommaire
========

.. contents:: :local:
   :depth: 2






Installation du projet en local
-------------------------------


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

Création des variables d'environnement
--------------------------------------

Créer des variables d'environnement est essentiel pour sécuriser et personnaliser la configuration d'un projet Django.
Cela permet de protéger les données sensibles, de rendre le code portable et de simplifier les mises à jour.
Les variables d'environnement peuvent être stockées dans un fichier .env et chargées dans le code à l'aide de bibliothèques comme python-decouple.
Cela garantit que les informations sensibles ne sont pas exposées dans le code source et facilite la gestion des environnements de développement.

Ce projet nécéssite la création d'un fichier .env à la racine du projet. Et à minima, les variables suivantes doivent être définies :
    - Django Secret Key
    - Django Debug
    - Sentry DSN

Démarrez le serveur local
-------------------------

Après avoir réalisé les étapes d’installation, démarrez le serveur avec :
   .. code-block::

       $ python manage.py runserver


Dans votre navigateur web, rendez vous à l’adresse suivante : http://localhost:8000/

Vous devriez être en mesure d'accéder et de naviguer sur le site de manière locale.
Vous retrouverez les fonctionnalités du site web de la start-up Orange County Lettings,
les profils des utilisateurs et les différentes locations.


Naviguer sur le site
--------------------

Les différents URLs du site sont les suivants :

 - / : Page d’accueil du site.

 - lettings/ : Liste des locations.

 - lettings/<letting_id>/ : Page détaillée d’une location.

 - profiles/ : Liste des profils utilisateurs.

 - profiles/<username>/ : Page détaillée d’un profil utilisateur.

 - admin/ : Interface de gestion administrateur du site.

L'accès à l'interface d'administration est réservé aux utilisateurs ayant les droits d'administration. Pour accéder à cette interface, vous devez créer un superutilisateur avec la commande suivante :

   .. code-block::

       $ python manage.py createsuperuser

Le code source est divisé en trois applications distinctes, permettant de séparer les fonctionnalités du site web:

 - oc_lettings_site : Dossier de configuration principal il centralise les URLs.

 - profiles : Dossier du modèle Profile. Cette application gère les profils utilisateurs.

 - lettings : Dossier du modèle Letting. Cette application gère les locations.




Technologies utilisées
----------------------

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


 - **Render**: Render est une plateforme cloud qui permet le déploiement, la gestion et le dimensionnement d'applications. Elle est connue pour sa facilité d'utilisation et sa capacité à simplifier les processus de déploiement d'applications web.

 - **SQlite3**: SQLite3 est un système de gestion de base de données relationnelle léger, qui est intégré dans l'application. Il est très apprécié pour sa simplicité, sa fiabilité et son indépendance, ne nécessitant pas de serveur de base de données séparé.