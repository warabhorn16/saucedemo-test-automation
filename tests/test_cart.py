import pytest
from playwright.sync_api import expect
from pages.cart_page import CartPage

@pytest.mark.cart
def test_tc_cart_001_able_to_remove_a_product_from_the_cart_when_user_clicks_remove_on_the_cart_page(
    products_page
):
    product_name = products_page.add_product_to_cart()

    products_page.open_cart()

    cart_page = CartPage(products_page.page)

    cart_page.remove_product()

    cart_product_names = cart_page.get_product_names()

    assert product_name not in cart_product_names

@pytest.mark.cart
def test_tc_cart_002_verify_that_the_cart_is_empty_after_user_removes_all_products(
    products_page
):
    
    products_page.add_multiple_products_to_cart(2)

    products_page.open_cart()

    cart_page = CartPage(products_page.page)

    cart_page.remove_all_products()

    cart_product_names = cart_page.get_product_names()

    assert cart_product_names == []

@pytest.mark.cart
def test_tc_cart_003_able_to_return_to_the_products_page_when_user_clicks_continue_shopping(
    products_page
):
    products_page.open_cart()

    cart_page = CartPage(products_page.page)

    cart_page.continue_shopping()

    expect(products_page.products_title).to_be_visible()
    expect(products_page.page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

@pytest.mark.cart
def test_tc_cart_004_able_to_proceed_to_checkout_when_user_clicks_checkout_from_the_cart_page(
    products_page
):
    products_page.add_product_to_cart()

    products_page.open_cart()

    cart_page = CartPage(products_page.page)

    cart_page.checkout()

    expect(products_page.page.get_by_text("Checkout: Your Information")).to_be_visible()
    expect(products_page.page).to_have_url(
        "https://www.saucedemo.com/checkout-step-one.html"
    )

@pytest.mark.cart
def test_tc_cart_005_verify_that_cart_items_persist_when_user_navigates_between_the_products_and_cart_pages(
    products_page
):
    product_name = products_page.add_product_to_cart()

    products_page.open_cart()

    cart_page = CartPage(products_page.page)

    cart_page.continue_shopping()

    products_page.open_cart()

    cart_page = CartPage(products_page.page)

    cart_product_names = cart_page.get_product_names()

    assert product_name in cart_product_names





