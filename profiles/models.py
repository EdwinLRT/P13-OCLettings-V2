from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model representing additional user data.

    This model extends the default User model provided by Django's authentication system. It adds
    additional information about the user, like their favorite city.

    Attributes:
        user: A OneToOneField relationship with the User model.
         Each user can only have one profile.
        favorite_city: A CharField to store the user's favorite city;
         This field is optional.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns a string representation of this 'Profile' object.

        This string is used when a 'Profile' object is printed or displayed.
         It includes the username
        of the associated user.

        Returns:
            str: A string representation of the profile, consisting of the user's username.
        """
        return self.user.username
