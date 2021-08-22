from pages.addtocart.flipkartautomate_page import AddProductPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AddProductTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.product = AddProductPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.product.allf("Vishvaguru Vivekananda (Hindi)", "110006")
        result = self.product.verifyFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")