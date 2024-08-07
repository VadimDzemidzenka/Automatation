from selenium import webdriver
from selenium.webdriver.common.by import By

Chrome = webdriver.Chrome()
Chrome.implicitly_wait(16)

Chrome.get("http://www.uitestingplayground.com/ajax")
Chrome.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

content = Chrome.find_element(By.CSS_SELECTOR, "#content")
content.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(content.find_element(By.CSS_SELECTOR, "p.bg-success").text)


Chrome.quit()