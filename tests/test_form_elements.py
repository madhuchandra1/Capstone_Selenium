# tests/test_form_elements.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.form_page import FormPage

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_radio_buttons(driver):
    page = FormPage(driver)
    page.go_to_radio_button_page()
    page.select_yes_radio()
    assert page.is_yes_radio_selected() == True
    page.select_impressive_radio()
    assert page.is_impressive_radio_selected() == True
    assert page.is_yes_radio_selected() == False

def test_checkboxes(driver):
    page = FormPage(driver)
    page.go_to_checkbox_page()
    page.expand_home()
    page.check_home()
    # Verify checkbox is checked
    assert page.is_home_checked() == True

def test_dropdowns(driver):
    page = FormPage(driver)
    page.go_to_select_menu_page()
    page.select_color_from_old_dropdown("Green")
    assert page.get_selected_color() == "Green"
    page.select_multiple_cars(["Volvo", "Audi"])
    selected = page.get_selected_cars()
    assert "Volvo" in selected
    assert "Audi" in selected