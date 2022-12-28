import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By

# from .celery import app

# @app.task
# def get_day_results():
# option = Options()
# option.headless = True
driver = uc.Chrome()
driver.get('https://bet365.com')

time.sleep(5)

login_button = driver.find_element(By.CLASS_NAME, 'hm-MainHeaderRHSLoggedOutWide_LoginContainer')

driver.execute_script('arguments[0].click();', login_button)

time.sleep(5)

driver.quit()