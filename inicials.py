#1-Demana per teclat una quantitat i a continuació entra per teclat diversos noms fins a la quantitat entrada. Al final mostra tots els noms per pantalla.

# lista=[]
# nombre=""
# print("Escribe 4 nombres")
# i=0
# while i < 4:
#     i+=1
#     nombre=input()
#     lista.append(nombre)
# print(lista)

#2-Igual a l’exercici 1, però sense permetre noms repetits.

# lista2=[]
# nombre2=""
# i=0
# print("Introduce un nombre")
# while i<4:
#     print(i)
#     nombre2 = input(f"{i+1}. Nombre: ")
#     if nombre2 in lista2:
#          print("Repetido, introduce uno distinto")
#     else:
#         lista2.append(nombre2)
#         i+=1

# print(lista2)

# 3-Crea un diccionari, amb diverses dades d’un individu, seguint aquesta estructura:
# {“nom”: …. , “cognom”: …. , “edat”: …. , “pes”: …. }
# Demana les dades per teclat i mostra la informació al final. Si l’individu és major d’edat, afegeix “(major d’edat)”.

nombre=input(f"Nombre: ")
apellido=input(f"Apellido: ")
edad=input(f"Edad: ")
peso=input(f"Peso: ")
if(int(edad)<18):
    print(f"Estos son los datos: {nombre} {apellido} {edad} {peso}")
else:
    print(f"Estos son los datos: {nombre} {apellido} {edad} {peso} (mayor de edad)")

# 4-Crea una llista (list) de diccionaris com els de l’exercici 3. No fa falta llegir les dades per teclat, es pot inicialitzar al codi.
# Mostra el contingut de tota la llista segons s’indica a l’exercici 3.
# Mostra la quantitat d’individus majors d’edat.
# Mostra la mitjana del pes de tots els individus.
# Mostra els noms què s’han repetit o el missatge “SENSE NOMS REPETITS”.


# 5-Mostra tots els individus de l’exercici 4, què són majors d’edat i tenen un pes igual o superior a la mitjana.

