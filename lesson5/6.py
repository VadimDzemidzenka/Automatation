# Откройте страницу http://the-internet.herokuapp.com/login.
# В поле username введите значение tomsmith.
# В поле password введите значение SuperSecretPassword!.
# Нажмите кнопку Login.

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    chrome.get("http://the-internet.herokuapp.com/login")
    chrome.find_element (By.ID, "username").send_keys("tomsmith")
    firefox.get("http://the-internet.herokuapp.com/login")
    firefox.find_element (By.ID, "username").send_keys("tomsmith")
    sleep(1)

    chrome.find_element(
    By.ID, "password").send_keys("SuperSecretPassword!")
    firefox.find_element(
    By.ID, "password").send_keys("SuperSecretPassword!")
    sleep(1)

    chrome.find_element(By.TAG_NAME, "button").click()
    firefox.find_element(By.TAG_NAME, "button").click()
    sleep(2)

except Exception as ex:
    print(ex)

finally:
    chrome.quit()
    firefox.quit()
    