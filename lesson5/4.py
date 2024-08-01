# Откройте страницу http://the-internet.herokuapp.com/entry_ad.
# В модальном окне нажмите на кнопку Сlose.


import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver. support import expected_conditions as EC
from selenium.webdriver.common.by import By

Chrome = webdriver.Chrome()
Firefox = webdriver.Firefox()
try:

    Chrome.get("http://the-internet.herokuapp.com/entry_ad")
    Firefox.get("http://the-internet.herokuapp.com/entry_ad")

    wait = WebDriverWait(Chrome, 10) 
    modal_window = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
    close_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".modal-footer")))
    
    wait = WebDriverWait(Firefox, 10) 
    modal_window = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
    close_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".modal-footer")))
    time.sleep (2)

    close_button.click()
    time.sleep (2)
    

except Exception as ex:
    print(ex)

finally:
    Chrome.quit()
    Firefox.quit()