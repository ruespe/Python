'''
1- Crea un script per realitzar còpia de seguretat de diversos orígens.
Farà falta una funció per a fer la còpia d'un origen a un destí.
def copiaDades(origen, desti): # Còpia l'origen amb tot el seu contingut a destí.
L'script tindrà una variable amb la llista d'orígens que s'han de copiar i
una altra variable amb el destí de les còpies.
origens=['/home/usuari/', '/root/', '/etc/', '/dades/']  # Fan falta drets de lectura
desti='/copies/'  # Fan falta drets d'escriptura
S'ha de fer un bucle per recorrer la llista origens i fer la còpia de cada un.

Funcions útils:
os.path.join(path, path2, ...)  EX:  nom=os.path.join("/info/",  desti)
shutil.copytree(src, dst,  dirs_exist_ok=True)
shutil.copy2(src, dst)
os.makedirs(os.path.dirname(desti), exist_ok=True)
os.path.isdir(path)
'''
import os
import shutil

def copiaDades(origen, desti): # Còpia l'origen amb tot el seu contingut a destí.
    try:
        print("Còpia des de", origen, "a", desti)
        if os.path.isdir(origen):
            shutil.copytree(origen, desti, dirs_exist_ok=True)
        else:
            os.makedirs(os.path.dirname(desti), exist_ok=True)
            shutil.copy2(origen, desti)
    except FileNotFoundError as e:
        print("No existeix", origen)

if __name__=='__main__':
    origens=['/home/informatica/.ssh',
             '/home/informatica/Documentos/',
             '/home/informatica/Descargas/empresa.mwb',
             '/dades',
             'Exercici1.py'
             ]

    desti='/home/informatica/copies/'
    for org in origens:
        if org[0]=='/': nomDesti=os.path.join(desti, org[1:])
        else: nomDesti=os.path.join(desti, org)
        copiaDades(org, nomDesti)


'''
2- Crea un script per realitzar la restauració de la còpia de seguretat anterior.
L'script tindrà dues variables: origen de les còpies i destí de restauració.
copies='/copies/'  # Fan falta drets de lectura
desti='/proves/'  # Fan falta drets d'escriptura

Funcions útils:
os.listdir(path)  Ex:  llista=os.listdir('/copies')
'''
import os
from .Exercici1 import copiaDades

if __name__=='__main__':
    copies='/home/informatica/copies/'
    desti='/home/informatica/proves/'
    copiaDades(copies, desti)

'''
3- Modifica els scripts per permetre tenir diverses còpies.
Es tracta d'afegir una variable amb la quantitat de còpies a conservar.
S'hauran de crear diversos directoris amb les còpies.
S'han de conservar la quantitat de còpies indicades, sempre les últimes n còpies fetes.
En fer la restauració farà falta saber quina és la còpia que volem restaurar.
Exemple:
desti='/home/dades/copies/'
ncopies=5

Això crearia:
/home
  |
  --dades
     |
     --copies
        |
        --1
        |
        --2
        |
        --3
        |
        --4
        |
        --5

Si ja hem completat totes les possibles còpies i en volem
fer una més, s'haurà de sobreescriure la més antiga.

Funcions útils:
os.path.getmtime(path)
os.path.isdir(path)
'''

import os, time, shutil
from Exercici1 import copiaDades

def ncopia(desti, ncopies):
    '''
    Detecta quin és el directori de còpies més antic
    '''
    data_min=time.gmtime()
    copia_min=0
    for n in range(1,ncopies+1):
        ndesti=os.path.join(desti, str(n))
        if os.path.exists(ndesti) and os.path.isdir(ndesti):
            fhora=os.path.join(ndesti, "__hora__.txt")
            if os.path.exists(fhora):
                data=time.gmtime(os.path.getmtime(fhora))
            else:
                data=time.gmtime(os.path.getmtime(ndesti))
            if data<data_min:
                copia_min=n
                data_min=data
        else:
            return n
    return copia_min

