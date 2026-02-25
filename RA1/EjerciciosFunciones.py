"""
1- Crea una funció longituds que a partir d’una llista de paraules i una longitud, retorni tres valors: quantes paraules tenen la mateixa longitud,  quantes una longitud inferior i quantes una longitud superior.
iguals, petites, grans = longituds(paraules, lon)

"""

"""
def CalcularLongitud():
    lista = [
        "sol",
        "lago",
        "nube",
        "cactus",
        "ratón",
        "planeta",
        "código",
        "montaña",
        "universo",
        "bicicleta",
        "electricidad",
        "responsable",
    ]

    longitud = int(input("Introduce la longitud de la cadena: "))
    longitud = int(longitud)

    contMismaLongitud = 0
    contSuperiorLongitud = 0
    contInferiorLongitud = 0

    for palabra in lista:
        largo = len(palabra)
        if largo == longitud:
            contMismaLongitud += 1
        elif largo < longitud:
            contInferiorLongitud += 1
        else:
            contSuperiorLongitud += 1

    print("Palabras con la misma longitud: ", contMismaLongitud)
    print("Palabras con una longitud superior: ", contSuperiorLongitud)
    print("Palabras con longitud inferior: ", contInferiorLongitud)


CalcularLongitud()
"""
"""
2- Crea una funció puntsDaus que a partir d’una llista de valors de tirades de daus, calculi una puntuació de la següent manera:
Si hi ha algun dau que sigui menor que 3, aleshores la puntuació final és zero punts.
En altre cas la puntuació es calcula de la següent manera:
Se sumen tots els daus.
2 punts més si la suma és més gran de 12.
1 punt més per cada dau que marqui un 6.

puntuacio=puntsDaus(punts)

"""
"""


def puntosDados():
    puntos = 0
    puntos0 = False
    puntosExtra = 0
    listaTiradas = [13, 3, 10, 11, 6, 7, 9]

    for tiradas in listaTiradas:
        puntos += tiradas
        if tiradas < 3:
            puntos0 = True
        elif tiradas == 6:
            puntosExtra += 1

    if puntos > 12:
        puntos += 2
    if puntos0 == True:
        puntos = 0        

    return puntos

print(puntosDados())

"""

"""
3- Crea una funció valorsRang que a partir d’una llista de valors, un valor mínim i un valor màxim, retorni una nova llista amb tots els valors de la primera què es troben entre els dos valors entrats per teclat (inclosos), sense valors repetits.

escollits=valorsRang(llista, valmin, valmax)

"""
"""
def valorsRang(listaRango,valorMinimo,valorMaximo):
    
    listaNueva=[]

    if valorMinimo > valorMaximo :
        valorMinimo, valorMaximo = valorMaximo, valorMinimo

    for numero in listaRango:
        if(numero>valorMinimo and numero<valorMaximo and numero not in listaNueva):
            listaNueva.append(numero)            
    
    return listaNueva

listaRango = [42, 117, 6, 89, 133, 25, 74, 150, 6, 58, 101]
valorMinimo = int(input("Introduce un numero: "))
valorMaximo = int(input("Introduce un numero: "))

resultado = valorsRang(listaRango,valorMinimo, valorMaximo)

print(resultado)

"""
"""
4- Crea una funció calcula_segons que calculi la quantitat de segons en un temps donat en hores, minuts i segons.
segons = calcula_segons( hores, minuts, segons)

"""
# def calcula_segundos(horas, minutos, segundos):
#     horasEnsegundos= horas*60*60
#     minutosEnSegundos= minutos*60

#     segundosTotales = horasEnsegundos + minutosEnSegundos + segundos

#     return segundosTotales


# horas = int(input("Introduce las horas: "))
# minutos = int(input("Introduce las minutos: "))
# segundos = int(input("Introduce las segundos: "))

# calcula_segundos(horas, minutos, segundos)

# resultado = calcula_segundos(horas,minutos,segundos)

# print(resultado)

"""
5- Crea una funció temps que calculi la quantitat d’hores, minuts i segons d’un temps donat en segons.
hores, minuts, segons = temps(segons)

"""
# def tiempo(horas, minutos, segundos):
#     horasEnSegundos = horas*3600
#     minutosEnSegundos = minutos*60

#     segundosTotales = horasEnSegundos + minutosEnSegundos + segundos

#     return segundosTotales


# horas =  int(input("Introduce las horas: "))
# minutos = int(input("Introduce los minutos: "))
# segundos = int(input("Introduce los segundos: "))

# resultado = tiempo(horas, minutos, segundos)

# print(resultado)

"""
6- Escriu una funció esvocal que a partir un caràcter torni True si el caràcter és una vocal o False en cas contrari.
if esvocal(caracter):
    print(caracter, “és una vocal”)
else:
    print(caracter, “NO és una vocal”)

"""
# EXAMEN PYTHON HABRÁ QUE HACER UN MENÚ

