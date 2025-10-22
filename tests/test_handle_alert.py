# tests/test_handle_alert.py
import pytest
from selenium import webdriver
from pages.alert_page import AlertPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_handle_alert(driver):
    page = AlertPage(driver)
    page.open()
    page.trigger_alert()
    alert_text = page.get_alert_text()
    print(f"Alert says: {alert_text}")
    page.accept_alert()

    # Assert that the alert text matches the expected message
    assert "You clicked a button" in alert_text
