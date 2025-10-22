# pages/alert_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

class AlertPage:
    ALERT_BUTTON = (By.ID, "alertButton")
    RESULT_TEXT = (By.ID, "confirmResult")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://demoqa.com/alerts")

    def trigger_alert(self):
        self.driver.find_element(*self.ALERT_BUTTON).click()

    def get_alert_text(self):
        alert = Alert(self.driver)
        return alert.text

    def accept_alert(self):
        alert = Alert(self.driver)
        alert.accept()
