import random
from datetime import datetime
import codecs
import sqlite3
import re

"""
Instruccions: Creeu un únic fitxer anomenat cognom1_cognom2_nom.py amb les funcions completades.
Cada secció conté una breu narrativa (context) i l'enunciat tècnic.
Podeu executar aquest fitxer per veure exemples i provar les vostres funcions.
"""

# -------------------------------------------------------------
# 1) Les Proves de la Saviesa  — 10 pt
# Abans d’entrar al temple, un pedestall de pedra t’interroga:
#
# “Només els qui coneixen la mesura de la seva experiència podran passar.”
# Implementa la funció calcular_nivell(xp) que, segons els punts d’experiència, et revela el teu nivell d’aprenentatge.
#
# Enunciat: Implementeu calcular_nivell(xp: int) -> int:
#   - si xp < 100 -> retorna 1
#   - si 100 <= xp < 500 -> retorna 2
#   - si xp >= 500 -> retorna 3
# A més, imprimiu per consola: "Nivell assolit: X"
def calcular_nivell(xp: int) -> int:
    """Retorna el nivell segons xp. Implementa la regla descrita a l'enunciat."""
    if xp < 100:
        nivell = 1
    elif xp < 500:
        nivell = 2
    else:
        nivell = 3
    print(f"Nivell assolit: {nivell}")
    return nivell


# -------------------------------------------------------------
# 2) El Combat de la Lògica — 10 pt
#
# Abans d’entrar al temple, un pedestall de pedra t’interroga:
# “Només els qui coneixen la mesura de la seva experiència podran passar.”
# Implementa la funció calcular_nivell(xp) que, segons els punts d’experiència, et revela el teu nivell d’aprenentatge.
#
# Enunciat: implementar atacar(pdv_enemic: int, dany: int) -> int
#   - retorna els PDV restants (no negatius)
#   - imprimeix: "Enemic: PDV restants = Y"
def atacar(pdv_enemic: int, dany: int) -> int:
    """Aplica dany i retorna PDV restants (>=0)."""
    restants = max(0, pdv_enemic - dany)
    print(f"Enemic: PDV restants = {restants}")
    return restants


# -------------------------------------------------------------
# 3) L'Alè del Destí  — 10 pt
#
# El vent canvia. Els déus poden afavorir-te... o no.
# Implementa atac_critic(dany) que usa el mòdul random per decidir amb un 20% de probabilitat si el teu atac és crític (x2 de dany).
#
# Enunciat: atac_critic(dany: int) -> int
#   - 20% probabilitat d'aplicar dany * 2
#   - retorna el dany final aplicable
def atac_critic(dany: int) -> int:
    """Retorna dany o dany*2 amb probabilitat 20% per al crític."""
    if random.random() < 0.20:
        dany *= 2
    return dany


# -------------------------------------------------------------
# 4) El Llibre dels Conjurs  — 10 pt
#
# Tens davant teu un grimori polsós. Alguns conjurs només poden ser llançats si els registres correctament al llibre.
# Crea conjurs() que permeti triar entre registrar un nou conjur o mostrar l’hora en què un conjur fou inscrit.
#
# Enunciat:
#   - Implementa un objecte Conjurs amb mètodes:
#       mostrar_hora_conjur() -> imprimeix datetime.now().isoformat() i retorna la cadena
#       registrar_conjur(nom_conjur: str, filename='conjurs.txt') -> desa "Timestamp | nom_conjur"
#   - A més, proveeix funcions globals mostrar_hora_conjur() i registrar_conjur(...) que deleguin a l'objecte.
class Conjurs:
    """Classe que gestiona el registre de conjurs (fitxer + hora)."""

    def __init__(self, filename='conjurs.txt'):
        self.filename = filename

    def mostrar_hora_conjur(self) -> str:
        """Imprimeix i retorna l'hora actual en format ISO-8601."""
        ara = datetime.now().isoformat()
        print(ara)
        return ara

    def registrar_conjur(self, nom_conjur: str, filename: str = None) -> str:
        """Desa una línia 'Timestamp | nom_conjur' al fitxer i retorna la ruta del fitxer."""
        if filename is None:
            filename = self.filename
        timestamp = datetime.now().isoformat()
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f"{timestamp} | {nom_conjur}\n")
        return filename


# Instància pública per compatibilitat amb el test runner
conjurs = Conjurs()


def mostrar_hora_conjur():
    """Funció global que mostra l'hora (delegació)."""
    return conjurs.mostrar_hora_conjur()


def registrar_conjur(nom_conjur: str, filename: str = None):
    """Funció global que registra conjur (delegació)."""
    return conjurs.registrar_conjur(nom_conjur, filename=filename)


