from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
button.click()
 
confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text

import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)
 
input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control")
input1.send_keys(y)


button = browser.find_element(By.XPATH, "//button[text()='Submit']")
button.click()

time.sleep(5)
    