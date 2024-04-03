#import all libraries
from selenium.webdriver import ActionChains
from selenium import webdriver as web
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


#useless
def cont():
    return "ibrahim-instagram.py"


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


#login instagram
def login(usern,passw):
    time.sleep(1)
    
    #write username
    driver.find_element(By.XPATH,xpaths("i-xpath",0)).send_keys(usern)
    
    #write password
    driver.find_element(By.XPATH,xpaths("i-xpath",1)).send_keys(passw)
    time.sleep(1)

    #click login button
    driver.find_element(By.XPATH,xpaths("i-xpath",2)).click()
    time.sleep(10)

    print("Logged in")
    
    driver.get("https://www.instagram.com")
    time.sleep(8)
    
    #click notification decline
    driver.find_element(By.XPATH,xpaths("i-xpath",3)).click()
    time.sleep(2)

#share photo in instagram 
def share_photo(text,photo_url,usern):
    
    print("Start Sharing")

    #open create popup
    driver.find_element(By.XPATH,xpaths("i-xpath",4)).click()
    time.sleep(3)
    
    #upload photo
    driver.find_element(By.XPATH,xpaths("i-xpath",5)).send_keys(photo_url)
    time.sleep(5)
    
    #share actions
    driver.find_element(By.XPATH,xpaths("i-xpath",6)).click()
    time.sleep(2)
    driver.find_element(By.XPATH,xpaths("i-xpath",6)).click()
    time.sleep(3)
    
    #write caption
    driver.find_element(By.XPATH,xpaths("i-xpath",7)).send_keys(text)
    time.sleep(0.5)
    
    #share actions
    driver.find_element(By.XPATH,xpaths("i-xpath",6)).click()
    time.sleep(15)

    print("Post Shared")

    #open profile
    driver.get(f"https://www.instagram.com/{usern}/")
