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
driver.implicitly_wait(5)
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
android = driver.find_element_by_css_selector('li.post-169 a:nth-child(1)')
android.click()
price1 = driver.find_element_by_css_selector('.price > del > span')
price1_text = price1.text
price2 = driver.find_element_by_css_selector('.price >ins >span')
price2_text = price2.text

assert price1_text =="₹600.00"
assert price2_text =="₹450.00"

cover = WebDriverWait(driver, 5).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, "#content >div >.images>a")) )
cover.click()

close_cover = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
close_cover.click()
