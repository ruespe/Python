'''
1-Crea una llista de valors numèrics enters, no fa falta
llegir-la del teclat.
Mitjançant un bucle crea una segona llista, igual a l’anterior,
però modificant tots els valors negatius per el seu valor en
positiu. Mostra les dues llistes per consola.
Exemple:
Llista 1: [45, -6, 0, -32, 23, 9]
Resultat:
Llista 1: [45, -6, 0, -32, 23, 9]
Llista 2: [45, 6, 0, 32, 23, 9]
'''

llista1=[45, -6, 0, -32, 23, 9]

llista2=[]
for n in llista1:
    if n<0: n=-n
    llista2.append(n)

print("Llista 1:", llista1)
print("Llista 2:", llista2)


'''
2-Crea una llista de valors numèrics enters, no fa falta
llegir-la del teclat.
Mostra per consola els valors de la llista sense repetir cap.
Fes servir un bucle i un tipus set.
Exemple:
Llista: [45, -6, 0, -32, -6, 0, 45, 45, 23, 9]
Resultat:
Llista: [45, -6, 0, -32, -6, 0, 45, 45, 23, 9]
Sense repetits: -32 -6 0 45 23 9
'''

llista1=[45, -6, 0, -32, -6, 0, 45, 45, 23, 9]

norepetits=set()

for n in llista1:
    norepetits.add(n)

print("Llista:", llista1)
print("Sense repetits:", norepetits)

'''
3-Crea una llista amb contingut de tipus str, amb diverses
paraules.
Mostra les paraules començant per l’inici de la llista i
començant pel final.
Utilitza bucles.
Exemple:
Llista: ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
Resultat:
the quick brown fox jumps over the lazy dog
dog lazy the over jumps fox brown quick the
'''

llista1=["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

for n in llista1:
    print(n, end=' ')

print()

for n in llista1[-1::-1]:
    print(n, end=' ')

'''
4-Seguint l’exercici 3, mostra les paraules
de posicions parelles i posicions senars.
Exemple:
Llista: ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
Resultat:
parelles: the brown jumps the dog
senars: quick fox over lazy
'''

llista1=["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

print("parelles:", end=' ')
for n in llista1[::2]:
    print(n, end=' ')

print()
print("senars:", end=' ')
for n in llista1[1::2]:
    print(n, end=' ')

'''
5-Seguint l’exercici 1, mostra una tercera llista
amb els enters parells de la llista 2.
Exemple:
Llista 1: [45, -6, 0, -32, 23, 9]
Resultat:
Llista 1: [45, -6, 0, -32, 23, 9]
Llista 2: [45, 6, 0, 32, 23, 9]
Llista 3: [6, 0, 32]
'''

llista1=[45, -6, 0, -32, 22, 9]
llista2=[]
llista3=[]

for n in llista1:
    if n<0:
        n=-n
    llista2.append(n)
    if n%2==0:
        llista3.append(n)

print("Llista 1:", llista1)
print("Llista 2:", llista2)
print("Llista 3:", llista3)

'''
6- Crea una list de 100 enters, omple'l amb els
números de l'1 al 100 i després mostra'ls.
'''

llista=list(range(1,101))

for n in llista:
    print(n, end=' ')

'''
7- Crea una list de 100 enters, omple'l amb els
números del 101 al 200 i després mostra'ls.
'''

llista=list(range(101,201))

for n in llista:
    print(n, end=' ')

'''
8- Mostra la taula de multiplicar d’un nombre entrat per teclat.
El programa ha de validar que el valor entrat estigui entre 1 i 10.
Si no ho està, repeteix la pregunta.
Sortida del programa:
---------------------------------------
Quina taula vols veure (1-10)? : 15
Quina taula vols veure (1-10)? : 0
Quina taula vols veure (1-10)? : 4

TAULA DEL 4
=============
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
4 * 6 = 24
4 * 7 = 28
4 * 8 = 32
4 * 9 = 36
4 * 10 = 40
'''

taula=0
while taula<1 or taula>10:
    taula=int(input("Quina taula vols veure (1-10)? : "))

print()
print("TAULA DEL", taula)
print("=============")
for i in range(1,11):
    print(taula, "*", i, "=", i*taula)

'''
9- Tenim una list amb strings(str) amb noms i cognoms, com per exemple:
"Angel","Cuesta","Eva","López","Pol","Castro"
on cada nom va seguit del seu cognom.
Mostra les dades per consola de manera que surti un nom i el seu
cognom a cada línia.
Exemple:
Angel Cuesta
Eva López
Pol Castro
'''

nomcognoms=["Angel","Cuesta","Eva","López","Pol","Castro"]

for i in range(0,len(nomcognoms),2):
    nom, cognom = nomcognoms[i:i+2]
    print(nom, cognom)