# -------------------------------------------------------------
# 5) El Laberint dels Ecos  — 10 pt
#
# Una màgia antiga t’ofereix un repte: generar el teu propi camí.
# Crea generar_laberint_aleatori(filas, columnes, percentatge_parets) que generi un mapa amb ‘S’ (inici), ‘E’ (sortida), i ‘X’ (parets). Desa’l a laberint_auto.txt.
#
# Enunciat: generar_laberint_aleatori(filas, columnes, percentatge_parets, fitxer='laberint_auto.txt')
#   - utilitza S per start i E per exit, X per paret, '.' o ' ' per espai lliure
#   - desa el resultat a fitxer
def generar_laberint_aleatori(filas=6, columnes=6, percentatge_parets=25, fitxer='laberint_auto.txt') -> str:
    """Genera i desa el laberint; retorna la ruta del fitxer creat."""
    laberint = []
    for i in range(filas):
        fila = []
        for j in range(columnes):
            if random.randint(1, 100) <= percentatge_parets:
                fila.append('X')
            else:
                fila.append('.')
        laberint.append(fila)
    laberint[0][0] = 'S'
    laberint[filas - 1][columnes - 1] = 'E'
    with open(fitxer, 'w', encoding='utf-8') as f:
        for fila in laberint:
            f.write(''.join(fila) + '\n')
    return fitxer


# -------------------------------------------------------------
# 6) La Mirada del Buscador  — 10 pt
#
# Un cop dins del laberint, només el coneixement et salvarà.
# Implementa mostrar_laberint(fitxer) que imprimeixi el mapa i compti els espais lliures.
#
# Enunciat: mostrar_laberint(fitxer) -> int (retorna nombre d'espais lliures '.' o ' ' segons aixis decidit en l'exercici anterior)
#   - imprimeix el laberint per pantalla i retorna el comptatge
def mostrar_laberint(fitxer: str) -> int:
    """Mostra laberint i retorna nombre d'espais lliures (inclou S i E)."""
    lliures = 0
    try:
        with open(fitxer, 'r', encoding='utf-8') as f:
            for linia in f:
                print(linia, end='')
                lliures += linia.count('.') + linia.count('S') + linia.count('E')
    except FileNotFoundError:
        print(f"No existeix el fitxer {fitxer}")
    return lliures


# -------------------------------------------------------------
# 7) El Grimori Fragmentat  — 10 pt
#
# Trobes fragments de textos màgics escrits en un llenguatge antic (ROT13).
# Crea processar_grimori(file_input, file_output) que:
# - Llegeixi el fitxer grimori.txt
# - Decodifiqui ROT13
# - Ordeni les línies
# - Les mostri i guardi a grimori_sorted.txt
#
# Enunciat: processar_grimori(file_input='grimori.txt', file_output='grimori_sorted.txt')
#   - llegeix, decodifica ROT13, ordena alfabèticament, imprimeix i desa
def processar_grimori(file_input="grimori.txt", file_output="grimori_sorted.txt") -> str:
    """Processa el grimori i desa el resultat ordenat; retorna la ruta del fitxer de sortida."""
    try:
        with open(file_input, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"No existeix {file_input}")
        return file_output
    decoded = [codecs.decode(line, 'rot_13') for line in lines]
    decoded.sort()
    with open(file_output, 'w', encoding='utf-8') as f:
        for line in decoded:
            print(line, end='')
            f.write(line)
    return file_output


