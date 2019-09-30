from selenium import webdriver
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_css_selector("input.form-control[name='firstname'][required]")
    first_name.send_keys("Name")

    last_name = browser.find_element_by_css_selector("input.form-control[name='lastname'][required]")
    last_name.send_keys("Last name")

    email = browser.find_element_by_css_selector("input.form-control[name='email'][required]")
    email.send_keys("email@gmail.com")

    current_dir = os.path.abspath(
        os.path.dirname( __file__ ) )
    file_path = os.path.join( current_dir, 'file.txt' )
    element = browser.find_element_by_id("file")
    element.send_keys( file_path )

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
