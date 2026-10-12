
from playwright.sync_api import Page
from pages.base_page import BasePage


class ProductDetailPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        # จำกัด locator ให้อยู่ในส่วนรายละเอียดสินค้า
        self.details_container = page.locator(
            ".inventory_details_container"
        )

        self.product_name = self.details_container.locator(
            '[data-test="inventory-item-name"]'
        )

        self.product_description = self.details_container.locator(
            '[data-test="inventory-item-desc"]'
        )

        self.product_price = self.details_container.locator(
            '[data-test="inventory-item-price"]'
        )

        self.product_image = self.details_container.locator(
            ".inventory_details_img"
        )

        self.add_to_cart_button = self.details_container.get_by_role(
            "button",
            name="Add to cart"
        )

        self.remove_button = self.details_container.get_by_role(
            "button",
            name="Remove"
        )

        self.back_to_products_button = page.locator(
            '[data-test="back-to-products"]'
        )

    def get_product_name(self):
        return self.product_name.inner_text()

    def get_product_description(self):
        return self.product_description.inner_text()

    def get_product_price(self):
        return self.product_price.inner_text()

    def get_product_image(self):
        return self.product_image

    def add_to_cart(self):
        self.add_to_cart_button.click()

    def remove_from_cart(self):
        self.remove_button.click()

    def back_to_products(self):
        self.back_to_products_button.click()
