from turtle import home
from django.urls import URLPattern, path

from .views import PetsList


urlpatterns = [path("", PetsList.as_view())]
