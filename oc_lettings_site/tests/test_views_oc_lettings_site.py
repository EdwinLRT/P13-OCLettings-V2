import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_view(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Welcome to Holiday Homes' in response.content.decode()
    # Ajoutez d'autres assertions si nécessaire, comme vérifier les liens vers les autres pages


@pytest.mark.django_db
def test_error_500_view(client):
    url = reverse('error-500')
    response = client.get(url)
    assert "Une erreur serveur" in response.content.decode()
