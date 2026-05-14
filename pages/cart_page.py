# pages/cart_page.py
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class CartPage(BasePage):
    URL = "/cart.html"

    # Selectors
    REMOVE_BACKPACK = "[data-test=\"remove-sauce-labs-backpack\"]"
    CHECKOUT_BUTTON = "[data-test=\"checkout\"]"
    CART_BADGE = "[data-test=\"shopping-cart-badge\"]"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def navigate_to(self, base_url: str) -> None:
        self.navigate(self.build_url(base_url, self.URL))

    def remove_first_product(self) -> None:
        self.page.click(self.REMOVE_BACKPACK)

    def click_checkout(self) -> None:
        self.page.click(self.CHECKOUT_BUTTON)