# def esvocal(caracter):

#     listaVocales=["a","e","i","o","u"]
#     vocalLocalizada = False

#     for letra in listaVocales:
#         if letra == caracter:
#             vocalLocalizada = True

#     if vocalLocalizada == True:
#         print(f"{caracter} es una vocal.")
#     else:
#         print(f"{caracter} no es una vocal.")


# caracter = str(input("Introduce un solo caracter: "))

# while len(caracter) != 1:
#     print("Sólo se permite un carácter")
#     caracter = str(input("Introduce un solo carácter: "))

# esvocal(caracter)


"""
7-Crea una funció canviaMorse programa que sigui capaç de transformar text natural a codi morse i viceversa.
Heu de detectar automàticament de quin tipus es tracta i realitzar la conversió.
En morse se suporta ratlla "-", punt ".", s'ha de fer servir un espai " " per separar lletres i dos espais "  " entre paraules.
L'alfabet morse suportat serà el mostrat a https://es.wikipedia.org/wiki/Código_morse.
"""

# def canviaMorse(fraseMorse):

#     listaLetrasYnumeros = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#     morseDiccionario = {
#     "a": ".-",    "b": "-...",  "c": "-.-.",  "d": "-..",   "e": ".",     "f": "..-.",
#     "g": "--.",   "h": "....",  "i": "..",    "j": ".---",  "k": "-.-",   "l": ".-..",
#     "m": "--",    "n": "-.",    "o": "---",   "p": ".--.",  "q": "--.-",  "r": ".-.",
#     "s": "...",   "t": "-",     "u": "..-",   "v": "...-",  "w": ".--",   "x": "-..-",
#     "y": "-.--",  "z": "--..",
#     "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
#     "6": "-....", "7": "--...", "8": "---..", "9": "----."
#         }

#     tipo = ""
#     fraseTraducidaAMorse = ""
#     fraseAminusculas = fraseMorse.lower()
#     fraseTraducidaANormal = ""

#     for texto in fraseAminusculas:
#         if texto not in listaLetrasYnumeros:
#             tipo = "morse"
#         else:
#             tipo = "normal"

#     Traduccón Normal a Morse
#     if tipo == "normal":
#         for caracter in fraseAminusculas:
#             if caracter in morseDiccionario:
#                 fraseTraducidaAMorse += morseDiccionario[caracter]
#                 fraseTraducidaAMorse += " "
#             elif caracter == " ":
#                 fraseTraducidaAMorse += "  "

#     Traducción Morse a Normal
#     if tipo == "morse":
#         for clave, valor in morseDiccionario.items():
#             if valor in fraseMorse:
#                 fraseTraducidaANormal += clave


#    print(fraseTraducidaAMorse)
#     print(fraseTraducidaANormal)


# fraseMorse = input("Introduce la frase que quieras que sea traducida a Morse: ")

# canviaMorse(fraseMorse)

"""
8-Crea una funció diferencies que a partir de dues cadenes de text gairebé iguals, retorneu les diferències.
La funció ha de trobar les diferències a la segona cadena i retornar-les en format llista.
Les dues cadenes de text han de ser iguals en longitud.
Exemples:
Em dic mouredev / Em dic meuredov -> ["e", "o"]
Em dic.Brais Moure / Em dic brais moure -> [" ", "b", "m"]
"""

"""
9-Crea una funció comptaLA que a partir d'una frase retorni la quantitat de LA trobades.
No es diferencia entre majúscules i minúscules. No s'ha de fer servir el mètode count.
Exemple:
Ell s'ha passat la tarda cantant La, LA, lA, ...
Retorna 4

Exemple:
Ell s'ha passat la tarda cantant LaLAlA, ...
Retorna 4
"""
def comptaLA(frase):
    fraseMinuscula = frase.lower()

    for i in range(len(fraseMinuscula)):
        i



frase = input("Introduce una frase para contar los la que contiene")

comptaLA(frase)



"""
10-Crea una funció comptaLES que a partir d'una frase retorni la quantitat de LES trobades.
No es diferencia entre majúscules i minúscules. No s'ha de fer servir el mètode count.
Exemple:
Ell es passa totes les tardes cantant LaLESlesla...
Retorna 3

"""


# def comptaLES(frase):
#     fraseLower = frase.lower()
#     cont=0
#     palabra1 = ""
#     palabra2 = ""
#     palabra3 = ""


#     for i in range(len(fraseLower) - 2):  
#         palabra1 = fraseLower[i]
#         if i + 1 <len(frase):
#             palabra2 = fraseLower[i+1]
#         if i + 2 <len(frase):
#             palabra3 = fraseLower[i+2]
#         nueva = "".join([palabra1, palabra2, palabra3])
        
#         if nueva == "les":
#             cont+=1
        
#     print(f"Numero de veces: {cont}")


# frase = input("Introduce una frase para contar los les: ")

# comptaLES(frase)
