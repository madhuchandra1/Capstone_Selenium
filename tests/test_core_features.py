# tests/test_core_features.py
import pytest
import os
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.config import *


@pytest.fixture
def driver():
    """Use Edge browser for this test to avoid Chrome issues"""
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    edge_options = EdgeOptions()
    edge_options.add_argument("--start-maximized")
    # edge_options.add_argument("--headless")  # Uncomment if you want headless mode

    driver = webdriver.Edge(options=edge_options)
    yield driver
    driver.quit()


def test_complete_ecommerce_flow(driver):
    wait = WebDriverWait(driver, 20)

    # 1. Launch browser & navigate
    driver.get(BASE_URL)
    driver.save_screenshot("screenshots/01_home.png")

    # 2. Login
    login_page = LoginPage(driver)
    login_page.login(VALID_USER, VALID_PASSWORD)

    # 3. Verify title
    inventory = InventoryPage(driver)
    assert inventory.get_title() == "Products"

    # 4. Sort products
    inventory.sort_by("Price (low to high)")
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

    # 5. Add to cart
    inventory.add_first_product_to_cart()

    # 6. Go to cart
    inventory.go_to_cart()
    wait.until(EC.url_contains("/cart.html"))

    # 7. Wait for cart items to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))

    # 8. Proceed to checkout
    cart = CartPage(driver)
    cart.proceed_to_checkout()

    # 9. Fill checkout info
    checkout = CheckoutPage(driver)
    checkout.fill_info("John", "Doe", "12345")
    checkout.finish_order()

    # 10. Verify order confirmation
    assert "Thank you" in checkout.get_order_confirmation()
    driver.save_screenshot("screenshots/02_order_complete.png")

    # 11. Logout
    inventory.logout()