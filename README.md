# SauceDemo UI Test Automation

A web UI test automation project built with **Python, Playwright, and Pytest** to test core e-commerce workflows on [SauceDemo](https://www.saucedemo.com/).

The project follows the **Page Object Model (POM)** design pattern to separate page interactions from test cases and improve maintainability.

## Project Overview

This project covers the main user journeys of an e-commerce application, including authentication, product browsing, shopping cart operations, checkout, and application navigation.

### Test Results

| Metric | Result |
|---|---:|
| Total Test Cases | 51 |
| Passed | 51 |
| Failed | 0 |
| Errors | 0 |
| Browser | Chromium |

*Results from the latest full regression test run.*

## Tech Stack

- **Language:** Python
- **Browser Automation:** Playwright
- **Test Framework:** Pytest
- **Test Reporting:** pytest-html
- **Design Pattern:** Page Object Model (POM)
- **Browser:** Chromium

## Test Coverage

| Test Suite | Test Cases | Coverage |
|---|---:|---|
| Login | 9 | Valid and invalid credentials, empty fields, locked user |
| Products | 18 | Product information, sorting, cart operations, product details |
| Cart | 5 | Remove products, empty cart, continue shopping, checkout, cart persistence |
| Checkout | 14 | Form validation, order review, quantities, totals, order completion |
| Menu | 5 | Open menu, navigation, logout, reset application state |
| **Total** | **51** | |

## Project Structure

```text
saucedemo/
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
├── reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone warabhorn16/saucedemo-automation
cd saucedemo
```

Replace the placeholder with the actual repository URL after publishing the project to GitHub.

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install the Playwright browser

```bash
playwright install chromium
```

## Running Tests

### Run all test cases

```bash
pytest -v
```

### Run a specific test suite

```bash
pytest tests/test_login.py -v
pytest tests/test_products.py -v
pytest tests/test_cart.py -v
pytest tests/test_checkout.py -v
pytest tests/test_menu.py -v
```

### Generate an HTML test report

```bash
pytest -v --html=reports/regression-report.html --self-contained-html
```

Open the generated report in your browser:

```bash
open reports/regression-report.html
```

The HTML report provides a summary of test execution results and details for individual test cases.

## Framework Design

### Page Object Model (POM)

The project uses the Page Object Model to organize browser interactions into reusable page classes.

- **`pages/`** — Contains page classes, locators, and reusable page interaction methods.
- **`tests/`** — Contains test scenarios and assertions.
- **`test_data/`** — Stores reusable test data.
- **`conftest.py`** — Defines shared Pytest fixtures.
- **`pytest.ini`** — Configures Pytest test discovery and markers.

This structure helps reduce duplicated code and makes test maintenance easier.

## Skills Demonstrated

- UI test automation with Playwright and Python
- Test case design and functional testing
- Positive and negative testing
- Form validation testing
- End-to-end checkout workflow testing
- Reusable Page Object Model design
- Pytest fixtures and test organization
- HTML test report generation
- Regression testing

## Future Improvements

- Add API test automation.
- Add automated screenshots or Playwright traces for failed tests.
- Integrate the test suite with GitHub Actions CI.
- Expand browser coverage where appropriate.
- Improve test data management and test categorization.

## Author

QA Automation Portfolio Project