if __name__=='__main__':
    origens=['/home/informatica/.ssh',
             '/home/informatica/Documentos/',
             '/home/informatica/Descargas/empresa.mwb',
             '/dades',
             'Exercici1.py'
             ]

    desti='/home/informatica/copies/'
    ncopies=5
    ncopia=ncopia(desti, ncopies)
    for org in origens:
        nomDesti=os.path.join(desti, str(ncopia))
        if os.path.exists(nomDesti): shutil.rmtree(nomDesti)
        if org[0]=='/': nomDestiCopia=os.path.join(nomDesti, org[1:])
        else: nomDestiCopia=os.path.join(nomDesti, org)
        copiaDades(org, nomDestiCopia)
        open(os.path.join(nomDesti, "__hora__.txt"), 'a')


'''
4- Unifica els scripts i selecciona la tasca a realitzar
segons els paràmetres que rebi.
Nom script: filesadm.py

Paràmetres:
-h --help            Missatge informatiu del funcionament.
-b --backup          Fa la còpia de seguretat.
-r --restore         Recupera l'última còpia guardada.
-R num --restn num   Recupera la còpia amb número num.
-d path --dest path  Destí de les còpies de seguretat.
-n num               Quantitat de còpies de seguretat guardades.
-o --overwrite       Permet sobreescriure les dades guardades o recuperades.
'''

import getopt, sys, os, shutil
from Exercici1 import copiaDades
from Exercici3 import ncopia

def usage():
    print('Funcionament:\n'
            +'-h --help             Missatge informatiu del funcionament.\n'
            +'-b --backup           Fa la còpia de seguretat.\n'
            +'-r --restore          Recupera l\'última còpia guardada.\n'
            +'-R num --restn num    Recupera la còpia amb número num.\n'
            +'-d path --dest path   Destí de les còpies de seguretat.\n'
            +'-n num                Quantitat de còpies de seguretat guardades.\n'
            +'-o --overwrite        Permet sobreescriure les dades guardades o recuperades.\n')

origens=['/home/informatica/proves/',
         '/home/informatica/Descargas/empresa.mwb',
         '/dades',
         ]

def main():
    maxcopies=5
    copia=0
    desti=None
    volemRestore=volemBackup=False
    overwrite=False
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hbrR:d:n:o", ["help", "backup", "restore", "restn=", "dest=", "overwrite"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    if not opts:
        #Si no té cap opció, mostra help
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--overwrite"):
            overwrite=True
        elif o in ("-d", "--dest"):
            desti=a
        elif o in ("-n", "--num"):
            maxcopies=int(a)
        elif o in ("-r", "--restore"):
            if not volemBackup: volemRestore=True
        elif o in ("-b", "--backup"):
            if not volemRestore: volemBackup=True
        elif o in ("-R", "--restn"):
            a=int(a)
            if a>0 and not volemBackup:
                copia=a
                volemRestore=True
        else:
            assert False, "unhandled option"

    if (volemBackup or volemRestore) and not desti:
        print("Falta el path destí.")
        sys.exit()

    if volemBackup and desti:
        # Còpia del procediment de l'exercici 3
        copia=ncopia(desti, maxcopies)
        nomDesti=os.path.join(desti, str(copia))
        if os.path.exists(nomDesti):
            if overwrite:
                shutil.rmtree(nomDesti)
            else:
                print("Existeix", nomDesti, "i no hi ha overwrite activat.")
                sys.exit()
        for org in origens:
            if org[0]=='/': nomDestiCopia=os.path.join(nomDesti, org[1:])
            else: nomDestiCopia=os.path.join(nomDesti, org)
            copiaDades(org, nomDestiCopia)
            open(os.path.join(nomDesti, "__hora__.txt"), 'a')

    if volemRestore and desti:
        # Per defecte fa restore de la còpia 1
        if copia==0: copia=1
        nomOrg=os.path.join(desti, str(copia))
        if not os.path.exists(nomOrg):
            print("No s'ha trobat la còpia", nomOrg)
            sys.exit()
        for dst in origens:
            if dst[0]=='/': nomOrgCopia=os.path.join(nomOrg, dst[1:])
            else: nomOrgCopia=os.path.join(nomOrg, dst)
            copiaDades(nomOrgCopia, dst)

