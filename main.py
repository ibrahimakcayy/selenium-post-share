#import all libraries
import twitter
import instagram
import facebook
import threads
import time
from selenium import webdriver as web


#import check
print(instagram.cont(),twitter.cont(),facebook.cont(),threads.cont(),"\n")
options = web.EdgeOptions()
driver = web.Edge(options=options)
time.sleep(5)

#set all integer to 0
twtrlogged=0
instalogged=0
facelogged=0
thrdlogged=0

#counter function
def count():

    #open file and add 1
    f=open("count.txt","r")
    accnt=list(map(str,f.read().split()))
    accnt=int(accnt[0])
    f.close()
    fi=open("count.txt","w")
    fi.write(str(accnt+1))
    fi.close
    return accnt


#secrets.txt file inculude username and password
def secrets(check):

    #open file
    f=open("secrets.txt","r")
    accnt=list(f.read().split("\n"))
    f.close()

    #set all username and password || 1. instagram: username password || 2. twitter: username password || 3. facebook: email password || 4. threads: username password ||
    insta=accnt[0].split(" ")
    twtr=accnt[1].split(" ")
    face=accnt[2].split(" ")
    thrd=accnt[3].split(" ")

    if check=="instausrn":
        return insta[1]
    
    elif check=="instapass":
        return insta[2]
    
    elif check=="twtrusrn":
        return twtr[1]
    
    elif check=="twtrpass":
        return twtr[2]
    
    elif check=="faceusrn":
        return face[1]
    
    elif check=="facepass":
        return face[2]
    
    elif check=="thrdusrn":
        return thrd[1]
    
    elif check=="thrdpass":
        return thrd[2] 


