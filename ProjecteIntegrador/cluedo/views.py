import json
import random
from functools import wraps

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.views.decorators.http import require_http_methods

from .models import Arma, Habitacio, Intent, Personatge, Solucio


def auth_required(view_func):
    """Decorador que exigeix que l'usuari estigui autenticat."""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Autenticació requerida'}, status=401)
        return view_func(request, *args, **kwargs)
    return wrapper


# ---------------------------------------------------------------------------
# CSRF
# ---------------------------------------------------------------------------

@ensure_csrf_cookie
def get_csrf(request):
    """GET /api/csrf/ - Retorna el token CSRF i assegura que la cookie s'envia."""
    return JsonResponse({'csrfToken': get_token(request)})


# ---------------------------------------------------------------------------
# Autenticació
# ---------------------------------------------------------------------------

@ensure_csrf_cookie
def me_view(request):
    """GET /api/auth/me/ - Retorna l'estat d'autenticació de l'usuari actual."""
    if request.user.is_authenticated:
        return JsonResponse({'authenticated': True, 'username': request.user.username})
    return JsonResponse({'authenticated': False})


@csrf_exempt
@require_http_methods(['POST'])
def login_view(request):
    """POST /api/auth/login/ - Inicia sessió amb usuari i contrasenya."""
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON invàlid'}, status=400)

    username = data.get('username', '').strip()
    password = data.get('password', '')

    if not username or not password:
        return JsonResponse({'error': 'Cal usuari i contrasenya'}, status=400)

    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return JsonResponse({'ok': True, 'username': user.username})
    return JsonResponse({'error': 'Credencials incorrectes'}, status=400)


@csrf_exempt
@require_http_methods(['POST'])
def register_view(request):
    """POST /api/auth/register/ - Registra un nou usuari i inicia sessió."""
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON invàlid'}, status=400)

    username = data.get('username', '').strip()
    password = data.get('password', '')

    if not username or not password:
        return JsonResponse({'error': 'Cal usuari i contrasenya'}, status=400)
    if len(password) < 6:
        return JsonResponse({'error': 'La contrasenya ha de tenir almenys 6 caràcters'}, status=400)
    if User.objects.filter(username=username).exists():
        return JsonResponse({'error': "L'usuari ja existeix"}, status=400)

    user = User.objects.create_user(username=username, password=password)
    login(request, user)
    return JsonResponse({'ok': True, 'username': user.username})


@require_http_methods(['POST'])
def logout_view(request):
    """POST /api/auth/logout/ - Tanca la sessió de l'usuari."""
    logout(request)
    return JsonResponse({'ok': True})


# ---------------------------------------------------------------------------
# Dades del joc (lectura pública)
# ---------------------------------------------------------------------------

def personatges_view(request):
    """GET /api/personatges/ - Llista tots els personatges disponibles."""
    personatges = list(Personatge.objects.values('id', 'nom', 'descripcio'))
    return JsonResponse(personatges, safe=False)


def armes_view(request):
    """GET /api/armes/ - Llista totes les armes disponibles."""
    armes = list(Arma.objects.values('id', 'nom', 'descripcio'))
    return JsonResponse(armes, safe=False)


def habitacions_view(request):
    """GET /api/habitacions/ - Llista totes les habitacions disponibles."""
    habitacions = list(Habitacio.objects.values('id', 'nom', 'descripcio'))
    return JsonResponse(habitacions, safe=False)


# ---------------------------------------------------------------------------
# Lògica del joc
# ---------------------------------------------------------------------------

@auth_required
def partida_activa_view(request):
    """GET /api/partida-activa/ - Retorna la partida activa de l'usuari, si n'hi ha."""
    try:
        solucio = Solucio.objects.filter(
            usuari=request.user, resolta=False
        ).latest('creada_en')
        return JsonResponse({
            'activa': True,
            'solucio_id': solucio.id,
            'num_intents': solucio.intents.count(),
        })
    except Solucio.DoesNotExist:
        return JsonResponse({'activa': False})


