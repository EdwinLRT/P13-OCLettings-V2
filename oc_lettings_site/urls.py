# oc_lettings_site/urls.py
from django.urls import include, path
from . import views
from .views import error_500
from django.contrib import admin

handler500 = 'oc_lettings_site.views.error_500'


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('profiles/', include('profiles.urls')),
    path('lettings/', include('lettings.urls')),
    path('error-500/', views.error_500, name='error-500'),
    path('sentry-debug/', trigger_error),
]
