from .base_page import BasePage


class MainPage(BasePage):
    main_page_link="http://selenium1py.pythonanywhere.com/"

    def __init__(self,browser):
        BasePage.__init__(self, browser, MainPage.main_page_link)

