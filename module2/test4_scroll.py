from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 200);")

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
