
''' 
|----------------------------------------------------|
| Nom: Rubén                                            |
| Cognoms: Espín Pérez                                           |
| Grup: DAW 2                                       |
| Data: 07/10/2025                                              |
|----------------------------------------------------|
Agrupa tots els exercicis en un únic fitxer A01.1_NOM_COGNOM.py. Posa un comentari a l’inici de cada exercici

indicant quin és. Els exercicis han de funcionar amb qualsevol conjunt de dades de prova.
1-(2,5p) Crea una list amb paraules diverses, directament al codi.
Demana per teclat una longitud de paraula (quantitat de caràcters).
Fent servir un bucle, compta les paraules de la llista que tenen la mateixa longitud, les que tenen
una longitud inferior i les que tenen una longitud superior.
Mostra el resultat.
Nota: per obtenir la longitud d’una paraula es pot fer servir len(paraula)
Exemple:
list →
"Fent",
"servir",
"un",
"bucle",
"compta",
"les",
"paraules",
"de",
"la",
"llista",
"que",
"tenen",
"la",
"mateixa",
"longitud"
longitud 6
longitud igual a 6: 3
longitud inferior a 6: 9
longitud superior a 6: 3
''' 
'''

lista1=["Fent","servir","un","bucle","compta","les","paraules","de","la","llista","que","tenen","longitud"]
caracteres=input("Introduce la cantidad de caracteres:" )

for longitud in lista1:
    #if(caracteres.count==longitud.)
    #print(caracteres)
    print(str(caracteres))
'''

''' 

2-(2,5p) Realitza un joc de daus en els qual es guanyen uns punts en funció del resultat de diversos daus tirats. Si hi ha algun dau que sigui menor que 3, aleshores la puntuació final és zero punts. En altre cas la puntuació es calcula de la següent manera:
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



''' 

3-(2,5p) Crea una list amb valors enters, directament al codi.
Demana per teclat dos valors numèrics. Crea una nova llista amb tots els valors de la primera què es troben entre els dos valors entrats per teclat (inclosos), sense valors repetits.
Mostra la nova llista. Utilitza bucles.
Exemple:
list → 5, 8, -32, 0, -5, 88, 20, -5, 7, 8, 9, -100, 100
Límits -10 a 20
Resultat:
5, 8, 0, -5, 20, 7, 9
''' 


lista3=[5, 8, -32, 0, -5, 88, 20, -5, 7, 8, 9, -100, 100]
listaNueva=[]
numero = 1
n1=input("Introduce un numero: ")
n2=input("Introduce otro numero: ") # pon el limite y el maximo como en el ejemplo

if(n1 < n2):
    limiteMenor = n1
    limiteMayor = n2
else:
    limiteMenor = n2
    limiteMayor = n1
lista3.reverse

for numero in lista3:
    if(numero >= int(limiteMenor) and numero <= int(limiteMayor)):
        #print(numero)
        listaNueva.append(numero)
cont=0
for repetido in listaNueva:
    print(f"listaNueva: {repetido}")
    if(cont==2):
        listaNueva.remove(repetido)
    for repetido2 in lista3:
     print(f"lista3: {repetido2}")
    if(repetido2==repetido):
            cont+=1
            print(cont)
print("""""""""""")

print(listaNueva)  #limite funciona, eliminar repetido no

''' 

4-(2,5p) Fent servir el següent diccionari: edats={'Jim': 16, 'Bob': 26, 'Carol': 83, 'Dave': 21, 'Flow': 38, 'Katie': 47, 'Nate': 89}. Crea un bucle que demani per teclat diversos valors clau (key), fins que el valor sigui 'FI'. Per cada clau, si existeix al diccionari, mostra un missatge amb el valor que li correspon. Si no existeix, demana per teclat un valor i afegeix la clau:valor al diccionari.
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
{'Jim': 16, 'Bob': 26, 'Carol': 83, 'Dave': 21, 'Flow': 38, 'Katie': 47, 'Nate':89, 'Clint': 99, 'Tom': 65}
''' 

edats={'Jim': 16, 'Bob': 26, 'Carol': 83, 'Dave': 21, 'Flow': 38, 'Katie': 47, 'Nate': 89,}
clave=""
fin=""    

while clave != "FI":  ####para acabar el bucle PON FI EN MAYUSCULAS
    clave=input("Introduce una clave: ") #escribe los nombres tal cual aparecen en la lista
    for datos in edats: 
        if(datos == clave):
            print(edats[datos])
        if(datos == ValueError):
           nuevoDato = input("Dale un valor: ")
           edats[clave].get(nuevoDato)




