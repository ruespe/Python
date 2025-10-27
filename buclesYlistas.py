# 1-Crea una llista de valors numèrics enters, no fa falta llegir-la del teclat.
# Mitjançant un bucle crea una segona llista, igual a l’anterior, però modificant tots els valors negatius per el seu valor en positiu. Mostra les dues llistes per consola.
# Exemple:
# Llista 1: [45, -6, 0, -32, 23, 9]
# Resultat:
# Llista 1: [45, -6, 0, -32, 23, 9]
# Llista 2: [45, 6, 0, 32, 23, 9]

lista1 = [45, -6, 0, -32, 23, 9]
lista2 = []

for numero in lista1:    
    if numero < 0:
        newnumero = abs(numero)
        lista2.append(newnumero)
    else:
        lista2.append(numero)

print(f"Lista antigua: {lista1}")
print(f"Lista nueva: {lista2}")

# 2-Crea una llista de valors numèrics enters, no fa falta llegir-la del teclat.
# Mostra per consola els valors de la llista sense repetir cap. Fes servir un bucle i un tipus set.
# Exemple:
# Llista: [45, -6, 0, -32, -6, 0, 45, 45, 23, 9]
# Resultat:
# Llista: [45, -6, 0, -32, -6, 0, 45, 45, 23, 9]
# Sense repetits: -32 -6 0 45 23 9

lista = [45, -6, 0, -32, -6, 0, 45, 45, 23, 9]
listaNoRepetida = []

for numero in lista:
    if numero not in listaNoRepetida:
        listaNoRepetida.append(numero)

print(f"Lista con valores no repetidos: {listaNoRepetida}")

# 3-Crea una llista amb contingut de tipus str, amb diverses paraules.
# Mostra les paraules començant per l’inici de la llista i començant pel final.
# Utilitza bucles.
# Exemple:
# Llista: ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
# Resultat:
# the quick brown fox jumps over the lazy dog
# dog lazy the over jumps fox brown quick the

listaPalabras = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

fraseDeLaLista = " ".join(listaPalabras)

print(f"Frase hecha: {fraseDeLaLista}")


# 4-Seguint l’exercici 3, mostra les paraules de posicions parelles i posicions senars.
# Exemple:
# Llista: ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
# Resultat:
# parelles: the brown jumps the dog
# senars: quick fox over lazy

