#import all libraries
from selenium.webdriver import ActionChains
from selenium import webdriver as web
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


#useless
def cont():
    
    return "ibrahim-facebook.py"


#get driver from main page
def drivers(driv):
    
    global driver
    driver=driv


#open url and max window
def openurl(url):
    
    driver.get(url)
    driver.maximize_window()
    time.sleep(1.5)

    print("Webpage opened")


#get xpaths from notepad
def xpaths(name,paths):
    f=open(f"{name}.txt","r")
    raw_xpaths=list(f.read().split("\n"))
    f.close()
    b=[i.split(":")[1] for i in raw_xpaths]
    return(b[paths])


#login webpage
def login(usrn,passw):
    
    #write username
    driver.find_element(By.XPATH,xpaths("f-xpath",0)).send_keys(usrn)
    time.sleep(0.3)
    
    #write password 
    driver.find_element(By.XPATH,xpaths("f-xpath",1)).send_keys(passw)
    time.sleep(0.3)
    
    #click login button
    driver.find_element(By.XPATH,xpaths("f-xpath",2)).click()
    time.sleep(1)

    print("Logged in")


#share post (with pic or without)
def share_post(text,photo_url="None"):

    print("Start Sharing")
    
    #share post button click
    driver.find_element(By.XPATH,xpaths("f-xpath",3)).click()
    time.sleep(20)

    #if you choose photo+text mode active this section
    if photo_url!="None":

        #open drop img section
        driver.find_element(By.XPATH,xpaths("f-xpath",4)).click()
        time.sleep(1)

        #upload img
        driver.find_element(By.XPATH,xpaths("f-xpath",5)).send_keys(photo_url)
        time.sleep(2)

    #write text
    driver.find_element(By.XPATH,xpaths("f-xpath",6)).send_keys(text)
    time.sleep(1)
    
    #click share button
    driver.find_element(By.XPATH,xpaths("f-xpath",7)).click()
    
    print("Post Shared")
