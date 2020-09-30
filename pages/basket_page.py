from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Items is presented, but should not be"

    def should_be_empty_basket_message(self):
        text='Ваша корзина пуста'
        message=self.browser.find_element(*BasketPageLocators.BASKET_CONTENT).text
        assert text in message, \
            "Should be empty basket message"