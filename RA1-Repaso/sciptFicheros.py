1- Crea un script que busqui una paraula dins d'un fitxer de text. Ha de mostrar la quantitat de vegades que ha trobat la paraula.
Ha d'admetre les següents opcions:
-f o --fitxer amb el nom del fitxer.
-p o --paraula amb la paraula que volem trobar.
--help o -h mostra un missatge informatiu del funcionament.
Ha de detectar correctament les opcions i paràmetres i mostrar-ne un missatge en cas de dades errònies. Si hi ha diverses opcions, les ha de gestionar totes.
S’ha de fer print, des del main, dels resultats retornats per les funcions.

import getopt, sys

def quantesParaules(nomfitxer, paraula):
    if not nomfitxer or not paraula: return 0
    try:
        fitxer=open(nomfitxer, "r")
    except FileNotFoundError:
        return 0
    compt=0
    for linia in fitxer:
        compt = compt + linia.count(paraula)
    fitxer.close()
    return compt

def usage():
    print("Mostra la quantitat de vegades que ha trobat una paraula dins d'un fitxer de text.\n"+
            "Opcions vàlides:\n"+
            "-f o --fitxer amb el nom del fitxer.\n"+
            "-p o --paraula amb la paraula que volem trobar.\n"+
            "--help o -h mostra un missatge informatiu del funcionament.\n")

def main():
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "f:p:h",
            ["fitxer=", "paraula=", "help"] )
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    if not opts:
        usage()

    paraula=None
    fitxer=None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-f", "--fitxer"):
            fitxer=a
        elif o in ("-p", "--paraula",):
            paraula=a
        else:
            print("Opció desconeguda")

    if fitxer and paraula:
        print("La paraula",paraula, "surt", quantesParaules(fitxer, paraula))

if __name__=="__main__":
    main()



2- Crea un script que insereixi una frase en un número de fila d'un fitxer de text. No ha de sobreescriure, ha de inserir a la fila indicada i conservar la resta de dades del fitxer.
Ha d'admetre les següents opcions:
-f o --fitxer amb el nom del fitxer.
-t o --text amb la frase que volem inserir.
-p o --pos amb el número de fila a on fer l'insert.
--help o -h mostra un missatge informatiu del funcionament.
Ha de detectar correctament les opcions i paràmetres i mostrar-ne un missatge en cas de dades errònies. Si hi ha diverses opcions, les ha de gestionar totes.
S’ha de fer print, des del main, dels resultats retornats per les funcions.
Exemple:
Si posició=0 i text="Con diez cañones por banda,"
Fitxer original:
viento en popa a toda vela,
no corta el mar, sino vuela
un velero bergantín;
Fitxer final:
Con diez cañones por banda,
viento en popa a toda vela,
no corta el mar, sino vuela
un velero bergantín;

import getopt, sys, shutil

def usage():
    print("Opcions vàlides:\n"+
          "-f o --fitxer  nom del fitxer.\n"+
          "-t o --text    frase que volem inserir.\n"+
          "-p o --pos     posició a on fer l'insert.\n"+
          "--help o -h    mostra un missatge informatiu del funcionament.\n")

def inserta(nomfitxer, frase, pos):
    if not nomfitxer or not frase:
        return
    if pos is None or pos < 0:
        return
    try:
        fitxer=open(nomfitxer, "r")
    except FileNotFoundError:
        print("No existeix el fitxer", nomfitxer)
        return
    try:
        fitxer_tmp=open("file_temp.txt", "w")
    except FileNotFoundError:
        print("No pot crear-se file_temp.txt")
        return
    except PermissionError:
        print("No pot crear-se file_temp.txt")
        return
    num_linia=0
    for linia in fitxer:
        if num_linia==pos:
            #escriu la frase a la pos indicada
            fitxer_tmp.write(frase+"\n")
            num_linia=num_linia+1
        fitxer_tmp.write(linia)
        num_linia=num_linia+1
    #La línia es posterior al final del fitxer
    if pos>=num_linia:
        for n in range(pos-num_linia):
            fitxer_tmp.write("\n")
        fitxer_tmp.write(frase+"\n")

    fitxer.close()
    fitxer_tmp.close()
    #rename del fitxer temporal
    shutil.move("file_temp.txt", nomfitxer)
    return

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:t:p:h", ["fitxer=", "text=", "pos=", "help"] )
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    if not opts:
        usage()

    nfitxer=None
    frase=None
    pos=None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-f", "--fitxer"):
            nfitxer=a
        elif o in ("-t", "--text"):
            frase=a
        elif o in ("-p", "--pos"):
            try:
                pos=int(a)
                if pos<0:
                    print("Posició incorrecta")
                    pos=None
            except:
                print("Posició incorrecta")
                pos=None
        else:
            print("Opció desconeguda")

    inserta(nfitxer, frase, pos)

if __name__=="__main__":
    main()




3- Programa un script que creï un nou fitxer de text amb contingut de part d'un altre fitxer.
Ha d'admetre les següents opcions:
-o o --origen amb el nom del fitxer origen.
-d o --desti amb el nom del fitxer nou.
--liniai amb la primera línia que volem guardar, comptant des d'1.
--liniaf amb l'última línia que volem guardar, comptant des d'1.
--help o -h mostra un missatge informatiu del funcionament.
Ha de detectar correctament les opcions i paràmetres i mostrar-ne un missatge en cas de dades errònies. Si hi ha diverses opcions, les ha de gestionar totes.
S’ha de fer print, des del main, dels resultats retornats per les funcions.
Exemple:
Si liniai=2 i liniaf=3
Fitxer origen:
Con diez cañones por banda,
viento en popa a toda vela,
no corta el mar, sino vuela
un velero bergantín;
Fitxer nou:
viento en popa a toda vela,
no corta el mar, sino vuela

import getopt, sys

def usage():
    print("Opcions vàlides:\n"+
          "Crea un nou fitxer de text amb contingut de part d'un altre fitxer.\n"+
          "-o o --origen amb el nom del fitxer origen.\n"+
          "-d o --desti amb el nom del fitxer nou.\n"+
          "--liniai amb la primera línia que volem guardar, comptant des d'1.\n"+
          "--liniaf amb l'última línia que volem guardar, comptant des d'1.\n"+
          "--help o -h mostra un missatge informatiu del funcionament.\n")

def fragment(nomorigen, nomdesti, liniai, liniaf):
    if not nomorigen or not nomdesti:
        return
    try:
        fitxer=open(nomorigen, "r")
    except FileNotFoundError:
        print("No existeix el fitxer", nomorigen)
        return
    try:
        fitxer_dst=open(nomdesti, "w")
    except FileNotFoundError:
        print("No pot crear-se", nomdesti)
        return
    except PermissionError:
        print("No pot crear-se", nomdesti)
        return
    num_linia=1
    for linia in fitxer:
        if num_linia>=liniai and num_linia<=liniaf:
            fitxer_dst.write(linia)
        num_linia=num_linia+1
    fitxer.close()
    fitxer_dst.close()
    return

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "o:d:h", ["origen=", "desti=", "liniai=", "liniaf=", "help"] )
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    if not opts:
        usage()

    nomorigen=None
    nomdesti=None
    liniai=None
    liniaf=None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-o", "--origen"):
            nomorigen=a
        elif o in ("-d", "--desti"):
            nomdesti=a
        elif o == "--liniai":
            liniai=int(a)
        elif o == "--liniaf":
            liniaf=int(a)
        else:
            print("Opció desconeguda")

    fragment(nomorigen, nomdesti, liniai, liniaf)

if __name__=="__main__":
    main()

