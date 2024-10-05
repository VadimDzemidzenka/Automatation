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

          # c h r o m e
    wait = WebDriverWait(Chrome, 10) 
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
    Chrome_close_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".modal-footer")))
    time.sleep (2)
    Chrome_close_button.click()

          #f i r e f o x
    wait = WebDriverWait(Firefox, 10) 
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
    Firefox_close_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".modal-footer")))
    time.sleep (2)
    Firefox_close_button.click()
    

except Exception as ex:
    print(ex)

finally:
    Chrome.quit()
    Firefox.quit()
    