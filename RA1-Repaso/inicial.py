'''
1-Demana per teclat una quantitat i a continuació entra
per teclat diversos noms fins a la quantitat entrada.
Al final mostra tots els noms per pantalla.
Exemple:
Entra quantitat: 4
nom 1 ? Mortadelo
nom 2 ? Anacleto
nom 3 ? Mortadelo
nom 4 ? Filemón
Els noms són: Mortadelo Anacleto Mortadelo Filemón
'''

#versió amb bucle for

quantitat=int(input("Entra quantitat: "))

llista=[]

for i in range(1,quantitat+1):
    nom=input("nom "+str(i)+" ? ")
    llista.append(nom)

print("Els noms són:", end=' ')
for nom in llista:
    print(nom, end=' ')

print()

#versió amb bucle while

quantitat=int(input("Entra quantitat: "))

llista=[]
i=0
while i<quantitat:
    i=i+1
    nom=input("nom "+str(i)+" ?")
    llista.append(nom)

print("Els noms són:", end=' ')
i=0
while i<len(llista):
    print(llista[i], end=' ')
    i=i+1

'''
2-Igual a l’exercici 1, però sense permetre noms repetits.
Exemple:
Entra quantitat: 4
nom 1 ? Mortadelo
nom 2 ? Anacleto
nom 3 ? Mortadelo
Repetit, nom 3 ? Sacarino
nom 4 ? Filemón
Els noms són: Mortadelo Anacleto Filemón Sacarino
'''

quantitat=int(input("Entra quantitat: "))

llista=[]

i=1
while i<=quantitat:
    nom=input("nom "+str(i)+" ? ")
    if nom in llista:
        # Repetit
        print("Repetit,", end='')
    else:
        # Nou
        llista.append(nom)
        i=i+1

print("Els noms són:", end=' ')
for nom in llista:
    print(nom, end=' ')

'''
3-Crea un diccionari, amb diverses dades d’un individu,
seguint aquesta estructura:

{“nom”: …. , “cognom”: …. , “edat”: …. , “pes”: …. }

Demana les dades per teclat i mostra la informació al final.
Si l’individu és major d’edat, afegeix “(major d’edat)”.
Exemple 1:
Entra nom: Bob Esponja
Entra cognom: SquarePants
Entra edat: 15
Entra pes: 0.2
Aquestes són les dades: Bob Esponja SquarePants 15 anys 0.2 Kg
Exemple 2:
Entra nom: Arenita
Entra cognom: Mejillas
Entra edat: 19
Entra pes: 1.1
Aquestes són les dades: Arenita Mejillas 19 anys 1.1 Kg (major d’edat)
'''

nom=input("Entra el nom: ")
cognom=input("Entra el cognom: ")
edat=int(input("Entra edat: "))
pes=float(input("Entra pes: "))

dades={"nom": nom , "cognom": cognom, "edat": edat , "pes": pes}

print(dades["nom"], dades["cognom"], dades["edat"], "anys",
      dades["pes"], "Kg", end='')

if dades["edat"]>=18:
    print(" (major d'edat)")

'''
4-Crea una llista (list) de diccionaris com els de l’exercici 3.
No fa falta llegir les dades per teclat, es pot inicialitzar al codi.
Mostra el contingut de tota la llista segons s’indica a l’exercici 3.
Mostra la quantitat d’individus majors d’edat.
Mostra la mitjana del pes de tots els individus.
Mostra els noms què s’han repetit o el missatge “SENSE NOMS REPETITS”.
'''

dades1={"nom": "Bob Esponja" , "cognom": "Squarepants", "edat": 14 , "pes": 0.3}
dades2={"nom": "Arenita" , "cognom": "Mejillas", "edat": 20 , "pes": 1.8}
dades3={"nom": "Patricio" , "cognom": "Estrella", "edat": 21 , "pes": 0.4}
dades4={"nom": "Patricio" , "cognom": "Estrella", "edat": 15 , "pes": 0.4}
dades5={"nom": "Arenita" , "cognom": "Mejillas", "edat": 13 , "pes": 1.8}
dades6={"nom": "Arenita" , "cognom": "Mejillas", "edat": 18 , "pes": 1.8}

