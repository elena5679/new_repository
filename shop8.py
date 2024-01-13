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
shop = driver.find_element_by_css_selector('#menu-item-40 > a')
shop.click()
book = driver.find_element_by_css_selector('li.post-182 >a >img')
book.click()
add_button = driver.find_element_by_css_selector('#product-182 > div.summary.entry-summary > form > button')
add_button.click()
basket_items = driver.find_element_by_css_selector('#wpmenucartli > a > span.cartcontents')
basket_items_check = basket_items.text
print(basket_items_check)
assert basket_items_check =="1 Item"
price_basket = driver.find_element_by_css_selector('#wpmenucartli > a > span.amount')
price_basket_check = price_basket.text
print(price_basket_check)
assert price_basket_check =="₹180.00"

view_basket = driver.find_element_by_css_selector('a.button.wc-forward')
view_basket.click()

subt = driver.find_element_by_css_selector('tr.cart-subtotal > td > span')
subt_text = subt.text
print(subt_text)

subtotal  = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr.cart-subtotal > td > span"), "₹180.00"))

total_cost = driver.find_element_by_css_selector('tr.order-total > td > strong > span')
total_check = total_cost.text
print(total_check)

total = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr.order-total > td > strong > span"), "₹183.60"))
