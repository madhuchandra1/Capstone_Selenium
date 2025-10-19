import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time  # ← ADD THIS

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_mouse_hover_and_drag_drop(driver):
    driver.get("https://demoqa.com/menu")  # ← NO TRAILING SPACES
    actions = ActionChains(driver)
    main = driver.find_element(By.LINK_TEXT, "Main Item 2")
    actions.move_to_element(main).perform()
    time.sleep(2)

def test_drag_drop(driver):
    driver.get("https://demoqa.com/droppable")
    actions = ActionChains(driver)
    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")
    actions.drag_and_drop(source, target).perform()
    assert "Dropped!" in target.text

def test_right_click(driver):
    driver.get("https://demoqa.com/buttons")
    actions = ActionChains(driver)
    btn = driver.find_element(By.ID, "rightClickBtn")
    actions.context_click(btn).perform()
    msg = driver.find_element(By.ID, "rightClickMessage").text
    assert "You have done a right click" in msg

def test_double_click(driver):
    driver.get("https://demoqa.com/buttons")
    actions = ActionChains(driver)
    btn = driver.find_element(By.ID, "doubleClickBtn")
    actions.double_click(btn).perform()
    msg = driver.find_element(By.ID, "doubleClickMessage").text
    assert "You have done a double click" in msg