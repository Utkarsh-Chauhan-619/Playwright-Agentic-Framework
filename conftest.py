"""Pytest configuration and fixtures for Playwright tests."""
import pytest
import os
import shutil
from pathlib import Path
from playwright.sync_api import BrowserContext, Page
from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getini('base_url') or os.environ.get("BASE_URL", "https://www.saucedemo.com/")


@pytest.fixture(scope="session", autouse=True)
def reports_dir():
    os.makedirs("reports", exist_ok=True)
    os.makedirs("reports/videos", exist_ok=True)


@pytest.fixture
def browser_context(browser):
    """Create a browser context with optimized timeouts for fast test execution."""
    context = browser.new_context()
    # Set shorter default timeout for faster failure detection (5 seconds instead of 30)
    context.set_default_timeout(5000)
    context.set_default_navigation_timeout(5000)
    yield context
    context.close()


@pytest.fixture
def page(browser_context: BrowserContext) -> Page:
    """Create a new page in the browser context."""
    page = browser_context.new_page()
    yield page
    page.close()


@pytest.fixture
def authenticated_page(page: Page, base_url: str) -> Page:
    """Create an authenticated page by logging in."""
    login_page = LoginPage(page)
    login_page.navigate_to(base_url)
    login_page.login("standard_user", "secret_sauce")
    return page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshot for failed tests."""
    outcome = yield
    rep = outcome.get_result()
    
    # Only process after the test call completes
    if rep.when == "call" and rep.failed:
        try:
            page = item.funcargs.get('page')
            if page:
                # Capture screenshot for failed test
                screenshot_path = f"reports/failure-{item.name}.png"
                page.screenshot(path=screenshot_path, full_page=True)
                print(f"\nScreenshot saved to: {screenshot_path}")
        except Exception as e:
            print(f"Warning: Could not capture screenshot for failed test {item.name}: {e}")


