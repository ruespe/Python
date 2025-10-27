# # sudo apt install sqlitebrowser

# import sqlite3


# # Crear o connectar-se a la base de dades
# conn = sqlite3.connect('exemple.db')

# # Crear un cursor per executar comandes SQL
# cursor = conn.cursor()

# # Crear una taula
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS usuaris (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nom TEXT,
#     edat INTEGER
# )
# ''')

# # Inserir dades
# cursor.execute('''
# INSERT INTO usuaris (nom, edat)
# VALUES (?, ?)
# ''', ("Anna", 25))

# # Guardar els canvis
# conn.commit()

# # Llegir dades
# cursor.execute('SELECT * FROM usuaris')
# usuaris = cursor.fetchall()
# for usuari in usuaris:
#     print(usuari)

# # Tancar la connexió
# conn.close()
"""
1- Crea un script que donat un atleta ens mostri les seves marques:
Ha d'admetre les següents opcions:
-a o --atleta amb el nom de l'atleta
--help o -h mostra un missatge informatiu del funcionament.
Ha de detectar correctament les opcions i paràmetres i mostrar-ne un missatge en cas de dades errònies. Si hi ha diverses opcions, les ha de gestionar totes.

"""
import sqlite3

conexion = sqlite3.connect('exemple.db')

cursor = conexion.cursor()


# Ejemplo: listar tablas existentes
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cursor.fetchall()
print("Tablas:", tablas)

# Ejemplo: consultar una tabla
cursor.execute("SELECT * FROM usuarios;")
filas = cursor.fetchall()
for fila in filas:
    print(fila)
