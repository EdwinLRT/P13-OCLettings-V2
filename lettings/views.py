from django.shortcuts import render
from .models import Letting


def index(request):
    """
    Renders the index page with a list of all lettings.

    Fetches all letting objects from the database and passes them to
    the 'lettings/index.html' template.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered index page with all lettings.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Renders the detail page for a specific letting.

    Fetches a single letting object based on its ID and passes it
     to the 'lettings/letting.html' template.

    Args:
        request: The HTTP request object.
        letting_id (int): The ID of the letting to display.

    Returns:
        HttpResponse: The rendered detail page for the specified letting.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
