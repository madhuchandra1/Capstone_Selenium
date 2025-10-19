# tests/test_login_data_driven_csv.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.data_reader import read_csv
from config.config import BASE_URL

# Load CSV test data
TEST_DATA = read_csv("data/email_data.csv")  # or create a dedicated login CSV

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-password-manager-reauthentication")
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.mark.parametrize("test_case", TEST_DATA, ids=[tc["TestCaseID"] for tc in TEST_DATA])
def test_login_data_driven_csv(driver, test_case):
    """Data-driven login test using CSV"""
    username = test_case.get("Username", "")
    password = test_case.get("Password", "")
    expected = test_case.get("ExpectedResult", "Error")

    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.login(username, password)

    if expected == "Success":
        inventory = InventoryPage(driver)
        assert inventory.get_title() == "Products"
        inventory.logout()
    else:
        error_msg = login_page.get_error_message()
        assert "Epic sadface" in error_msg