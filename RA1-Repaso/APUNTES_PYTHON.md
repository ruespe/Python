# Apuntes Python — RA1 Repaso

Estos apuntes resumen todos los ejercicios de la carpeta `RA1-Repaso` y explican cómo funciona cada concepto.

---

## 1. BUCLES Y LISTAS (`bucleYlista.py`)

### ¿Qué es una lista?

Una lista guarda varios valores en orden. Se crea con corchetes `[]`.

```python
llista1 = [45, -6, 0, -32, 23, 9]
```

### Bucle `for` sobre una lista

Recorre cada elemento uno a uno:

```python
for n in llista1:
    print(n)
```

### Agregar elementos a una lista: `append`

```python
llista2 = []
llista2.append(valor)  # Añade 'valor' al final de la lista
```

### Valor absoluto (quitar el signo negativo)

```python
if n < 0:
    n = -n   # Cambia el negativo a positivo
```

### Eliminar repetidos con `set`

Un `set` (conjunto) no permite elementos repetidos:

```python
norepetits = set()
norepetits.add(n)   # Añade n; si ya existe, no hace nada
```

### Recorrer una lista al revés con slicing

```python
for n in llista1[-1::-1]:   # Empieza por el último, va hacia atrás
    print(n, end=' ')
```

- `[-1]` = último elemento
- `[::-1]` = paso -1 (al revés)
- `[::2]` = posiciones pares (0, 2, 4...)
- `[1::2]` = posiciones impares (1, 3, 5...)

### `print` en la misma línea

```python
print(n, end=' ')   # end=' ' evita el salto de línea, pone un espacio
print()             # Salto de línea manual
```

---

## 2. DICCIONARIOS (`diccionari.py`)

### ¿Qué es un diccionario?

Guarda pares **clave → valor**. Se crea con llaves `{}`.

```python
vocals = {}                # Diccionario vacío
vocals['a'] = 1            # Añade clave 'a' con valor 1
vocals['a'] += 1           # Incrementa el valor
```

### Comprobar si una clave existe

```python
if lletra in vocals:
    vocals[lletra] += 1    # La clave ya existe → sumamos 1
else:
    vocals[lletra] = 1     # La clave no existe → la creamos con 1
```

### Recorrer un rango con `range`

```python
for dau1 in range(1, 7):   # Genera: 1, 2, 3, 4, 5, 6 (el 7 no se incluye)
```

### Convertir texto a lista de enteros

```python
valors = input("Entra la llista: ")           # Ejemplo: "1 -4 3 1"
llista = list(map(int, valors.split(" ")))    # → [1, -4, 3, 1]
```

- `split(" ")` divide por espacios → lista de strings
- `map(int, ...)` convierte cada string a entero
- `list(...)` lo convierte en lista

### Histograma con `get`

```python
histograma.get(n, 0)   # Devuelve el valor de n, o 0 si n no existe
'*' * 3                # Repite el carácter '*' 3 veces → '***'
```

### Formatear números con ancho fijo

```python
print("{0:3d}".format(n))   # Imprime n con 3 caracteres de ancho (alineado)
```

---

## 3. FUNCIONES (`funcion.py`, `funcion2.py`)

### Definir una función

```python
def nombre_funcion(parametro1, parametro2):
    # Código
    return resultado
```

### Retornar múltiples valores

Python permite devolver varios valores a la vez:

```python
def longituds(paraules, lon):
    iguals, petites, grans = 0, 0, 0
    # ...lógica...
    return iguals, petites, grans

# Llamada:
iguals, petites, grans = longituds(paraules, 6)
```

### Longitud de una palabra: `len()`

```python
len("hola")   # → 4
```

### Función con litas como parámetro

La función recibe la lista y devuelve una nueva lista procesada:

