#upto 5 accounts you can auto tweet
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

driver.get("https://twitter.com/compose/tweet") #url redirect to login 
time.sleep(5)
email = driver.find_element_by_name('text')
email.send_keys("Twitter123") #replace with your valid twitter username
email.send_keys(Keys.ENTER)
time.sleep(1)
password = driver.find_element_by_name("password")
password.send_keys("Twitter_12345") #replace with your valid twitter password
password.send_keys(Keys.ENTER)
time.sleep(3)

counter = 0
while True:
    try:
        
        #Post the tweet
        send_button = driver.find_element(By.XPATH, '//div[@data-testid="tweetTextarea_0"]')
        send_button.send_keys(random.choice(commentsDict))
        time.sleep(1)

        #Click the post button
        post_button = driver.find_element(By.XPATH, '//span[text()="Post"]')
        post_button.click()
        time.sleep(2)  

        counter += 1
        if counter == 5: #Change '5' to 'how many auto tweets for a acc....
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break  
        
time.sleep(2)
driver.close()

#2nd account login
driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/compose/tweet") #url redirect to login 
time.sleep(5)
email = driver.find_element_by_name('text')
email.send_keys("Twitter123") #replace with your valid twitter username
email.send_keys(Keys.ENTER)
time.sleep(1)
password = driver.find_element_by_name("password")
password.send_keys("Twitter_12345") #replace with your valid twitter password
password.send_keys(Keys.ENTER)
time.sleep(3)

counter = 0
while True:
    try:
        
        #Post the tweet
        send_button = driver.find_element(By.XPATH, '//div[@data-testid="tweetTextarea_0"]')
        send_button.send_keys(random.choice(commentsDict))
        time.sleep(1)

        #Click the post button
        post_button = driver.find_element(By.XPATH, '//span[text()="Post"]')
        post_button.click()
        time.sleep(2)  

        counter += 1
        if counter == 5: #Change '5' to 'how many auto tweets for a acc....
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break  
        
time.sleep(2)
driver.close()

#3rd account login
driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/compose/tweet") #url redirect to login 
time.sleep(5)
email = driver.find_element_by_name('text')
email.send_keys("Twitter123") #replace with your valid twitter username
email.send_keys(Keys.ENTER)
time.sleep(1)
password = driver.find_element_by_name("password")
password.send_keys("Twitter_12345") #replace with your valid twitter password
password.send_keys(Keys.ENTER)
time.sleep(3)

counter = 0
while True:
    try:
        
        #Post the tweet
        send_button = driver.find_element(By.XPATH, '//div[@data-testid="tweetTextarea_0"]')
        send_button.send_keys(random.choice(commentsDict))
        time.sleep(1)

        #Click the post button
        post_button = driver.find_element(By.XPATH, '//span[text()="Post"]')
        post_button.click()
        time.sleep(2)  

        counter += 1
        if counter == 5: #Change '5' to 'how many auto tweets for a acc....
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break  
        
time.sleep(2)
driver.close()

#4th account login
driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/compose/tweet") #url redirect to login 
time.sleep(5)
email = driver.find_element_by_name('text')
email.send_keys("Twitter123") #replace with your valid twitter username
email.send_keys(Keys.ENTER)
time.sleep(1)
password = driver.find_element_by_name("password")
password.send_keys("Twitter_12345") #replace with your valid twitter password
password.send_keys(Keys.ENTER)
time.sleep(3)

counter = 0
while True:
    try:
        
        #Post the tweet
        send_button = driver.find_element(By.XPATH, '//div[@data-testid="tweetTextarea_0"]')
        send_button.send_keys(random.choice(commentsDict))
        time.sleep(1)

        #Click the post button
        post_button = driver.find_element(By.XPATH, '//span[text()="Post"]')
        post_button.click()
        time.sleep(2)  

        counter += 1
        if counter == 5: #Change '5' to 'how many auto tweets for a acc....
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break  
        
time.sleep(2)
driver.close()

#5th account login
driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/compose/tweet") #url redirect to login 
time.sleep(5)
email = driver.find_element_by_name('text')
email.send_keys("Twitter123") #replace with your valid twitter username
email.send_keys(Keys.ENTER)
time.sleep(1)
password = driver.find_element_by_name("password")
password.send_keys("Twitter_12345") #replace with your valid twitter password
password.send_keys(Keys.ENTER)
time.sleep(3)

counter = 0
while True:
    try:
        
        #Post the tweet
        send_button = driver.find_element(By.XPATH, '//div[@data-testid="tweetTextarea_0"]')
        send_button.send_keys(random.choice(commentsDict))
        time.sleep(1)

        #Click the post button
        post_button = driver.find_element(By.XPATH, '//span[text()="Post"]')
        post_button.click()
        time.sleep(2)  

        counter += 1
        if counter == 5: #Change '5' to 'how many auto tweets for a acc....
            break
        
    except Exception as e:
        print("An error occurred:", e)
        break  
        
time.sleep(2)
driver.close()



