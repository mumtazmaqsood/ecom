from selenium.webdriver import ActionChains
from time import sleep
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.common.keys import Keys


class Main_Menu():
    def __init__(self, driver):
        self.driver = driver
        self.random_item = []
        # MAIN MENU Furniture, Art , Jewelry & Watches
        self.main_menu_xpath = "//div[@class='_149e6e48']//div[@class='_d519ca1b']"
        self.main_sub_menu = "//a[@class='_a1295835']"   #it has 186 elements

        # FURNITURE MENU MENU XPATH
        self.furniture_menu_xpath = "//a[@class='_b86fb47b'][contains(text(),'Furniture')]"

        # ART MAIN MENU XPATH
        self.art_menu_xpath = "//a[@class='_b86fb47b'][contains(text(),'Art')]"

        # JWELRY & WATCHES MAIN MENU XPATH
        self.jw_menu_xpath = "//a[@class='_b86fb47b'][contains(text(),'Jewelry & Watches')]"

        #FASHION MAIN MENU XPATH
        self.fashion_xpath = "//a[@class='_b86fb47b'][contains(text(),'Fashion')]"

        # INTERIORS MAIN MENU XPATH
        self.interiors_xpath = "//a[contains(text(),'Interiors')]"

        # NEW & CUSTOM MAIN MENU XPATH
        self.nc_xpath = "//a[@class='_b86fb47b'][contains(text(),'New & Custom')]"

        # STYLES MAIN MENU XPATH
        self.style_xpath = "//a[@class='_b86fb47b'][contains(text(),'Styles')]"

        # SALE MAIN MENU XPATH
        self.sale_xpath = "//a[@class='_b86fb47b _93be6d7e']"

        self.action = ActionChains(self.driver)



# ------------------------------------------------------------------------------------------------------------------------
# this method hover mouse over all main menus
# FURNITURE -- ART -- JEWELRY & WATCHES -- FASHION -- INTERIORS -- NEW & CUSTOMS -- STYLE -- SALE
# ------------------------------------------------------------------------------------------------------------------------
    def main_menu(self):
        main_menu_xpath = self.driver.find_elements(By.XPATH, self.main_menu_xpath)
        for self.i in range(len(main_menu_xpath)):
            self.action = ActionChains(self.driver)
            self.action.move_to_element(self.driver.find_elements(By.XPATH, self.main_menu_xpath)[self.i]).perform()
            sleep(1)
# ------------------------------------------------------------------------------------------------------------------------
#   END main_menu(self):
# ------------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------------------
# this method perform mouse over on Furniture main menu and then clicks on Furniture's submenus 41
# ------------------------------------------------------------------------------------------------------------------------
    def furniture_subMenu(self):
        main_sub_menu = self.driver.find_elements(By.XPATH, self.main_sub_menu)
        for self.j in range(len(main_sub_menu)-145):
            self.action = ActionChains(self.driver)
            self.action.move_to_element(self.driver.find_element_by_xpath(self.furniture_menu_xpath)).perform()
            self.action.move_to_element(self.driver.find_elements(By.XPATH, self.main_sub_menu)[self.j]).perform()
            # random append all sub menus in list and then click randomly on a submenu , at the end it will clear
            # self.random_item bcz this list variable are using by other submenus
            self.random_item.append(self.driver.find_elements(By.XPATH, self.main_sub_menu)[self.j])
        f_item = random.choice(self.random_item)
        f_item.click()
        sleep(1)
        # self.driver.back()
        # sleep(2)
        self.random_item.clear()
