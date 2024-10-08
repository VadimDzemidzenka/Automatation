from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver. support import expected_conditions as EC
from selenium.webdriver.common.by import By

Chrome = webdriver.Chrome()
wait = WebDriverWait(Chrome, 40, 0.1)

Chrome.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
wait.until(EC.text_to_be_present_in_element((By.ID, "text"), 'Done!'))
src = Chrome.find_element(By.ID, "award").get_attribute("src")
print(src)

Chrome.quit()
