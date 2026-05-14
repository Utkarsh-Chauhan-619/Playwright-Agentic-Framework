# tests/test_login.py
import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage

class TestLogin:

    @pytest.mark.smoke
    def test_successful_login(self, page, base_url):
        login_page = LoginPage(page)
        login_page.navigate_to(base_url)
        login_page.login("standard_user", "secret_sauce")
        expect(page).to_have_url(f"{base_url}/inventory.html")

    @pytest.mark.regression
    def test_invalid_login_credentials(self, page, base_url):
        login_page = LoginPage(page)
        login_page.navigate_to(base_url)
        login_page.login("invalid_user", "wrong_password")
        expect(page.locator(login_page.ERROR_MESSAGE)).to_contain_text("Username and password do not match any user in this service")