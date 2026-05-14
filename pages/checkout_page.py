# pages/checkout_page.py
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class CheckoutPage(BasePage):
    URL_STEP_ONE = "/checkout-step-one.html"
    URL_STEP_TWO = "/checkout-step-two.html"
    URL_COMPLETE = "/checkout-complete.html"

    # Selectors
    FIRST_NAME = "[data-test=\"firstName\"]"
    LAST_NAME = "[data-test=\"lastName\"]"
    ZIP_CODE = "[data-test=\"postalCode\"]"
    CONTINUE_BUTTON = "[data-test=\"continue\"]"
    FINISH_BUTTON = "[data-test=\"finish\"]"
    ERROR_MESSAGE = "[data-test=\"error\"]"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def fill_customer_info(self, first_name: str, last_name: str, zip_code: str) -> None:
        self.page.fill(self.FIRST_NAME, first_name)
        self.page.fill(self.LAST_NAME, last_name)
        self.page.fill(self.ZIP_CODE, zip_code)
        self.page.click(self.CONTINUE_BUTTON)
        # Wait for navigation to checkout step two
        self.page.wait_for_load_state("networkidle")

    def click_finish(self) -> None:
        self.page.click(self.FINISH_BUTTON)