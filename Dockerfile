# Utiliser une image de base Python officielle
FROM python:3.11-slim

# Définir l'environnement en non-interactif (pour automatiser)
ENV PYTHONUNBUFFERED 1

# Utiliser ARG pour passer la SECRET_KEY lors de la construction
ARG DJANGO_SECRET_KEY
ENV DJANGO_SECRET_KEY $DJANGO_SECRET_KEY

WORKDIR /app

# Copier le fichier des dépendances et installer les dépendances
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copier le projet dans le répertoire de travail
COPY . /app/

# Créer le dossier static si nécessaire
RUN mkdir -p /app/static

# Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput


# Exposer le port sur lequel l'application va tourner
EXPOSE 8000

# Lancer le serveur Django avec gunicorn (par exemple)
CMD ["gunicorn", "-b", "0.0.0.0:$PORT", "oc_lettings_site.wsgi:application"]
