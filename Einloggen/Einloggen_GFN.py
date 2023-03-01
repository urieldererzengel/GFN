#Login GFN Website Morgens
import gfn_login as gfl
import random
import time
import sqlite3 




connection =sqlite3.connect("GFN-Moodle-Login.db")
crsr = connection.cursor()


sql_anweisung = """CREATE TABLE Moodle_Login (AccNr int(50), email varchar(50), passwort varchar(50));"""
sql_anweisung2 = 'INSERT INTO Moodle_Login (AccNr, email, passwort) VALUES (?, ?, ?)'
sql_anweisung3 = """SELECT * FROM Moodle_Login;"""

try:
    crsr.execute(sql_anweisung)
    accNrs = input("AccNr: ",)
    emaillogin = input("E-Mail: ",)
    passwortstr = input("Passwort: ",)
    params = (accNrs, emaillogin, passwortstr)
    crsr.execute(sql_anweisung2, params)
    connection.commit()
except:
    print("Es besteht bereits ein Datensatz!")





try:
    zufallszahl = random.randint(5, 200)
    print("Sekunden bis Programm beginn: ", zufallszahl)
    time.sleep(zufallszahl)
    print("Programm Start!")
    gfl.loginToTW()
    gfl.startTimeTracking()
    print("Login erfolgreich!")
except:
    print("Login fehlgeschlagen!")

connection.close()