# # tests/conftest.py
# import pytest
# import os
#
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == "call" and rep.failed:
#         driver = item.funcargs.get('driver')
#         if driver:
#             if not os.path.exists("screenshots"):
#                 os.makedirs("screenshots")
#             driver.save_screenshot(f"screenshots/FAIL_{item.name}.png")
# tests/conftest.py
import pytest
import os
from selenium.common.exceptions import NoAlertPresentException, UnexpectedAlertPresentException

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver')
        if driver:
            try:
                # Dismiss any open alert before taking a screenshot
                alert = driver.switch_to.alert
                alert.dismiss()
            except (NoAlertPresentException, UnexpectedAlertPresentException):
                pass

            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            driver.save_screenshot(f"screenshots/FAIL_{item.name}.png")
