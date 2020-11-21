import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com")
print(driver.title)

search = driver.find_element_by_xpath(
    '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
search.send_keys("Test")
search.send_keys(Keys.RETURN)

time.sleep
driver.quit()
