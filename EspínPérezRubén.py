import random
from datetime import datetime
import sqlite3

# -------------------------------------------------------------
# 1) L'Escànner de Biometria — 10 pt
# Per accedir a la nau, l'ordinador central ha de validar el teu rang.
# Enunciat: Implementeu calcular_rang(punts: int) -> str:
#   - si punts < 200 -> retorna "Cadet"
#   - si 200 <= punts < 1000 -> retorna "Oficial"
#   - si punts >= 1000 -> retorna "Capità"
# A més, imprimiu per consola: "Rang assignat: X"
def calcular_rang(punts: int) -> str:
    # TODO: Implementa la funció
    if punts < 200:
        rang = "Cadet"
    if punts < 1000:
        rang = "Oficial"
    if punts >= 1000:
        rang = "Capità"
    print(f"Rango assignat: {rang}")
    return rang


# -------------------------------------------------------------
# 2) Gestió de Combustible — 10 pt
# Durant el viatge, consumeixes heli-3. No pots quedar-te amb valors negatius.
# Enunciat: implementar consumir_recursos(actuals: float, consum: float) -> float
#   - retorna el combustible restant (mínim 0.0)
#   - imprimeix: "Dipòsit: Queden Y unitats"
def consumir_recursos(actuals: float, consum: float) -> float:
    # TODO: Implementa la funció
    restant = actuals - consum
    if restant < 0:
        restant = 0.0
    print(f"Diposit: Quedan {restant} unitats")
    return restant

# -------------------------------------------------------------
# 3) Salt Hiperespacial — 10 pt
# El motor de salt no és 100% fiable. A vegades, el salt és "Perfecte" i recorre el doble.
# Enunciat: salt_hiperespacial(distancia_base: int) -> int
#   - 15% de probabilitat de fer un salt crític (distancia_base * 2)
#   - retorna la distància final recorreguda
def salt_hiperespacial(distancia_base: int) -> int:
    # TODO: Implementa la funció
    if random.random() < 0.15:
        return distancia_base * 2
    return distancia_base

# -------------------------------------------------------------
# 4) El Log de Bitàcola — 10 pt
# Cada acció important s'ha de registrar amb un timestamp professional.
# Enunciat:
#   - Implementa un objecte Bitacola amb mètodes:
#       obtenir_timestamp() -> retorna datetime.now().strftime("%Y-%m-%d %H:%M")
#       escriure_entrada(missatge: str, fitxer='log_nau.txt') -> desa "TIMESTAMP | missatge"
class Bitacola:
    def __init__(self, fitxer='log_nau.txt'):
        self.fitxer = fitxer

    def obtenir_timestamp(self) -> str:
        # TODO: Implementa mètode
        return datetime.now().strftime("%Y-%m-%d %H:%M")


    def escriure_entrada(self, missatge: str, fitxer: str = None) -> str:
        # TODO: Implementa mètode
        fitxer = self.fitxer
        entrada = f"{self.obtenir_timestamp()} | {missatge}\n"
        with open(fitxer, "a") as f:
            f.write(entrada)
        return entrada

# Instància global per a les proves
log_sistema = Bitacola()

# -------------------------------------------------------------
# 5) Generador de Sectors Estel·lars — 10 pt
# Crea un mapa espacial on '#' són asteroides i '.' és espai buit.
# Enunciat: generar_sector(files, columnes, prob_ast, fitxer='sector.txt')
#   - '#' per asteroides, '.' per espai buit.
#   - Desa el mapa al fitxer línia per línia.
def generar_sector(files=5, columnes=5, prob_ast=20, fitxer='sector.txt') -> str:
    # TODO: Implementa la funció
    with open(fitxer, "w") as f:
        for a in range(files):
            linea = ""
        for a in range(columnes):
            if random.randint(1, 100) <= prob_ast:
                linea += "#"
            else:
                linea += "."
        f.write(linea + "\n")

