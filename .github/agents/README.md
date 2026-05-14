# Playwright Agentic Framework - Agent Instructions

This directory contains agent configuration files for the Playwright Agentic Framework. All agents are now configured to work with **Python** and **pytest** for test generation, planning, and debugging.

## Available Agents

### 1. playwright-test-planner
**Purpose:** Creates comprehensive test plans by exploring web applications

**Capabilities:**
- Navigates and explores web interfaces
- Identifies user flows and critical paths
- Designs test scenarios for happy paths, edge cases, and error handling
- Creates structured test plans in Markdown format
- Outputs plans suitable for test generation

**Output Format:** Markdown test plan file with:
- Feature overview
- Test suites grouped by functionality
- Individual test scenarios with steps
- Expected outcomes for each step
- Seed file references (e.g., `tests/seed.spec.py`)

**Language:** Python/pytest (test plans are language-agnostic)

### 2. playwright-test-generator
**Purpose:** Generates Python/pytest test code from test plans

**Capabilities:**
- Reads test plans created by the planner
- Sets up page and browser contexts for testing
- Executes test steps interactively using Playwright
- Generates clean, readable test code
- Outputs class-based pytest tests with async support

**Output Format:** Python test file (`.spec.py`) containing:
```python
import pytest
from playwright.async_api import async_playwright

class TestFeatureName:
    @pytest.mark.asyncio
    async def test_scenario_name(self, page):
        # Test implementation
        await page.goto("...")
        await page.click("...")
```

**Key Features:**
- Uses pytest fixtures for page management
- Async/await syntax with `@pytest.mark.asyncio`
- Automatic page fixture injection
- Comment-driven step documentation
- Best practices from recorded interactions

### 3. playwright-test-healer
**Purpose:** Debugs and fixes failing Playwright tests

**Capabilities:**
- Lists and runs all tests to identify failures
- Debugs individual test failures step-by-step
- Analyzes error details and page context
- Provides root cause analysis
- Edits test code to fix issues

**Debugging Approach:**
1. Runs all tests to identify failures
2. Debugs each failing test individually
3. Examines errors, selectors, and timing issues
4. Fixes test code to resolve issues
5. Verifies fixes with test re-execution

**Language Support:** Python/pytest
- Handles pytest exceptions and assertions
- Uses `@pytest.mark.skip()` for known issues
- Updates Python syntax as needed

## MCP Server Configuration

All agents use the `playwright-test` MCP server configured in `.vscode/mcp.json`:

```json
"playwright-test": {
  "type": "stdio",
  "command": "python",
  "args": ["-m", "playwright", "run-test-mcp-server"]
}
```

This configuration:
- Executes Python-based Playwright tests
- Provides MCP tools for test generation and debugging
- Supports pytest test discovery and execution

## Using the Agents

 Debug

1. **Create Test Plans**
   - Use `playwright-test-planner` agent
   - Specify the application URL to test
   - Agent explores and creates comprehensive plans

2. **Generate Test Code**
   - Use `playwright-test-generator` agent
   - Provide test plan and test scenario name
   - Agent generates Python/pytest test file

3. **Debug Failing Tests**
   - Use `playwright-test-healer` agent
   - Runs tests and identifies failures
   - Fixes test code automatically

## Agent Models

- **playwright-test-planner:** Claude Sonnet 4.6 (comprehensive exploration)
- **playwright-test-generator:** Claude Haiku 4.5 (focused code generation)
- **playwright-test-healer:** Claude Sonnet 4.6 (complex debugging)

## Test Execution

Generated tests run with:
```bash
# Install dependencies first
pip install -r requirements.txt
playwright install

# Run all tests
pytest

# Run specific test
pytest tests/your_test.spec.py::TestClass::test_method

# Run with options
pytest -v --headless=false
```

## Framework Structure

```
.github/
  agents/
    playwright-test-generator.agent.md
    playwright-test-planner.agent.md
    playwright-test-healer.agent.md
    README.md (this file)
  workflows/
    ...

.vscode/
  mcp.json (MCP server configuration)

conftest.py (pytest fixtures)
pytest.ini (pytest configuration)
requirements.txt (Python dependencies)
seed.spec.py (base test file)
tests/ (generated test files)
specs/ (test plans)
pages/ (optional: page objects)
```

## Key Notes

- All agents are configured for **Python 3.8+**
- Tests use **pytest** with async support via **pytest-asyncio**
- Playwright automation uses the **async API** (`from playwright.async_api import`)
- Tests are discovered from `*.spec.py` files in the `tests/` directory
- Fixtures are centrally managed in `conftest.py`

## For More Information

- See `README.md` in the framework root for setup and usage
 Python migration details
- See `specs/README.md` for test plan format guidelines
