from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_backet(self):
        button= self.findt(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def get_product_name(self):
        return self.find(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.find(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_product_name_in_message(self, product_name):
        message = self.find(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name in message, "No product name '%s' in message" % product_name

    def should_be_product_price_in_message(self, product_price):
        message = self.find(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_price in message, "No product price '%s' in message" % product_price

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"

