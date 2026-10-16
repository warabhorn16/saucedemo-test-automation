# SauceDemo UI Test Automation

[![Playwright UI Tests](https://github.com/warabhorn16/saucedemo-test-automation/actions/workflows/tests.yml/badge.svg)](https://github.com/warabhorn16/saucedemo-test-automation/actions/workflows/tests.yml)

A UI test automation portfolio project built with **Python, Playwright, and Pytest** to validate the core shopping workflows of the SauceDemo web application.

This project demonstrates practical QA Automation skills, including test case design, Page Object Model (POM), reusable test components, test data management, regression testing, failure screenshot capture, HTML test reporting, and Continuous Integration (CI) with GitHub Actions.

In addition to traditional UI automation, this project explores **AI-assisted browser testing using Playwright MCP and GitHub Copilot Agent**. This allows an AI agent to interact with the browser, inspect page elements and browser states, perform user interactions, and evaluate observed behavior against expected results.

## Project Overview

| Item | Details |
|---|---|
| Project Type | Web UI Test Automation |
| Application Under Test | [SauceDemo](https://www.saucedemo.com/) |
| Programming Language | Python |
| Automation Framework | Playwright |
| Test Framework | Pytest |
| Design Pattern | Page Object Model (POM) |
| Test Data Management | Separate test data modules |
| Test Reporting | pytest-html |
| CI/CD | GitHub Actions |
| Browser | Chromium |
| Total Automated Test Cases | 51 |
| AI-Assisted Testing | Playwright MCP and GitHub Copilot Agent |

## Objectives

- Automate critical end-to-end shopping workflows.
- Validate application behavior using positive and negative test scenarios.
- Apply the Page Object Model to improve code organization and maintainability.
- Reuse fixtures and test data across test modules.
- Capture screenshots when test execution fails.
- Generate HTML test reports for reviewing test results.
- Execute automated regression tests through GitHub Actions.
- Explore AI-assisted browser testing using Playwright MCP.
- Evaluate test outcomes based on browser evidence and expected results.

## Test Coverage

The project contains **51 automated test cases** across five test modules.

| Test Module | Test Cases | Coverage |
|---|---:|---|
| Login | 9 | Authentication, valid and invalid credentials, and login validation |
| Products | 18 | Product listing, product information, sorting, and product interactions |
| Cart | 5 | Adding and removing products, cart contents, and cart navigation |
| Checkout | 14 | Checkout information, form validation, order review, and order completion |
| Menu | 5 | Navigation menu, application links, logout, and application state reset |
| **Total** | **51** | |

The test suite covers successful workflows and relevant error-handling scenarios to validate expected application behavior.

## Test Case Portfolio

Test cases are documented in an Excel workbook to support test planning, execution, and review.

The workbook includes:

- Test Case ID and test module
- Test scenario and preconditions
- Test steps and test data
- Expected results
- Actual results and execution status
- Priority and automation status
- Evidence and notes

**[View Test Case Portfolio (Excel)](docs/SauceDemo_Test_Cases.xlsx)**

## Tech Stack

- **Python** — Programming language for test automation.
- **Playwright** — Browser automation and UI interaction.
- **Pytest** — Test execution, assertions, fixtures, and test organization.
- **pytest-html** — HTML test report generation.
- **Page Object Model (POM)** — Separates page locators and actions from test logic.
- **Git and GitHub** — Version control and source code management.
- **GitHub Actions** — Automated test execution on pushes and pull requests.
- **Playwright MCP** — Provides browser interaction tools that an AI agent can use.
- **GitHub Copilot Agent** — AI agent used with Playwright MCP for browser exploration and interactive testing.

## Project Structure

```text
saucedemo-test-automation/
├── .github/
│   └── workflows/
│       └── tests.yml
├── .playwright-mcp/
│   └── MCP-generated browser files
├── pages/
│   ├── base_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── login_page.py
│   ├── menu_page.py
│   ├── order_complete_page.py
│   ├── order_review_page.py
│   ├── product_detail_page.py
│   └── products_page.py
├── test_data/
│   ├── checkout_data.py
│   └── login_data.py
├── tests/
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_login.py
│   ├── test_menu.py
│   └── test_products.py
├── docs/
│   └── SauceDemo_Test_Cases.xlsx
├── .gitignore
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt
```

The `.playwright-mcp/` directory contains files generated during MCP-assisted browser exploration and testing. Review its contents before committing them to GitHub, and exclude temporary files, sensitive information, or unnecessary session artifacts.

## Test Automation Design

### 1. Page Object Model (POM)

The project uses the Page Object Model to separate page-specific locators and interactions from test logic.

Each page class encapsulates the elements and actions associated with a particular page or workflow.

Benefits:

- Reduces duplicated locator and interaction code.
- Makes test cases easier to read and maintain.
- Allows page-level changes to be managed in one place.
- Encourages reusable automation components.

### 2. Pytest Fixtures

Shared test setup is managed through Pytest fixtures in `conftest.py`.

Examples include:

- `login_page` — Opens the application and provides a `LoginPage` object.
- `products_page` — Logs in with valid test credentials and provides a `ProductsPage` object.

Fixtures reduce repetitive setup code and keep test cases focused on the behavior being tested.

### 3. Test Data Management

Test data is organized into separate modules under `test_data/`.

This separates test inputs from test logic, making test data easier to reuse, maintain, and update.

### 4. Failure Screenshot Capture

A custom Pytest reporting hook in `conftest.py` captures a full-page screenshot when a test fails during its call phase.

Screenshots are saved under:

```text
test-results/screenshots/
```

These screenshots provide visual evidence to support debugging and failure investigation.

### 5. HTML Test Reporting

The project uses `pytest-html` to generate a self-contained HTML report containing test execution results.

The report can be generated locally and opened in a browser for review.

## AI-Assisted Testing with Playwright MCP

This project explores **Playwright MCP and GitHub Copilot Agent** alongside the existing Python and Pytest automation framework.

Playwright MCP provides browser interaction tools that an AI agent can use to inspect and interact with a web application.

The AI-assisted browser testing workflow includes:

- **Browser Navigation:** Opening the application and navigating to the target page.
- **Page Inspection:** Reviewing page snapshots and identifying interactive elements.
- **Browser Interaction:** Filling form fields and clicking buttons.
- **State Verification:** Observing page states, URLs, and application responses after interactions.
- **Expected Result Validation:** Comparing observed behavior against the expected outcome of a test scenario.
- **Evidence-Based Reporting:** Reviewing tool calls, tool results, and page snapshots to support test conclusions.

This exploration provides practical experience in using AI agents for browser-based testing, writing clear test instructions, defining expected results, and evaluating evidence rather than relying solely on AI-generated summaries.

### Relationship to the Existing Automation Framework

The project uses two complementary approaches:

**Python + Playwright + Pytest**

A structured, executable UI automation suite designed for repeatable testing and regression testing.

**Playwright MCP + GitHub Copilot Agent**

An AI-assisted approach for browser exploration, interactive test execution, and observation of application behavior.

MCP-assisted test runs are separate from the 51 Pytest automated test cases. They are not counted as additional Pytest tests unless the scenarios are separately implemented in the executable test suite.

The `.playwright-mcp/` directory contains files generated during MCP-assisted browser exploration and testing. These files are separate from the main Python test modules.

## Continuous Integration with GitHub Actions

GitHub Actions is configured to run the automated test suite when code is pushed to the `main` branch or when a pull request targets `main`.

The workflow performs the following steps:

1. Checks out the repository.
2. Sets up Python.
3. Installs project dependencies.
4. Installs Chromium and its required system dependencies.
5. Runs the Pytest test suite.
6. Uploads failure screenshot artifacts when the workflow fails, according to the workflow configuration.

**Workflow configuration:** `.github/workflows/tests.yml`

[View GitHub Actions Workflow Runs](https://github.com/warabhorn16/saucedemo-test-automation/actions)

## Getting Started

### Prerequisites

- Python 3.13 or a compatible Python version
- Git
- Internet access to install dependencies and access SauceDemo

### 1. Clone the Repository

```bash
git clone https://github.com/warabhorn16/saucedemo-test-automation.git
cd saucedemo-test-automation
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
playwright install chromium
```

## Running Tests

### 1. Run All Tests

```bash
pytest -v
```

### 2. Run a Specific Test Module

Run login tests:

```bash
pytest tests/test_login.py -v
```

Run checkout tests:

```bash
pytest tests/test_checkout.py -v
```

### 3. Run Tests with a Visible Browser

```bash
pytest -v --headed
```

### 4. Generate an HTML Test Report

Create the reports directory if it does not exist:

```bash
mkdir -p reports
```

Generate a self-contained HTML report:

```bash
pytest -v --html=reports/report.html --self-contained-html
```

Open `reports/report.html` in a browser to review the test results.

## Test Results and Artifacts

Test execution results can be reviewed through the local Pytest output and generated HTML report.

Failure screenshots are saved locally under `test-results/screenshots/`.

The GitHub Actions workflow is intended to upload failure screenshot artifacts when a workflow fails. Refer to the workflow run to verify artifact availability.

Test reports and screenshots are not committed to the repository by default.

## Skills Demonstrated

- Python programming for test automation
- Web UI automation using Playwright
- Test case design and regression testing
- Positive and negative test scenarios
- Page Object Model implementation
- Pytest fixtures and test organization
- Test data separation and reuse
- HTML test reporting and failure investigation
- Browser inspection and evidence-based evaluation
- AI-assisted testing with Playwright MCP
- Git and GitHub version control
- CI automation using GitHub Actions

## Author

**QA Automation Portfolio Project**

[GitHub Repository](https://github.com/warabhorn16/saucedemo-test-automation)