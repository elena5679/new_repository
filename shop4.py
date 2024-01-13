import time
from selenium import webdriver
driver = webdriver.Chrome()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

time.sleep(5)
driver.get("https://practice.automationtesting.in")
driver.maximize_window()
time.sleep(3)
driver.execute_script("window.scrollBy(0, 600);")

account = driver.find_element_by_css_selector('#menu-item-50 > a')
account.click()

register = driver.find_element_by_css_selector('#reg_email')
register.send_keys("anna@yandex.ru")

password = driver.find_element_by_css_selector('#reg_password')
password.send_keys("657987def567dfv")

submit = driver.find_element_by_css_selector('p.woocomerce-FormRow.form-row > input.woocommerce-Button.button')
submit.click()

shop = driver.find_element_by_css_selector('#menu-item-40 > a')
shop.click()
html5_book = driver.find_element_by_css_selector('#content > ul > li.post-181')
html5_book.click()
html_5 = driver.find_element_by_css_selector('div.summary.entry-summary > h1')
check_text = html_5.text
print(check_text)
assert "HTML5 Forms" in check_text

html5_forms = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.summary.entry-summary > h1"), "HTML5 Forms"))
