# Откройте страницу http://uitestingplayground.com/dynamicid.
# Кликните на синюю кнопку.
# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.


from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    count = 0
    chrome.get("http://uitestingplayground.com/dynamicid")
    firefox.get("http://uitestingplayground.com/dynamicid")

    blue_button = chrome.find_element(
        "xpath", '//button[text()="Button with Dynamic ID"]').click()
    blue_button = firefox.find_element(
        "xpath", '//button[text()="Button with Dynamic ID"]').click()

    for _ in range(3):
        blue_button = chrome.find_element(
        "xpath", '//button[text()="Button with Dynamic ID"]').click()
        blue_button = firefox.find_element(
        "xpath", '//button[text()="Button with Dynamic ID"]').click()
        count = count + 1
        sleep(3)
        print (f'Нажатие на синюю кнопку в Сhrome {count}')
        print (f'Нажатие на синюю кнопку в Firefox {count}')
        
except Exception as ex:
    print (ex)
finally:
    chrome.quit()
    firefox.quit()