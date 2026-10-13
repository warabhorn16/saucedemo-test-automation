import pytest
from playwright.sync_api import expect

from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
from pages.order_review_page import OrderReviewPage
from pages.order_complete_page import OrderCompletePage

from test_data.checkout_data import (
    VALID_FIRST_NAME,
    VALID_LAST_NAME,
    VALID_POSTAL_CODE,
    EMPTY_FIRST_NAME,
    EMPTY_LAST_NAME,
    EMPTY_POSTAL_CODE,
)


@pytest.mark.checkout
def test_tc_checkout_001_able_to_proceed_to_the_order_review_when_user_enters_valid_checkout_information(
    products_page
):
    products_page.add_product_to_cart()

    products_page.open_cart()

    cart_page = CartPage(products_page.page)

    cart_page.checkout()

    checkout_page = CheckoutPage(products_page.page)

    checkout_page.enter_first_name(VALID_FIRST_NAME)
    checkout_page.enter_last_name(VALID_LAST_NAME)
    checkout_page.enter_postal_code(VALID_POSTAL_CODE)

    checkout_page.click_continue()

    expect(
        products_page.page.get_by_text("Checkout: Overview")
    ).to_be_visible()

    expect(products_page.page).to_have_url(
        "https://www.saucedemo.com/checkout-step-two.html"
    )


@pytest.mark.checkout
def test_tc_checkout_002_unable_to_continue_checkout_when_user_leaves_the_first_name_field_empty(
    products_page
):
    products_page.add_product_to_cart()

    products_page.open_cart()

    cart_page = CartPage(products_page.page)

    cart_page.checkout()

    checkout_page = CheckoutPage(products_page.page)

    checkout_page.enter_first_name(EMPTY_FIRST_NAME)
    checkout_page.enter_last_name(VALID_LAST_NAME)
    checkout_page.enter_postal_code(VALID_POSTAL_CODE)

    checkout_page.click_continue()

    expect(
        products_page.page.get_by_text(
            "Error: First Name is required"
        )
    ).to_be_visible()

    expect(
        products_page.page.get_by_text(
            "Checkout: Your Information"
        )
    ).to_be_visible()

    expect(products_page.page).to_have_url(
        "https://www.saucedemo.com/checkout-step-one.html"
    )


@pytest.mark.checkout
def test_tc_checkout_003_unable_to_continue_checkout_when_user_leaves_the_last_name_field_empty(
    products_page
):
    products_page.add_product_to_cart()

    products_page.open_cart()

    cart_page = CartPage(products_page.page)

    cart_page.checkout()

    checkout_page = CheckoutPage(products_page.page)

    checkout_page.enter_first_name(VALID_FIRST_NAME)
    checkout_page.enter_last_name(EMPTY_LAST_NAME)
    checkout_page.enter_postal_code(VALID_POSTAL_CODE)

    checkout_page.click_continue()

    expect(
        products_page.page.get_by_text(
            "Error: Last Name is required"
        )
    ).to_be_visible()

    expect(
        products_page.page.get_by_text(
            "Checkout: Your Information"
        )
    ).to_be_visible()

    expect(products_page.page).to_have_url(
        "https://www.saucedemo.com/checkout-step-one.html"
    )


@pytest.mark.checkout
def test_tc_checkout_004_unable_to_continue_checkout_when_user_leaves_the_postal_code_field_empty(
    products_page
):
    products_page.add_product_to_cart()

    products_page.open_cart()

    cart_page = CartPage(products_page.page)

    cart_page.checkout()

    checkout_page = CheckoutPage(products_page.page)

    checkout_page.enter_first_name(VALID_FIRST_NAME)
    checkout_page.enter_last_name(VALID_LAST_NAME)
    checkout_page.enter_postal_code(EMPTY_POSTAL_CODE)

    checkout_page.click_continue()

    expect(
        products_page.page.get_by_text(
            "Error: Postal Code is required"
        )
    ).to_be_visible()

    expect(
        products_page.page.get_by_text(
            "Checkout: Your Information"
        )
    ).to_be_visible()

    expect(products_page.page).to_have_url(
        "https://www.saucedemo.com/checkout-step-one.html"
    )


