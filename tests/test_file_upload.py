import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By  # ← ADD THIS
from utils.file_uploader import upload_with_send_keys

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_file_upload_sendkeys(driver):
    with open("data/upload_test.txt", "w") as f:
        f.write("Test upload file")
    driver.get("https://the-internet.herokuapp.com/upload")
    upload_with_send_keys(driver, "file-upload", "data/upload_test.txt")
    driver.find_element(By.ID, "file-submit").click()
    assert "File Uploaded!" in driver.find_element(By.TAG_NAME, "h3").text
    os.remove("data/upload_test.txt")