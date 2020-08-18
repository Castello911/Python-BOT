from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

f = open("") #add your local .txt file which contains id's and passwords.
idpw = []

for x in range(0,10):
    y = f.readline()
    idpw.insert(x,"%s" %y)
f.close()


for p in range (0,10):
    
    driver = webdriver.Firefox()
    driver.get("") #add website link here that you want to send bot
    time.sleep(2)


    username = driver.find_element_by_xpath("/html/body/form/div/blabla") #This parts can be change but basically you should find a text box that it contains username area // add chrome xpath finder extension if you do that easy
    username.click()
    username.send_keys("%s" % idpw[0])


    pw = driver.find_element_by_xpath("/html/body/form/div/blabla") #This parts can be change but basically you should find a text box that it contains password area // add chrome xpath finder extension if you do that easy
    pw.click()
    pw.send_keys("%s" % idpw[0])


    pw2 = driver.find_element_by_xpath("/html/body/form/div/blabla") #This parts can be change but basically you should find a text box that it contains re-password area // add chrome xpath finder extension if you do that easy
    pw2.click()
    pw2.send_keys("%s" % idpw[0])


    register = driver.find_element_by_xpath("/html/body/form/div/input[4]") #This parts can be change but basically you should find a button which is sign-in // add chrome xpath finder extension if you do that easy
    register.click()
    driver.close()
    