@pytest.mark.checkout
def test_tc_checkout_005_verify_that_the_order_review_displays_the_selected_product(
    products_page
):
    selected_product = products_page.get_product_information(1)[0]

    products_page.add_product_to_cart()

    products_page.open_cart()

    cart_page = CartPage(products_page.page)

    cart_page.checkout()

    checkout_page = CheckoutPage(products_page.page)

    checkout_page.enter_first_name(VALID_FIRST_NAME)
    checkout_page.enter_last_name(VALID_LAST_NAME)
    checkout_page.enter_postal_code(VALID_POSTAL_CODE)

    checkout_page.click_continue()

    order_review_page = OrderReviewPage(products_page.page)

    review_product = order_review_page.get_product_information(1)[0]

    assert selected_product["name"] == review_product["name"]
    assert selected_product["description"] == review_product["description"]
    assert selected_product["price"] == review_product["price"]


@pytest.mark.checkout
def test_tc_checkout_006_verify_that_the_product_quantity_on_the_order_review_matches_the_cart(
    products_page
):
    products_page.add_product_to_cart()

    products_page.open_cart()

    cart_page = CartPage(products_page.page)

    cart_page.checkout()

    checkout_page = CheckoutPage(products_page.page)

    checkout_page.enter_first_name(VALID_FIRST_NAME)
    checkout_page.enter_last_name(VALID_LAST_NAME)
    checkout_page.enter_postal_code(VALID_POSTAL_CODE)

    checkout_page.click_continue()

    order_review_page = OrderReviewPage(products_page.page)

    quantity = order_review_page.get_first_product_quantity()

    assert quantity == "1"


@pytest.mark.checkout
def test_tc_checkout_007_verify_that_all_selected_products_appear_on_the_order_review(
    products_page
):
    selected_products = products_page.get_product_information(2)

    products_page.add_multiple_products_to_cart(2)

    products_page.open_cart()

    cart_page = CartPage(products_page.page)

    cart_page.checkout()

    checkout_page = CheckoutPage(products_page.page)

    checkout_page.enter_first_name(VALID_FIRST_NAME)
    checkout_page.enter_last_name(VALID_LAST_NAME)
    checkout_page.enter_postal_code(VALID_POSTAL_CODE)

    checkout_page.click_continue()

    order_review_page = OrderReviewPage(products_page.page)

    review_products = order_review_page.get_product_information(2)

    assert selected_products == review_products


@pytest.mark.checkout
def test_tc_checkout_008_verify_that_the_order_totals_are_calculated_correctly_on_the_order_review(
    products_page
):
    products_page.add_product_to_cart()

    products_page.open_cart()

    cart_page = CartPage(products_page.page)

    cart_page.checkout()

    checkout_page = CheckoutPage(products_page.page)

    checkout_page.enter_first_name(VALID_FIRST_NAME)
    checkout_page.enter_last_name(VALID_LAST_NAME)
    checkout_page.enter_postal_code(VALID_POSTAL_CODE)

    checkout_page.click_continue()

    order_review_page = OrderReviewPage(products_page.page)

    totals = order_review_page.get_order_totals()

    assert round(
        totals["item_total"] + totals["tax"],
        2
    ) == totals["total"]


@pytest.mark.checkout
def test_tc_checkout_009_able_to_cancel_checkout_when_user_clicks_cancel(
    products_page
):
    products_page.add_product_to_cart()

    products_page.open_cart()

    cart_page = CartPage(products_page.page)

    cart_page.checkout()

    checkout_page = CheckoutPage(products_page.page)

    checkout_page.enter_first_name(VALID_FIRST_NAME)
    checkout_page.enter_last_name(VALID_LAST_NAME)
    checkout_page.enter_postal_code(VALID_POSTAL_CODE)

    checkout_page.click_continue()

    order_review_page = OrderReviewPage(products_page.page)

    order_review_page.cancel_checkout()

    expect(products_page.page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )


