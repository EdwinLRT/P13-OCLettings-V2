# oc_lettings_site/urls.py
from django.contrib import admin
from django.urls import include, path

from . import views

handler500 = 'oc_lettings_site.views.error_500'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('profiles/', include('profiles.urls')),
    path('lettings/', include('lettings.urls')),
    path('error-500/', views.error_500, name='error-500'),
]
