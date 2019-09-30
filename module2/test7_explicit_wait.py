from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    text = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button = browser.find_element_by_id("book")
    button.click()

    x_element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "input_value"))
    )
    x = x_element.text
    y = calc(x)

    y_element = browser.find_element_by_id("answer")
    y_element.send_keys(y)

    button = browser.find_element_by_id("solve")
    button.click()

finally:
    time.sleep(20)
    browser.quit()
