from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path=r'C:/Users/Dell/Downloads/Softwares/chromedriver.exe')

driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()
driver.implicitly_wait(5)

element1 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[1]/div[1]/div[2]/span/span/span[1]/input")
element2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[1]/div[1]/div[2]/span/span/span[2]/button")

action = ActionChains(driver)
action.click(on_element= element1)
action.send_keys("Interview Preperation")
action.pause(2)
action.click(on_element= element2)
action.perform()