#main activity
while True:
    
    try:
        
        #select platform
        choose =input("Twitter(x/twitter) || Instagram(i/instagram) || Facebook(f/facebook) || Threads(t/threads) || Quit(q/quit): ")
 
        if choose.lower()=="twitter" or choose.lower()=="x":
            
            #write caption of post
            caption=input("Write caption: ")
            
            #select tweet mode
            post_mode=input("Normal(n/normal) || With Photo(p/photo): ")

            #if select normal mode this will be activated
            if post_mode.lower()=="normal" or post_mode.lower()=="n":
                
                #if already logged in this will be activated
                if twtrlogged:

                    #open twitter
                    twitter.openurl("https://twitter.com/home")
                    print("Already logged in")
                    
                else:

                    #open chromedriver
                    twitter.drivers(driver)
                    
                    #open twitter
                    twitter.openurl("https://twitter.com/i/flow/login")
                    time.sleep(8)

                    #login twitter
                    twitter.login(secrets("twtrusrn"),secrets("twtrpass"))

                    #login check set 1
                    twtrlogged=1

                #share normal tweet
                time.sleep(15)
                twitter.share_tweet(caption+str(count()))

            #if select photo mode this will be activated
            elif post_mode.lower()=="photo" or post_mode.lower()=="p":

                #enter photo url (don't forget double \\)
                img_url=input("Enter photo url: ")

                #if already logged in this will be activated
                if twtrlogged:

                    #open twitter
                    twitter.openurl("https://twitter.com/home")
                    print("Already logged in")
                    
                else:

                    #open chromedriver
                    twitter.drivers(driver)
                    
                    #open twitter
                    twitter.openurl("https://twitter.com/i/flow/login")
                    time.sleep(8)

                    #login twitter
                    twitter.login(secrets("twtrusrn"),secrets("twtrpass"))

                    #login check set 1
                    twtrlogged=1

                #share tweet with photo
                time.sleep(15)
                twitter.share_tweet(caption+str(count()),img_url)

            else:
                
               print("Invalid selection")
               
        elif choose.lower()=="instagram" or choose.lower()=="i":

            #write caption of post
            caption=input("Write caption: ")
            
            #enter photo url (don't forget double \\)
            img_url=input("Enter photo url: ")

            #if already logged in this will be activated
            if instalogged:

                #open instagram
                instagram.openurl("https://www.instagram.com/")
                print("Already logged in")
                
            else:
                
                #open chromedriver
                instagram.drivers(driver)

                #open instagram
                instagram.openurl("https://www.instagram.com/")
                time.sleep(8)

                #login instagram
                instagram.login(secrets("instausrn"),secrets("instapass"))

                #login check set 1
                instalogged=1

            #share intagram post
            time.sleep(8)
            instagram.share_photo(caption+str(count()),img_url,secrets("instausrn"))

        elif choose.lower()=="facebook" or choose.lower()=="f":

            #write caption of post
            caption=input("Write caption: ")

            #select post mode
            post_mode=input("Normal(n/normal) || With Photo(p/photo): ")

            #if select normal mode this will be activated
            if post_mode.lower()=="normal" or post_mode.lower()=="n":

                #if already logged in this will be activated
                if facelogged:

                    #open facebook
                    facebook.openurl("https://facebook.com")
                    print("Already logged in")
                    
                else:

                    #open chromedriver
                    facebook.drivers(driver)

                    #open facebook
                    facebook.openurl("https://facebook.com")
                    time.sleep(8)

                    #login facebook
                    facebook.login(secrets("faceusrn"),secrets("facepass"))
                    
                    #login check set 1
                    facelogged=1

                #share facebook post
                time.sleep(10)   
                facebook.share_post(caption+str(count()))

            #if select photo mode this will be activated  
            elif post_mode.lower()=="photo" or post_mode.lower()=="p":
                
                #enter photo url (don't forget double \\)
                img_url=input("Enter photo url: ")

                #if already logged in this will be activated
                if facelogged:
                    
                    #open facebook
                    facebook.openurl("https://facebook.com")
                    print("Already logged in")

                else:
                    
                    #open chromedriver
                    facebook.drivers(driver)

                    #open facebook
                    facebook.openurl("https://facebook.com")
                    time.sleep(8)

                    #login facebook
                    facebook.login(secrets("faceusrn"),secrets("facepass"))
                    
                    #login check set 1
                    facelogged=1

                #share facebook post with photo
                time.sleep(10)    
                facebook.share_post(caption+str(count()),img_url)

            else:
                
               print("Invalid selection")
               
        elif choose.lower()=="threads" or choose.lower()=="t":
            
            #write caption of post
            caption=input("Write caption: ")
            
            #select threads mode
            post_mode=input("Normal(n/normal) || With Photo(p/photo): ")

            #if select normal mode this will be activated
            if post_mode.lower()=="normal" or post_mode.lower()=="n":
                
                #if already logged in this will be activated
                if thrdlogged:

                    #open threads
                    threads.openurl("https://www.threads.net/")
                    print("Already logged in")
                    
                else:

                    #open chromedriver
                    threads.drivers(driver)
                    
                    #open threads
                    threads.openurl("https://www.threads.net/login")
                    time.sleep(10)

                    #login threads
                    threads.login(secrets("thrdusrn"),secrets("thrdpass"))

                    #login check set 1
                    thrdlogged=1

                #share normal thread
                time.sleep(15)
                threads.share_thread(caption+str(count()))

            #if select photo mode this will be activated
            elif post_mode.lower()=="photo" or post_mode.lower()=="p":

                #enter photo url (don't forget double \\)
                img_url=input("Enter photo url: ")

                #if already logged in this will be activated
                if thrdlogged:

                    #open threads
                    threads.openurl("https://www.threads.net/")
                    print("Already logged in")
                    
                else:

                    #open chromedriver
                    threads.drivers(driver)
                    
                    #open threads
                    threads.openurl("https://www.threads.net/login")
                    time.sleep(8)

                    #login threads
                    threads.login(secrets("thrdusrn"),secrets("thrdpass"))

                    #login check set 1
                    thrdlogged=1

                #share thread with photo
                time.sleep(15)
                threads.share_thread(caption+str(count()),img_url)

            else:
                
               print("Invalid selection")
      
        elif choose.lower()=="quit" or choose.lower()=="q":

            #close chromedriver
            driver.close()
            
            #exterminate loop
            break
        

        else:
            
            print("Invalid selection try again")
            
    except Exception as e:
        
        print(e)

print("Closed")
