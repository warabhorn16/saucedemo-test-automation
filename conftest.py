
import pytest
from pathlib import Path

from pages.login_page import LoginPage
from pages.products_page import ProductsPage

from test_data.login_data import (
    VALID_USERNAME,
    VALID_PASSWORD
)


@pytest.fixture
def login_page(page):
    page.goto("https://www.saucedemo.com/")

    return LoginPage(page)


@pytest.fixture
def products_page(page):
    page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(page)
    login_page.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )

    page.get_by_text("Products", exact=True).wait_for(
        state="visible"
    )

    return ProductsPage(page)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    page = item.funcargs.get("page")

    if page is None or page.is_closed():
        return

    screenshot_dir = Path("test-results/screenshots")
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    screenshot_path = screenshot_dir / f"{item.name}.png"

    try:
        page.screenshot(
            path=str(screenshot_path),
            full_page=True
        )
        print(f"\nFailure screenshot saved: {screenshot_path}")
    except Exception as exc:
        print(f"\nCould not save failure screenshot: {exc}")