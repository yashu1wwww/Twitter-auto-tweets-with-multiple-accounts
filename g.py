#upto 5 accounts you can auto tweet for more add more twitter username and password in list 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import random

# List of Twitter accounts (replace with valid credentials)
accounts = [
    {"username": "Twitter123", "password": "Twitter_12345"},
    {"username": "Twitter456", "password": "Twitter_67890"},
    {"username": "Twitter789", "password": "Twitter_11223"},
    {"username": "Twitter321", "password": "Twitter_44556"},
    {"username": "Twitter654", "password": "Twitter_77889"}
]

# List of comments to tweet
commentsDict = [
    'good', 'amazing one', 'keep going', 'excellent', 'next video please',
    'sub to your channel', 'shared to others', 'made my day', 'keep it up', 
    'sensational', 'rock it', 'challenge it', 'post video daily', 
    'work was amazing', 'needed more edit', 'edit was awesome',
    'what a video man', 'watched yesterday', 'your are genius', 
    'faster than light', 'your work needed success', 'new fan of you', 
    'keep rock dude', 'copy cat', 'link the video', 'listening', 
    'writing', 'reading', 'playing'
]

def login_and_tweet(account):
    """Logs into Twitter and posts tweets."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    try:
        driver.get("https://twitter.com/compose/tweet")
        time.sleep(5)

        # Login process
        email = driver.find_element(By.NAME, 'text')
        email.send_keys(account["username"])
        email.send_keys(Keys.ENTER)
        time.sleep(2)

        password = driver.find_element(By.NAME, 'password')
        password.send_keys(account["password"])
        password.send_keys(Keys.ENTER)
        time.sleep(3)

        # Tweet posting loop (up to 5 tweets per account)
        for _ in range(5):  # Change 5 to the desired tweet count
            try:
                tweet_box = driver.find_element(By.XPATH, '//div[@data-testid="tweetTextarea_0"]')
                tweet_box.send_keys(random.choice(commentsDict))
                time.sleep(1)

                post_button = driver.find_element(By.XPATH, '//span[text()="Post"]')
                post_button.click()
                time.sleep(2)

            except Exception as e:
                print(f"Error posting tweet for {account['username']}: {e}")
                break
        
    except Exception as e:
        print(f"Error logging in for {account['username']}: {e}")

    finally:
        time.sleep(2)
        driver.quit()

# Loop through accounts and post tweets
for acc in accounts:
    login_and_tweet(acc)
    
