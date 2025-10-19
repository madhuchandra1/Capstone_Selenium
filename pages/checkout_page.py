# pages/checkout_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def fill_info(self, fname, lname, zip_code):
        self.type(self.FIRST_NAME, fname)
        self.type(self.LAST_NAME, lname)
        self.type(self.POSTAL_CODE, zip_code)
        self.click(self.CONTINUE_BTN)

    def finish_order(self):
        # Wait for "Finish" button to be clickable
        finish_btn = self.wait.until(EC.element_to_be_clickable(self.FINISH_BTN))
        # Scroll to ensure visibility
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", finish_btn)
        finish_btn.click()

    def get_order_confirmation(self):
        return self.get_text(self.COMPLETE_HEADER)