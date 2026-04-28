from django.urls import path
from . import views

urlpatterns = [
    # Token CSRF (necessari per al frontend Vue)
    path("csrf/", views.get_csrf, name="csrf"),
    # Autenticació
    path("auth/me/", views.me_view, name="auth-me"),
    path("auth/login/", views.login_view, name="auth-login"),
    path("auth/logout/", views.logout_view, name="auth-logout"),
    path("auth/register/", views.register_view, name="auth-register"),
    # Dades del joc
    path("personatges/", views.personatges_view, name="personatges"),
    path("armes/", views.armes_view, name="armes"),
    path("habitacions/", views.habitacions_view, name="habitacions"),
    # Lògica del joc
    path("partida-activa/", views.partida_activa_view, name="partida-activa"),
    path("nova-partida/", views.nova_partida_view, name="nova-partida"),
    path("acusar/", views.acusar_view, name="acusar"),
    path("historial/", views.historial_view, name="historial"),
]
