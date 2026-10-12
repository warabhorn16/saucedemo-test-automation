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
def test_tc_login_001_login_with_valid_credentials(page, login_page):

    login_page.login(
        VALID_USERNAME,
        VALID_PASSWORD
    )

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

@pytest.mark.login
def test_tc_login_002_login_with_invalid_username(page, login_page):

    login_page.login(
        INVALID_USERNAME,
        VALID_PASSWORD
    )

    expect(login_page.error_message).to_be_visible()

    expect(login_page.error_message).to_contain_text(
        "Username and password do not match any user in this service"
    )

@pytest.mark.login
def test_tc_login_003_login_with_invalid_password(page, login_page):

    login_page.login(
        VALID_USERNAME,
        INVALID_PASSWORD
    )

    expect(login_page.error_message).to_be_visible()

    expect(login_page.error_message).to_contain_text(
        "Username and password do not match any user in this service"
    )

@pytest.mark.login
def test_tc_login_004_login_with_invalid_username_and_password(page, login_page):

    login_page.login(
        INVALID_USERNAME,
        INVALID_PASSWORD
    )

    expect(login_page.error_message).to_be_visible()

    expect(login_page.error_message).to_contain_text(
        "Username and password do not match any user in this service"
    )

@pytest.mark.login
def test_tc_login_005_login_with_empty_username(page, login_page):

    login_page.login(
        EMPTY_USERNAME,
        VALID_PASSWORD
    )

    expect(login_page.error_message).to_be_visible()

    expect(login_page.error_message).to_contain_text(
        "Username is required"
    )

@pytest.mark.login
def test_tc_login_006_login_with_empty_password(page, login_page):

    login_page.login(
        VALID_USERNAME,
        EMPTY_PASSWORD
    )

    expect(login_page.error_message).to_be_visible()

    expect(login_page.error_message).to_contain_text(
        "Password is required"
    )

@pytest.mark.login
def test_tc_login_007_login_with_empty_username_and_password(page, login_page):

    login_page.login(
        EMPTY_USERNAME,
        EMPTY_PASSWORD
    )

    expect(login_page.error_message).to_be_visible()

    expect(login_page.error_message).to_contain_text(
        "Username is required"
    )

@pytest.mark.login
def test_tc_login_008_login_with_locked_user(page, login_page):

    login_page.login(
        LOCKED_USERNAME,
        VALID_PASSWORD
    )

    expect(login_page.error_message).to_be_visible()

    expect(login_page.error_message).to_contain_text(
        "Sorry, this user has been locked out."
    )

@pytest.mark.login
def test_tc_login_009_unsuccessful_login_remains_on_login_page(page, login_page):

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