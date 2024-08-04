# Откройте страницу http://uitestingplayground.com/classattr.
# Кликните на синюю кнопку.
# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.


from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()
try:
    chrome.get("http://uitestingplayground.com/classattr")
    firefox.get("http://uitestingplayground.com/classattr")
    
    for _ in range(3):
          # c h r o m e
        chrome_button = chrome.find_element(
            "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        chrome_button.click()
        sleep(2)
        chrome.switch_to.alert.accept()
          #f i r e f o x
        firefox_button = firefox.find_element(
            "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        firefox_button.click()
        sleep(2)
        firefox.switch_to.alert.accept()
        
except Exception as ex:
    print (ex)
finally:
    chrome.quit()
    firefox.quit()
    