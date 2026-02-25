from django.urls import path
from . import views

urlpatterns = [
    path("", views.personaje, name="personaje"),
    path("nuevo/", views.crear_personaje, name="crear_personaje"),
]