@auth_required
@csrf_exempt
@require_http_methods(['POST'])
def nova_partida_view(request):
    """POST /api/nova-partida/ - Inicia una nova partida amb solució aleatòria."""
    personatges = list(Personatge.objects.all())
    armes = list(Arma.objects.all())
    habitacions = list(Habitacio.objects.all())

    if not personatges or not armes or not habitacions:
        return JsonResponse({'error': 'No hi ha dades al joc. Executa poblar_dades.'}, status=500)

    solucio = Solucio.objects.create(
        usuari=request.user,
        personatge=random.choice(personatges),
        arma=random.choice(armes),
        habitacio=random.choice(habitacions),
    )
    return JsonResponse({'ok': True, 'solucio_id': solucio.id})


@auth_required
@csrf_exempt
@require_http_methods(['POST'])
def acusar_view(request):
    """POST /api/acusar/ - Processa una acusació i retorna el resultat."""
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON invàlid'}, status=400)

    solucio_id = data.get('solucio_id')
    personatge_id = data.get('personatge_id')
    arma_id = data.get('arma_id')
    habitacio_id = data.get('habitacio_id')
    temps = data.get('temps', 0)

    if not all([solucio_id, personatge_id, arma_id, habitacio_id]):
        return JsonResponse({'error': 'Falten camps obligatoris'}, status=400)

    # Verificar que la partida existeix i pertany a l'usuari
    try:
        solucio = Solucio.objects.get(id=solucio_id, usuari=request.user, resolta=False)
    except Solucio.DoesNotExist:
        return JsonResponse({'error': 'Partida no trobada o ja resolta'}, status=404)

    # Obtenir els objectes acusats
    try:
        personatge = Personatge.objects.get(id=personatge_id)
        arma = Arma.objects.get(id=arma_id)
        habitacio = Habitacio.objects.get(id=habitacio_id)
    except (Personatge.DoesNotExist, Arma.DoesNotExist, Habitacio.DoesNotExist):
        return JsonResponse({'error': 'Dades invàlides'}, status=400)

    # Comprovar quants elements són correctes
    encert_personatge = personatge.id == solucio.personatge.id
    encert_arma = arma.id == solucio.arma.id
    encert_habitacio = habitacio.id == solucio.habitacio.id
    correcte = encert_personatge and encert_arma and encert_habitacio

    # Desar l'intent a la base de dades
    Intent.objects.create(
        solucio=solucio,
        personatge=personatge,
        arma=arma,
        habitacio=habitacio,
        encert_personatge=encert_personatge,
        encert_arma=encert_arma,
        encert_habitacio=encert_habitacio,
        correcte=correcte,
    )

    # Si és correcte, marcar la partida com a resolta i desar el temps
    if correcte:
        solucio.resolta = True
        solucio.temps_resolucio = temps
        solucio.save()

    return JsonResponse({
        'correcte': correcte,
        'encert_personatge': encert_personatge,
        'encert_arma': encert_arma,
        'encert_habitacio': encert_habitacio,
        'num_intent': solucio.intents.count(),
    })


@auth_required
def historial_view(request):
    """GET /api/historial/ - Retorna l'historial de partides de l'usuari."""
    solucions = (
        Solucio.objects
        .filter(usuari=request.user)
        .prefetch_related('intents__personatge', 'intents__arma', 'intents__habitacio')
        .select_related('personatge', 'arma', 'habitacio')
        .order_by('-creada_en')
    )

    historial = []
    for solucio in solucions:
        intents = [
            {
                'personatge': intent.personatge.nom,
                'arma': intent.arma.nom,
                'habitacio': intent.habitacio.nom,
                'encert_personatge': intent.encert_personatge,
                'encert_arma': intent.encert_arma,
                'encert_habitacio': intent.encert_habitacio,
                'correcte': intent.correcte,
                'creat_en': intent.creat_en.isoformat(),
            }
            for intent in solucio.intents.all()
        ]
        historial.append({
            'id': solucio.id,
            'creada_en': solucio.creada_en.isoformat(),
            'resolta': solucio.resolta,
            'temps_resolucio': solucio.temps_resolucio,
            'num_intents': solucio.intents.count(),
            'intents': intents,
        })

    return JsonResponse(historial, safe=False)