@pytest.mark.checkout
def test_tc_checkout_010_able_to_complete_the_order_when_user_clicks_finish(
    products_page
):
    products_page.add_product_to_cart()

    products_page.open_cart()

    cart_page = CartPage(products_page.page)

    cart_page.checkout()

    checkout_page = CheckoutPage(products_page.page)

    checkout_page.enter_first_name(VALID_FIRST_NAME)
    checkout_page.enter_last_name(VALID_LAST_NAME)
    checkout_page.enter_postal_code(VALID_POSTAL_CODE)

    checkout_page.click_continue()

    order_review_page = OrderReviewPage(products_page.page)

    order_review_page.finish_checkout()

    expect(products_page.page).to_have_url(
        "https://www.saucedemo.com/checkout-complete.html"
    )


@pytest.mark.checkout
def test_tc_checkout_011_verify_that_the_thank_you_message_is_displayed_after_order_completion(
    products_page
):
    products_page.add_product_to_cart()

    products_page.open_cart()

    cart_page = CartPage(products_page.page)

    cart_page.checkout()

    checkout_page = CheckoutPage(products_page.page)

    checkout_page.enter_first_name(VALID_FIRST_NAME)
    checkout_page.enter_last_name(VALID_LAST_NAME)
    checkout_page.enter_postal_code(VALID_POSTAL_CODE)

    checkout_page.click_continue()

    order_review_page = OrderReviewPage(products_page.page)

    order_review_page.finish_checkout()

    expect(
        products_page.page.get_by_text(
            "Thank you for your order!"
        )
    ).to_be_visible()



@pytest.mark.checkout
def test_tc_checkout_012_verify_that_the_cart_is_empty_after_order_completion(
    products_page
):
    products_page.add_product_to_cart()

    products_page.open_cart()

    products_page.page.wait_for_url("**/cart.html")

    cart_page = CartPage(products_page.page)

    expect(cart_page.cart_title).to_have_text("Your Cart")

    cart_page.checkout()

    checkout_page = CheckoutPage(products_page.page)

    checkout_page.enter_first_name(VALID_FIRST_NAME)
    checkout_page.enter_last_name(VALID_LAST_NAME)
    checkout_page.enter_postal_code(VALID_POSTAL_CODE)

    checkout_page.click_continue()

    order_review_page = OrderReviewPage(products_page.page)
    order_review_page.finish_checkout()

    order_complete_page = OrderCompletePage(products_page.page)
    order_complete_page.back_home()

    expect(products_page.products_title).to_be_visible()

    products_page.open_cart()

    products_page.page.wait_for_url("**/cart.html")

    cart_page = CartPage(products_page.page)

    expect(cart_page.cart_title).to_have_text("Your Cart")

    cart_products = cart_page.get_product_names()

    assert cart_products == []



@pytest.mark.checkout
def test_tc_checkout_013_verify_that_the_cart_badge_is_not_displayed_after_order_completion(
    products_page
):
    products_page.add_product_to_cart()

    products_page.open_cart()

    cart_page = CartPage(products_page.page)

    cart_page.checkout()

    checkout_page = CheckoutPage(products_page.page)

    checkout_page.enter_first_name(VALID_FIRST_NAME)
    checkout_page.enter_last_name(VALID_LAST_NAME)
    checkout_page.enter_postal_code(VALID_POSTAL_CODE)

    checkout_page.click_continue()

    order_review_page = OrderReviewPage(products_page.page)

    order_review_page.finish_checkout()

    order_complete_page = OrderCompletePage(products_page.page)

    order_complete_page.back_home()

    expect(
        products_page.cart_badge
    ).not_to_be_visible()


@pytest.mark.checkout
def test_tc_checkout_014_able_to_return_to_the_products_page_when_user_clicks_back_home_after_order_completion(
    products_page
):
    products_page.add_product_to_cart()

    products_page.open_cart()

    cart_page = CartPage(products_page.page)

    cart_page.checkout()

    checkout_page = CheckoutPage(products_page.page)

    checkout_page.enter_first_name(VALID_FIRST_NAME)
    checkout_page.enter_last_name(VALID_LAST_NAME)
    checkout_page.enter_postal_code(VALID_POSTAL_CODE)

    checkout_page.click_continue()

    order_review_page = OrderReviewPage(products_page.page)

    order_review_page.finish_checkout()

    order_complete_page = OrderCompletePage(products_page.page)

    order_complete_page.back_home()

    expect(products_page.page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )