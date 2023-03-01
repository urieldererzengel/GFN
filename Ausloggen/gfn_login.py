from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3 


browser = webdriver.Chrome('C:/Users/Student/OneDrive - GFN AG (EDU)/Programierung/Python/chromedriver.exe')


connection =sqlite3.connect("GFN-Moodle-Login.db")
crsr = connection.cursor()

sql_anweisung3 = """SELECT * FROM Moodle_Login;"""
    
crsr.execute(sql_anweisung3)
inhalt = crsr.fetchall()
print("inhalt", inhalt[0][1], inhalt[0][2])
emaillogin = inhalt[0][1]
passwortstr = inhalt[0][2]

#Login on the Tribal Wars homepage
def loginToTW():
    

    
    browser.get('https://lernplattform.gfn.de/login/index.php')
    browser.find_element(By.CSS_SELECTOR, '#username').send_keys(emaillogin)
    browser.find_element(By.CSS_SELECTOR, '#password').send_keys(passwortstr)
    browser.find_element(By.CSS_SELECTOR, '#loginbtn').click()

def endTimeTracking():
    browser.find_element(By.CSS_SELECTOR, '#inst13307 > div > div > a > button').click()

def startTimeTracking():
    browser.find_element(By.CSS_SELECTOR, '#inst13307 > div > div > a > button').click()

#page-site-index > nav > ul.nav.navbar-nav.ml-auto > li.usermenu > span > a

def logout():
    browser.find_element(By.CSS_SELECTOR, '#action-menu-toggle-1').click()
    browser.find_element(By.CSS_SELECTOR, '#actionmenuaction-7').click()