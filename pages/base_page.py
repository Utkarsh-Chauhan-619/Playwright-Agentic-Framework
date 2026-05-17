# pages/base_page.py
from urllib.parse import urljoin
from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def build_url(self, base_url: str, path: str) -> str:
        return urljoin(base_url.rstrip('/') + '/', path.lstrip('/'))

    def navigate(self, url: str) -> None:
        # Use 'commit' for fastest navigation (as soon as response is received)
        # Reduced timeout to 5 seconds for faster failure detection
        self.page.goto(url, wait_until="commit", timeout=5000)

    def get_title(self) -> str:
        return self.page.title()

    def take_screenshot(self, name: str) -> None:
        self.page.screenshot(path=f"reports/{name}.png", full_page=True)