from .models import Profile
import logging
from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.http import Http404

logger = logging.getLogger(__name__)


def index(request):
    """
    Render the index view for the profiles.

    This view displays a list of all user profiles. It retrieves all profiles from the database
    and passes them to the 'profiles/index.html' template.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: An HttpResponse object with the rendered index page.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Render the profile detail view for a specific user.

    This view displays the profile details of a specific user identified by their username.
    It retrieves the user's profile from the database and passes it to the 'profiles/profile.html'
    template. If the profile does not exist, it raises a 404 error.

    Args:
        request: The HTTP request object.
        username: The username of the user whose profile is to be displayed.

    Returns:
        HttpResponse: An HttpResponse object with the rendered profile page.
    """
    try:
        profile = Profile.objects.get(user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Profile.DoesNotExist:
        logger.error(f'Profile with id {username} not found')
        raise Http404("Profile not found")
