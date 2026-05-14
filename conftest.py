"""Pytest configuration and fixtures for Playwright tests."""
import pytest
import os
from playwright.sync_api import Browser, BrowserContext, Page
from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getini('base_url') or os.environ.get("BASE_URL", "https://www.saucedemo.com/")


@pytest.fixture
def browser_context(browser: Browser) -> BrowserContext:
    context = browser.new_context(record_video_dir="reports/videos/")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    context.tracing.stop(path="reports/trace.zip")
    context.close()


@pytest.fixture
def page(browser_context: BrowserContext, request) -> Page:
    page = browser_context.new_page()
    yield page
    # if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
    #     page.screenshot(path=f"reports/failure-{request.node.name}.png", full_page=True)
    page.close()


@pytest.fixture
def authenticated_page(page: Page, base_url: str) -> Page:
    login_page = LoginPage(page)
    login_page.navigate_to(base_url)
    login_page.login("standard_user", "secret_sauce")
    return page


@pytest.fixture(scope="session", autouse=True)
def reports_dir():
    os.makedirs("reports", exist_ok=True)
    os.makedirs("reports/videos", exist_ok=True)
