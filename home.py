import time
from selenium import webdriver
driver = webdriver.Chrome()
time.sleep(5)
driver.get("https://practice.automationtesting.in")
driver.maximize_window()
time.sleep(3)
driver.execute_script("window.scrollBy(0, 600);")

book = driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0")
book.click()
review = driver.find_element_by_css_selector('#product-160 > div.woocommerce-tabs.wc-tabs-wrapper > ul > li.reviews_tab > a')
review.click()
star = driver.find_element_by_css_selector('a.star-5')
star.click()
#button = driver.find_element_by_tag_name("button")
#driver.execute_script("return arguments[0].scrollIntoView(true);", button)
#button.click()

comment = driver.find_element_by_css_selector('#comment')
comment.send_keys("Nice book!")

name = driver.find_element_by_css_selector("#author")
name.send_keys("Anna")
email = driver.find_element_by_css_selector('#email')
email.send_keys("anna@yandex.ru")
submit = driver.find_element_by_css_selector('#submit')
submit.click()
