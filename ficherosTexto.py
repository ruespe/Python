
#fichero = open('nombreFichero',w)

#r lee el fichero
#w crea fichero o lo machaca en caso de existir
#a añadir al final del documento
#x falla al crear si ya existe

#fitxerwrite("a\n")
#writeline("bbbbb") escribe en la linea de abajo

"""
"""



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

def concatena(archivo1, archivo2):
    try:
        with open(archivo1, 'w') as archivoCrear:
            contenido = archivoCrear.write("Me convertiré en")
    except IOError:
        print("No se puede leer el archivo")

    try:
        with open(archivo2, 'a') as archivoAñadir:
            archivoAñadir.write("el rey de los Piteros")
    except FileNotFoundError:
        print("No existe bro")
    except IOError:
        print("No funciona bro")
    
    with open(archivo1, 'r') as archivoLeer:
            lectura = archivoLeer.read()
            print(lectura)

nombreArchivo1 = input("Nombre archivo1: ")
nombreArchivo2 = input("Nombre archivo2: ")

concatena(nombreArchivo1,nombreArchivo2)