import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Read credentials from JSON file
with open('credentials.json') as f:
    credentials = json.load(f)

username = credentials['username']
password = credentials['password']

driver = webdriver.Chrome()

driver.get("https://prod.idp.collegeboard.org/")
driver.implicitly_wait(0.5)

# Fill in the login form
username_box = driver.find_element(by=By.ID, value="idp-discovery-username")
username_box.send_keys(username)
next_button = driver.find_element(by=By.ID, value="idp-discovery-submit")
next_button.click()

password_box = driver.find_element(by=By.ID, value="okta-signin-password")
password_box.send_keys(password)
submit_button = driver.find_element(by=By.ID, value="okta-signin-submit")
submit_button.click()

time.sleep(10)