from django.contrib import admin
from django.urls import path, include
from personaje import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("personaje/", include("personaje.urls")),
]
