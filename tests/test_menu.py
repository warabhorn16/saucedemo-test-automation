import pytest
from playwright.sync_api import expect

from pages.menu_page import MenuPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@pytest.mark.menu
def test_tc_menu_001_able_to_open_the_side_menu_when_user_clicks_the_menu_button(products_page):

    menu_page = MenuPage(products_page.page)

    menu_page.open_menu()

    expect(menu_page.all_items_link).to_be_visible()
    expect(menu_page.about_link).to_be_visible()
    expect(menu_page.logout_link).to_be_visible()
    expect(menu_page.reset_app_state_link).to_be_visible()


@pytest.mark.menu
def test_tc_menu_002_able_to_navigate_to_the_products_page_when_user_selects_all_items_from_the_side_menu(products_page):

    menu_page = MenuPage(products_page.page)

    menu_page.open_menu()

    menu_page.click_all_items()

    expect(products_page.products_title).to_be_visible()
    expect(products_page.product_items.first).to_be_visible()

    expect(products_page.page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )


@pytest.mark.menu
def test_tc_menu_003_able_to_navigate_to_the_about_page_when_user_selects_about_from_the_side_menu(products_page):

    menu_page = MenuPage(products_page.page)

    menu_page.open_menu()

    menu_page.click_about()

    expect(products_page.page).to_have_url(
        "https://saucelabs.com/"
    )


@pytest.mark.menu
def test_tc_menu_004_able_to_log_out_when_user_selects_logout_from_the_side_menu(products_page):

    menu_page = MenuPage(products_page.page)

    menu_page.open_menu()

    menu_page.click_logout()

    login_page = LoginPage(products_page.page)

    expect(login_page.username_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()
    expect(login_page.login_button).to_be_visible()

    expect(products_page.page).to_have_url(
        "https://www.saucedemo.com/"
    )


@pytest.mark.menu
def test_tc_menu_005_able_to_reset_the_application_state_when_user_selects_reset_app_state_from_the_side_menu(products_page):

    products_page.add_product_to_cart()

    expect(products_page.cart_badge).to_have_text("1")

    menu_page = MenuPage(products_page.page)

    menu_page.open_menu()

    menu_page.click_reset_app_state()

    expect(products_page.cart_badge).not_to_be_visible()

    products_page.open_cart()

    cart_page = CartPage(products_page.page)

    expect(cart_page.cart_product_names).to_have_count(0)