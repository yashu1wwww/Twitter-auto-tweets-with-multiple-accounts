from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import random

commentsDict = ['good','amazing one','keep going','excellent','next video please','sub to your channel','shared to others','made my day','keep it up','sensational','rock it','challenge it','post video daily','work was amazing','needed more edit','edit was awesome',
'what a video man','watched yesterday','your are genious','faster than light','your work needed success','new fan of you','keep rock dude','copy cat','link the video','listening','writing','reading','playing',] #replace with your words

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(7)
email = driver.find_element_by_name('text')
email.send_keys("tweet123@#$%") #replace with your valid twitter username
email.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("tweet123@#$%") #replace with your valid twitter password
password.send_keys(Keys.ENTER)
time.sleep(5)


counter = 0
while True:
    try:
        
        # Post the tweet
        send_button = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
        send_button.send_keys(random.choice(commentsDict))
        
        time.sleep(1)

        # Click the post button
        driver.execute_script('document.querySelector("#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-14lw9ot.r-jumn1c.r-xd6kpl.r-gtdqiz.r-ipm5af.r-184en5c > div:nth-child(2) > div > div > div > div.css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19u6a5r.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr > div > span > span").click()')

        time.sleep(2)  

           
        counter += 1
        if counter == 5: #Change '5' to 'how many auto tweet for a acc....
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break  
        
time.sleep(2)
driver.close()

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(7)
email = driver.find_element_by_name('text')
email.send_keys("tweet123@#$%") #replace with your valid twitter username
email.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("tweet123@#$%") #replace with your valid twitter password
password.send_keys(Keys.ENTER)
time.sleep(5)


counter = 0
while True:
    try:
        
        # Post the tweet
        send_button = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
        send_button.send_keys(random.choice(commentsDict))
        
        time.sleep(1)

        # Click the post button
        driver.execute_script('document.querySelector("#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-14lw9ot.r-jumn1c.r-xd6kpl.r-gtdqiz.r-ipm5af.r-184en5c > div:nth-child(2) > div > div > div > div.css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19u6a5r.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr > div > span > span").click()')


        time.sleep(2)  

           
        counter += 1
        if counter == 5: #Change '5' to 'how many auto tweet for a acc....
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break  
        
time.sleep(2)
driver.close()

