#here i am added upto 2 accs which auto login and tweet if you want more means copy line from 57 to 97 and paste that in 97 line use note++ to find the number line if you want more means do copy paste and again and again and dont forgot to replace acc with password
#(note for auto login used accs must be non authentication accounts)

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

commentsDict = ['good','amazing one','keep going','excellent','next video please','sub to your channel','shared to others','made my day','keep it up','sensational','rock it','challenge it','post video daily','work was amazing','needed more edit','edit was awesome',
'what a video man','watched yesterday','your are genious','faster than light','your work needed success','new fan of you','keep rock dude','copy cat','link the video','listening','writing','reading','playing',] #replace with your words

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(11)
email = driver.find_element_by_name('text')
email.send_keys("@12q121") #replace with your twitter username
email.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("twitter12#$") #replace with your twitter password
password.send_keys(Keys.ENTER)
time.sleep(10)
driver.find_element_by_class_name('public-DraftStyleDefault-block').send_keys(random.choice(commentsDict))
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
time.sleep(4)
driver.find_element_by_class_name('public-DraftStyleDefault-block').send_keys(random.choice(commentsDict))
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
time.sleep(4)
driver.find_element_by_class_name('public-DraftStyleDefault-block').send_keys(random.choice(commentsDict))
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
time.sleep(4)
driver.find_element_by_class_name('public-DraftStyleDefault-block').send_keys(random.choice(commentsDict))
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
time.sleep(4)
driver.find_element_by_class_name('public-DraftStyleDefault-block').send_keys(random.choice(commentsDict))
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
time.sleep(4)
driver.find_element_by_class_name('public-DraftStyleDefault-block').send_keys(random.choice(commentsDict))
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
time.sleep(4)
driver.find_element_by_class_name('public-DraftStyleDefault-block').send_keys(random.choice(commentsDict))
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
time.sleep(4)
driver.find_element_by_class_name('public-DraftStyleDefault-block').send_keys(random.choice(commentsDict))
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
time.sleep(4)
driver.find_element_by_class_name('public-DraftStyleDefault-block').send_keys(random.choice(commentsDict))
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
time.sleep(4)
driver.find_element_by_class_name('public-DraftStyleDefault-block').send_keys(random.choice(commentsDict))
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
time.sleep(4)
driver.close()

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(11)
email = driver.find_element_by_name('text')
email.send_keys("@12wewrt") #replace with your twitter username
email.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("elonwes$%&") #replace with your twitter password
password.send_keys(Keys.ENTER)
time.sleep(4)
driver.find_element_by_class_name('public-DraftStyleDefault-block').send_keys(random.choice(commentsDict))
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
time.sleep(4)
driver.find_element_by_class_name('public-DraftStyleDefault-block').send_keys(random.choice(commentsDict))
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
time.sleep(4)
driver.find_element_by_class_name('public-DraftStyleDefault-block').send_keys(random.choice(commentsDict))
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
time.sleep(4)
driver.find_element_by_class_name('public-DraftStyleDefault-block').send_keys(random.choice(commentsDict))
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
time.sleep(4)
driver.find_element_by_class_name('public-DraftStyleDefault-block').send_keys(random.choice(commentsDict))
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
driver.find_element_by_css_selector('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(3) > div > div > div:nth-child(2) > div.css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19u6a5r.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr > div > span > span').click()
time.sleep(4)
driver.find_element_by_class_name('public-DraftStyleDefault-block').send_keys(random.choice(commentsDict))
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
time.sleep(4)
driver.find_element_by_class_name('public-DraftStyleDefault-block').send_keys(random.choice(commentsDict))
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
time.sleep(4)
driver.find_element_by_class_name('public-DraftStyleDefault-block').send_keys(random.choice(commentsDict))
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
time.sleep(4)
driver.find_element_by_class_name('public-DraftStyleDefault-block').send_keys(random.choice(commentsDict))
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
time.sleep(4)
driver.close()
