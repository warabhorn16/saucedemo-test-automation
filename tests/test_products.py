
import pytest
from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.product_detail_page import ProductDetailPage


@pytest.mark.products
def test_tc_product_001_verify_products_are_displayed(
    products_page
):
    expect(products_page.products_title).to_be_visible()
    expect(products_page.product_items).to_have_count(6)


@pytest.mark.products
def test_tc_product_002_verify_product_information(
    products_page
):
    product_count = products_page.product_items.count()

    expect(products_page.product_names).to_have_count(product_count)
    expect(products_page.product_descriptions).to_have_count(product_count)
    expect(products_page.product_prices).to_have_count(product_count)
    expect(products_page.product_images).to_have_count(product_count)

    for product_name in products_page.product_names.all():
        expect(product_name).to_be_visible()

    for product_description in products_page.product_descriptions.all():
        expect(product_description).to_be_visible()

    for product_price in products_page.product_prices.all():
        expect(product_price).to_be_visible()

    for product_image in products_page.product_images.all():
        expect(product_image).to_be_visible()


@pytest.mark.products
def test_tc_product_003_sort_products_by_name_ascending(
    products_page
):
    products_page.sort_by_name_ascending()

    actual_names = products_page.product_names.all_text_contents()
    expected_names = sorted(actual_names)

    assert actual_names == expected_names


@pytest.mark.products
def test_tc_product_004_sort_products_by_name_descending(
    products_page
):
    products_page.sort_by_name_descending()

    actual_names = products_page.product_names.all_text_contents()
    expected_names = sorted(actual_names, reverse=True)

    assert actual_names == expected_names


@pytest.mark.products
def test_tc_product_005_sort_products_by_price_ascending(
    products_page
):
    products_page.sort_by_price_ascending()

    actual_prices = [
        float(price.replace("$", ""))
        for price in products_page.product_prices.all_text_contents()
    ]

    expected_prices = sorted(actual_prices)

    assert actual_prices == expected_prices


@pytest.mark.products
def test_tc_product_006_sort_products_by_price_descending(
    products_page
):
    products_page.sort_by_price_descending()

    actual_prices = [
        float(price.replace("$", ""))
        for price in products_page.product_prices.all_text_contents()
    ]

    expected_prices = sorted(actual_prices, reverse=True)

    assert actual_prices == expected_prices


@pytest.mark.products
def test_tc_product_007_add_product_to_cart(
    products_page
):
    product_name = products_page.add_product_to_cart()

    products_page.open_cart()

    cart_page = CartPage(products_page.page)
    cart_product_names = cart_page.get_product_names()

    assert product_name in cart_product_names


@pytest.mark.products
def test_tc_product_008_add_multiple_products_to_cart(
    products_page
):
    selected_product_names = (
        products_page.add_multiple_products_to_cart(2)
    )

    products_page.open_cart()

    cart_page = CartPage(products_page.page)
    cart_product_names = cart_page.get_product_names()

    assert all(
        product_name in cart_product_names
        for product_name in selected_product_names
    )


@pytest.mark.products
def test_tc_product_009_add_to_cart_button_changes_to_remove(
    products_page
):
    remove_button = (
        products_page.add_product_and_get_remove_button()
    )

    expect(remove_button).to_be_visible()


@pytest.mark.products
def test_tc_product_010_remove_product_from_products_page(
    products_page
):
    product_name = products_page.add_product_to_cart()

    products_page.remove_product_from_cart()
    products_page.open_cart()

    products_page.page.wait_for_url("**/cart.html")

    cart_page = CartPage(products_page.page)

    expect(cart_page.cart_title).to_have_text(
        "Your Cart",
        timeout=5000
    )

    cart_product_names = cart_page.get_product_names()

    assert product_name not in cart_product_names


@pytest.mark.products
def test_tc_product_011_navigate_to_cart(
    products_page
):
    products_page.open_cart()

    cart_page = CartPage(products_page.page)

    expect(cart_page.cart_title).to_be_visible()


@pytest.mark.products
def test_tc_product_012_cart_badge_after_adding_products(
    products_page
):
    products_page.add_multiple_products_to_cart(2)

    expect(products_page.cart_badge).to_have_text("2")


@pytest.mark.products
def test_tc_product_013_cart_badge_after_removing_product(
    products_page
):
    products_page.add_multiple_products_to_cart(2)

    products_page.remove_buttons.first.click()

    expect(products_page.cart_badge).to_have_text("1")


@pytest.mark.products
def test_tc_product_014_open_product_detail_page(
    products_page
):
    selected_product_name = products_page.open_product_detail()

    product_detail_page = ProductDetailPage(products_page.page)
    detail_product_name = product_detail_page.get_product_name()

    assert selected_product_name == detail_product_name


@pytest.mark.products
def test_tc_product_015_verify_product_information(
    products_page
):
    selected_products = products_page.get_product_information(1)
    selected_product = selected_products[0]

    products_page.open_product_detail()

    product_detail_page = ProductDetailPage(products_page.page)

    assert (
        selected_product["name"]
        == product_detail_page.get_product_name()
    )

    assert (
        selected_product["description"]
        == product_detail_page.get_product_description()
    )

    assert (
        selected_product["price"]
        == product_detail_page.get_product_price()
    )

    expect(product_detail_page.get_product_image()).to_be_visible()


@pytest.mark.products
def test_tc_product_016_add_product_to_cart_from_product_detail(
    products_page
):
    products_page.open_product_detail()

    product_detail_page = ProductDetailPage(products_page.page)
    product_detail_page.add_to_cart()

    expect(products_page.cart_badge).to_have_text("1")


@pytest.mark.products
def test_tc_product_017_return_to_products_from_product_detail(
    products_page
):
    products_page.open_product_detail()

    product_detail_page = ProductDetailPage(products_page.page)
    product_detail_page.back_to_products()

    expect(products_page.products_title).to_be_visible()


@pytest.mark.products
def test_tc_product_018_remove_product_from_cart_from_product_detail(
    products_page
):
    products_page.open_product_detail()

    product_detail_page = ProductDetailPage(products_page.page)

    product_detail_page.add_to_cart()
    product_detail_page.remove_from_cart()

    expect(products_page.cart_badge).not_to_be_visible()
