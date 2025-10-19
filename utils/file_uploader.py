import os
import pyautogui
import time

def upload_with_send_keys(driver, file_input_id, file_path):
    driver.find_element("id", file_input_id).send_keys(os.path.abspath(file_path))

def upload_with_pyautogui(driver, file_input_id, file_path):
    driver.find_element("id", file_input_id).click()
    time.sleep(2)
    pyautogui.write(os.path.abspath(file_path))
    pyautogui.press('enter')
    time.sleep(2)