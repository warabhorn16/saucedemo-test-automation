
from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.first_name_input = page.locator(
            '[data-test="firstName"]'
        )

        self.last_name_input = page.locator(
            '[data-test="lastName"]'
        )

        self.postal_code_input = page.locator(
            '[data-test="postalCode"]'
        )

        self.continue_button = page.get_by_role(
            "button",
            name="Continue"
        )

        self.checkout_overview_title = page.get_by_text(
            "Checkout: Overview",
            exact=True
        )

        self.error_message = page.locator(
            '[data-test="error"]'
        )

    def enter_first_name(self, first_name):
        self.first_name_input.fill(first_name)

    def enter_last_name(self, last_name):
        self.last_name_input.fill(last_name)

    def enter_postal_code(self, postal_code):
        self.postal_code_input.fill(postal_code)

    def click_continue(self):
        self.continue_button.click()

        # Wait for either successful navigation or validation error.
        self.page.wait_for_function(
            """
            () => {
                const overview = Array.from(
                    document.querySelectorAll('[data-test="title"]')
                ).some(
                    element =>
                        element.textContent.trim() === "Checkout: Overview"
                );

                const error = document.querySelector('[data-test="error"]');

                const errorVisible = error
                    && error.textContent.trim() !== ""
                    && getComputedStyle(error).display !== "none"
                    && getComputedStyle(error).visibility !== "hidden";

                return overview || errorVisible;
            }
            """
        )
