# pages/menu_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage

class MenuPage(BasePage):
    MAIN_ITEM_2 = (By.LINK_TEXT, "Main Item 2")
    SUB_SUB_LIST = (By.XPATH, "//a[contains(text(), 'SUB SUB LIST')]")
    SUB_SUB_ITEM_2 = (By.XPATH, "//a[text()='Sub Sub Item 2']")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/menu"

    def open(self):
        self.driver.get(self.url)

    def hover_main_item_2(self):
        """Hover over 'Main Item 2' to reveal submenu"""
        main_item = self.wait.until(EC.visibility_of_element_located(self.MAIN_ITEM_2))
        ActionChains(self.driver).move_to_element(main_item).perform()

    def hover_sub_sub_list(self):
        """Hover over 'SUB SUB LIST' to reveal sub-submenu"""
        sub_sub = self.wait.until(EC.visibility_of_element_located(self.SUB_SUB_LIST))
        ActionChains(self.driver).move_to_element(sub_sub).perform()

    def click_sub_sub_item_2(self):
        """Click 'Sub Sub Item 2'"""
        item = self.wait.until(EC.element_to_be_clickable(self.SUB_SUB_ITEM_2))
        item.click()

    def scroll_to_bottom(self):
        """Scroll to bottom of page"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        """Scroll to top of page"""
        self.driver.execute_script("window.scrollTo(0, 0);")

    def take_screenshot(self, name):
        """Take screenshot and save in screenshots/ folder"""
        import os
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        self.driver.save_screenshot(f"screenshots/{name}.png")