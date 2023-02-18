from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text

import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)
 
input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control")
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
    