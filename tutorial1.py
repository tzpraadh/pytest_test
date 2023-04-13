# Selenium Tutorial 

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://app.mas-stage.symphony-dev.com/demo_customer")

driver.implicitly_wait(5)


