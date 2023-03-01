#Logout auf der GFN Website
import gfn_login as gfl
import random
import time


try:
    zufallszahl = random.randint(5, 200)
    print("Sekunden bis Programm beginn: ", zufallszahl)
    time.sleep(zufallszahl)
    print("Programm Start!")
    gfl.loginToTW()
    gfl.startTimeTracking()
    print("Login erfolgreich!")
except:
    print("Logout fehlgeschlagen!")