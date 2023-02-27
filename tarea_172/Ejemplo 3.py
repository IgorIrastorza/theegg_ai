# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 16:37:35 2023

@author: igori
"""

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

CHROMIUM_PATH='C:\\Users\\drivers\\chromedriver_win32\\chromedriver.exe'


def wait_until(driver, secs):
    try:
        wait = WebDriverWait(driver, secs)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@id='btn1']")))
    except:
        pass


options = webdriver.ChromeOptions()
options.add_argument(
    '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(executable_path=CHROMIUM_PATH, chrome_options=options)
web = "https://www.instagram.com/"
driver.get(web)

cookie_button = driver.find_element(f"//button[text()='Permitir solo cookies necesarias']")
cookie_button.click()

# get element
element = driver.find_element_by_name("username")
# send keys
element.send_keys("xxxxxx")
wait_until(driver, 1)
element = driver.find_element_by_name("password")
element.send_keys("xxxx")

driver.find_element_by_id("loginForm").submit()

driver.get("https://www.instagram.com/explore/locations/307177342743013/torre-eiffel/")

directory="./screenshots"
px_scroll = 60
elements = driver.find_elements_by_xpath('//img')
for idx, element in enumerate(elements):
    with open(f"{directory}/capture-{idx}.png", 'wb') as file:
        try:
            file.write(element.screenshot_as_png)
        except:
            pass
    wait_until(driver, 1)

    driver.execute_script(f"window.scrollTo(0,{300+(idx*px_scroll)})")
    wait_until(driver, 1)

    if idx > 50:
        break