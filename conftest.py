"""Pytest configuration and fixtures for Playwright tests."""
import pytest
from playwright.async_api import async_playwright


@pytest.fixture
async def playwright_instance():
    """Provide a Playwright instance for tests."""
    async with async_playwright() as pw:
        yield pw


@pytest.fixture
async def browser(playwright_instance):
    """Provide a browser instance for tests."""
    browser = await playwright_instance.chromium.launch()
    yield browser
    await browser.close()


@pytest.fixture
async def context(browser):
    """Provide a browser context for tests."""
    context = await browser.new_context()
    yield context
    await context.close()


@pytest.fixture
async def page(context):
    """Provide a page instance for tests."""
    page = await context.new_page()
    yield page
    await page.close()