```python
def senseNegatius(llista):
    llista2 = []
    for n in llista:
        if n < 0: n = -n
        llista2.append(n)
    return llista2

llista1 = [45, -6, 0, -32, 23, 9]
llista2 = senseNegatius(llista1)   # llista1 no se modifica
```

### Función que retorna lista sin repetidos: `set`

```python
def valorsRang(llista, valmin, valmax):
    escollits = set()
    for n in llista:
        if valmin <= n <= valmax:   # Comprobación encadenada
            escollits.add(n)
    return list(escollits)          # Convertir set a lista
```

### Conversión de tiempo (horas, minutos, segundos)

```python
def calcula_segons(hores, minuts, segons):
    return (hores * 60 + minuts) * 60 + segons

def temps(segons):
    minuts = segons // 60    # División entera
    segons = segons % 60     # Resto (los segundos que sobran)
    hores = minuts // 60
    minuts = minuts % 60
    return hores, minuts, segons
```

- `//` = división entera (sin decimales)
- `%` = módulo (el resto de la división)

### Comprobar vocal con `in`

```python
def esvocal(caracter):
    return caracter.lower() in "aeiouáéíóúàèìòùäëïöü"
```

- `.lower()` convierte a minúscula para comparar sin importar mayúsculas
- `in "cadena"` comprueba si el carácter está en esa cadena

---

## 4. FICHEROS DE TEXTO (`ficherosDEtext.py`)

### Abrir un fichero para leer

```python
fitxer = open("nombre.txt", "r")   # "r" = read (lectura)
for linia in fitxer:
    print(linia, end="")
fitxer.close()                      # Siempre hay que cerrarlo
```

### Modos de apertura de ficheros

| Modo   | Significado                            |
| ------ | -------------------------------------- |
| `"r"`  | Leer (el fichero debe existir)         |
| `"w"`  | Escribir (borra el contenido anterior) |
| `"a"`  | Append (escribe al final sin borrar)   |
| `"r+"` | Leer y escribir                        |

### Manejo de errores con `try/except`

```python
try:
    fitxer = open(nomfitxer, "r")
except FileNotFoundError:
    print("No existeix el fitxer", nomfitxer)
    return    # Sale de la función
```

Si el fichero no existe, Python lanza `FileNotFoundError` y entra en el `except`.

### Escribir en un fichero

```python
fitxer = open("salida.txt", "a")   # "a" = append, no borra lo que hay
fitxer.write("texto\n")             # \n = salto de línea
fitxer.close()
```

**Forma recomendada con `with`** (se cierra automáticamente):

```python
with open("salida.txt", "a", encoding='utf-8') as f:
    f.write("texto\n")
# No hace falta f.close()
```

### Moverse dentro de un fichero: `seek`

```python
fitxer.seek(0)              # Va al principio del fichero
fitxer.seek(0, os.SEEK_END) # Va al final del fichero (retorna el tamaño)
fitxer.seek(pos)            # Va a la posición 'pos' en bytes
```

---

## 5. CLASES Y OBJETOS (`dos.py` — clase `Conjurs`)

### ¿Qué es una clase?

Una clase es como una plantilla para crear objetos que agrupan datos y funciones.

```python
class Conjurs:
    def __init__(self, filename='conjurs.txt'):
        self.filename = filename     # Atributo del objeto

    def mostrar_hora_conjur(self) -> str:
        ara = datetime.now().isoformat()
        print(ara)
        return ara

    def registrar_conjur(self, nom_conjur: str, filename: str = None) -> str:
        if filename is None:
            filename = self.filename
        timestamp = datetime.now().isoformat()
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f"{timestamp} | {nom_conjur}\n")
        return filename
```

- `__init__` = constructor, se ejecuta al crear el objeto
- `self` = referencia al propio objeto
- `self.filename` = atributo que guarda el nombre del fichero

### Usar la clase

```python
conjurs = Conjurs()                        # Crear objeto
conjurs.mostrar_hora_conjur()              # Llamar método
conjurs.registrar_conjur("Bola de fuego") # Llamar método con parámetro
```

