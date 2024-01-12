import pytest
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from ..models import Address


@pytest.mark.django_db
def test_create_address():
    # Test successful address creation
    address = Address.objects.create(
        number=123,
        street='Baker Street',
        city='London',
        state='LN',
        zip_code=12345,
        country_iso_code='GBR'
    )
    assert address.number == 123
    assert address.street == 'Baker Street'


def test_address_str():
    # Test the custom __str__ method
    address = Address(
        number=221,
        street='Baker Street',
        city='London',
        state='LN',
        zip_code=12345,
        country_iso_code='GBR'
    )
    assert str(address) == '221 Baker Street'


def test_address_validation():
    # Test field validation for the Address model
    address = Address(
        number=12345,  # Should be invalid as it's greater than 9999
        street='Baker Street',
        city='London',
        state='LN',
        zip_code=12345,
        country_iso_code='GBR'
    )
    with pytest.raises(ValidationError):
        address.full_clean()  # This should raise a ValidationError because number is too large


def test_address_plural_name():
    # Test that the verbose_name_plural is correctly set
    assert Address._meta.verbose_name_plural == "Addresses"

