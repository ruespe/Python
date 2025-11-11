
import random


def tirar(dice_notation: str, k: int = 1):
    """Interpreta notació NdM, fa k repeticions, imprimeix resultats i retorna
    (millor, mitjana)."""
    n, m = map(int, dice_notation.lower().split("d"))
    resultats = []

    for _ in range(k):
        tirada = sum(random.randint(1, m) for _ in range(n))
        resultats.append(tirada)
        print(f"Tirada: {tirada}")

    millor = max(resultats)
    mitjana = sum(resultats) / len(resultats)
    return millor, mitjana


def atac_critic(dany: int) -> int:
    """Retorna dany o dany*2 amb probabilitat 20% per al crític."""
    if random.random() < 0.2:
        return dany * 2
    return dany

# TESTS UNITARIOS
# Test para la función tirar


def test_tirar_tipo():
    mejor, media = tirar("1d6", k=3)
    assert isinstance(mejor, int)
    assert isinstance(media, float)


def test_tirar_rango():
    n, m = 2, 6
    k = 5
    mejor, media = tirar(f"{n}d{m}", k)
    assert n <= mejor <= n*m
    assert n <= media <= n*m


def test_tirar_1d6():
    mejor, media = tirar("1d6", k=10)
    assert 1 <= mejor <= 6
    assert 1 <= media <= 6


def test_tirar_multiples():
    n, m, k = 3, 4, 5
    mejor, media = tirar(f"{n}d{m}", k)
    assert n <= mejor <= n*m
    assert n <= media <= n*m

# Test para la función atac_critic


def test_atac_critic_tipo():
    resultado = atac_critic(10)
    assert isinstance(resultado, int)


def test_atac_critic_valores():
    dany = 10
    resultado = atac_critic(dany)
    assert resultado in (dany, dany * 2)


def test_atac_critic_determinista():
    random.seed(1)
    dany = 10
    resultado = atac_critic(dany)
    assert resultado in (dany, dany * 2)
