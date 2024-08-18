# Importing Libraries
from selenium import webdriver
import time
from pandas import DataFrame


web = "https://www.saucedemo.com/v1/"
path = "D:\code\Selenium\chromedriver-win64/chromedriver"
driver = webdriver.Chrome(executable_path=path)
driver.get(web)
driver.maximize_window()

form = driver.find_element_by_tag_name("form")
username = form.find_element_by_id("user-name")
password = form.find_element_by_id("password")
button = form.find_element_by_id("login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
button.click()
time.sleep(8)

Items = []
Price = []

inventory = driver.find_element_by_class_name("inventory_list")
for item in inventory.find_elements_by_class_name("inventory_item"):
    Name = item.find_element_by_class_name("inventory_item_name")
    price = item.find_element_by_class_name("inventory_item_price")
    Items.append(Name.text)
    Price.append(price.text)

df = DataFrame({"Items": Items, "Price": Price})
df.to_csv("Scraped_items.csv", index=False)

driver.quit()
