from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents a physical address.

    This model stores all details of an address including street,
    city, state, zip code, and country ISO code.

    Attributes:
        number (PositiveIntegerField): The house or building number. Must be less than 9999.
        street (CharField): The street name.
        city (CharField): The city name.
        state (CharField): The state or province code, 2 characters long.
        zip_code (PositiveIntegerField): The postal or zip code. Must be less than 99999.
        country_iso_code (CharField): The ISO country code, 3 characters long.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Returns a human-readable representation of the Address model.

        Returns:
            str: The full address combining the number and the street.
        """
        return f'{self.number} {self.street}'

    class Meta:
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Represents a letting or rental listing.

    This model stores the details of a letting such as its title and associated address.

    Attributes:
        title (CharField): The title of the letting.
        address (OneToOneField): The linked Address object for this letting.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a human-readable representation of the Letting model.

        Returns:
            str: The title of the letting.
        """
        return self.title
