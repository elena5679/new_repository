from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium import webdriver
driver = webdriver.Chrome()
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
html = driver.find_element_by_css_selector('li.cat-item.cat-item-19 > a')
html.click()
amount = driver.find_element_by_css_selector('li.cat-item.cat-item-19.current-cat > span')
number = amount.text
print(number)
assert number == "(3)"
amount = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "li.cat-item.cat-item-19.current-cat > span"), "3"))
