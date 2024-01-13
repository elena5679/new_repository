from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium import webdriver
driver = webdriver.Chrome()
time.sleep(3)
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
from selenium.webdriver.support.select import Select
select = Select(driver.find_element_by_css_selector("#content > form > select"))
all_selected_options = select.all_selected_options

items_selector = driver.find_element_by_name("orderby")
items_selector_default=items_selector.get_attribute("value")
if items_selector_default =="menu_order":
    print ('default sorting')
else: print ('not')

from selenium.webdriver.support.select import Select
element = driver.find_element_by_css_selector("#content > form > select")
select = Select(element)
select.select_by_value("price")
time.sleep(3)

items_select = driver.find_element_by_name("orderby")
items_select_price = items_select.get_attribute("value")
if items_select_price == "price":
    print ('price from low to high')