llista =[ dades1, dades2, dades3, dades4, dades5, dades6]

majors=0  # comptabilitza els majors d'edat
sumapes=0; # suma de tots els pesos per càlcul de la mitjana
apareguts=list() # llista de noms apareguts
repetits=set() # set de noms repetits

for dades in llista:
    print(dades["nom"], dades["cognom"], dades["edat"], "anys",
      dades["pes"], "Kg", end='')
    if dades["edat"]>=18:
        print(" (major d'edat)")
        majors=majors+1
    else:
        # S'ha de fer salt de línia si no és major d'edat
        print()
    sumapes=sumapes+dades["pes"]
    if dades["nom"] in apareguts:
        # És un nom repetit
        repetits.add(dades["nom"])
    else:
        # És la primera vegada que surt el nom
        apareguts.append(dades["nom"])

mitjana=sumapes/len(llista)
print("Hi ha",majors, "individus majors d'edat")
print("La mitjana dels pesos és", mitjana, "Kg")
if len(repetits)==0:
    print("SENSE NOMS REPETITS")
else:
    print("Els nom repetits són: ", repetits)


'''
5-Mostra tots els individus de l’exercici 4, què són majors d’edat i
tenen un pes igual o superior a la mitjana.

'''

dades1={"nom": "Bob Esponja" , "cognom": "Squarepants", "edat": 14 , "pes": 0.3}
dades2={"nom": "Arenita" , "cognom": "Mejillas", "edat": 20 , "pes": 1.8}
dades3={"nom": "Patricio" , "cognom": "Estrella", "edat": 21 , "pes": 0.4}
dades4={"nom": "Patricio" , "cognom": "Estrella", "edat": 15 , "pes": 0.4}
dades5={"nom": "Arenita" , "cognom": "Mejillas", "edat": 13 , "pes": 1.8}
dades6={"nom": "Arenita" , "cognom": "Mejillas", "edat": 18 , "pes": 1.8}

llista =[ dades1, dades2, dades3, dades4, dades5, dades6]

sumapes=0; # suma de tots els pesos per càlcul de la mitjana

for dades in llista:
    sumapes=sumapes+dades["pes"]

mitjana=sumapes/len(llista)
print("La mitjana dels pesos és", mitjana, "Kg")

for dades in llista:
    if dades["edat"]>=18 and dades["pes"]>=mitjana:
        print(dades["nom"], dades["cognom"], dades["edat"], "anys",
          dades["pes"], "Kg", end='')
        if dades["edat"]>=18:
            print(" (major d'edat)")
        else:
            # S'ha de fer salt de línia si no és major d'edat
            print()






Copilot is an AI and may make mistakes. Using Copilot means you agree to the Terms of Use. See our Privacy Statement.
Today
You said

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
    pass


# -------------------------------------------------------------
# 2) Gestió de Combustible — 10 pt
# Durant el viatge, consumeixes heli-3. No pots quedar-te amb valors negatius.
# Enunciat: implementar consumir_recursos(actuals: float, consum: float) -> float
#   - retorna el combustible restant (mínim 0.0)
#   - imprimeix: "Dipòsit: Queden Y unitats"
def consumir_recursos(actuals: float, consum: float) -> float:
    # TODO: Implementa la funció
    pass


# -------------------------------------------------------------
# 3) Salt Hiperespacial — 10 pt
# El motor de salt no és 100% fiable. A vegades, el salt és "Perfecte" i recorre el doble.
# Enunciat: salt_hiperespacial(distancia_base: int) -> int
#   - 15% de probabilitat de fer un salt crític (distancia_base * 2)
#   - retorna la distància final recorreguda
def salt_hiperespacial(distancia_base: int) -> int:
    # TODO: Implementa la funció
    pass


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
        pass

    def escriure_entrada(self, missatge: str, fitxer: str = None) -> str:
        # TODO: Implementa mètode
        pass

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
    pass


