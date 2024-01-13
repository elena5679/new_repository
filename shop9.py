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
driver.execute_script("window.scrollBy(0, 700);")
shop = driver.find_element_by_css_selector('#menu-item-40 > a')
shop.click()
add_html5 = driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]')
add_html5.click()
time.sleep(3)
add_java = driver.find_element_by_xpath ('//*[@id="content"]/ul/li[5]/a[2]')
add_java.click()
time.sleep(3)
basket = driver.find_element_by_css_selector('#wpmenucartli > a > i')
basket.click()
button_remove = driver.find_element_by_css_selector('td.product-remove >a')
button_remove.click()
undo = driver.find_element_by_css_selector('div.woocommerce-message > a')
undo.click()
quantity_selector = driver.find_element_by_css_selector('tbody > tr:nth-child(1) > td.product-quantity > div > input')
quantity_selector.clear()
quantity_selector.send_keys("3")
update_basket = driver.find_element_by_css_selector('td.actions > input.button')
update_basket.click()
quantity_selector_check = quantity_selector.get_attribute("value")
print(quantity_selector_check)
assert quantity_selector_check == "3"
time.sleep(3)
coupon = driver.find_element_by_css_selector('tbody > tr:nth-child(3) > td > div > input.button')
coupon.click()
coupon_text = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > ul > li')
coupon_text_check = coupon_text.text
print(coupon_text_check)