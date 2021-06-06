
from base.basepage import BasePage

class LoginPage(BasePage):
        #log = cl.customLogger(logging.DEBUG)
        def __init__(self, driver):
          super().__init__(driver)
          self.driver = driver
        #Locators
        _email = "//input[@class='_2IX_2- VJZDxU']"
        _password = "//input[@type='password']"
        _submit = "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']"

        def enterEmail(self, email):
            self.sendKeys(email, self._email, locatorType="xpath")


        def enterPassword(self, password):
            self.sendKeys(password, self._password, locatorType="xpath")


        def clickLoginButton(self):
            self.elementClick(self._submit, locatorType="xpath")

        # def login2(self, email, password):
        #     self.clearFields()
        #     self.enterEmail(email)
        #     self.enterPassword(password)
        #     self.clickLoginButton()

        def login(self, email, password):

            self.enterEmail(email)
            self.enterPassword(password)
            self.clickLoginButton()
           # self.getTitle()

        def validlog(self):
            result = self.isElementPresent("//div[text()='Poonam']", locatorType="xpath")
            return  result

        def invalid(self):
            result =self.isElementPresent("//span[text()='Your username or password is incorrect']", locatorType= "xpath")
            return  result

        def verifyLoginTitle(self):
            return self.verifyPageTitle("Books")

