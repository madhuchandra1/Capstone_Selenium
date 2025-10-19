# pages/form_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class FormPage(BasePage):
    # Radio Buttons
    YES_RADIO_LABEL = (By.XPATH, "//label[@for='yesRadio']")
    IMPRESSIVE_RADIO_LABEL = (By.XPATH, "//label[@for='impressiveRadio']")

    # Checkboxes - USE LABELS (not hidden inputs)
    HOME_LABEL = (By.XPATH, "//label[@for='tree-node-home']")
    DESKTOP_LABEL = (By.XPATH, "//label[@for='tree-node-desktop']")
    DOCUMENTS_LABEL = (By.XPATH, "//label[@for='tree-node-documents']")
    DOWNLOADS_LABEL = (By.XPATH, "//label[@for='tree-node-downloads']")

    # Dropdowns
    OLD_SELECT_MENU = (By.ID, "oldSelectMenu")
    MULTI_SELECT = (By.ID, "cars")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com"  # Fixed: no trailing spaces

    def go_to_radio_button_page(self):
        self.driver.get(f"{self.url}/radio-button")

    def go_to_checkbox_page(self):
        self.driver.get(f"{self.url}/checkbox")

    def go_to_select_menu_page(self):
        self.driver.get(f"{self.url}/select-menu")

    # Radio Button Methods
    def select_yes_radio(self):
        self.click(self.YES_RADIO_LABEL)

    def select_impressive_radio(self):
        self.click(self.IMPRESSIVE_RADIO_LABEL)

    def is_yes_radio_selected(self):
        return self.driver.execute_script("return document.getElementById('yesRadio').checked;")

    def is_impressive_radio_selected(self):
        return self.driver.execute_script("return document.getElementById('impressiveRadio').checked;")

    # Checkbox Methods
    def expand_home(self):
        """Expand 'Home' if collapsed"""
        try:
            expand_btn = self.find((By.XPATH, "//button[@title='Toggle' and contains(@class, 'rct-node-collapsed')]"))
            if expand_btn.is_displayed():
                expand_btn.click()
                # Wait for Desktop to appear (confirms expansion)
                self.wait.until(EC.presence_of_element_located((By.ID, "tree-node-desktop")))
        except:
            pass  # Already expanded

    def check_home(self):
        """Click the VISIBLE 'Home' label (not hidden input)"""
        home_label = self.wait.until(EC.element_to_be_clickable(self.HOME_LABEL))
        home_label.click()

    def check_desktop(self):
        desktop_label = self.wait.until(EC.element_to_be_clickable(self.DESKTOP_LABEL))
        desktop_label.click()

    def is_home_checked(self):
        """Check if 'Home' is selected by inspecting SVG icon"""
        svg = self.find((By.XPATH, "//label[@for='tree-node-home']//*[name()='svg']"))
        return "rct-icon-check" in svg.get_attribute("class")

    # Dropdown Methods
    def select_color_from_old_dropdown(self, color):
        dropdown = Select(self.find(self.OLD_SELECT_MENU))
        dropdown.select_by_visible_text(color)

    def get_selected_color(self):
        dropdown = Select(self.find(self.OLD_SELECT_MENU))
        return dropdown.first_selected_option.text

    def select_multiple_cars(self, cars):
        dropdown = Select(self.find(self.MULTI_SELECT))
        for car in cars:
            dropdown.select_by_visible_text(car)

    def get_selected_cars(self):
        dropdown = Select(self.find(self.MULTI_SELECT))
        return [option.text for option in dropdown.all_selected_options]