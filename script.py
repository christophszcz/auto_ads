from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

LOGIN_URL = 'https://www.kijiji.ca/t-login.html'
DRIVER_PATH =  os.environ['DRIVER_PATH']
EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']

def login():
    driver = webdriver.Chrome(DRIVER_PATH)

    driver.get(LOGIN_URL)

    time.sleep(5)

    email_field = driver.find_element(By.ID, 'LoginEmailOrNickname')
    password_field = driver.find_element(By.ID, 'login-password')
    login_button = driver.find_element(By.XPATH, '//button[@type="submit" and text()="Log In"]')

    email_field.send_keys(EMAIL)
    password_field.send_keys(PASSWORD)

    login_button.click()
    time.sleep(5)

    try:
        user_icon = driver.find_element(By.XPATH, '//a[@title="My Kijiji"]')
        print("Login successful")
    except Exception as e:
        print("Login failed", e)

    driver.quit()

login()
