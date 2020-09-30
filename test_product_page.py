from pages.base_page import BasePage
from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    product_page = ProductPage(browser, link)
    product_page.open()

    product_name =product_page.get_product_name()
    print("\n"+product_name)
    product_price=product_page.get_product_price()
    print("\n" + product_price)

    product_page.add_product_to_backet()

    BasePage.solve_quiz_and_get_code(product_page)

    message = browser.find_element_by_css_selector("#messages").text

    product_page.should_be_product_name_in_message(product_name)
    product_page.should_be_product_price_in_message(product_price)

