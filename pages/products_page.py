# pages/products_page.py
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class ProductsPage(BasePage):
    URL = "/inventory.html"

    # Selectors
    ADD_TO_CART_BACKPACK = "[data-test=\"add-to-cart-sauce-labs-backpack\"]"
    ADD_TO_CART_BIKE_LIGHT = "[data-test=\"add-to-cart-sauce-labs-bike-light\"]"
    CART_ICON = "[data-test=\"shopping-cart-link\"]"
    CART_BADGE = "[data-test=\"shopping-cart-badge\"]"
    MENU_BUTTON = "#react-burger-menu-btn"
    LOGOUT_LINK = "[data-test=\"logout-sidebar-link\"]"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def navigate_to(self, base_url: str) -> None:
        self.navigate(self.build_url(base_url, self.URL))

    def add_first_product_to_cart(self) -> None:
        self.page.click(self.ADD_TO_CART_BACKPACK)

    def add_second_product_to_cart(self) -> None:
        self.page.click(self.ADD_TO_CART_BIKE_LIGHT)

    def get_cart_badge_count(self) -> str:
        return self.page.text_content(self.CART_BADGE)

    def click_cart_icon(self) -> None:
        self.page.click(self.CART_ICON)

    def logout(self) -> None:
        #self.page.wait_for_selector(self.MENU_BUTTON, timeout=10000)
        self.page.click(self.MENU_BUTTON)
        #self.page.wait_for_selector(self.LOGOUT_LINK, timeout=10000)
        self.page.click(self.LOGOUT_LINK)
        #self.page.wait_for_load_state("networkidle")