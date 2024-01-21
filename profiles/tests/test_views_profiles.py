import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from profiles.models import Profile


@pytest.mark.django_db
def test_index_view_renders_profiles(client):
    # Création de données de test
    user1 = User.objects.create_user(username='user1', password='password123')
    profile1 = Profile.objects.create(user=user1, favorite_city='Springfield')
    user2 = User.objects.create_user(username='user2', password='password123')
    profile2 = Profile.objects.create(user=user2, favorite_city='Shelbyville')

    # Appel de la vue index
    url = reverse('profiles:index')
    response = client.get(url)

    # Vérification que la réponse est 200 OK
    assert response.status_code == 200

    # Vérification que les profils créés sont présents dans le contexte de la réponse
    assert 'profiles_list' in response.context
    profiles_in_context = response.context['profiles_list']
    assert profile1 in profiles_in_context
    assert profile2 in profiles_in_context

    # Vérification que le contenu rendu contient les informations des profils
    content = response.content.decode()
    assert user1.username in content
    assert user2.username in content


@pytest.mark.django_db
def test_profile_view_displays_favorite_city(client):
    # Création de données de test
    user = User.objects.create_user(username='john_doe', password='password123')
    favorite_city = 'Springfield'
    Profile.objects.create(user=user, favorite_city=favorite_city)

    # Appel de la vue de détail du profil
    url = reverse('profiles:profile', kwargs={'username': 'john_doe'})
    response = client.get(url)

    # Vérification que la réponse est 200 OK
    assert response.status_code == 200

    # Vérification que le contenu rendu contient la ville favorite
    content = response.content.decode()
    assert favorite_city in content
