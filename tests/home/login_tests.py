from selenium import webdriver
import unittest
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus

import  pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):

        @pytest.fixture(autouse=True)
        def classSetup(self, oneTimeSetUp):

                self.lp = LoginPage(self.driver)
                self.ts = TestStatus(self.driver)

        pytest.mark.run(order=2)
        def test_VALID(self):


                self.lp.login("atomationtest@yahoo.com", "helloworld")
                result1 = self.lp.verifyLoginTitle()
                self.ts.mark(result1, "Title Verified")
                result = self.lp.validlog()
                self.ts.markFinal("test_validLogin", result, "Login was successful")


        pytest.mark.run(order=1)
        def test_INVALID(self):

                self.lp.login("7974537935", "23244")
                result2 = self.lp.invalid()
                assert result2 == True



