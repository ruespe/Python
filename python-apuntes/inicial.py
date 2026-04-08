'''
1-Demana per teclat una quantitat i a continuació entra
per teclat diversos noms fins a la quantitat entrada.
Al final mostra tots els noms per pantalla.
Exemple:
Entra quantitat: 4
nom 1 ? Mortadelo
nom 2 ? Anacleto
nom 3 ? Mortadelo
nom 4 ? Filemón
Els noms són: Mortadelo Anacleto Mortadelo Filemón
'''

#versió amb bucle for

quantitat=int(input("Entra quantitat: "))

llista=[]

for i in range(1,quantitat+1):
    nom=input("nom "+str(i)+" ? ")
    llista.append(nom)

print("Els noms són:", end=' ')
for nom in llista:
    print(nom, end=' ')

print()

#versió amb bucle while

quantitat=int(input("Entra quantitat: "))

llista=[]
i=0
while i<quantitat:
    i=i+1
    nom=input("nom "+str(i)+" ?")
    llista.append(nom)

print("Els noms són:", end=' ')
i=0
while i<len(llista):
    print(llista[i], end=' ')
    i=i+1

'''
2-Igual a l’exercici 1, però sense permetre noms repetits.
Exemple:
Entra quantitat: 4
nom 1 ? Mortadelo
nom 2 ? Anacleto
nom 3 ? Mortadelo
Repetit, nom 3 ? Sacarino
nom 4 ? Filemón
Els noms són: Mortadelo Anacleto Filemón Sacarino
'''

quantitat=int(input("Entra quantitat: "))

llista=[]

i=1
while i<=quantitat:
    nom=input("nom "+str(i)+" ? ")
    if nom in llista:
        # Repetit
        print("Repetit,", end='')
    else:
        # Nou
        llista.append(nom)
        i=i+1

print("Els noms són:", end=' ')
for nom in llista:
    print(nom, end=' ')

'''
3-Crea un diccionari, amb diverses dades d’un individu,
seguint aquesta estructura:

{“nom”: …. , “cognom”: …. , “edat”: …. , “pes”: …. }

Demana les dades per teclat i mostra la informació al final.
Si l’individu és major d’edat, afegeix “(major d’edat)”.
Exemple 1:
Entra nom: Bob Esponja
Entra cognom: SquarePants
Entra edat: 15
Entra pes: 0.2
Aquestes són les dades: Bob Esponja SquarePants 15 anys 0.2 Kg
Exemple 2:
Entra nom: Arenita
Entra cognom: Mejillas
Entra edat: 19
Entra pes: 1.1
Aquestes són les dades: Arenita Mejillas 19 anys 1.1 Kg (major d’edat)
'''

nom=input("Entra el nom: ")
cognom=input("Entra el cognom: ")
edat=int(input("Entra edat: "))
pes=float(input("Entra pes: "))

dades={"nom": nom , "cognom": cognom, "edat": edat , "pes": pes}

print(dades["nom"], dades["cognom"], dades["edat"], "anys",
      dades["pes"], "Kg", end='')

if dades["edat"]>=18:
    print(" (major d'edat)")

'''
4-Crea una llista (list) de diccionaris com els de l’exercici 3.
No fa falta llegir les dades per teclat, es pot inicialitzar al codi.
Mostra el contingut de tota la llista segons s’indica a l’exercici 3.
Mostra la quantitat d’individus majors d’edat.
Mostra la mitjana del pes de tots els individus.
Mostra els noms què s’han repetit o el missatge “SENSE NOMS REPETITS”.
'''

dades1={"nom": "Bob Esponja" , "cognom": "Squarepants", "edat": 14 , "pes": 0.3}
dades2={"nom": "Arenita" , "cognom": "Mejillas", "edat": 20 , "pes": 1.8}
dades3={"nom": "Patricio" , "cognom": "Estrella", "edat": 21 , "pes": 0.4}
dades4={"nom": "Patricio" , "cognom": "Estrella", "edat": 15 , "pes": 0.4}
dades5={"nom": "Arenita" , "cognom": "Mejillas", "edat": 13 , "pes": 1.8}
dades6={"nom": "Arenita" , "cognom": "Mejillas", "edat": 18 , "pes": 1.8}

llista =[ dades1, dades2, dades3, dades4, dades5, dades6]

majors=0  # comptabilitza els majors d'edat
sumapes=0; # suma de tots els pesos per càlcul de la mitjana
apareguts=list() # llista de noms apareguts
repetits=set() # set de noms repetits

for dades in llista:
    print(dades["nom"], dades["cognom"], dades["edat"], "anys",
      dades["pes"], "Kg", end='')
    if dades["edat"]>=18:
        print(" (major d'edat)")
        majors=majors+1
    else:
        # S'ha de fer salt de línia si no és major d'edat
        print()
    sumapes=sumapes+dades["pes"]
    if dades["nom"] in apareguts:
        # És un nom repetit
        repetits.add(dades["nom"])
    else:
        # És la primera vegada que surt el nom
        apareguts.append(dades["nom"])

mitjana=sumapes/len(llista)
print("Hi ha",majors, "individus majors d'edat")
print("La mitjana dels pesos és", mitjana, "Kg")
if len(repetits)==0:
    print("SENSE NOMS REPETITS")
else:
    print("Els nom repetits són: ", repetits)


'''
5-Mostra tots els individus de l’exercici 4, què són majors d’edat i
tenen un pes igual o superior a la mitjana.

'''

dades1={"nom": "Bob Esponja" , "cognom": "Squarepants", "edat": 14 , "pes": 0.3}
dades2={"nom": "Arenita" , "cognom": "Mejillas", "edat": 20 , "pes": 1.8}
dades3={"nom": "Patricio" , "cognom": "Estrella", "edat": 21 , "pes": 0.4}
dades4={"nom": "Patricio" , "cognom": "Estrella", "edat": 15 , "pes": 0.4}
dades5={"nom": "Arenita" , "cognom": "Mejillas", "edat": 13 , "pes": 1.8}
dades6={"nom": "Arenita" , "cognom": "Mejillas", "edat": 18 , "pes": 1.8}

llista =[ dades1, dades2, dades3, dades4, dades5, dades6]

sumapes=0; # suma de tots els pesos per càlcul de la mitjana

for dades in llista:
    sumapes=sumapes+dades["pes"]

mitjana=sumapes/len(llista)
print("La mitjana dels pesos és", mitjana, "Kg")

for dades in llista:
    if dades["edat"]>=18 and dades["pes"]>=mitjana:
        print(dades["nom"], dades["cognom"], dades["edat"], "anys",
          dades["pes"], "Kg", end='')
        if dades["edat"]>=18:
            print(" (major d'edat)")
        else:
            # S'ha de fer salt de línia si no és major d'edat
            print()
