from selenium.webdriver import ActionChains
from time import sleep
from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.login_link = "//span[contains(text(),'Log In')]"
        self.user_email = "//input[@id='form-input-login-email']"
        self.user_password = "//input[@id='form-input-login-password']"
        self.login_btn = "//button[@class='_acdf6688 _b437af84 _bdfbeec1']"

        # ACCEPT COOKIES LOCATOR
        accept_cookies_xpath = "//a[contains(text(),'Allow')]"

        # after clicking on login button "welcome back window opens"
        self.chkbox = "//input[@id='consumer-input']"  #(shop myself checkbox)
        self.continue_btn = "//button[@class='_acdf6688 _b437af84 _bdfbeec1']"
        self.ask_later = "//span[contains(text(),'Ask later')]"
        self.ask_later1 = "//a[@class='_5f858b1f']"


        # after login'
        self.notification = "//span[@class='_3c9497e9']"
        self.myAccount = "//a[@class='_bc89ece3']"
        self.logout = "//div[@class='_1d7c6f6']//div[@class='_cde6a70c']//span[@class='_1dd3bfbf']"
        self.my_order = "//a[@class='_1dd3bfbf']//span[contains(text(),'My Orders')]"
        self.myConversation = "//span[contains(text(),'My Conversations')]"

        self.topright_menu = "//div[@class='_2e35ec41']//div[@class='_4b1878d4']"
        self.myAccount_xpath = "//div[@class='_1d7c6f6']//div[@class='_cde6a70c']//a[@class='_1dd3bfbf']"


        # MAIN MENU Furniture, Art , Jewelry & Watches
        self.main_menu_xpath = "//div[@class='_149e6e48']//div[@class='_d519ca1b']"

        self.action = ActionChains(self.driver)


    # def accept_cookies(self):
    #     # self.driver.find_element_by_xpath(self.accept_cookies_xpath).click()
    #     cookies = self.driver.get_cookies()

    def login_link_click(self):
        self.driver.find_element_by_xpath(self.login_link).click()

    def enter_user_email(self, user_email):
        self.driver.find_element_by_xpath(self.user_email).clear()
        self.driver.find_element_by_xpath(self.user_email).send_keys(user_email)

    def enter_user_password(self, user_password):
        self.driver.find_element_by_xpath(self.user_password).clear()
        self.driver.find_element_by_xpath(self.user_password).send_keys(user_password)

    def click_login_btn(self):
        self.driver.find_element_by_xpath(self.login_btn).click()

    def click_welcome_window(self):
        # self.driver.find_element_by_xpath(self.chkbox).click()
        self.driver.find_element_by_xpath(self.continue_btn).click()
        self.driver.find_element_by_xpath(self.ask_later1).click()

    def topright_menu1(self):
        self.action.move_to_element(self.driver.find_element_by_xpath(self.notification)).perform()
        sleep(2)
        topright_menu_xpath = self.driver.find_elements(By.XPATH, self.topright_menu)
        for self.sub_menu in range(len(topright_menu_xpath)):
            self.action = ActionChains(self.driver)
            self.action.move_to_element(self.driver.find_elements(By.XPATH, self.topright_menu)
                                        [self.sub_menu]).perform()
            sleep(2)



# -----------------------------------------------------------------------------------------------------------------------
#     THIS METHOD cover  TOP RIGHT MENU "My Account -->
#                                        Account information
#                                        My Order
#                                        My Conversation
#                                        Logout"
#
# # -----------------------------------------------------------------------------------------------------------------------
    def myAccount_menu(self):
        # sleep(2)
        self.action.move_to_element(self.driver.find_element_by_xpath(self.notification)).perform()
        sleep(2)
        self.action.move_to_element(self.driver.find_element_by_xpath(self.myAccount)).perform()
        sleep(2)
        myAccount_menu_xpath = self.driver.find_elements(By.XPATH, self.myAccount_xpath)

        for self.sub_menu in range(len(myAccount_menu_xpath)+1):
            # logout submenu has different xpath thats why if statment used, other elements has been
            # captured by using for loop
            if self.sub_menu == 3:
                # self.action.move_to_element(self.driver.find_element_by_xpath(self.myAccount)).perform()
                self.action = ActionChains(self.driver)
                self.action.move_to_element(self.driver.find_element_by_xpath(self.myAccount)).perform()
                sleep(1)
                self.driver.find_element_by_xpath(self.logout).click()
            else:
                self.action = ActionChains(self.driver)
                # print(self.sub_menu)
                sleep(1)
                self.action.move_to_element(self.driver.find_element_by_xpath(self.myAccount)).perform()
                sleep(1)
                self.driver.find_elements(By.XPATH, self.myAccount_xpath)[self.sub_menu].click()
                sleep(1)
                self.driver.find_element_by_xpath(self.notification).click()
                sleep(1)
#-----------------------------------------------------------------------------------------------------------------------
#                       END myAccount_menu(self):
# -----------------------------------------------------------------------------------------------------------------------


