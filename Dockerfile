# Utiliser une image de base Python officielle
FROM python:3.11-slim

# Définir l'environnement en non-interactif (pour automatiser)
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Copier le fichier des dépendances et installer les dépendances
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copier le projet dans le répertoire de travail
COPY . /app/

# Exposer le port sur lequel l'application va tourner
EXPOSE 8000

# Lancer le serveur Django avec gunicorn (par exemple)
CMD ["gunicorn", "-b", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
