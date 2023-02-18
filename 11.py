from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()

browser.get(link)
 
people_radio = browser.find_element(By.ID, "treasure")
x_element = people_radio.get_attribute("valuex")
x = x_element

import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)
 
input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)
time.sleep(1)
option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
option1.click()
time.sleep(1)
option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
option1.click()

button = browser.find_element(By.XPATH, "//button[text()='Submit']")
button.click()

time.sleep(30)
    