# Откройте страницу http://the-internet.herokuapp.com/inputs.
# Введите в поле текст 1000.
# Очистите это поле (метод clear).
# Введите в это же поле текст 999.

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

Chrome = webdriver.Chrome()
Firefox = webdriver.Firefox()

try:

    Chrome.get ("http://the-internet.herokuapp.com/inputs")
    input_field = Chrome.find_element(By.TAG_NAME, "input")
    input_field.send_keys("1000")
    print (f"Chrome say 1000")
    sleep(2)
    input_field.clear()
    print (f"Chrome say DELETE")
    sleep(1)
    input_field.send_keys("999")
    print (f"Chrome say 999")
    sleep (2)
    
    Firefox.get ("http://the-internet.herokuapp.com/inputs")
    input_field = Firefox.find_element(By.TAG_NAME, "input")
    input_field.send_keys("1000")
    print (f"Firefox say 1000")
    sleep(2)
    input_field.clear()
    print (f"Firefox say DELETE")
    sleep(1)
    input_field.send_keys("999")
    print (f"Firefox say 999")
    sleep (2)

except Exception as ex:
    print (ex)
finally:
    Chrome.quit()
    Firefox.quit()