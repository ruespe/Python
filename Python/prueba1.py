"""
print("HOLA")
num1=int(input("mete un número"))
num2=int(input("mete otro"))
sum = num1 + num2
print(sum)
#print("La suma dels dos valors és: " str(sum))
print(f"La suma será: {sum: .2f}")
sum="Hola"
print(type(sum))

sum=5
print(f" {sum**0.5:.2f}")



sum=34
result=0
if sum==25:
    result= sum ** 0.5
else:
    result= sum
    print(f"El resultat es {result}")

    """
"""

num= int (input("Introduce un numero: "))
if num>15:
print("Te has pasado")
else if num<15 :
print("no es ese")
else:
print("Correcto")


#num= int (input("Introduce un numero: "))

if num>0 and num<5:
    print("S")
elif num>5 and num<7:
    print("A")
else:
    print("E")


numDerechoVoto= int (input("Numero que tienen derecho a voto: "))

numVotos= int(input("Total que han votado: "))

votosPositivos = int(input("Votos Positivos: "))

votosNegativos = int(input("Votos Negativos: "))

PorcentageParticipacion = (numVotos/numDerechoVoto)*100
print(PorcentageParticipacion)

PorcentageAfirmativos = (votosPositivos/numVotos)*100
print(f"{PorcentageAfirmativos: .2f}%")

PorcentageNegativos = (votosNegativos/numVotos)*100
print(PorcentageNegativos)

PorcentageEnBlanco = (numVotos-votosPositivos-votosNegativos)/numVotos
print(PorcentageEnBlanco)

if votosPositivos>votosNegativos:
    print("Ha ganado el SÍ")
elif votosPositivos<votosNegativos:
    print("Ha ganado el NO")
else:
    print("Empate")
#mirar tutorial de listas append y remove sort y demás movidaa

#.upper para convertir a mayusculas y .lower para convertir a miniscúlas 

# mirar .split .join .replace .slice

lista=[3,24,5,7,6,2,0,9]
print(lista)
"""
"""
#Añade un elemento al final de la lista
list.append
print("Añade numero al final: ")

#Elimina el primer elemento que coincida
list.remove
print("eliminar")

#Ver el largo de una lista
list.len
print("Ordenar 4 más grandes ")

list.insert
print("Añadir a la posicion X")

list.pop
print("Eliminar posición X")

lista=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
"""
lista1=[]
print("En rango 20")
for i in range(20):
    lista1.append(i)
print()


lista2=[]
for j in range(2,20):
    print(j)
    lista2.append(i)
print()

lista3=[]
for z in range(2,20,3):
    lista3.append(i)
    print(z)