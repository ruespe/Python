'''
1-Calcula amb un diccionari la freqüència d'aparició de vocals en una frase (suposem que no fem servir accents).
Exemple:
Entra frase: les vocals son aeiou
Resultat:
{'e':2, 'o':3, 'a':2, 'i':1, 'u':1}
'''

vocals={}

frase=input("Entra una frase: ")

for lletra in frase:
    if lletra in vocals:
        # Si la lletra és dins del diccionari es tracta d'una vocal
        vocals[lletra]+=1
    else:
        # La lletra no és al diccionari, s'afegeix si és una vocal
        if lletra in "aeiou":
            vocals[lletra]=1

print(vocals)

'''
2-Calcula amb un diccionari la freqüència d'aparició de números en una llista i les posicions a on apareixen.
Exemple:  (entra cada valor per separat) o fer servir llista=list(map(int, frase.split(" ")))
Entra llista: 1 -4 3 1 1 5 7 7
Resultat:
{1:[0,3,4], -4:[1], 3:[2], 5:[5], 7:[6,7]}
'''

posicions={}

valors=input("Entra la llista: ")
llista=list(map(int, valors.split(" ")))

p=0  # Serveix per saber la posició de cada valor
for num in llista:
    if num in posicions:
        # num és dins del diccionari, guardem la posició a la seva llista
        posicions[num].append(p)
    else:
        # num no és al diccionari, afegim num a la posició p
        posicions[num]=[p]  # el valor és una llista
    p=p+1 # avancem a la següent posició

print(posicions)

'''
3-De totes les possibles tirades de dos daus, agrupa-les pel mateix valor.
Resultat:
{2: [[1, 1]], 3: [[1, 2], [2, 1]], 4: [[1, 3], [2, 2], [3, 1]], ... , 12: [[6, 6]]}
'''

tirades={}

for dau1 in range(1,7):
    for dau2 in range(1,7):
        tirada=dau1+dau2
        if tirada in tirades:
            tirades[tirada].append([dau1,dau2])
        else:
            tirades[tirada]=[[dau1,dau2]]

print(tirades)

'''
4-D'una llista de valors, crea un histograma gràfic.
Exemple:  (entra cada valor per separat) o fer servir llista=list(map(int, frase.split(" ")))
Entra llista: 1 -4 3 1 1 5 2 2 7 7 -2 3 3 3
Resultat:
-4 *
-3
-2 *
-1
 0
 1 ***
 2 **
 3 ****
 4
 5 *
 6
 7 **
'''

valors=input("Entra llista: ")
llista=list(map(int, valors.split(" ")))
llista.sort()
histograma={}
m=min(llista)
M=max(llista)
for n in llista:
    if n in histograma:
        histograma[n]+=1
    else:
        histograma[n]=1

for n in range(m, M+1):
    print("{0:3d}".format(n), '*' * histograma.get(n, 0))

