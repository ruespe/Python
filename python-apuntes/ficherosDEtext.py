# 1- Crea un mètode mostra, que a partir d'un nom de fitxer, mostri el seu contingut per consola. Si el fitxer no és vàlid, ha de mostrar un missatge informatiu.


def mostra(nomfitxer):
    try:
        fitxer = open(nomfitxer, "r")
    except FileNotFoundError:
        print("No existeix el fitxer", nomfitxer)
        return
    for linia in fitxer:
        print(linia, end="")
    fitxer.close()


# 2- Crea un mètode concatena, que a partir de dos fitxers, afegeixi el contingut del segon fitxer al primer fitxer. Si el segon fitxer no és vàlid, ha de mostrar un missatge informatiu.


def concatena(nomfitxer1, nomfitxer2):
    try:
        fitxer2 = open(nomfitxer2, "r")
    except FileNotFoundError:
        print("No existeix el fitxer", nomfitxer2)
        return
    try:
        fitxer1 = open(nomfitxer1, "a")
    except FileNotFoundError:
        print("No pot crear-se", nomfitxer1)
        return
    for linia in fitxer2:
        fitxer1.write(linia)
    fitxer1.close()
    fitxer2.close()
    return


# 3- Crea un mètode afegir, que escrigui el contingut d'una llista en un fitxer. S'ha de fer append, el contingut original del fitxer no s'ha d'esborrar.


def afegir(llista, nomfitxer):
    try:
        fitxer = open(nomfitxer, "a")
    except FileNotFoundError:
        print("No pot crear-se", nomfitxer)
        return
    for e in llista:
        fitxer.write(e + "\n")
    fitxer.close()
    return


# 4- Crea un mètode escriuPos, que escrigui una frase en un fitxer, a una posició concreta. Si la posició és incorrecta, ha de mostrar un missatge informatiu.

import sys, os


def escriuPos(frase, pos, nomfitxer):
    try:
        fitxer = open(nomfitxer, "r+")
    except FileNotFoundError:
        try:
            fitxer = open(nomfitxer, "w+")
        except FileNotFoundError:
            print("No pot crear-se", nomfitxer)
            return
    if pos < 0:
        print("Posició incorrecta")
        return
    mida = fitxer.seek(0, os.SEEK_END)
    if pos > mida:
        fitxer.write(" " * (pos - mida))
    fitxer.seek(pos)
    fitxer.write(frase)
    fitxer.close()
    return
