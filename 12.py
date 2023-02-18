from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

browser.get(link)
 
x_element = browser.find_element(By.ID, "num1")
x = x_element.text

y_element = browser.find_element(By.ID, "num2")
y = y_element.text

def calc (x, y):
  return str(int(x) + int(y)) 
z = calc(x, y)

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(z)
 
button = browser.find_element(By.XPATH, "//button[text()='Submit']")
button.click()
time.sleep(30)