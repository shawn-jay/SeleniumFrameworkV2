from pages.home.products_page import ProductPage
from pages.home.login_page import LoginPage
from utilities.test_status import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ProductTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.prodp = ProductPage(self.driver)
        self.ts = TestStatus()
        self.lp = LoginPage(self.driver)
        self.lp.login("standard_user", "secret_sauce")

    @pytest.mark.run(order=2)
    def test_filtering_pricelowtohigh(self):
        self.prodp.filter_by_visible_text("Price (low to high)")

    @pytest.mark.run(order=1)
    def test_testing_attributes(self):
        self.prodp.get_attribute("add-to-cart-sauce-labs-bike-light", "name", "class")

