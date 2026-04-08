'''
1- Crea una funció longituds que a partir d’una llista
de paraules i una longitud, retorni tres valors:
quantes paraules tenen la mateixa longitud,
quantes una longitud inferior i
quantes una longitud superior.
iguals, petites, grans = longituds(paraules, lon)
'''

def longituds(paraules, lon):
    iguals=0
    grans=0
    petites=0
    for p in paraules:
        if len(p)==lon:
            iguals+=1
        else:
            if len(p)>lon:
                grans+=1
            else:
                petites+=1
    return iguals, petites, grans


#Exemples d'utilització
paraules=["proves", "exercicis", "prog"]

iguals6, petites6, grans6 = longituds(paraules, 6)
print(iguals6, petites6, grans6)

iguals7, petites7, grans7 = longituds(paraules, 7)
print(iguals7, petites7, grans7)

print(longituds(paraules, 10))

'''
2- Crea una funció puntsDaus que a partir d’una llista
de valors de tirades de daus, calculi una puntuació
de la següent manera:
Si hi ha algun dau que sigui menor
que 3, aleshores la puntuació final és zero punts.
En altre cas la puntuació es calcula de la següent manera:
Se sumen tots els daus.
2 punts més si la suma és més gran de 12.
1 punt més per cada dau que marqui un 6.

puntuacio=puntsDaus(punts)
'''

def puntsDaus(punts):
    puntuacio=0
    if 1 not in punts and 2 not in punts:
        sis=0
        for p in punts:
            puntuacio+=p
            if p==6: sis+=1
        if puntuacio>12: puntuacio+=2
        puntuacio+=sis
    return puntuacio


#Exemples d'utilització
daus=[5, 6, 2, 5, 6]
p=puntsDaus(daus)
print(p)

p=puntsDaus([5, 6, 4, 5, 6])
print(p)

p=puntsDaus([5, 5, 5, 6])
print(p)

print(puntsDaus([5, 6, 4, 5, 6]))

'''
3- Crea una funció valorsRang que a partir d’una llista de valors,
un valor mínim i un valor màxim,
retorni una nova llista amb tots els valors de la primera
què es troben entre els dos valors entrats per teclat (inclosos),
sense valors repetits.

escollits=valorsRang(llista, valmin, valmax)
'''

def valorsRang(llista, valmin, valmax):
    escollits=set()
    for n in llista:
        if n>=valmin and n<=valmax:
            escollits.add(n)
    return list(escollits)

#Exemples d'utilització
llista=[4, 6, 2, -3, 0, 3, 3, 7]
nova=valorsRang(llista, 2, 7)
print(nova)

'''
4- Crea una funció calcula_segons que calculi
la quantitat de segons en un temps donat en hores, minuts i segons.
segons = calcula_segons( hores, minuts, segons)
'''

def calcula_segons( hores, minuts, segons):
    return (hores*60+minuts)*60+segons

#Exemples d'utilització
# 00:10:05  -->  605 seg
print(calcula_segons( 0, 10, 5))

'''
5- Crea una funció temps que calculi la
quantitat d’hores, minuts i segons d’un temps donat en segons.
hores, minuts, segons = temps(segons)
'''

def temps(segons):
    negatiu=False
    if segons<0:
        segons=-segons
        negatiu=True
    minuts=segons//60
    segons=segons%60
    hores=minuts//60
    minuts=minuts%60
    if negatiu: return -hores, -minuts, -segons
    return hores, minuts, segons

#Exemples d'utilització
#605 seg   -->  00:10:05
hores, minuts, segons = temps(605)
print(hores, minuts, segons)

#3661 seg  -->  01:01:01
print (temps(3661))

h,m,s =temps(1000)
print (calcula_segons(h,m,s))

'''
6- Escriu una funció esvocal que a partir un caràcter
torni True si el caràcter és una vocal o False en cas contrari.
if esvocal(caracter):
    print(caracter, “és una vocal”)
else:
    print(caracter, “NO és una vocal”)
'''

