from playwright.sync_api import Page
from pages.base_page import BasePage


class OrderCompletePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.back_home_button = page.get_by_role(
            "button",
            name="Back Home"
        )

    def back_home(self):
        self.back_home_button.click()