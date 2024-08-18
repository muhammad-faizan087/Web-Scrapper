from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pandas import DataFrame

root = "https://www.gulahmedshop.com/mens-clothes/western"
path = "D:\code\Selenium\chromedriver-win64/chromedriver"
driver = webdriver.Chrome(executable_path=path)

titles = []
price = []
currentPage = 1
# stoppingPage = getLastPage()
driver.maximize_window()
while True:
    driver.get(f"{root}?p={currentPage}")
    try:
        container = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//ol[contains(@class,'products list items')]")
            )
        )
        products = WebDriverWait(container, 20).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "li"))
        )
        for product in products:
            try:
                titles.append(
                    product.find_element_by_xpath(
                        ".//span[@class='product-item-link']"
                    ).text
                )
                price.append(
                    product.find_element_by_xpath(".//span[@class='price']").text
                )
            except:
                continue
    except:
        continue
    nextPage = driver.find_element_by_xpath(
        "(//li[@class='item pages-item-next']//a[contains(@class,'action next')])[2]"
    )
    value = nextPage.get_attribute("class")
    if "disabled" in value:
        break
    currentPage += 1

df = DataFrame({"Product": titles, "Price": price})
df.to_csv("GulahmedScraped.csv", index=False)
driver.quit()