if __name__ == "__main__":
    main()


'''
5- Crea un script que accepti els següents paràmetres:
-m --missatge         Mostra el text "Missatge de prova"
-f text --frase text  Mostra "FRASE: " i el text passat per paràmetre
-h --help             Mostra informació sobre com fer servir aquest script
'''

import getopt, sys

def usage():
    print('Funcionament:\n'
        +'-m --missatge          Mostra el text "Missatge de prova"\n'
        +'-f text --frase text   Mostra "FRASE: " i el text passat per paràmetre\n'
        +'-h --help              Mostra informació sobre com fer servir aquest script')

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "mf:h", ["missatge", "frase=", "help"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    if not opts and not args:
        #Si no té cap opció, mostra help
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-f", "--frase"):
            print("FRASE: "+a)
            sys.exit()
        elif o in ("-m", "--missatge"):
            print("Missatge de prova")
            sys.exit()
        else:
            assert False, "unhandled option"

if __name__ == "__main__":
    main()


'''
6- Crea un script que mostri el contingut d'un directori passat per paràmetre.
'''

import getopt, sys, os

def usage():
    print('Funcionament:\n'
        +'-d dir  --directory dir Mostra el contingut del directori\n'
        +'-h --help               Mostra informació sobre com fer servir aquest script')

def mostraDir(path):
    if not path: return
    if os.path.exists(path) and os.path.isdir(path):
        for f in os.listdir(path):
            print(f)
    else:
        print("No és un directori")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "d:h", ["directory=", "help"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-d", "--directory"):
            mostraDir(a)
            sys.exit()
        else:
            assert False, "unhandled option"
    # Si té paràmetres intenta utilitzar el primer
    if args: mostraDir(args[0])
    else:
        usage()
        sys.exit(2)

if __name__ == "__main__":
    main()


'''
7- Crea un script que faci la creació d'un directori amb el nom passat per paràmetre.
'''

import getopt, sys, os

def usage():
    print('Funcionament:\n'
        +'-d dir  --mkdir dir  Crea un directori amb el nom indicat\n'
        +'-h --help            Mostra informació sobre com fer servir aquest script')

def creaDir(path):
    if not path: return
    if os.path.exists(path) and os.path.isfile(path):
        print("Existeix un fitxer amb el mateix nom")
    else:
        os.makedirs(path, exist_ok=True)
        print("S'ha creat el directori",path)

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "d:h", ["mkdir=", "help"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-d", "--mkdir"):
            creaDir(a)
            sys.exit()
        else:
            assert False, "unhandled option"
    # Si té paràmetres intenta utilitzar el primer
    if args: creaDir(args[0])
    else:
        usage()
        sys.exit(2)

if __name__ == "__main__":
    main()


'''
8- Crea un script que mostri la data de creació d'un fitxer o directori passat per paràmetre.
'''

import getopt, sys, os, time

def usage():
    print('Funcionament:\n'
        +'-s element --source element  Mostra la data de l\'element amb el nom indicat\n'
        +'-h --help                    Mostra informació sobre com fer servir aquest script')

def mostraData(path):
    if not path: return
    if not os.path.exists(path):
        print("No existeix", path)
    else:
        print(path, time.strftime("%c",
                time.gmtime(os.path.getmtime(path))))

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:h", ["source=", "help"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-s", "--source"):
            mostraData(a)
            sys.exit()
        else:
            assert False, "unhandled option"
    # Si té paràmetres intenta utilitzar el primer
    if args: mostraData(args[0])
    else:
        usage()
        sys.exit(2)

if __name__ == "__main__":
    main()


