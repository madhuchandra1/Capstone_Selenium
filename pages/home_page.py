# pages/home_page.py
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    URL = "https://demoqa.com"

    def open(self):
        """Open the page and wait until the title contains 'DEMOQA'"""
        self.driver.get(self.URL)
        try:
            WebDriverWait(self.driver, 20).until(
                EC.title_contains("DEMOQA")
            )
        except Exception as e:
            print(f"Error waiting for page title: {e}")

    @property
    def title(self):
        return self.driver.title
