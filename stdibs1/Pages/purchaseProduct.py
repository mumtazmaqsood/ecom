from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
class PP():
    def __init__(self, driver):
        self.driver = driver
        self.quantity_xpath = "//div[@class='_af550483 _7274b5d']//select"
        self.purchaseBtn_xpath = "//button[@class='_acdf6688 _b437af84 _bdfbeec1 _a82a0b63 _2e3a1260']"
        self.makeOfferBtn_xpath ="//div[@class='_f89cc499']"

    #   after clicking on purchase , when page clicked for back , there is a pop-up
        self.pop_xpath = "//div[@class='_a1f8755c']"
        self.logo_xpath = "//a[@class='_d037225c']"

    def purchase_product(self):
        try:
            self.driver.find_element_by_xpath(self.purchaseBtn_xpath).click()
            sleep(1)
            self.driver.back()
            sleep(1)
            # self.driver.find_element_by_xpath(self.pop_xpath).click()
            self.driver.back()
        except NoSuchElementException:
            self.driver.find_element_by_xpath(self.logo_xpath).click()
            print("Element not found")