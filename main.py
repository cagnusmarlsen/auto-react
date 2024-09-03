from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

def sign_in(driver, username, password):
    driver.get("https://dev.to/enter")
    time.sleep(2)
    
    # fill in the username
    username_input = driver.find_element(By.ID, "user_email")
    username_input.send_keys(username)
    
    # fill in the password
    password_input = driver.find_element(By.ID, "user_password")
    password_input.send_keys(password)
    
    # Submit the login form by hitting return
    password_input.send_keys(Keys.RETURN)
    time.sleep(3)

def updoot(driver, blog_url):
    try:
        driver.get(blog_url)
        time.sleep(3)
        
        # Randomly scrolls the page
        scroll_height = driver.execute_script("return document.body.scrollHeight")
        for i in range(5):
            driver.execute_script(f"window.scrollTo(0, {scroll_height * random.uniform(0.2, 0.8)});")
            time.sleep(random.uniform(0.5, 2))

        # Locate and click on all reactions
        time.sleep(0.5)
        like_button = driver.find_element(By.XPATH, "//*[@id='reaction-drawer-trigger']")
        like_button.click()

        time.sleep(0.5)
        unicorn_button = driver.find_element(By.XPATH, "//*[@id='reaction-butt-unicorn']")
        unicorn_button.click()

        time.sleep(0.5)
        exploding_head = driver.find_element(By.XPATH, "//*[@id='reaction-butt-exploding_head']")
        exploding_head.click()

        time.sleep(0.5)
        raised_hands = driver.find_element(By.XPATH, "//*[@id='reaction-butt-raised_hands']")
        raised_hands.click()

        time.sleep(0.5)
        fire = driver.find_element(By.XPATH, "//*[@id='reaction-butt-fire']")
        fire.click()

        time.sleep(2)
        save_button = driver.find_element(By.XPATH, "//*[@id='reaction-butt-readinglist']")
        save_button.click()

        return True
    
    except Exception as e:
        print(f"Error adding reaction or saving: {e}")
    
def sign_out(driver):
    try:
        driver.get("https://dev.to/signout_confirm")
        sign_out_button = driver.find_element(By.XPATH, "//*[@id='page-content-inner']/div[2]/form/button")
        sign_out_button.click()
        time.sleep(2)
    except Exception as e:
        print(f"Error signing out: {e}")

def handleStuff():

    used_accouts = 0
    # chrome can be replaced with other browsers(Edge, Firefox)
    driver = webdriver.Chrome()

    # The url of the article you want to add the reactions to
    # url = "https://dev.to/miguelrodriguezp99/frontend-resources-v2-57mj"
    url = "article url"

    # The path to the CSV file containing the usernames and passwords
    with open("./details.csv", 'r') as f:
        users = [line.strip().split(',') for line in f.readlines()]
    
    for username, password in users:
        try:
            sign_in(driver, username, password)

            success = updoot(driver, url)
            if(success):
                used_accouts += 1

            print(f"Used accounts: {used_accouts}/{len(users)}")
            time.sleep(2.5)

            sign_out(driver)

            time.sleep(random.uniform(2, 5))

        except Exception as e:
            print(f"An error occurred with account {username}: {e}")
    
    driver.quit()

handleStuff()