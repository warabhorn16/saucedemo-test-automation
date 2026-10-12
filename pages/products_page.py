
from playwright.sync_api import Page

from pages.base_page import BasePage


class ProductsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.products_title = page.get_by_text(
            "Products",
            exact=True
        )

        self.product_items = page.locator(".inventory_item")

        self.product_names = page.locator(
            '[data-test="inventory-item-name"]'
        )

        self.product_descriptions = page.locator(
            '[data-test="inventory-item-desc"]'
        )

        self.product_prices = page.locator(
            '[data-test="inventory-item-price"]'
        )

        self.product_images = page.locator(
            ".inventory_item_img img"
        )

        self.sort_dropdown = page.locator(
            '[data-test="product-sort-container"]'
        )

        self.add_to_cart_buttons = page.locator(
            '[data-test^="add-to-cart-"]'
        )

        self.remove_buttons = page.locator(
            '[data-test^="remove-"]'
        )

        self.cart_link = page.locator(
            '[data-test="shopping-cart-link"]'
        )

        self.cart_badge = page.locator(
            '[data-test="shopping-cart-badge"]'
        )

    # Sorting products

    def sort_by_name_ascending(self):
        self.sort_dropdown.select_option("az")

    def sort_by_name_descending(self):
        self.sort_dropdown.select_option("za")

    def sort_by_price_ascending(self):
        self.sort_dropdown.select_option("lohi")

    def sort_by_price_descending(self):
        self.sort_dropdown.select_option("hilo")

    # Add products to cart

    def add_product_to_cart(self):
        product = self.product_items.first

        product_name = product.locator(
            '[data-test="inventory-item-name"]'
        ).inner_text()

        product.get_by_role(
            "button",
            name="Add to cart"
        ).click()

        return product_name

    def add_multiple_products_to_cart(self, count):
        selected_product_names = []
        products = self.product_items.all()

        for product in products[:count]:
            product_name = product.locator(
                '[data-test="inventory-item-name"]'
            ).inner_text()

            product.get_by_role(
                "button",
                name="Add to cart"
            ).click()

            selected_product_names.append(product_name)

        return selected_product_names

    def add_product_and_get_remove_button(self):
        product = self.product_items.first

        product.get_by_role(
            "button",
            name="Add to cart"
        ).click()

        return product.get_by_role(
            "button",
            name="Remove"
        )

    # Remove products from cart on the products page


    def remove_product_from_cart(self):
        product = self.product_items.first

        product_name = product.locator(
            '[data-test="inventory-item-name"]'
        ).inner_text()

        print("Removing product:", product_name)
        print("Badge before remove:", self.cart_badge.all_text_contents())

        product.get_by_role(
            "button",
            name="Remove"
        ).click()

        product.get_by_role(
            "button",
            name="Add to cart"
        ).wait_for(state="visible")

        print("Badge after remove:", self.cart_badge.all_text_contents())
        print("Current URL after remove:", self.page.url)


    # Navigation

    def open_cart(self):
        self.cart_link.click()

    def open_product_detail(self):
        product = self.product_items.first

        product_name = product.locator(
            '[data-test="inventory-item-name"]'
        )

        selected_product_name = product_name.inner_text()

        product_name.click()

        return selected_product_name

    # Product information

    def get_product_information(self, count):
        selected_products = []
        products = self.product_items.all()

        for product in products[:count]:
            selected_products.append({
                "name": product.locator(
                    '[data-test="inventory-item-name"]'
                ).inner_text(),

                "description": product.locator(
                    '[data-test="inventory-item-desc"]'
                ).inner_text(),

                "price": product.locator(
                    '[data-test="inventory-item-price"]'
                ).inner_text()
            })

        return selected_products

    


