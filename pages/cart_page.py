from playwright.sync_api import Page

from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.cart_title = page.locator(
            '[data-test="title"]'
        )

        self.cart_product_names = page.locator(
            '[data-test="inventory-item-name"]'
        )

        self.remove_buttons = page.get_by_role(
            "button",
            name="Remove"
        )

        self.continue_shopping_button = page.get_by_role(
            "button",
            name="Continue Shopping"
        )

        self.checkout_button = page.get_by_role(
            "button",
            name="Checkout"
        )

    def get_product_names(self):
        return self.cart_product_names.all_text_contents()

    def remove_product(self):
        self.remove_buttons.first.click()

    def remove_all_products(self):
        while self.remove_buttons.count() > 0:
            self.remove_buttons.first.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()

    def checkout(self):
        self.checkout_button.click()