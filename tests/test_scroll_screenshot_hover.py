# tests/test_scroll_screenshot_hover.py
import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_scroll_screenshot_hover(driver):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    wait = WebDriverWait(driver, 15)  # Increased timeout

    # 1. Open menu page (FIX: removed trailing spaces)
    driver.get("https://demoqa.com/menu")
    driver.save_screenshot("screenshots/01_menu_initial.png")

    # 2. Scroll to bottom and top
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.save_screenshot("screenshots/02_scrolled_to_bottom.png")
    driver.execute_script("window.scrollTo(0, 0);")
    driver.save_screenshot("screenshots/03_scrolled_to_top.png")

    # 3. Hover over "Main Item 2"
    main_item = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Main Item 2")))
    ActionChains(driver).move_to_element(main_item).perform()
    driver.save_screenshot("screenshots/04_hover_main_item_2.png")

    # 4. Hover over "SUB SUB LIST" — use correct locator and wait
    # The actual text is "SUB SUB LIST »" — so use contains
    sub_sub = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'SUB SUB LIST')]"))
    )
    ActionChains(driver).move_to_element(sub_sub).perform()
    driver.save_screenshot("screenshots/05_hover_sub_sub_list.png")

    # 5. Click "Sub Sub Item 2"
    sub_sub_item = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Sub Sub Item 2']"))
    )
    sub_sub_item.click()
    driver.save_screenshot("screenshots/06_after_click.png")