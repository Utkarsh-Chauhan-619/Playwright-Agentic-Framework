# pages/login_page.py
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class LoginPage(BasePage):
    URL = "/"

    # Selectors
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test=\"error\"]"  # Assuming this is correct for error

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def navigate_to(self, base_url: str) -> None:
        self.navigate(self.build_url(base_url, self.URL))

    def login(self, username: str, password: str) -> None:
        self.page.wait_for_selector(self.USERNAME_INPUT, timeout=10000)
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)
        self.page.wait_for_load_state("networkidle")

    def get_error_message(self) -> str:
        return self.page.text_content(self.ERROR_MESSAGE)