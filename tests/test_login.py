import pytest

from playwright.sync_api import expect

from test_data.login_data import (
    VALID_USERNAME,
    VALID_PASSWORD,
    INVALID_USERNAME,
    INVALID_PASSWORD,
    EMPTY_USERNAME,
    EMPTY_PASSWORD,
    LOCKED_USERNAME
)

@pytest.mark.login
def test_tc_login_001_able_to_log_in_successfully_when_user_enters_valid_credentials(page, login_page):

    login_page.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

@pytest.mark.login
def test_tc_login_002_unable_to_log_in_when_user_enters_an_invalid_username(page, login_page):

    login_page.login(
        INVALID_USERNAME,
        VALID_PASSWORD
    )

    expect(login_page.error_message).to_be_visible()

    expect(login_page.error_message).to_contain_text(
        "Username and password do not match any user in this service"
    )

@pytest.mark.login
def test_tc_login_003_unable_to_log_in_when_user_enters_an_invalid_password(page, login_page):

    login_page.login(
        VALID_USERNAME,
        INVALID_PASSWORD
    )

    expect(login_page.error_message).to_be_visible()

    expect(login_page.error_message).to_contain_text(
        "Username and password do not match any user in this service"
    )

@pytest.mark.login
def test_tc_login_004_unable_to_log_in_when_user_enters_an_invalid_username_and_password(page, login_page):

    login_page.login(
        INVALID_USERNAME,
        INVALID_PASSWORD
    )

    expect(login_page.error_message).to_be_visible()

    expect(login_page.error_message).to_contain_text(
        "Username and password do not match any user in this service"
    )

@pytest.mark.login
def test_tc_login_005_unable_to_log_in_when_user_leaves_the_username_field_empty(page, login_page):

    login_page.login(
        EMPTY_USERNAME,
        VALID_PASSWORD
    )

    expect(login_page.error_message).to_be_visible()

    expect(login_page.error_message).to_contain_text(
        "Username is required"
    )

@pytest.mark.login
def test_tc_login_006_unable_to_log_in_when_user_leaves_the_password_field_empty(page, login_page):

    login_page.login(
        VALID_USERNAME,
        EMPTY_PASSWORD
    )

    expect(login_page.error_message).to_be_visible()

    expect(login_page.error_message).to_contain_text(
        "Password is required"
    )

@pytest.mark.login
def test_tc_login_007_unable_to_log_in_when_user_leaves_both_username_and_password_fields_empty(page, login_page):

    login_page.login(
        EMPTY_USERNAME,
        EMPTY_PASSWORD
    )

    expect(login_page.error_message).to_be_visible()

    expect(login_page.error_message).to_contain_text(
        "Username is required"
    )

@pytest.mark.login
def test_tc_login_008_unable_to_log_in_when_user_enters_credentials_for_a_locked_out_user(page, login_page):

    login_page.login(
        LOCKED_USERNAME,
        VALID_PASSWORD
    )

    expect(login_page.error_message).to_be_visible()

    expect(login_page.error_message).to_contain_text(
        "Sorry, this user has been locked out."
    )

@pytest.mark.login
def test_tc_login_009_verify_that_the_user_remains_on_the_login_page_when_login_fails(page, login_page):

    login_page.login(
        INVALID_USERNAME,
        INVALID_PASSWORD
    )

    expect(login_page.error_message).to_be_visible()

    expect(login_page.error_message).to_contain_text(
        "Username and password do not match any user in this service"
    )

    expect(page).to_have_url(
         "https://www.saucedemo.com/"
    )