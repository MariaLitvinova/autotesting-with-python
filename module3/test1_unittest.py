import unittest
from selenium import webdriver
import time


class TestAbs(unittest.TestCase):
    def test_correct_form(self):
        self.check_form("http://suninjuly.github.io/registration1.html")

    def test_incorrect_form(self):
        self.check_form("http://suninjuly.github.io/registration2.html")

    def check_form(self, link):
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element_by_css_selector("input.form-control.first[required]")
        first_name.send_keys("Name")

        last_name = browser.find_element_by_css_selector("input.form-control.second[required]")
        last_name.send_keys("Last name")

        email = browser.find_element_by_css_selector("input.form-control.third[required]")
        email.send_keys("email@gmail.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "Text is different: " + welcome_text)


if __name__ == "__main__":
    unittest.main()
