from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)
    result = num1 + num2

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(result))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(20)
    browser.quit()
