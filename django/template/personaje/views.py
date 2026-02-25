from django.shortcuts import redirect, render

from .forms import PersonajeForm


def personaje(request):
    personajes = [
        {
            "nombre": "Gustaf",
            "raza": "Humano",
            "clase": "Clerigo",
            "nivel": 10,
            "stats": {"STR": 18, "DEX": 10, "CON": 18, "INT": 18, "WIS": 10, "CHA": 10},
            "habilidades": ["Bendición", "Sanar"],
            "equipamiento": ["Morning Star", "Daga"],
        },
        {
            "nombre": "Lyra",
            "raza": "Elfa",
            "clase": "Maga",
            "nivel": 40,
            "stats": {"STR": 8, "DEX": 14, "CON": 12, "INT": 19, "WIS": 13, "CHA": 11},
            "habilidades": ["Bola de fuego", "Escudo arcano"],
            "equipamiento": ["Báculo", "Túnica"],
        },
    ]
    contexto = {"personajes": personajes}
    return render(request, "personaje.html", contexto)


def crear_personaje(request):
    if request.method == "POST":
        form = PersonajeForm(request.POST)
        if form.is_valid():
            # commit=False: crea el objeto en memoria pero no lo guarda aún en la BD
            personaje_obj = form.save(commit=False)

            if form.cleaned_data.get("auto_generar"):
                # reescribe raza, clase y todos los stats con tiradas 4d6
                personaje_obj.generate_stats()

            # Ahora sí se gurda BD
            personaje_obj.save()
            return redirect("crear_personaje")
    else:
        form = PersonajeForm()

    return render(request, "personaje_form.html", {"form": form})
