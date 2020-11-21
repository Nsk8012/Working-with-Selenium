# Basic code of selenium
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://nishanths.net/")  # Opens the website
print(driver.title)  # To print the title of the webpage

# driver.close()   is used to close that certain page
driver.quit()  # used to close the full automation
