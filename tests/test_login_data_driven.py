# tests/test_login_data_driven.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.data_reader import read_excel
from config.config import BASE_URL


# Load test data once
TEST_DATA = read_excel("data/login_data.xlsx", "LoginTests")


@pytest.fixture
def driver():
    """Reusable browser fixture with Chrome options to suppress alerts"""
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")           # Disable notifications
    chrome_options.add_argument("--disable-password-manager-reauthentication")  # Disable password re-auth
    chrome_options.add_argument("--disable-save-password-bubble")     # Disable save password prompt
    chrome_options.add_argument("--disable-web-security")            # Optional: if CORS blocks are an issue
    chrome_options.add_argument("--no-sandbox")                      # For CI/CD environments
    chrome_options.add_argument("--disable-gpu")                     # For headless mode
    chrome_options.add_argument("--disable-dev-shm-usage")           # Prevent /dev/shm issues

    # Optional: Start maximized
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.mark.parametrize("test_case", TEST_DATA, ids=[tc["TestCaseID"] for tc in TEST_DATA])
def test_login_data_driven(driver, test_case):
    """
    Data-Driven Login Test using Excel
    Covers:
    - Valid logins (standard_user, problem_user, etc.)
    - Invalid logins (locked_out_user, empty fields, wrong creds)
    """
    # Arrange
    username = test_case.get("Username", "")
    password = test_case.get("Password", "")
    expected_result = test_case["ExpectedResult"]  # "Success" or "Error"

    # Act
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.login(username, password)

    # Assert
    if expected_result == "Success":
        # Should land on inventory page
        inventory = InventoryPage(driver)
        assert inventory.get_title() == "Products"
        # Optional: logout to reset state for next test
        inventory.logout()
    else:
        # Should see an error message
        error_msg = login_page.get_error_message()
        assert "Epic sadface" in error_msg