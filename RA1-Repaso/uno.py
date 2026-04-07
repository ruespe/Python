'''
1-(2,5p) Crea una list amb paraules diverses, directament al codi.
Demana per teclat una longitud de paraula (quantitat de caràcters).
Fent servir un bucle, compta les paraules de la llista que tenen la mateixa longitud,
les que tenen una longitud inferior i les que tenen una longitud superior.
Mostra el resultat.
Nota: per obtenir la longitud d’una paraula es pot fer servir len(paraula)
Exemple:
list → "Fent", "servir", "un", "bucle", "compta", "les", "paraules", "de", "la", "llista", "que", "tenen", "la", "mateixa", "longitud"
longitud 6
longitud igual a 6:    3
longitud inferior a 6: 9
longitud superior a 6: 3
'''

paraules=["Fent", "servir", "un", "bucle", "compta", "les", "paraules", "de", "la", "llista", "que", "tenen", "la", "mateixa", "longitud"]
lon=int(input("Entra longitud: "))
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

print("longitud igual a", lon, "   : ",iguals)
print("longitud inferior a", lon, ": ",petites)
print("longitud superior a", lon, ": ",grans)


'''
2-(2,5p) Realitza un joc de daus en els qual es guanyen uns punts en funció del resultat de diversos daus tirats.
Si hi ha algun dau que sigui menor que 3, aleshores la puntuació final és zero punts.
En altre cas la puntuació es calcula de la següent manera:
Es sumen tots els daus.
2 punts més si la suma és més gran de 12.
1 punt més per cada dau que marqui un 6.
Llegeix del teclat la quantitat de daus i a continuació el valor de tots els daus.
Calcula i mostra la puntuació corresponent.
Utilitza bucles.
Exemples:
3 Daus 3,6,3
Puntuació 13
3 Daus 4,3,6
Puntuació 16
5 Daus 1,1,3,6,1
Puntuació 0
4 Daus 6,6,4,3
Puntuació 23
'''

daus=int(input("Quants daus? "))
punts=[]
for d in range(0,daus):
    puntsDau=int(input("Entra els punts d'un dau: "))
    punts.append(puntsDau)

puntuacio=0
if 1 not in punts and 2 not in punts:
    sis=0
    for p in punts:
        puntuacio+=p
        if p==6: sis+=1
    if puntuacio>12: puntuacio+=2
    puntuacio+=sis

print("Puntuació", puntuacio)

'''
3-(2,5p) Crea una list amb valors enters, directament al codi.
Demana per teclat dos valors numèrics.
Crea una nova llista amb tots els valors de la primera què es troben entre els
dos valors entrats per teclat (inclosos), sense valors repetits.
Mostra la nova llista. Utilitza bucles.
Exemple:
list → 5, 8, -32, 0, -5, 88, 20, -5, 7, 8, 9, -100, 100
Límits -10 a 20
Resultat:
5, 8, 0, -5, 20, 7, 9
'''

llista=[5, 8, -32, 0, -5, 88, 20, -5, 7, 8, 9, -100, 100]
val1=int(input("Entra valor 1: "))
val2=int(input("Entra valor 2: "))
escollits=set()
for n in llista:
    if n>=val1 and n<=val2:
        escollits.add(n)

novallista=list(escollits)
print(novallista)

'''
4-(2,5p) Fent servir el següent diccionari:
edats={'Jim': 16, 'Bob': 26, 'Carol': 83, 'Dave': 21, 'Flow': 38, 'Katie': 47, 'Nate': 89}.
Crea un bucle que demani per teclat diversos valors clau (key), fins que el valor sigui 'FI'.
Per cada clau, si existeix al diccionari, mostra un missatge amb el valor que li correspon.
Si no existeix, demana per teclat un valor i afegeix la clau:valor al diccionari.
Mostra el diccionari final.
Exemple:
Entra clau: Bob
Bob té 26
Entra clau: Clint
Nou valor: 99
Entra clau: Nate
Nate té 89
Entra clau: Katie
Katie té 47
Entra clau: Tom
Nou valor: 65
Entra clau: FI
Resultat:
{'Jim': 16, 'Bob': 26, 'Carol': 83, 'Dave': 21, 'Flow': 38, 'Katie': 47, 'Nate': 89, 'Clint': 99, 'Tom': 65}
'''

edats={'Jim': 16, 'Bob': 26, 'Carol': 83, 'Dave': 21, 'Flow': 38, 'Katie': 47, 'Nate': 89}

clau=''
while clau!='FI':
    clau=input("Entra clau: ")
    if clau in edats:
        print(clau, "té", edats[clau])
    else:
        if clau!='FI':
            valor=int(input("Nou valor: "))
            edats[clau]=valor

print(edats)
