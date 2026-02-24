from django.shortcuts import render


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
