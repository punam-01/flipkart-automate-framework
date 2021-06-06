from pages.courses.flipkartautomate_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.product = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.product.allf("Vishvaguru Vivekananda (Hindi)", "110006")
        result = self.product.verifyFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")