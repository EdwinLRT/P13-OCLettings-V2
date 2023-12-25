from django.urls import include, path
from . import views

app_name = 'oc_lettings_site'

urlpatterns = [
    path('', views.index, name='index'),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('lettings/', include('lettings.urls', namespace='lettings')),
]

