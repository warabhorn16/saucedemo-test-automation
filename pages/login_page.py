from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        # Locators
        self.username_input = page.locator(
            "#user-name"
        )

        self.password_input = page.locator(
            "#password"
        )

        self.login_button = page.get_by_role(
            "button",
            name="Login"
        )
        self.error_message = page.locator(
            '[data-test="error"]'
        )

    def enter_username(self, username):
        self.username_input.fill(username)

    def enter_password(self, password):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()