# -------------------------------------------------------------
# 6) Radar de Proximitat — 10 pt
# Llegiu el fitxer del sector i compteu quants asteroides hi ha en total.
# Enunciat: escanejar_sector(fitxer) -> int
#   - imprimeix el mapa per pantalla línia a línia.
#   - retorna el recompte total de '#' trobats.
def escanejar_sector(fitxer: str) -> int:
    # TODO: Implementa la funció
    pass


# -------------------------------------------------------------
# 7) Analitzador de Telemetria — 10 pt (NOU: Substitueix el xifrat)
# Reps un fitxer de text amb temperatures del motor: "motor1:45, motor2:55, motor3:120".
# Enunciat: processar_telemetria(fitxer_entrada, llindar_alerta) -> list
#   - Llegeix el fitxer (format "nom:valor" per línia).
#   - Retorna una llista amb els noms dels motors que superen el llindar_alerta.
def processar_telemetria(fitxer_entrada="telemetria.txt", llindar_alerta=100) -> list:
    # TODO: Implementa la funció
    pass


# -------------------------------------------------------------
# 8) Base de Dades de Tripulació — 20 pt
# Gestió dels tripulants mitjançant SQLite.
# Enunciat:
#   - Taula 'tripulants' (id PK, nom TEXT, rang TEXT, edat INTEGER)
#   - Funcions: inicialitzar_db(conn), afegir_tripulant(db, ...), list_tripulants(db).
def inicialitzar_db(conn):
    # TODO: Implementa la creació de taula
    pass

def afegir_tripulant(dbpath, nom, rang, edat):
    # TODO: Implementa l'insert
    pass


# -------------------------------------------------------------
# 9) Inventari de Recursos — 10 pt (NOU: Substitueix Regex)
# Gestiona el diccionari de recanvis de la nau.
# Enunciat: actualitzar_inventari(inventari: dict, item: str, quantitat: int) -> dict
#   - Si l'item ja existeix al diccionari, suma la quantitat.
#   - Si no existeix, afegeix-lo amb la quantitat donada.
#   - Retorna el diccionari actualitzat.
def actualitzar_inventari(inventari: dict, item: str, quantitat: int) -> dict:
    # TODO: Implementa la gestió del diccionari
    pass




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
Copilot said
Aquí tens una versió completament implementada del teu exercici. He mantingut l’estil del teu codi i he afegit totes les funcionalitats que demanen els enunciats. Pots copiar‑lo i executar-lo directament.

🚀 Solució completa del programa
python


Copy
import random
from datetime import datetime
import sqlite3

# -------------------------------------------------------------
# 1) L'Escànner de Biometria — 10 pt
def calcular_rang(punts: int) -> str:
    if punts < 200:
        rang = "Cadet"
    elif punts < 1000:
        rang = "Oficial"
    else:
        rang = "Capità"
    print(f"Rang assignat: {rang}")
    return rang


# -------------------------------------------------------------
# 2) Gestió de Combustible — 10 pt
def consumir_recursos(actuals: float, consum: float) -> float:
    restant = max(0.0, actuals - consum)
    print(f"Dipòsit: Queden {restant} unitats")
    return restant


# -------------------------------------------------------------
# 3) Salt Hiperespacial — 10 pt
def salt_hiperespacial(distancia_base: int) -> int:
    if random.random() < 0.15:
        return distancia_base * 2
    return distancia_base


