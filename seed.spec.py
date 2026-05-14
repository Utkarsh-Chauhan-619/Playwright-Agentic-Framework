import pytest
from playwright.async_api import async_playwright


class TestGroup:
    @pytest.mark.asyncio
    async def test_seed(self, page):
        """Seed test - generate code here."""
        pass
