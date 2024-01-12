from django.shortcuts import render
from .models import Letting
import logging
from django.http import Http404


logger = logging.getLogger(__name__)


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
    logger.info(f'Index view: {len(lettings_list)} lettings fetched')
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
    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Letting.DoesNotExist:
        logger.error(f'Letting with id {letting_id} not found')
        raise Http404("Letting not found")


"""
Logs could be used to track errors and debug your application.
The logging module is part of the Python standard library.
These lines could be used to implement logging in this application:

import logging

logger = logging.getLogger(__name__)

def ma_fonction():
    try:
        # code to be executed - could raise an exception
    except Exception as e:
        logger.error('Something appened', exc_info=True)
        # exc_info=True will include the traceback in the log
"""