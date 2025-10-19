from selenium import webdriver
from utils.broken_link_checker import check_broken_links

def test_broken_links():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/broken")
    broken = check_broken_links(driver, "https://demoqa.com")
    driver.quit()
    assert len(broken) == 0, f"Broken links found: {broken}"