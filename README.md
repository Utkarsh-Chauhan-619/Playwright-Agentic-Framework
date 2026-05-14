# Playwright Agentic Framework - Python/pytest Edition

This is an agentic test automation framework that uses AI agents to generate, plan, and debug Python-based Playwright tests with pytest.

## Framework Overview

The framework consists of 3 specialized agents:

1. **Playwright Test Planner** - Creates comprehensive test plans by exploring the application
2. **Playwright Test Generator** - Generates Python/pytest test code based on test plans
3. **Playwright Test Healer** - Debugs and fixes failing tests

## Prerequisites

- Python 3.8+
- pip or venv for dependency management

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install Playwright browsers:
```bash
playwright install
```

## Project Structure

- **specs/** - Test plans created by the planner agent
- **tests/** - Generated Python test files (pytest)
- **pages/** - Page object models or helper utilities
- **seed.spec.py** - Base seed test file for test generation
- **requirements.txt** - Python dependencies

## Running Tests

To run all tests:
```bash
pytest
```

To run specific test file:
```bash
pytest tests/your_test.spec.py
```

To run with verbose output:
```bash
pytest -v
```

To run with headless browser:
```bash
pytest --headed=false
```

## Test File Format

Generated test files follow this pattern:

```python
import pytest
from playwright.async_api import async_playwright


class TestYourFeature:
    @pytest.mark.asyncio
    async def test_your_scenario(self, page):
        # Test code here
        await page.goto("https://example.com")
        await page.click("button")
        assert await page.is_visible("text=Success")
```

## Configuration

- MCP configuration: `.vscode/mcp.json`
- Agent instructions: `.github/agents/`

## Notes

- All tests are async and use pytest-asyncio
- Tests are automatically instrumented with Playwright
- The framework is designed for use with GitHub Copilot agents
