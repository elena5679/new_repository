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
shop = driver.find_element_by_css_selector('#menu-item-40 > a')
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
HTML5 = driver.find_element_by_css_selector('li.post-182 >a >img')
HTML5.click()
add_to_basket = driver.find_element_by_css_selector('div.summary.entry-summary > form > button')
add_to_basket.click()
view_basket = driver.find_element_by_css_selector('a.button.wc-forward')
view_basket.click()
#wpmenucartli > a > i
proceed_button = WebDriverWait(driver,5).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, "#page-34 > div > div.woocommerce > div > div > div > a")) )
proceed_button.click()

first_name = WebDriverWait(driver,5).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, "#billing_first_name")) )
first_name.send_keys("Alisa")

last_name = driver.find_element_by_css_selector('#billing_last_name')
last_name.send_keys('T')

email_adress = driver.find_element_by_css_selector("#billing_email")
email_adress.send_keys("alisa@mail.ru")
time.sleep(3)
arrow = driver.find_element_by_css_selector('#s2id_billing_country > a > span.select2-arrow > b')
arrow.click()
country = driver.find_element_by_css_selector('#s2id_autogen1_search')
country.send_keys("Russia")
select_country = driver.find_element_by_css_selector('#select2-results-1')
select_country.click()

street_adress = driver.find_element_by_css_selector('#billing_address_1')
street_adress.send_keys("Bolshaya Sadovaya")
city = driver.find_element_by_css_selector('#billing_city')
city.send_keys("Rostov-on-Don")
state = driver.find_element_by_css_selector('#billing_state')
state.send_keys("Rostov")
phone = driver.find_element_by_css_selector('#billing_phone')
phone.send_keys(+79085674333)
postcode = driver.find_element_by_css_selector('#billing_postcode')
postcode.send_keys("657432")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
check_payments = driver.find_element_by_css_selector('#payment_method_cheque')
check_payments.click()
place_order = driver.find_element_by_css_selector('#place_order')
place_order.click()

recieve_order = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

payment_method = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot > tr:nth-child(3) > td"), "Check Payments"))


driver.get("https://practice.automationtesting.in")
driver.maximize_window()
driver.implicitly_wait(5)
shop = driver.find_element_by_css_selector('#menu-item-40 > a')
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
HTML5 = driver.find_element_by_css_selector('li.post-182 >a >img')
HTML5.click()
add_to_basket = driver.find_element_by_css_selector('div.summary.entry-summary > form > button')
add_to_basket.click()
view_basket = driver.find_element_by_css_selector('a.button.wc-forward')
view_basket.click()
#wpmenucartli > a > i
proceed_button = WebDriverWait(driver,5).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, "#page-34 > div > div.woocommerce > div > div > div > a")) )
proceed_button.click()

first_name = WebDriverWait(driver,5).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, "#billing_first_name")) )
first_name.send_keys("Alisa")

last_name = driver.find_element_by_css_selector('#billing_last_name')
last_name.send_keys('T')

email_adress = driver.find_element_by_css_selector("#billing_email")
email_adress.send_keys("alisa@mail.ru")
time.sleep(3)
arrow = driver.find_element_by_css_selector('#s2id_billing_country > a > span.select2-arrow > b')
arrow.click()
country = driver.find_element_by_css_selector('#s2id_autogen1_search')
country.send_keys("Russia")
select_country = driver.find_element_by_css_selector('#select2-results-1')
select_country.click()

street_adress = driver.find_element_by_css_selector('#billing_address_1')
street_adress.send_keys("Bolshaya Sadovaya")
city = driver.find_element_by_css_selector('#billing_city')
city.send_keys("Rostov-on-Don")
state = driver.find_element_by_css_selector('#billing_state')
state.send_keys("Rostov")
phone = driver.find_element_by_css_selector('#billing_phone')
phone.send_keys(+79085674333)
postcode = driver.find_element_by_css_selector('#billing_postcode')
postcode.send_keys("657432")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
place_order = driver.find_element_by_css_selector('#place_order')
place_order.click()

recieve_order = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

payment_method = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "ul.woocommerce-thankyou-order-details.order_details > li.method"), "Check Payments"))
