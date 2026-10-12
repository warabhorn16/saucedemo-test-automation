from playwright.sync_api import Page
from pages.base_page import BasePage


class MenuPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = page.get_by_role(
            "button",
            name="Open Menu"
        )

        self.all_items_link = page.get_by_text(
            "All Items",
            exact=True
        )

        self.about_link = page.get_by_text(
            "About",
            exact=True
        )

        self.logout_link = page.get_by_text(
            "Logout",
            exact=True
        )

        self.reset_app_state_link = page.get_by_text(
            "Reset App State",
            exact=True
        )

    def open_menu(self):
        self.menu_button.click()

    def click_all_items(self):
        self.all_items_link.click()

    def click_about(self):
        self.about_link.click()

    def click_logout(self):
        self.logout_link.click()

    def click_reset_app_state(self):
        self.reset_app_state_link.click()