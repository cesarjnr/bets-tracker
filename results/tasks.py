import time
import os
import undetected_chromedriver.v2 as uc
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

load_dotenv('/home/cesar/Desktop/Projects/bets-tracker/bets_tracker/.env')

# from .celery import app

# @app.task
# def get_day_results():
# option = Options()
# option.headless = True
driver = uc.Chrome()
driver.get('https://bet365.com')

time.sleep(2)

login_button = driver.find_element(By.CLASS_NAME, 'hm-MainHeaderRHSLoggedOutWide_LoginContainer')

login_button.click()

time.sleep(2)

login_username_input = driver.find_element(By.CLASS_NAME, 'lms-StandardLogin_Username')

login_username_input.send_keys(os.environ['BET365_USERNAME'])

time.sleep(2)

login_password_input = driver.find_element(By.CLASS_NAME, 'lms-StandardLogin_Password')

login_password_input.send_keys(os.environ['BET365_PASSWORD'])

time.sleep(2)

authenticate_button = driver.find_element(By.CLASS_NAME, 'lms-LoginButton')

authenticate_button.click()

time.sleep(2)

driver.quit()