# -------------------------------------------------------------
# 4) El Log de Bitàcola — 10 pt
class Bitacola:
    def __init__(self, fitxer='log_nau.txt'):
        self.fitxer = fitxer

    def obtenir_timestamp(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M")

    def escriure_entrada(self, missatge: str, fitxer: str = None) -> str:
        if fitxer is None:
            fitxer = self.fitxer
        entrada = f"{self.obtenir_timestamp()} | {missatge}\n"
        with open(fitxer, "a") as f:
            f.write(entrada)
        return entrada

log_sistema = Bitacola()


# -------------------------------------------------------------
# 5) Generador de Sectors Estel·lars — 10 pt
def generar_sector(files=5, columnes=5, prob_ast=20, fitxer='sector.txt') -> str:
    with open(fitxer, "w") as f:
        for _ in range(files):
            linia = ""
            for _ in range(columnes):
                if random.randint(1, 100) <= prob_ast:
                    linia += "#"
                else:
                    linia += "."
            f.write(linia + "\n")
    return fitxer


# -------------------------------------------------------------
# 6) Radar de Proximitat — 10 pt
def escanejar_sector(fitxer: str) -> int:
    total = 0
    with open(fitxer, "r") as f:
        for linia in f:
            print(linia.strip())
            total += linia.count("#")
    return total


# -------------------------------------------------------------
# 7) Analitzador de Telemetria — 10 pt
def processar_telemetria(fitxer_entrada="telemetria.txt", llindar_alerta=100) -> list:
    alertes = []
    with open(fitxer_entrada, "r") as f:
        for linia in f:
            nom, valor = linia.strip().split(":")
            if int(valor) > llindar_alerta:
                alertes.append(nom)
    return alertes


# -------------------------------------------------------------
# 8) Base de Dades de Tripulació — 20 pt
def inicialitzar_db(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tripulants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            rang TEXT,
            edat INTEGER
        )
    """)
    conn.commit()

def afegir_tripulant(dbpath, nom, rang, edat):
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tripulants (nom, rang, edat) VALUES (?, ?, ?)",
                   (nom, rang, edat))
    conn.commit








import random
from datetime import datetime
import sqlite3

def calcular_rang(punts):
    if punts < 200:
        rang = "Cadet"
    elif punts < 1000:
        rang = "Oficial"
    else:
        rang = "Capità"

    print("Rang assignat:", rang)
    return rang


def consumir_recursos(actuals, consum):
    restant = actuals - consum
    if restant < 0:
        restant = 0

    print("Dipòsit: Queden", restant, "unitats")
    return restant


def salt_hiperespacial(distancia_base):
    if random.random() < 0.15:
        return distancia_base * 2
    return distancia_base


class Bitacola:
    def __init__(self):
        self.fitxer = "log_nau.txt"

    def obtenir_timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M")

    def escriure_entrada(self, missatge):
        entrada = self.obtenir_timestamp() + " | " + missatge + "\n"
        f = open(self.fitxer, "a")
        f.write(entrada)
        f.close()
        return entrada


log_sistema = Bitacola()


def generar_sector(files=5, columnes=5, prob_ast=20, fitxer="sector.txt"):
    f = open(fitxer, "w")

    for _ in range(files):
        linea = ""
        for _ in range(columnes):
            if random.randint(1, 100) <= prob_ast:
                linea += "#"
            else:
                linea += "."
        f.write(linea + "\n")

    f.close()
    return fitxer


def escanejar_sector(fitxer):
    total = 0
    f = open(fitxer, "r")

    for linia in f:
        print(linia.strip())
        total += linia.count("#")

    f.close()
    return total


def processar_telemetria(fitxer_entrada, llindar_alerta):
    alertes = []
    f = open(fitxer_entrada, "r")

    for linia in f:
        nom, valor = linia.strip().split(":")
        if int(valor) > llindar_alerta:
            alertes.append(nom)

    f.close()
    return alertes


def inicialitzar_db(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tripulants(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        rang TEXT,
        edat INTEGER
    )
    """)
    conn.commit()


def afegir_tripulant(dbpath, nom, rang, edat):
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tripulants (nom, rang, edat) VALUES (?, ?, ?)",
        (nom, rang, edat)
    )

    conn.commit()
    conn.close()


def actualitzar_inventari(inventari, item, quantitat):
    if item in inventari:
        inventari[item] += quantitat
    else:
        inventari[item] = quantitat
    return inventari