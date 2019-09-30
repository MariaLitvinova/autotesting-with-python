import pytest
from selenium import webdriver
import time
import math

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"])
def test_guest_can_add_product_to_basket(link):
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(link)

    answer = math.log(int(time.time()))
    textarea = browser.find_element_by_css_selector("textarea.textarea")
    textarea.send_keys(str(answer))

    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()

    text = browser.find_element_by_css_selector("pre.smart-hints__hint").text
    print(text)

    time.sleep(10)


