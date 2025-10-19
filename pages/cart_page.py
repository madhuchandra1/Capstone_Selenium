# pages/cart_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")
    REMOVE_BTN = (By.ID, "remove-sauce-labs-backpack")

    def proceed_to_checkout(self):
        # Wait until the button is clickable
        checkout_btn = self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BTN))
        # Scroll to ensure it's in view (prevents click interception)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkout_btn)
        checkout_btn.click()

    def remove_item(self):
        self.click(self.REMOVE_BTN)