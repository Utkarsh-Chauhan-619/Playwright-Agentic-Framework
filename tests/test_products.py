# tests/test_products.py
import pytest
from playwright.sync_api import expect
from pages.products_page import ProductsPage

class TestProducts:

    @pytest.mark.smoke
    def test_logout(self, authenticated_page, base_url):
        products_page = ProductsPage(authenticated_page)
        products_page.logout()
        expect(authenticated_page).to_have_url(f"{base_url}/")

    @pytest.mark.functional
    def test_add_single_product_to_cart(self, authenticated_page):
        products_page = ProductsPage(authenticated_page)
        products_page.add_first_product_to_cart()
        expect(authenticated_page.locator(products_page.CART_BADGE)).to_have_text("1")

    @pytest.mark.edge_case
    def test_add_multiple_products_to_cart(self, authenticated_page):
        products_page = ProductsPage(authenticated_page)
        products_page.add_first_product_to_cart()
        products_page.add_second_product_to_cart()
        expect(authenticated_page.locator(products_page.CART_BADGE)).to_have_text("2")

    @pytest.mark.edge_case
    @pytest.mark.xfail(strict=False, reason="Session expiration cannot be reliably simulated in this environment")
    def test_session_expiration(self, authenticated_page):
        products_page = ProductsPage(authenticated_page)
        # Session expiry is not controllable in this live demo environment.
        assert False, "Session expiration flow requires environment control not available here"