### `datetime` — Fecha y hora actual

```python
from datetime import datetime
datetime.now().isoformat()  # → "2026-04-07T10:30:00.123456"
```

---

## 6. MÓDULO `random` (`dos.py`)

```python
import random

random.random()          # Número decimal aleatorio entre 0.0 y 1.0
random.randint(1, 6)     # Entero aleatorio entre 1 y 6 (ambos incluidos)
```

### Probabilidad del 20%

```python
if random.random() < 0.20:
    # Esto ocurre el 20% de las veces
    dany *= 2
```

### Notación de dados: `re.match` (expresiones regulares)

```python
import re

match = re.match(r'^(\d+)d(\d+)$', "4d6")
n = int(match.group(1))   # → 4 (número de dados)
m = int(match.group(2))   # → 6 (caras del dado)
```

- `\d+` = uno o más dígitos
- `()` = grupo de captura
- `^...$` = inicio y fin de la cadena

---

## 7. SQLITE — BASE DE DATOS (`dos.py` — bestiari)

### Conectar a una base de datos SQLite

```python
import sqlite3

conn = sqlite3.connect("bestiari.db")  # Crea el fichero si no existe
```

### Crear una tabla

```python
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
conn.commit()   # Guardar los cambios
cursor.close()
```

- `INTEGER PRIMARY KEY AUTOINCREMENT` = clave primaria que se incrementa sola
- `conn.commit()` = guarda los cambios en el fichero

### Insertar datos (con parámetros seguros, evita SQL injection)

```python
cursor.execute(
    "INSERT INTO monstres (nom, cr, hp, tipus) VALUES (?, ?, ?, ?)",
    (nom, cr, hp, tipus)    # Tuple con los valores
)
conn.commit()
mid = cursor.lastrowid   # ID del registro insertado
```

> **IMPORTANTE**: Usar siempre `?` como placeholder, NUNCA concatenar strings para evitar SQL injection.

### Consultar datos

```python
cursor.execute("SELECT * FROM monstres")
result = cursor.fetchall()   # Lista de tuples con todos los registros

# Con filtro (búsqueda parcial con LIKE):
cursor.execute("SELECT * FROM monstres WHERE nom LIKE ?", (f'%{term}%',))
```

- `%texto%` = contiene "texto" en cualquier posición

### Eliminar datos

```python
cursor.execute("DELETE FROM monstres WHERE id=?", (mid,))
conn.commit()
affected = cursor.rowcount   # Número de filas afectadas
```

### Patrón completo de función con SQLite

```python
def add_monstre(dbpath, nom, cr, hp, tipus):
    conn = sqlite3.connect(dbpath)
    inicialitzar_bestiari(conn)    # Crea la tabla si no existe
    cursor = conn.cursor()
    cursor.execute("INSERT INTO monstres (nom, cr, hp, tipus) VALUES (?,?,?,?)",
                   (nom, cr, hp, tipus))
    conn.commit()
    mid = cursor.lastrowid
    cursor.close()
    conn.close()
    return mid
```

---

## 8. SCRIPTS CON ARGUMENTOS (`sciptFicheros.py`, `scriptsymsql.py`)

### Leer argumentos de línea de comandos con `getopt`

```python
import getopt, sys

opts, args = getopt.getopt(
    sys.argv[1:],          # Argumentos del script (sin el nombre del script)
    "f:p:h",               # Opciones cortas: -f, -p (con valor), -h (sin valor)
    ["fitxer=", "paraula=", "help"]   # Opciones largas: --fitxer, --paraula, --help
)
```

- `f:` = la opción `-f` requiere un valor después
- `h` = la opción `-h` no requiere valor

### Procesar las opciones

```python
for o, a in opts:
    if o in ("-h", "--help"):
        usage()
    elif o in ("-f", "--fitxer"):
        fitxer = a        # 'a' es el valor que sigue a la opción
    elif o in ("-p", "--paraula"):
        paraula = a
```

