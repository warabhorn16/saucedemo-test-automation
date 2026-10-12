[![Playwright UI Tests](https://github.com/warabhorn16/saucedemo-test-automation/actions/workflows/tests.yml/badge.svg)](https://github.com/warabhorn16/saucedemo-test-automation/actions/workflows/tests.yml)

# SauceDemo UI Test Automation

A UI test automation project built with **Python, Playwright, and Pytest** to test the core shopping workflows of the SauceDemo web application.

This project demonstrates practical QA Automation skills, including test case design, Page Object Model (POM), reusable test components, automated regression testing, failure screenshot capture, HTML test reporting, and Continuous Integration (CI) with GitHub Actions.

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
| Test Reporting | Pytest HTML |
| CI/CD | GitHub Actions |
| Browser | Chromium |
| Total Test Cases | 51 |

## Objectives

- Automate critical end-to-end shopping workflows.
- Validate application behavior through positive and negative test scenarios.
- Apply the Page Object Model to improve code organization and maintainability.
- Reuse fixtures and test data across test modules.
- Capture screenshots when test execution fails.
- Generate HTML test reports for reviewing test results.
- Run automated regression tests through GitHub Actions.

## Application Under Test

SauceDemo is a sample e-commerce web application used to practice software testing and automation.

The project covers the main user journey, from authentication and product browsing to shopping cart management and checkout.

Application URL: https://www.saucedemo.com/

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

The test suite is designed to verify both successful workflows and relevant error-handling scenarios.

## Tech Stack

- **Python** — Programming language for test automation.
- **Playwright** — Browser automation and UI interaction.
- **Pytest** — Test execution, assertions, fixtures, and test organization.
- **Pytest HTML** — HTML test report generation.
- **Page Object Model (POM)** — Separates page locators and actions from test cases.
- **Git and GitHub** — Version control and source code management.
- **GitHub Actions** — Automated test execution on pushes and pull requests.

## Project Structure

```text
saucedemo-test-automation/
├── .github/
│   └── workflows/
│       └── tests.yml
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
├── .gitignore
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt
```

**Note:** Test reports and failure screenshots are generated during test execution and are not committed to the repository by default.

## Test Automation Design

### 1. Page Object Model (POM)

The project uses the Page Object Model to separate page-specific locators and interactions from test logic.

Each page class encapsulates the actions and elements associated with a particular page or workflow.

Benefits:
- Reduces duplicated locator and interaction code.
- Makes test cases easier to read and maintain.
- Allows page-level changes to be managed in one place.
- Encourages reusable automation components.

### 2. Pytest Fixtures

Shared setup is managed through Pytest fixtures in `conftest.py`.

Examples include:
- `login_page` — Opens the application and provides a LoginPage object.
- `products_page` — Logs in with valid test credentials and provides a ProductsPage object.

This approach reduces repetitive setup code and helps keep test cases focused on the behavior being tested.

### 3. Test Data Management

Test data is organized into separate modules under `test_data/`.

This separates test inputs from test logic and makes it easier to reuse and update test data.

### 4. Failure Screenshot Capture

A custom Pytest reporting hook in `conftest.py` captures a full-page screenshot when a test fails during its call phase.

Screenshots are saved under:

```text
test-results/screenshots/
```

This provides additional visual evidence for debugging failed test cases.

The screenshot capture feature has been tested locally. The GitHub Actions workflow is also configured to upload failure screenshots as artifacts when a workflow fails.

### 5. HTML Test Reporting

The project uses `pytest-html` to generate an HTML report containing test execution results.

The report can be generated locally and reviewed in a browser.

## Continuous Integration with GitHub Actions

GitHub Actions is configured to run the automated test suite when code is pushed to the `main` branch or when a pull request targets `main`.

The workflow performs the following steps:

1. Checks out the repository.
2. Sets up Python.
3. Installs project dependencies.
4. Installs Chromium and its required system dependencies.
5. Runs the Pytest suite.
6. Uploads failure screenshot artifacts if the workflow fails.

Workflow configuration:

```text
.github/workflows/tests.yml
```

### Latest Verified CI Result

The latest successful GitHub Actions run completed all 51 tests.

| Metric | Result |
|---|---|
| Tests Passed | 51 |
| Tests Failed | 0 |
| Test Execution Time | Approximately 25 seconds |
| CI Status | Passed |

The results above reflect the verified successful run. Future executions may produce different results.

## Getting Started

### Prerequisites

Install the following before running the project:

- Python 3.13 or a compatible Python version.
- Git.
- A terminal.
- Internet access to install dependencies and access SauceDemo.

### 1. Clone the Repository

```bash
git clone https://github.com/warabhorn16/saucedemo-test-automation.git
```

### 2. Navigate to the Project Directory

```bash
cd saucedemo-test-automation
```

### 3. Create a Virtual Environment

```bash
python3 -m venv .venv
```

### 4. Activate the Virtual Environment

For macOS or Linux:

```bash
source .venv/bin/activate
```

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 6. Install the Playwright Browser

For Chromium:

```bash
playwright install chromium
```

### 7. Run All Tests

```bash
pytest -v
```

### 8. Run a Specific Test Module

Run login tests:

```bash
pytest tests/test_login.py -v
```

Run checkout tests:

```bash
pytest tests/test_checkout.py -v
```

### 9. Generate an HTML Test Report

Create the reports directory if it does not exist:

```bash
mkdir -p reports
```

Generate a self-contained HTML report:

```bash
pytest -v --html=reports/report.html --self-contained-html
```

Open `reports/report.html` in a browser to review the results.

### 10. Run Tests with a Visible Browser

To observe browser interactions during test execution:

```bash
pytest -v --headed
```

## Example Test Execution

Run the full suite:

```bash
pytest -v
```

Example of a successful test summary:

```text
51 passed
```

The actual execution time and test results may vary depending on the environment and application availability.

## Skills Demonstrated

This project demonstrates practical experience in:

- Python programming for test automation.
- Web UI automation using Playwright.
- Test case design and regression testing.
- Positive and negative test scenarios.
- Page Object Model implementation.
- Pytest fixtures and test organization.
- Test data separation and reuse.
- HTML test reporting.
- Failure screenshot capture.
- Git and GitHub version control.
- CI automation using GitHub Actions.
- Debugging and investigating failed tests.

## Future Improvements

Potential enhancements for future iterations include:

- API test automation.
- Cross-browser testing with Chromium, Firefox, and WebKit.
- Test result summaries and richer CI reporting.
- Screenshot and trace collection for debugging.
- Additional edge cases and boundary-value scenarios.
- Improved test execution efficiency and parallelization.

## Author

**QA Automation Portfolio Project**

GitHub Repository: [saucedemo-test-automation](https://github.com/warabhorn16/saucedemo-test-automation)
