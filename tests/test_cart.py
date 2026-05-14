# tests/test_cart.py
import pytest
from playwright.sync_api import expect
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

class TestCart:

    @pytest.mark.functional
    def test_view_cart(self, authenticated_page, base_url):
        products_page = ProductsPage(authenticated_page)
        products_page.add_first_product_to_cart()
        products_page.click_cart_icon()
        expect(authenticated_page).to_have_url(f"{base_url}/cart.html")
        # Assume product is displayed, but no specific selector for item in cart

    @pytest.mark.functional
    def test_remove_product_from_cart(self, authenticated_page, base_url):
        products_page = ProductsPage(authenticated_page)
        products_page.add_first_product_to_cart()
        cart_page = CartPage(authenticated_page)
        cart_page.navigate_to(base_url)
        cart_page.remove_first_product()
        # Expect cart empty - cart badge should not be visible
        expect(authenticated_page.locator(cart_page.CART_BADGE)).not_to_be_visible()

    @pytest.mark.regression
    def test_checkout_with_empty_cart(self, authenticated_page, base_url):
        cart_page = CartPage(authenticated_page)
        cart_page.navigate_to(base_url)
        # Verify cart page is accessible when empty
        expect(authenticated_page).to_have_url(f"{base_url}/cart.html")