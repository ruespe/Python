# fichero = open('nombreFichero',w)

# r lee el fichero
# w crea fichero o lo machaca en caso de existir
# a añadir al final del documento
# x falla al crear si ya existe

# fitxerwrite("a\n")
# writeline("bbbbb") escribe en la linea de abajo

""" """


"""
1- Crea un mètode mostra, que a partir d'un nom de fitxer, mostri el seu contingut per consola. Si el fitxer no és vàlid, ha de mostrar un missatge informatiu.

"""
# def mostra(nombreArchivo):
#     try:
#         Comprueba por defecto la carpeta desde donde trabaja
#         with open(nombreArchivo, 'r') as archivo:
#             contenido = archivo.read()
#         print(contenido)
#     except FileNotFoundError:
#         print(f"Error: El archivo '{nombreArchivo}' no existe.")
#     except IOError:
#         print(F"Error: No se puede leer el archivo pe '{nombreArchivo}'.")


# archivo = input("Introduce el nombre del fichero: ")
# mostra(archivo)

"""
2- Crea un mètode concatena, que a partir de dos fitxers, afegeixi el contingut del segon fitxer al primer fitxer. Si el segon fitxer no és vàlid, ha de mostrar un missatge informatiu.

"""


# def concatena(archivo1, archivo2):
#     try:
#         with open(archivo2, "r") as archivoCrear:
#             contenido = archivoCrear.read()
#     except IOError:
#         print("No se puede leer el archivo")
#     except FileNotFoundError:
#         print("No se ha encontrado el archivo bro")

#     try:
#         with open(archivo1, "a") as archivoAñadir:
#             archivoAñadir.write(" ")
#             archivoAñadir.write(contenido)
#     except FileNotFoundError:
#         print("No existe bro")
#     except IOError:
#         print("No funciona bro")

#     with open(archivo1, "r") as archivoLeer:
#         lectura = archivoLeer.read()
#         print(lectura)


# nombreArchivo1 = input("Nombre archivo1: ")
# nombreArchivo2 = input("Nombre archivo2: ")

# concatena(nombreArchivo1, nombreArchivo2)

"""
3- Crea un mètode afegir, que escrigui el contingut d'una llista en un fitxer. S'ha de fer append, el contingut original del fitxer no s'ha d'esborrar.

"""
def añadir(nombreArchivo):
    entrada = input("Introduce los valores que quieras que posea la lista: ")
    lista = entrada.split()
    string = " ".join(lista)
    #print(lista)
    try:
        with open(nombreArchivo, 'a') as archivo:
            archivo.write(string + "\n")
    except FileNotFoundError:
        print("Archivo no encontrado")
    except IOError:
        print("Error desconocido")

    try:
        with open(nombreArchivo, 'r') as archivo:
            mostrar = archivo.read()
            print(mostrar)
    except FileNotFoundError:
        print("No se encuentra el archivo")
    except IOError:
        print("Error desconocido")


nombreArchivo = input("Nombre archivo: ")
añadir(nombreArchivo)

"""
4- Crea un mètode escriuPos, que escrigui una frase en un fitxer, a una posició concreta. Si la posició és incorrecta, ha de mostrar un missatge informatiu.

"""
def escribirPosicion(nombreArchivo):

    try:
        with open(nombreArchivo, 'a'):
            nombreArchivo.read()