# -------------------------------------------------------------
# 8) El Bestiari Perdut  — 20 pt
#
# Un arxiu de monstres antics espera ser reconstruït.
# Implementa bestiari() que gestioni una base de dades SQLite (bestiari.db) amb:
# (id INTEGER PK, nom TEXT, cr INTEGER, hp INTEGER, tipus TEXT)
# Permet: afegir, buscar, llistar i eliminar monstres.
# Enunciat:
#   - Crea la taula si no existeix: monstres(id INTEGER PK, nom TEXT, cr INTEGER, hp INTEGER, tipus TEXT)
#   - Proporciona funcions: inicialitzar_bestiari(conn), add_monstre(dbpath, nom, cr, hp, tipus),
#     search_monstre(dbpath, term), list_monstres(dbpath), delete_monstre(dbpath, id)
def inicialitzar_bestiari(conn):
    """Crea la taula 'monstres' si no existeix (utilitzat pel test runner)."""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS monstres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            cr INTEGER,
            hp INTEGER,
            tipus TEXT
        )
    ''')
    conn.commit()
    cursor.close()


def add_monstre(dbpath: str, nom: str, cr: int, hp: int, tipus: str) -> int:
    """Afegeix un monstre i retorna l'id (autoincrement)."""
    conn = sqlite3.connect(dbpath)
    inicialitzar_bestiari(conn)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO monstres (nom, cr, hp, tipus) VALUES (?, ?, ?, ?)",
        (nom, cr, hp, tipus)
    )
    conn.commit()
    mid = cursor.lastrowid
    cursor.close()
    conn.close()
    return mid


def search_monstre(dbpath: str, term: str):
    """Cerca monstres per nom (partial match) i retorna llistat de tuples."""
    conn = sqlite3.connect(dbpath)
    inicialitzar_bestiari(conn)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM monstres WHERE nom LIKE ?", (f'%{term}%',))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def list_monstres(dbpath: str):
    """Retorna la llista completa de monstres (tuples)."""
    conn = sqlite3.connect(dbpath)
    inicialitzar_bestiari(conn)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM monstres")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def delete_monstre(dbpath: str, mid: int) -> int:
    """Elimina per id i retorna nombre de registres afectats. Cal mirar el contingut del id."""
    conn = sqlite3.connect(dbpath)
    inicialitzar_bestiari(conn)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM monstres WHERE id=?", (mid,))
    conn.commit()
    affected = cursor.rowcount
    cursor.close()
    conn.close()
    return affected


# -------------------------------------------------------------
# 9) Els Daus del Destí  — 10 pt
#
# Les runes demanen una ofrena de sort.
# sCrea tirar(dice_notation) que accepti notació de daus (3d6, 1d20) i simuli diverses tirades, mostrant la millor i la mitjana.
#
# Enunciat: tirar(dice_notation: str, k: int) -> (millor, mitjana)
#   - llegir notació com 4d6, 1d20 etc.
#   - repetir k vegades, imprimir cada tirada amb detalls i retornar (millor, mitjana)
def tirar(dice_notation: str, k: int = 1):
    """Interpreta notació NdM, fa k repeticions, imprimeix resultats i retorna (millor, mitjana)."""
    match = re.match(r'^(\d+)d(\d+)$', dice_notation.strip())
    if not match:
        raise ValueError(f"Notació invàlida: {dice_notation}")
    n, m = int(match.group(1)), int(match.group(2))
    millor = None
    total_suma = 0
    for i in range(k):
        daus = [random.randint(1, m) for _ in range(n)]
        suma = sum(daus)
        print(f"Tirada {i + 1}: {daus} = {suma}")
        total_suma += suma
        if millor is None or suma > millor:
            millor = suma
    mitjana = total_suma / k if k > 0 else 0
    print(f"Millor: {millor}, Mitjana: {mitjana:.2f}")
    return millor, mitjana


# -------------------------------------------------------------
# Funció main amb exemples simulats
# -------------------------------------------------------------
def main():
    print("== Examen A — Les Fosques Tombes del Nord  ==")
    # Exemple 1: calcular_nivell
    try:
        print("-- Exemple: calcular_nivell(350) --")
        n = calcular_nivell(350)
        print("Retorn:", n)
    except Exception as e:
        print("calcular_nivell: NO IMPLEMENTAT:", e)

    # Exemple 2: atacar
    try:
        print("-- Exemple: atacar(120, 35) --")
        pdv = atacar(120, 35)
        print("Retorn:", pdv)
    except Exception as e:
        print("atacar: NO IMPLEMENTAT:", e)

    # Exemple 3: atac_critic
    try:
        print("-- Exemple: atac_critic(30) --")
        d = atac_critic(30)
        print("Retorn:", d)
    except Exception as e:
        print("atac_critic: NO IMPLEMENTAT:", e)

    # Exemple 4: conjurs
    try:
        print("-- Exemple: mostrar_hora_conjur() --")
        print(mostrar_hora_conjur())
    except Exception as e:
        print("mostrar_hora_conjur: NO IMPLEMENTAT:", e)

    try:
        print("-- Exemple: registrar_conjur('Escut Arca') --")
        registrar_conjur("Escut Arca")
    except Exception as e:
        print("registrar_conjur: NO IMPLEMENTAT:", e)

    # Exemple 5/6: laberint
    try:
        print("-- Exemple: generar_laberint_aleatori(6,6,25) --")
        f = generar_laberint_aleatori(6, 6, 25)
        print("-- Exemple: mostrar_laberint(f) --")
        mostrar_laberint(f)
    except Exception as e:
        print("laberint: NO IMPLEMENTAT:", e)

    # Exemple 7: grimori
    try:
        print("-- Exemple: processar_grimori() --")
        processar_grimori("grimori.txt", "grimori_sorted.txt")
    except Exception as e:
        print("processar_grimori: NO IMPLEMENTAT:", e)

    # Exemple 8: bestiari (proves no interactives)
    try:
        print("-- Exemple: add_monstre/test/list --")
        db = "bestiari_test_demo.db"
        add_monstre(db, "Goblin", 1, 7, "Humanoid")
        print(list_monstres(db))
        print(search_monstre(db,"Gob"))

    except Exception as e:
        print("bestiari: NO IMPLEMENTAT:", e)

    # Exemple 9: daus
    try:
        print("-- Exemple: tirar('4d6', 5) --")
        tirar("4d6", 5)
    except Exception as e:
        print("tirar: NO IMPLEMENTAT:", e)


if __name__ == '__main__':
    main()