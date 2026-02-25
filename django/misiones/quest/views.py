from django.shortcuts import render
from .models import Mision


def quest(request):
    misiones = Mision.objects.all()
    contexto = {"misiones": misiones}
    return render(request, "index.html", contexto)
