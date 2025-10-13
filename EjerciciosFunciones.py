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
def calcula_segundos(horas, minutos, segundos):
    horasEnsegundos= horas*60*60
    minutosEnSegundos= minutos*60

    segundosTotales = horasEnsegundos + minutosEnSegundos + segundos

    return segundosTotales

    

horas = int(input("Introduce las horas: "))
minutos = int(input("Introduce las minutos: "))
segundos = int(input("Introduce las segundos: "))

calcula_segundos(horas, minutos, segundos)

resultado = calcula_segundos(horas,minutos,segundos)

print(resultado)

"""
5- Crea una funció temps que calculi la quantitat d’hores, minuts i segons d’un temps donat en segons.
hores, minuts, segons = temps(segons)

"""
def tiempo(horas, minutos, segundos):
    horasEnSegundos = horas/60/60
    minutosEnSegundos = minutos/60

    segundosTotales = horasEnSegundos + minutosEnSegundos + segundos

    return segundosTotales


horas = 
minutos =

resultado = tiempo(horas, minutos, segundos)


"""
6- Escriu una funció esvocal que a partir un caràcter torni True si el caràcter és una vocal o False en cas contrari.
if esvocal(caracter):
    print(caracter, “és una vocal”)
else:
    print(caracter, “NO és una vocal”)

"""
