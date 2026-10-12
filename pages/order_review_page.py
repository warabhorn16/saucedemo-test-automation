from playwright.sync_api import Page
from pages.base_page import BasePage


class OrderReviewPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.product_items = page.locator(".cart_item")

        self.product_names = page.locator(
            '[data-test="inventory-item-name"]'
        )

        self.product_descriptions = page.locator(
            '[data-test="inventory-item-desc"]'
        )

        self.product_prices = page.locator(
            '[data-test="inventory-item-price"]'
        )

        self.product_quantities = page.locator(
            '[data-test="item-quantity"]'
        )

        self.item_total = page.locator(
            '[data-test="subtotal-label"]'
        )

        self.tax = page.locator(
            '[data-test="tax-label"]'
        )

        self.total = page.locator(
            '[data-test="total-label"]'
        )

        self.cancel_button = page.get_by_role(
            "button",
            name="Cancel"
        )

        self.finish_button = page.get_by_role(
            "button",
            name="Finish"
        )

    def cancel_checkout(self):
        self.cancel_button.click()

    def finish_checkout(self):
        self.finish_button.click()

    def get_product_information(self, count):
        review_products = []

        for product in self.product_items.all()[:count]:
            product_name = product.locator(
                '[data-test="inventory-item-name"]'
            ).inner_text()

            product_description = product.locator(
                '[data-test="inventory-item-desc"]'
            ).inner_text()

            product_price = product.locator(
                '[data-test="inventory-item-price"]'
            ).inner_text()

            review_products.append({
                "name": product_name,
                "description": product_description,
                "price": product_price
            })

        return review_products

    def get_first_product_quantity(self):
        return self.product_quantities.first.inner_text()

    def get_order_totals(self):
        item_total = self.item_total.inner_text()
        tax = self.tax.inner_text()
        total = self.total.inner_text()

        item_total = float(item_total.split("$")[1])
        tax = float(tax.split("$")[1])
        total = float(total.split("$")[1])

        return {
            "item_total": item_total,
            "tax": tax,
            "total": total
        }
    