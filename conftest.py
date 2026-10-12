import pytest

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

    # ตรวจสอบว่าล็อกอินสำเร็จและหน้า Products โหลดแล้ว
    page.get_by_text("Products", exact=True).wait_for(
        state="visible"
    )

    return ProductsPage(page)