# -------------------------------------------------------------
# 6) Radar de Proximitat — 10 pt
# Llegiu el fitxer del sector i compteu quants asteroides hi ha en total.
# Enunciat: escanejar_sector(fitxer) -> int
#   - imprimeix el mapa per pantalla línia a línia.
#   - retorna el recompte total de '#' trobats.
def escanejar_sector(fitxer: str) -> int:
    # TODO: Implementa la funció
    total = 0
    with open(fitxer, "r") as f:
        for linia in f:
            print(linia.strip())
            total += linia.count("#")
    return total


# -------------------------------------------------------------
# 7) Analitzador de Telemetria — 10 pt (NOU: Substitueix el xifrat)
# Reps un fitxer de text amb temperatures del motor: "motor1:45, motor2:55, motor3:120".
# Enunciat: processar_telemetria(fitxer_entrada, llindar_alerta) -> list
#   - Llegeix el fitxer (format "nom:valor" per línia).
#   - Retorna una llista amb els noms dels motors que superen el llindar_alerta.
def processar_telemetria(fitxer_entrada="telemetria.txt", llindar_alerta=100) -> list:
    # TODO: Implementa la funció
    alertes = []
    with open(fitxer_entrada, "r") as f:
        for linia in f:
            nom, valor = linia.strip().split(":")
            if int(valor) > llindar_alerta:
                alertes.append(nom)
    return alertes


# -------------------------------------------------------------
# 8) Base de Dades de Tripulació — 20 pt
# Gestió dels tripulants mitjançant SQLite.
# Enunciat:
#   - Taula 'tripulants' (id PK, nom TEXT, rang TEXT, edat INTEGER)
#   - Funcions: inicialitzar_db(conn), afegir_tripulant(db, ...), list_tripulants(db).
def inicialitzar_db(conn):
    # TODO: Implementa la creació de taula
    conn = sqlite3.connect("Space_Oditty.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tripulants(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        rang TEXT,
        edat INTEGER
    )
''')
    conn.commit()
    cursor.close()

def afegir_tripulant(dbpath, nom, rang, edat):
    # TODO: Implementa l'insert
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(
    f"INSERT INTO tripulants (nom, rang, edat) VALUES ('{nom}', '{rang}', {edat})"
)
    conn.commit()
    conn.close()


# -------------------------------------------------------------
# 9) Inventari de Recursos — 10 pt (NOU: Substitueix Regex)
# Gestiona el diccionari de recanvis de la nau.
# Enunciat: actualitzar_inventari(inventari: dict, item: str, quantitat: int) -> dict
#   - Si l'item ja existeix al diccionari, suma la quantitat.
#   - Si no existeix, afegeix-lo amb la quantitat donada.
#   - Retorna el diccionari actualitzat.
def actualitzar_inventari(inventari: dict, item: str, quantitat: int) -> dict:
    # TODO: Implementa la gestió del diccionari
    if item in inventari:
        inventari[item] += quantitat
    else:
        inventari[item] = quantitat
    return inventari




# -------------------------------------------------------------
# MAIN: Simulació de proves per a l'alumne
# -------------------------------------------------------------
def main():
    print("--- INICIANT PROVES DE L'ESTACIÓ ORBITAL (Recuperació) ---")

    # Prova 1 & 2
    print(f"Rang per 500 punts: {calcular_rang(500)}")
    print(f"Combustible restant: {consumir_recursos(100.0, 30.5)}")

    # Prova 4: Log
    try:
        log_sistema.escriure_entrada("Sistemes iniciats")
        print("Log registrat correctament.")
    except:
        print("Error en l'exercici del Log.")

    # Prova 7: Telemetria (creem fitxer de prova)
    with open("telemetria.txt", "w") as f:
        f.write("Motor_A:45\nMotor_B:120\nReactor_Principal:150")
    alertes = processar_telemetria("telemetria.txt", 100)
    print(f"Alertes de motor detectades: {alertes}")

    # Prova 9: Inventari
    stock = {"Oxigen": 10, "Bateries": 5}
    stock = actualitzar_inventari(stock, "Bateries", 3)
    stock = actualitzar_inventari(stock, "Menjar", 20)
    print(f"Inventari actualitzat: {stock}")

if __name__ == '__main__':
    main()