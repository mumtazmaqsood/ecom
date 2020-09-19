
from selenium.webdriver.common.by import By
from time import sleep
import random

class Product_Page():
    def __init__(self, driver):
        self.driver = driver
        self.product_list = []
        self.pp_xpath = "//div[@class='_10b2665f _b88c87ca']"


    def click_Product(self):
        product_OnPage = self.driver.find_elements(By.XPATH, "//div[@class='_10b2665f _b88c87ca']")
        for self.pIndex in range(len(product_OnPage)):
            self.product_list.append(self.driver.find_elements(By.XPATH, "//div[@class='_10b2665f _b88c87ca']")
                                     [self.pIndex])
        page_item = random.choice(self.product_list)
        page_item.click()
        sleep(2)