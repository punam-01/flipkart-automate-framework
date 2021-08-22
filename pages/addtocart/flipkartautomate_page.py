import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class AddProductPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        #self.driver.implicitly_Wait(10)

    _search = "//input[@title='Search for products, brands and more']"
     #Vishvaguru Vivekananda (Hindi)
    _submit1 = "//button[@type='submit']"
    _select_book = "//a[@class='s1Q9rs']"
    _continue = "//button[@class='_2KpZ6l _1seccl _3AWRsL']"
    order = "//button[@class='_2KpZ6l _2U9uOA ihZ75k _3AWRsL']"
    check = "//span[@class='_2P_LDn']"
    _pincode = "//input[@id='pincodeInputId']"
    credit = "//div[text()='Credit / Debit / ATM Card']"
    to_pay = "//button[@class='_2KpZ6l _2nejCf _3AWRsL']"
    choose = "//div[@class='_1OFgXD']"
    please_fill_out = "//span[@class='_2XN54t']"

    def enterProductName(self, name):
        self.sendKeys(name, self._search, locatorType="xpath")


    def clicksearchButton(self):
        self.elementClick(self._submit1, locatorType="xpath")


    def selectProduct(self):
        element = self.waitForElement(self._select_book, locatorType="xpath")
        self.elementClick(self._select_book, locatorType="xpath")

        handles = self.driver.window_handles
        parentHandle = self.driver.current_window_handle
        for handle in handles:
            if handle not in parentHandle:
              self.driver.switch_to.window(handle)

    def sendpincode(self, pi):
        self.sendKeys(pi, self._pincode, locatorType="xpath")
        self.elementClick(self.check, locatorType="xpath")
#        self.isElementDisplayed(self.check, locatorType="xpath")

    def addtocart(self):
        self.webScroll("down")
        self.elementClick(self.order, locatorType="xpath")
        self.elementClick(self.order, locatorType="xpath")
        #time.sleep(4)
        #element = self.waitForElement(self._continue, locatorType="xpath")
        self.elementClick(self._continue, locatorType="xpath")
    def payment(self):
        self.webScroll("down")
        self.elementClick(self.credit, locatorType="xpath")

    def paynow(self):
        self.elementClick(self.to_pay, locatorType="xpath")

    def allf(self, name, pi):
        time.sleep(2)
        self.enterProductName(name)

        self.clicksearchButton()
        time.sleep(3)
        self.selectProduct()
        #time.sleep(3)
        self.sendpincode(pi)
        #time.sleep(5)
        self.addtocart()



    def verifyFailed(self):
        result = self.isElementDisplayed(self.choose, locatorType="xpath")
        return result
