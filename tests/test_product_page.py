from pages.product_page import ProductPage


class TestGuestAddToBasketFromProductPage():

    def test_guest_can_add_product_to_basket(self,browser):
        product_page = ProductPage(browser)
        product_page.open()

        product_name =product_page.get_product_name()
        print("\n"+product_name)
        product_price=product_page.get_product_price()
        print("\n" + product_price)

        product_page.add_product_to_backet()

        product_page.verify_product_name_in_message(product_name)
        product_page.verify_product_price_in_message(product_price)


    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser)
        page.open()
        page.verify_login_link()


    def test_guest_can_go_to_login_page_from_product_page(self,browser):
        page = ProductPage(browser)
        page.open()
        page.go_to_login_page()