# ------------------------------------------------------------------------------------------------------------------------
#   END furniture_subMenu(self):
# ------------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------------------
# this method perform mouse over on Art main menu and then clicks on Art's submenus
# it has 18 items , and starting index is 41 --- ending index 58
# total items are 186
# loop starting point 41 to 58
# ------------------------------------------------------------------------------------------------------------------------
    def art_subMenu(self):
        self.total = 0
        self.art_index = 41
        while self.art_index <= 58:
            self.action = ActionChains(self.driver)
            self.action.move_to_element(self.driver.find_element_by_xpath(self.art_menu_xpath)).perform()
            # sleep(1)
            # self.driver.find_elements(By.XPATH, self.main_sub_menu)[self.art_index].click()
            self.action.move_to_element(self.driver.find_elements(By.XPATH, self.main_sub_menu)[self.art_index]).perform()
            # print(f"{self.driver.find_elements(By.XPATH, self.main_sub_menu)[self.art_index].text}:{self.art_index}")
            self.art_index += 1
            # random append all sub menus in list and then click randomly on a submenu , at the end it will clear
            # self.random_item bcz this list variable are using by other submenus
            self.random_item.append(self.driver.find_elements(By.XPATH, self.main_sub_menu)[self.art_index])
        a_item = random.choice(self.random_item)
        a_item.click()
        sleep(1)
        self.random_item.clear()
# ------------------------------------------------------------------------------------------------------------------------
#   END furniture_subMenu(self):
# ------------------------------------------------------------------------------------------------------------------------
#
#
#
# ------------------------------------------------------------------------------------------------------------------------
# this method perform mouse over on Jewlery & watches menu and then clicks on it's submenus
# it has 16 items , and starting index is 59 --- ending index 74
# total items are 186
# loop starting point 58 to 74
# ------------------------------------------------------------------------------------------------------------------------
    def jw_subMenu(self):
        self.jw_index = 59
        while self.jw_index <= 74:
            self.action = ActionChains(self.driver)
            self.action.move_to_element(self.driver.find_element_by_xpath(self.jw_menu_xpath)).perform()
            # sleep(1)
            self.action.move_to_element(self.driver.find_elements(By.XPATH, self.main_sub_menu)[self.jw_index]).perform()
            # print(f"{self.driver.find_elements(By.XPATH, self.main_sub_menu)[self.jw_index].text}:{self.jw_index}")
            self.jw_index += 1
            # random append all sub menus in list and then click randomly on a submenu , at the end it will clear
            # self.random_item bcz this list variable are using by other submenus
            self.random_item.append(self.driver.find_elements(By.XPATH, self.main_sub_menu)[self.jw_index])
        jw_item = random.choice(self.random_item)
        jw_item.click()
        sleep(1)
        self.random_item.clear()
# ------------------------------------------------------------------------------------------------------------------------
#   END jw_subMenu(self):
# ------------------------------------------------------------------------------------------------------------------------




# ------------------------------------------------------------------------------------------------------------------------
# this method perform mouse over on FASHION menu and then clicks on it's submenus
# it has 16 items , and starting index is 75 --- ending index 98
# total items are 24
# loop starting point 75 to 98
# ------------------------------------------------------------------------------------------------------------------------
    def fashion_subMenu(self):
        self.fashion_index = 75
        while self.fashion_index <= 98:
            self.action = ActionChains(self.driver)
            self.action.move_to_element(self.driver.find_element_by_xpath(self.fashion_xpath)).perform()
            # sleep(1)
            self.action.move_to_element(self.driver.find_elements(By.XPATH, self.main_sub_menu)[self.fashion_index]) \
                .perform()
            # print(f"{self.driver.find_elements(By.XPATH, self.main_sub_menu)[self.fashion_index].text}:"
            #       f"{self.fashion_index}")
            self.fashion_index += 1
            # random append all sub menus in list and then click randomly on a submenu , at the end it will clear
            # self.random_item bcz this list variable are using by other submenus
            self.random_item.append(self.driver.find_elements(By.XPATH, self.main_sub_menu)[self.fashion_index])
        f_item = random.choice(self.random_item)
        f_item.click()
        sleep(1)
        self.random_item.clear()

# ------------------------------------------------------------------------------------------------------------------------
#   END fashion_subMenu(self):
# ------------------------------------------------------------------------------------------------------------------------




