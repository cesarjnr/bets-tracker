import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def run():
    driver = uc.Chrome()
    driver.get('https://statmuse.com/nba')

    search_input = driver.find_element(By.NAME, 'question[query]')

    search_input.send_keys('Stephen Curry')
    search_input.send_keys(Keys.ENTER)

    time.sleep(2)
    driver.quit()