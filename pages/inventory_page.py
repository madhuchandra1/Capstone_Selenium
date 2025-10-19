from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from .base_page import BasePage

class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BTN = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def get_title(self):
        return self.get_text(self.TITLE)

    def add_first_product_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def sort_by(self, option_text):
        dropdown = Select(self.find(self.SORT_DROPDOWN))
        dropdown.select_by_visible_text(option_text)

    def open_burger_menu(self):
        """Click the burger menu to open the side navigation."""
        self.click(self.BURGER_MENU)

    def logout(self):
        """Logout by opening burger menu and clicking logout link."""
        self.open_burger_menu()
        self.click(self.LOGOUT_LINK)