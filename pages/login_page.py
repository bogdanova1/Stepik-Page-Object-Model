from .base_page import BasePage
from .locators import LoginPageLocators
import time  # в начале файла


class LoginPage(BasePage):
    def verify_login_page(self):
        self.verify_login_url()
        self.verify_login_form()
        self.verify_register_form()


    def verify_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url , "Url adress for login is not correct"


    def verify_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"


    def verify_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
