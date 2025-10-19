# tests/conftest.py
import pytest
import os

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver')
        if driver:
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            driver.save_screenshot(f"screenshots/FAIL_{item.name}.png")