def esvocal(caracter):
    return caracter.lower() in "aeiouáéíóúàèìòùäëïöü"

#Exemples d'utilització
print(esvocal('A'))
print(esvocal('É'))
print(esvocal('Ë'))
print(esvocal('Ò'))
print(esvocal('i'))
print(esvocal('à'))
print(esvocal('J'))
print(esvocal('ñ'))

'''
7-Crea una funció canviaMorse programa que sigui capaç de
transformar text natural a codi morse i viceversa.
Heu de detectar automàticament de quin tipus es tracta i
realitzar la conversió.
En morse se suporta ratlla "-", punt ".", s'ha de fer servir
un espai " " per separar lletres i dos espais "  " entre paraules.
L'alfabet morse suportat serà el mostrat
a https://es.wikipedia.org/wiki/Código_morse.
'''

def esMorse(missatge):
    for c in missatge:
        if c not in [' ','-','.']: return False
    return True

def obtenirMorse(missatge, codi):
    paraules=missatge.upper().split(' ')
    resultat=''
    for p in paraules:
        for c in p:
            resultat += codi.get(c,'')
            resultat += ' '
        resultat += ' '
    return resultat.strip()

def obtenirFrase(missatge, codi):
    paraules=missatge.split('  ')
    resultat=''
    for p in paraules:
        codis=p.split(' ')
        for c in codis:
            resultat += codi.get(c,'')
        resultat += ' '
    return resultat.strip()

def canviaMorse(missatge):
    lletra2morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'CH': '----', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.', 'Ñ': '--.--', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
    'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '"': '.-..-.', '/': '-..-.'
    }
    morse2lletra=dict(zip(lletra2morse.values(),lletra2morse.keys()))
    if esMorse(missatge):
        return obtenirFrase(missatge, morse2lletra)
    else:
        return obtenirMorse(missatge, lletra2morse)

print(canviaMorse("SOS"))
print(canviaMorse("Programacio de scripts"))
print(canviaMorse(canviaMorse("SOS")))
print(canviaMorse(canviaMorse("Programacio de scripts")))


'''
8-Crea una funció diferencies que a partir de dues cadenes
de text gairebé iguals, retorneu les diferències.
La funció ha de trobar les diferències a la segona cadena i
retornar-les en format llista.
Les dues cadenes de text han de ser iguals en longitud.
Exemples:
Em dic mouredev / Em dic meuredov -> ["e", "o"]
Em dic.Brais Moure / Em dic brais moure -> [" ", "b", "m"]
'''

def diferencies(frase1, frase2):
    if (len(frase1)!=len(frase2)): return None
    llista=[]
    for i in range(len(frase1)):
        if frase1[i]!=frase2[i]:
            llista.append(frase2[i])
    return llista

print(diferencies("Em dic mouredev", "Em dic meuredov"))
print(diferencies("Em dic.Brais Moure", "Em dic brais moure"))

'''
9-Crea una funció comptaLA que a partir d'una frase
retorni la quantitat de LA trobades.
No es diferencia entre majúscules i minúscules.
Exemple:
Ell s'ha passat la tarda cantant La, LA, lA, ...
Retorna 4

Exemple:
Ell s'ha passat la tarda cantant LaLAlA, ...
Retorna 4
'''

def comptaLA(frase):
    compt=0
    for i in range(len(frase)-1):
        if frase[i:i+2].lower()=="la":
            compt += 1
    return compt

print(comptaLA("Ell s'ha passat la tarda cantant La, LA, lA, ..."))
print(comptaLA("Ell s'ha passat la tarda cantant LaLAlA, ..."))

'''
10-Crea una funció comptaLES que a partir d'una frase
retorni la quantitat de LES trobades.
No es diferencia entre majúscules i minúscules.
Exemple:
Ell es passa totes les tardes cantant LaLESlesla...
Retorna 3
'''

def comptaLES(frase):
    compt=0
    for i in range(len(frase)-2):
        if frase[i:i+3].lower()=="les":
            compt += 1
    return compt

print(comptaLES("Ell es passa totes les tardes cantant LaLESlesla..."))
