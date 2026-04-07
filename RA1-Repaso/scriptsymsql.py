1- Crea un script que donat un atleta ens mostri les seves marques:
Ha d'admetre les següents opcions:
-a o --atleta amb el nom de l'atleta
--help o -h mostra un missatge informatiu del funcionament.
Ha de detectar correctament les opcions i paràmetres i mostrar-ne un missatge en cas de dades errònies. Si hi ha diverses opcions, les ha de gestionar totes.

import mysql.connector  # pip install mysql-connector-python
import getopt, sys

db_host = "127.0.0.1"
db_user = "useratleta"
db_password = "123456"
db_name = "atletisme"

def mostraMarques(db, atleta):
    cursor = db.cursor()
    cursor.execute("SELECT descripcio, datamarca, registre FROM marca NATURAL JOIN atleta \
                            NATURAL JOIN especialitat WHERE nomatleta=%s", (atleta,))
    result = cursor.fetchall()
    if not result:
        print("No hi ha marques d'aquest atleta")
    else:
        for descr, data, regis in result:
            print(descr, data, regis)
    cursor.close()

def usage():
    print("Mostra un atleta i les seves marques.\n"+
            "Opcions vàlides:\n"+
            "-a o --atleta amb el nom de l'atleta.\n"+
            "-h o --help   mostra un missatge informatiu del funcionament.\n")

def main():
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "a:h",
            ["atleta=", "help"] )
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    if not opts:
        usage()

    db = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )

    atleta=None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-a", "--atleta"):
            atleta=a
        else:
            print("Opció desconeguda")

    if atleta:
        mostraMarques(db, atleta)
    db.close()

if __name__=="__main__":
    main()




2- Crea un script que inserti un nou atleta a la base de dades.
Ha d'admetre les següents opcions:
-n amb el num. llicencia
-a amb el nom de l'atleta
-e amb l'email de l'atleta
-t amb el telèfon de l'atleta
--help o -h mostra un missatge informatiu del funcionament.
Ha de detectar correctament les opcions i paràmetres i mostrar-ne un missatge en cas de dades errònies. Si hi ha diverses opcions, les ha de gestionar totes.

import mysql.connector  # pip install mysql-connector-python
import getopt, sys

db_host = "127.0.0.1"
db_user = "useratleta"
db_password = "123456"
db_name = "atletisme"

def insertaAtleta(db, nllicencia, nomatleta, email, telefon):
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO atleta \
            VALUES (%s, %s, %s, %s)",
            (nllicencia, nomatleta, email, telefon))
        db.commit()
    except Exception as err:
        print("No es pot l'insert:", err)
    cursor.close()

def usage():
    print("Inserta un nou atleta a la base de dades.\n"+
        "-n  núm. llicencia\n"+
        "-a  nom de l'atleta\n"+
        "-e  email de l'atleta\n"+
        "-t  telèfon de l'atleta\n"+
        "--help o -h mostra aquest missatge.\n")

def main():
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            "n:a:e:t:h",
            ["help"] )
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    if not opts:
        usage()

    db = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )

    num=atleta=email=telef=None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o=="-n":
            num=a
        elif o=="-a":
            atleta=a
        elif o=="-e":
            email=a
        elif o=="-t":
            telef=a
        else:
            print("Opció desconeguda")

    if num and atleta and email and telef:
        insertaAtleta(db, num, atleta, email, telef)
    else:
        print("Falten dades per a fer l'insert")

    db.close()

if __name__=="__main__":
    main()



3- Demana per teclat el nom d'una ciutat i executa la sentència "SELECT * FROM reunio WHERE lloc=%s". Mostra la quantitat de files obtingudes.

import mysql.connector  # pip install mysql-connector-python

db_host = "127.0.0.1"
db_user = "useratleta"
db_password = "123456"
db_name = "atletisme"

def getFiles(db, ciutat):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM reunio WHERE lloc=%s", (ciutat, ))
    cursor.fetchall()
    files=cursor.rowcount
    cursor.close()
    return files

def main():
    db = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )

    ciutat=input("Entra un nom de ciutat:")

    print("La quantitat de reunions és", getFiles(db, ciutat))

    db.close()

if __name__=="__main__":
    main()



4- Modifica l'exercici 3, en cas de obtenir una quantitat de files > 0 mostra totes les dades amb un bucle.

import mysql.connector  # pip install mysql-connector-python

db_host = "127.0.0.1"
db_user = "useratleta"
db_password = "123456"
db_name = "atletisme"

def getFiles(db, ciutat):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM reunio WHERE lloc=%s", (ciutat, ))
    for cod, nom, ciutat, diai, diaf in cursor.fetchall():
        print(cod, nom, ciutat, diai, diaf)
    files=cursor.rowcount
    cursor.close()
    return files

def main():
    db = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )

    ciutat=input("Entra un nom de ciutat:")

    print("La quantitat de reunions és", getFiles(db, ciutat))

    db.close()

if __name__=="__main__":
    main()

