from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_backet(self):
        button= self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_product_name_in_message(self, product_name):
        message = self.browser.find_element(*ProductPageLocators.MESSAGES).text
        assert product_name in message, "No product name '%s' in message" % product_name

    def should_be_product_price_in_message(self, product_price):
        message = self.browser.find_element(*ProductPageLocators.MESSAGES).text
        assert product_price in message, "No product price '%s' in message" % product_price