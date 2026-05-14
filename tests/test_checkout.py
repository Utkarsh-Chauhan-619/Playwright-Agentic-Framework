# tests/test_checkout.py
import pytest
from playwright.sync_api import expect
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestCheckout:

    @pytest.mark.functional
    def test_complete_checkout(self, authenticated_page, base_url):
        products_page = ProductsPage(authenticated_page)
        products_page.add_first_product_to_cart()
        cart_page = CartPage(authenticated_page)
        cart_page.navigate_to(base_url)
        cart_page.click_checkout()
        checkout_page = CheckoutPage(authenticated_page)
        checkout_page.fill_customer_info("John", "Doe", "12345")
        checkout_page.click_finish()
        expect(authenticated_page).to_have_url(f"{base_url}/checkout-complete.html")

    @pytest.mark.regression
    def test_checkout_form_validation(self, authenticated_page, base_url):
        products_page = ProductsPage(authenticated_page)
        products_page.add_first_product_to_cart()
        cart_page = CartPage(authenticated_page)
        cart_page.navigate_to(base_url)
        cart_page.click_checkout()
        checkout_page = CheckoutPage(authenticated_page)
        # Leave fields empty and click continue
        authenticated_page.click(checkout_page.CONTINUE_BUTTON)
        # Expect validation error message to be visible
        expect(authenticated_page.locator(checkout_page.ERROR_MESSAGE)).to_be_visible()