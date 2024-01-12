import pytest
from django.urls import reverse
from lettings.models import Letting, Address

@pytest.mark.django_db
@pytest.mark.django_db
def test_index_view(client):
    # Create an address
    address = Address.objects.create(
        number=124, street='Test Street', city='Test City',
        state='TS', zip_code=54321, country_iso_code='TST'
    )
    # Utilisez cette adresse pour créer un nouvel objet Letting
    Letting.objects.create(title='Unique Test Letting', address=address)

    # La suite du test...
    url = reverse('lettings:index')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Test Letting' in response.content.decode()


@pytest.mark.django_db
def test_letting_view(client):
    # Assurez-vous qu'il y a un objet Letting dans la base de données
    address = Address.objects.create(number=123, street='Main Street', city='Anytown', state='AT', zip_code=12345, country_iso_code='USA')
    letting = Letting.objects.create(title='Test Letting', address=address)

    url = reverse('lettings:letting', kwargs={'letting_id': letting.id})
    response = client.get(url)
    assert response.status_code == 200
    assert 'Main Street' in response.content.decode()

