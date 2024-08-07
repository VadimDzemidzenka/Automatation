from selenium import webdriver

Chrome = webdriver.Chrome()

Chrome.get("http://uitestingplayground.com/textinput")

Chrome.find_element("id", "newButtonName").send_keys("SkyPro")
Chrome.find_element("id", "updatingButton").click()

text_click = Chrome.find_element("id", "updatingButton").text

print(text_click)

Chrome.quit()