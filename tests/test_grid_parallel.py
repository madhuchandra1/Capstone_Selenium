from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import threading
import time

def run_test(browser_name, options):
    driver = webdriver.Remote(
        command_executor='http://localhost:4444',
        options=options
    )
    try:
        driver.get("https://www.saucedemo.com/")
        print(f"{browser_name} - Title: {driver.title}")
        assert "Swag Labs" in driver.title
    finally:
        driver.quit()

def test_parallel_on_grid():
    chrome_opt = Options()
    edge_opt = webdriver.EdgeOptions()

    t1 = threading.Thread(target=run_test, args=("Chrome", chrome_opt))
    t2 = threading.Thread(target=run_test, args=("Edge", edge_opt))

    t1.start(); t2.start()
    t1.join(); t2.join()