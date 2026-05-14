# pages/base_page.py
from urllib.parse import urljoin
from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def build_url(self, base_url: str, path: str) -> str:
        return urljoin(base_url.rstrip('/') + '/', path.lstrip('/'))

    def navigate(self, url: str) -> None:
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    def wait_for_element(self, selector: str, timeout: int = 10000):
        return self.page.wait_for_selector(selector, timeout=timeout)

    def get_title(self) -> str:
        return self.page.title()

    def take_screenshot(self, name: str) -> None:
        self.page.screenshot(path=f"reports/{name}.png", full_page=True)