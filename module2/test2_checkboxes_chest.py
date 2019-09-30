from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    y_element = browser.find_element_by_id("answer")
    y_element.send_keys(y)

    robot_checkbox = browser.find_element_by_id("robotCheckbox")
    robot_checkbox.click()

    robots_rule_option = browser.find_element_by_id("robotsRule")
    robots_rule_option.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(20)
    browser.quit()