### `if __name__ == "__main__":`

```python
if __name__ == "__main__":
    main()
```

Este bloque solo se ejecuta cuando el script se lanza directamente, no cuando se importa como módulo. Es buena práctica colocar aquí el código principal.

---

## 9. COPIA DE FICHEROS Y DIRECTORIOS (`modulo.py`)

```python
import os
import shutil

os.path.isdir(path)                          # True si es un directorio
shutil.copytree(origen, desti, dirs_exist_ok=True)  # Copia un directorio completo
shutil.copy2(origen, desti)                  # Copia un fichero
os.makedirs(os.path.dirname(desti), exist_ok=True)  # Crea directorios intermedios
os.path.join("/home/", "usuario/")           # Une rutas: "/home/usuario/"
os.listdir(path)                             # Lista el contenido de un directorio
```

---

## 10. GENERACIÓN DE LABERINTOS (`dos.py`)

```python
def generar_laberint_aleatori(filas=6, columnes=6, percentatge_parets=25, fitxer='laberint_auto.txt'):
    laberint = []
    for i in range(filas):
        fila = []
        for j in range(columnes):
            if random.randint(1, 100) <= percentatge_parets:
                fila.append('X')    # Pared
            else:
                fila.append('.')    # Espacio libre
        laberint.append(fila)
    laberint[0][0] = 'S'                          # Inicio
    laberint[filas-1][columnes-1] = 'E'            # Salida
    with open(fitxer, 'w', encoding='utf-8') as f:
        for fila in laberint:
            f.write(''.join(fila) + '\n')          # Unir chars y escribir línea
    return fitxer
```

- `''.join(fila)` = une una lista de caracteres en un string: `['S','.','X']` → `"S.X"`

---

## 11. CODIFICACIÓN ROT13 (`dos.py`)

ROT13 es un cifrado simple que rota cada letra 13 posiciones. Aplicarlo dos veces decodifica el texto.

```python
import codecs

linea_decodificada = codecs.decode(linea, 'rot_13')
```

---

## 12. CONCEPTOS GENERALES

### Condicionales

```python
if condicion:
    ...
elif otra_condicion:
    ...
else:
    ...
```

### Bucle `while`

```python
i = 0
while i < 10:
    i += 1
```

### Conversión de tipos

```python
int("42")       # String → entero
str(42)         # Entero → string
float("3.14")   # String → decimal
```

### `max()` y `min()`

```python
max(0, pdv - dany)   # Devuelve el mayor: evita valores negativos
min(llista)           # Valor mínimo de una lista
max(llista)           # Valor máximo de una lista
```

### F-strings (interpolación de variables)

```python
nombre = "Goblin"
print(f"El monstre és {nombre}")    # → "El monstre és Goblin"
print(f"Resultat: {valor:.2f}")     # Decimal con 2 decimales
```

### Anotaciones de tipo (type hints)

```python
def calcular_nivell(xp: int) -> int:
```

- `xp: int` = el parámetro `xp` es un entero
- `-> int` = la función devuelve un entero
- Son opcionales, pero ayudan a documentar el código.

---

## Resumen visual de estructuras

| Concepto      | Sintaxis                               |
| ------------- | -------------------------------------- |
| Lista         | `llista = [1, 2, 3]`                   |
| Diccionario   | `d = {"clave": valor}`                 |
| Set           | `s = {1, 2, 3}` o `set()`              |
| Función       | `def f(param): return resultado`       |
| Clase         | `class Nom: def __init__(self): ...`   |
| Abrir fichero | `with open("f.txt", "r") as f:`        |
| SQLite        | `conn = sqlite3.connect("db.sqlite3")` |
| Random        | `random.randint(1, 6)`                 |
| Regex         | `re.match(r'\d+', texto)`              |
