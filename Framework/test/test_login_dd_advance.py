import unittest
import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from Framework.pages.login_page import LoginPage
from Framework.utils import excel_utils


class LoginTest(unittest.TestCase):
    def test_login_valid(SetUp):
        driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\Drivers"
                                                   "\\geckodriver_0.31.0.exe")

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)

        # Excel Implementation
        file = "E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\Framework\\data\\test_data.xlsx"
        sheet = "Sheet1"

        number_of_rows = excel_utils.get_row_count(file, sheet)

        for r in range(2, number_of_rows + 1):
            username = excel_utils.read_data(file, sheet, r, 1)
            password = excel_utils.read_data(file, sheet, r, 2)

            login_page_obj = LoginPage(driver)
            login_page_obj.login_orange(username, password)

            if driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index":
                excel_utils.write_data(file, sheet, r, 3, "Login")

                # Logout
                account = driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-name")
                account.click()
                time.sleep(2)
                logout = driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(4) > a[role='menuitem']")
                logout.click()
                time.sleep(3)

            else:
                excel_utils.write_data(file, sheet, r, 3, "Failed")

        driver.close()
