from django.contrib import admin
from .models import Arma, Habitacio, Intent, Personatge, Solucio


@admin.register(Personatge)
class PersonatgeAdmin(admin.ModelAdmin):
    list_display = ['nom', 'descripcio']
    search_fields = ['nom']


@admin.register(Arma)
class ArmaAdmin(admin.ModelAdmin):
    list_display = ['nom', 'descripcio']
    search_fields = ['nom']


@admin.register(Habitacio)
class HabitacioAdmin(admin.ModelAdmin):
    list_display = ['nom', 'descripcio']
    search_fields = ['nom']


@admin.register(Solucio)
class SolucioAdmin(admin.ModelAdmin):
    list_display = ['usuari', 'personatge', 'arma', 'habitacio', 'resolta', 'creada_en']
    list_filter = ['resolta']
    search_fields = ['usuari__username']


@admin.register(Intent)
class IntentAdmin(admin.ModelAdmin):
    list_display = ['solucio', 'personatge', 'arma', 'habitacio', 'correcte', 'creat_en']
    list_filter = ['correcte']