# ------------------------------------------------------------------------------------------------------------------------
# this method perform mouse over on INTERIORS menu and then clicks on it's submenus
# it has 21 items , and starting index is 99 --- ending index 119
# total items are 21
# loop starting point 99 to 119
# ------------------------------------------------------------------------------------------------------------------------
    def interiors_subMenu(self):
        self.interiors_index = 75
        while self.interiors_index <= 119:
            self.action = ActionChains(self.driver)
            self.action.move_to_element(self.driver.find_element_by_xpath(self.interiors_xpath)).perform()
            # sleep(1)
            self.action.move_to_element(self.driver.find_elements(By.XPATH, self.main_sub_menu)[self.interiors_index])\
                .perform()
            # print(f"{self.driver.find_elements(By.XPATH, self.main_sub_menu)[self.interiors_index].text}:"
            #       f"{self.interiors_index}")
            self.interiors_index += 1
# ------------------------------------------------------------------------------------------------------------------------
#   END interiors_subMenu(self):
# ------------------------------------------------------------------------------------------------------------------------



# ------------------------------------------------------------------------------------------------------------------------
# this method perform mouse over on NEW & CUSTOM menu and then clicks on it's submenus
# it has 21 items , and starting index is 120 --- ending index 137
# total items are 17
# loop starting point 120 to 137
# ------------------------------------------------------------------------------------------------------------------------
    def nc_subMenu(self):
        self.nc_index = 120
        while self.nc_index <= 137:
            self.action = ActionChains(self.driver)
            self.action.move_to_element(self.driver.find_element_by_xpath(self.nc_xpath)).perform()
            # sleep(1)
            self.action.move_to_element(self.driver.find_elements(By.XPATH, self.main_sub_menu)[self.nc_index])\
                .perform()
            # print(f"{self.driver.find_elements(By.XPATH, self.main_sub_menu)[self.nc_index].text}:"
            #       f"{self.nc_index}")
            self.nc_index += 1
# ------------------------------------------------------------------------------------------------------------------------
#   END interiors_subMenu(self):
# ------------------------------------------------------------------------------------------------------------------------


# 138-153


# ------------------------------------------------------------------------------------------------------------------------
# this method perform mouse over on STYLE menu and then clicks on it's submenus
# it has 15 items , and starting index is 138 --- ending index 154
# total items are 16
# loop starting point 138 to 153
# ------------------------------------------------------------------------------------------------------------------------
    def style_subMenu(self):
        self.style_index = 138
        while self.style_index <= 154:
            self.action = ActionChains(self.driver)
            self.action.move_to_element(self.driver.find_element_by_xpath(self.style_xpath)).perform()
            # sleep(1)
            self.action.move_to_element(self.driver.find_elements(By.XPATH, self.main_sub_menu)[self.style_index])\
                .perform()
            # print(f"{self.driver.find_elements(By.XPATH, self.main_sub_menu)[self.style_index].text}:"
            #       f"{self.style_index}")
            self.style_index += 1
# ------------------------------------------------------------------------------------------------------------------------
#   END style_subMenu(self):
# ------------------------------------------------------------------------------------------------------------------------


# 155 - 185

# ------------------------------------------------------------------------------------------------------------------------
# this method perform mouse over on SALE menu and then clicks on it's submenus
# it has 30 items , and starting index is 155 --- ending index 185
# total items are 30
# loop starting point 155 to 185
# ------------------------------------------------------------------------------------------------------------------------
    def sale_subMenu(self):
        self.sale_index = 155
        while self.sale_index <= 185:
            self.action = ActionChains(self.driver)
            self.action.move_to_element(self.driver.find_element_by_xpath(self.sale_xpath)).perform()
            # sleep(1)
            self.action.move_to_element(self.driver.find_elements(By.XPATH, self.main_sub_menu)[self.sale_index])\
                .perform()
            # print(f"{self.driver.find_elements(By.XPATH, self.main_sub_menu)[self.sale_index].text}:"
            #       f"{self.sale_index}")
            self.sale_index += 1
# ------------------------------------------------------------------------------------------------------------------------
#   END sale_subMenu(self):
# ------------------------------------------------------------------------------------------------------------------------
