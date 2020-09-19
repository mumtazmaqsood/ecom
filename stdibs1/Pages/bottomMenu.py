from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
import random


class BottomMenu():
    def __init__(self, driver):
        self.driver = driver
        # self.item = []
        # Bottom menu xpath
        self.bottomMenu_xpath = "//div[@class='_3deb9396']//div[@class='_58afde05 _40171845 _2b644246 _faf53c2a']//a"
        self.action = ActionChains(self.driver)

    def bottom_menu(self):
        bottom_menu = self.driver.find_elements(By.XPATH, self.bottomMenu_xpath)
        item = []
        for bm_index in range(len(bottom_menu)):
            self.action = ActionChains(self.driver)
            # item.append, append items in list, reason behind to create and append item
            # is that to use random funtion which select element randomly and click on it
            item.append(self.driver.find_elements(By.XPATH, self.bottomMenu_xpath)[bm_index])
            self.action.move_to_element(self.driver.find_elements(By.XPATH, self.bottomMenu_xpath)[bm_index]).perform()
        rnd_item = random.choice(item)
        print(rnd_item.text)
        rnd_item.click()
        sleep(2)
        self.driver.back()
        sleep(2)