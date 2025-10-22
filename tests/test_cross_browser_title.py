# tests/test_cross_browser_title.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from pages.home_page import HomePage

BROWSERS = ["chrome", "firefox", "edge"]

def get_driver(browser_name):
    if browser_name == "chrome":
        options = ChromeOptions()
        # options.add_argument("--headless")  # Remove to debug visually
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--remote-allow-origins=*")
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(120)
        driver.set_script_timeout(120)
        return driver

    elif browser_name == "firefox":
        options = FirefoxOptions()
        # options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--no-sandbox")
        driver = webdriver.Firefox(options=options)
        driver.set_page_load_timeout(120)
        driver.set_script_timeout(120)
        return driver

    elif browser_name == "edge":
        options = EdgeOptions()
        # options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--no-sandbox")
        driver = webdriver.Edge(options=options)
        driver.set_page_load_timeout(120)
        driver.set_script_timeout(120)
        return driver

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

@pytest.fixture(params=BROWSERS)
def driver(request):
    browser = request.param
    driver = get_driver(browser)
    yield driver
    driver.quit()

def test_page_title(driver):
    page = HomePage(driver)
    page.open()
    title = page.title
    print(f"\n✅ [{driver.name}] Page title: '{title}'")
    # Normalize to uppercase to avoid case mismatch
    assert title.upper() == "DEMOQA"
