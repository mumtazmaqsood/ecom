# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import random
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class MyCart():
    def __init__(self, driver):
        self.driver = driver
        # self.driver.refresh()
        self.cart_products = []
        self.remove_item = []
        self.pruchase_prod = []
        self.myCart_xpath = "//a[@class='_611981ea']"
        self.totalProdcts_xpath = "//div[@class='_7f728a8']"

        self.remove_product_xpath = "//div[@class='_7345603c']"
        self.confirmation_xpath = "//span[contains(text(),'Yes, Remove')]"
        # purchase btn on cart                                        _acdf6688 _b437af84 _bdfbeec1 _bbda1a7
        self.purchaseBtn_xpath = "//div[@class='_7f728a8']//a[@class='_acdf6688 _b437af84 _bdfbeec1 _bbda1a7']"
        # self.purchaseBtn_xpath = "//a[@class='_acdf6688 _b437af84 _bdfbeec1 _bbda1a7']"
        # self.purchaseBtn_xpath = "//a[@data-tn='item-actions-purchase-item']"
        # self.purchaseBtn_xpath = "//span[contains(text(), 'Purchase')]"

        # shipping method xpath
        self.shipping_method_xpath = "//form[@class='_7b8737db']//input"
        self.sBtn_continue_xpath = "//button[@class='_acdf6688 _b437af84 _bdfbeec1 _6a103a4e _e673b8a5 _a3100195 _d24b46d _62901629 ']"

        # payment method xpath
        self.creditCard_xpath = "//span[contains(text(),'Credit/ Debit Card')]"
        self.paymat_method_xpath = "//div[@class='_8128d658']//div[@class='_81bebf43']"
        self.payment_continue_xpath = "//button[@class='_acdf6688 _b437af84 _bdfbeec1 " \
                                      "_6a103a4e _e673b8a5 _a3100195 _d24b46d ']"

        # self.action = ActionChains(self.driver)

    #     XPATH ON CHECKOUT PAGE
        self.shipping_form_xpath = "//input[@class='_cbc8cf9e']"
        self.coutinue_btn = "//button[@class='_acdf6688 _b437af84 _bdfbeec1 _6909c4de _e673b8a5 _a3100195 _d24b46d']"

    # already save address
    #     self.save_address_xpath = "//input[@id='shipping-92947451']"
        self.save_address_xpath = "//div[@class='_b2db66f2']"


    def purchase_product(self):
        sleep(2)
        self.driver.find_element_by_xpath(self.myCart_xpath).click()
        count_products = self.driver.find_elements(By.XPATH, "//div[@class='_7f728a8']")
        p_product= self.driver.find_elements(By.XPATH, self.purchaseBtn_xpath)
        if len(count_products) > 0:
            for c_index in range(len(p_product)):
                # self.cart_products.append(self.driver.find_elements(By.XPATH, "//div[@class='_7f728a8']")[c_index])
                self.cart_products.append(self.driver.find_elements(By.XPATH, "//div[@class='_7f728a8']"
                                                                              "//a[@class='_acdf6688 "
                                                                              "_b437af84 _bdfbeec1 _bbda1a7']")[c_index])
            a = random.choice(self.cart_products)
            print(f"select item:{a.text}")
            sleep(2)
            a.click()
            sleep(2)
            # add new code
            # ---------------------
            shipping_adress = self.driver.find_elements(By.XPATH, self.shipping_form_xpath)
            self.driver.find_element_by_xpath("//span[contains(text(),'1.')]"
                                              "//span[contains(text(),'Shipping Address')]").click()
            sleep(2)
            save_address = self.driver.find_elements(By.XPATH, self.save_address_xpath)
            if len(save_address) <= 0:
                for s_index in range(len(shipping_adress)):
                    if s_index == 0:
                        # self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].clear()
                        self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('Mumtaz')
                    elif s_index == 1:
                        # self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].clear()
                        self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('Maqsood')
                    elif s_index == 2:
                        self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('Gladsaxe 33')
                    # elif s_index == 4:
                    #     self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('Denmark')
                    elif s_index == 6:
                        self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('Arhus')
                    elif s_index == 7:
                        self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('2860')
                    elif s_index == 8:
                        self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('123456478')
                    else:
                        self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('None')
                    sleep(2)
                self.driver.find_element_by_xpath(self.coutinue_btn).click()
                sleep(4)
                self.driver.find_element_by_xpath(self.sBtn_continue_xpath).click()
                sleep(2)
                # checking payments
                payment_methods = self.driver.find_elements(By.XPATH, self.paymat_method_xpath)
                for payment_index in range(len(payment_methods)):
                    self.driver.find_elements(By.XPATH, self.paymat_method_xpath)[payment_index].click()
                sleep(2)
                self.driver.find_element_by_xpath(self.creditCard_xpath).click()
                sleep(2)
                self.driver.find_element_by_xpath(self.payment_continue_xpath)
                sleep(5)
                # self.driver.find_element_by_xpath(self.shipping_method_xpath)[1].click()
            # ---------------------
            self.driver.back()
            sleep(2)
            #     -------------------------end---------------------------
            if len(save_address) > 0:
                print(self.save_address_xpath)
                # # if address already exit below code will delete it and write it again
                # # -----------------------------------------------------------------------------
                self.driver.find_element_by_xpath("//span[contains(text(),'Delete')]").click()
                sleep(2)
                self.driver.find_element_by_xpath("//button[@class='_acdf6688 _b437af84 "
                                                  "_cfe73161 _6c4b964c _689666ee']").click()
                sleep(2)
                for s_index in range(len(shipping_adress)):
                    if s_index == 0:
                        # self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].clear()
                        self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('Mumtaz')
                    elif s_index == 1:
                        # self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].clear()
                        self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('Maqsood')
                    elif s_index == 2:
                        self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('Gladsaxe 33')
                    # elif s_index == 4:
                    #     self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('Denmark')
                    elif s_index == 6:
                        self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('Arhus')
                    elif s_index == 7:
                        self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('2860')
                    elif s_index == 8:
                        self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('123456478')
                    else:
                        self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('None')
                    sleep(2)
                self.driver.find_element_by_xpath(self.coutinue_btn).click()
                sleep(4)
                self.driver.find_element_by_xpath(self.sBtn_continue_xpath).click()
                sleep(2)
                # checking payments
                payment_methods = self.driver.find_elements(By.XPATH, self.paymat_method_xpath)
                for payment_index in range(len(payment_methods)):
                    self.driver.find_elements(By.XPATH, self.paymat_method_xpath)[payment_index].click()
                sleep(2)
                self.driver.find_element_by_xpath(self.creditCard_xpath).click()
                sleep(2)
                self.driver.find_element_by_xpath(self.payment_continue_xpath)
                sleep(5)
                # self.driver.find_element_by_xpath(self.shipping_method_xpath)[1].click()
            # ---------------------
                self.driver.back()
                sleep(2)
                # -------------------------------------------------------------------------------
            #     # -------working code--------------------------------------------------------
                self.driver.find_element_by_xpath("//span[contains(text(),'Payment Method')]").click()
        else:
            print("there is no product in cart")
        self.driver.back()
        sleep(3)









    # def del_cart_product(self):
    #     self.driver.find_element_by_xpath(self.myCart_xpath).click()
    #     # count_products = self.driver.find_elements(By.XPATH, "//div[@class='_7f728a8']")
    #     del_products = self.driver.find_elements(By.XPATH, "//div[@class='_7345603c']")
    #     if len(del_products) > 0:
    #         for del_index in range(len(del_products)):
    #             # self.cart_products.append(self.driver.find_elements(By.XPATH, "//div[@class='_7f728a8']")[c_index])
    #             self.remove_item.append(self.driver.find_elements(By.XPATH, "//div[@class='_7345603c']")[del_index])
    #         a = random.choice(self.remove_item)
    #         a.click()
    #         sleep(2)
    #         self.driver.find_element_by_xpath(self.confirmation_xpath).click()
    #         sleep(2)
    #     else:
    #         print("there is no product in cart")

    #
    # def purchase_product(self):
    #     self.driver.find_element_by_xpath(self.myCart_xpath).click()
    #     sleep(2)
    #     purchase_products = self.driver.find_elements(By.XPATH, self.purchaseBtn_xpath)
    #     # del_products = self.driver.find_elements(By.XPATH, "//div[@class='_7345603c']")
    #     # sleep(2)
    #     if len(purchase_products) > 0:
    #         for c_index in range(len(purchase_products)):
    #             self.pruchase_prod.append(self.driver.find_elements(By.XPATH, self.purchaseBtn_xpath)[c_index])
    #         a = random.choice(self.pruchase_prod)
    #         sleep(2)
    #         a.click()
    #         sleep(2)
    #         shipping_adress = self.driver.find_elements(By.XPATH, self.shipping_form_xpath)
    #
    #         self.driver.find_element_by_xpath("//span[contains(text(),'1.')]"
    #                                           "//span[contains(text(),'Shipping Address')]").click()
    #         sleep(2)
    #         # save_address = self.driver.find_elements(By.XPATH, self.save_address_xpath)
    #         # if len(save_address) > 0:
    #         #     print(self.save_address_xpath)
    #         #     self.driver.find_element_by_xpath("//span[contains(text(),'Payment Method')]").click()
    #         # if len(save_address) <= 0:
    #         for s_index in range(len(shipping_adress)):
    #             if s_index == 0:
    #                 # self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].clear()
    #                 self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('Mumtaz')
    #             elif s_index == 1:
    #                 # self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].clear()
    #                 self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('Maqsood')
    #             elif s_index == 2:
    #                 self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('Gladsaxe 33')
    #             # elif s_index == 4:
    #             #     self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('Denmark')
    #             elif s_index == 6:
    #                 self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('Arhus')
    #             elif s_index == 7:
    #                 self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('2860')
    #             elif s_index == 8:
    #                 self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('123456478')
    #             else:
    #                 self.driver.find_elements(By.XPATH, self.shipping_form_xpath)[s_index].send_keys('None')
    #             sleep(2)
    #         self.driver.find_element_by_xpath(self.coutinue_btn).click()
    #         sleep(4)
    #         self.driver.find_element_by_xpath(self.sBtn_continue_xpath).click()
    #         sleep(2)
    #         # checking payments
    #         payment_methods = self.driver.find_elements(By.XPATH, self.paymat_method_xpath)
    #         for payment_index in range(len(payment_methods)):
    #             self.driver.find_elements(By.XPATH, self.paymat_method_xpath)[payment_index].click()
    #         sleep(2)
    #         self.driver.find_element_by_xpath(self.creditCard_xpath).click()
    #         sleep(2)
    #         self.driver.find_element_by_xpath(self.payment_continue_xpath)
    #         sleep(5)
    #         # self.driver.find_element_by_xpath(self.shipping_method_xpath)[1].click()
    #         # sleep(2)
    #         self.driver.back()
    #     else:
    #         print("there is no product in cart")
    #     # self.pruchase_prod.clear()
    #     self.driver.back()




