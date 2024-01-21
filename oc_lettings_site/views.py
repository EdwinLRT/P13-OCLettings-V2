import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    try:
        return render(request, 'index.html')
    except Exception as e:
        logger.error(f'Error rendering index: {e}', exc_info=True)


def error_500(request):
    return render(request, '500.html')
