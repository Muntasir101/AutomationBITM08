import unittest
import pytest
from selenium import webdriver
import time
from Framework.pages.login_page import LoginPage

class LoginTest(unittest.TestCase):
    def test_login_valid(SetUp):
        driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\Drivers"
                                                   "\\geckodriver_0.31.0.exe")

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        login_page_obj = LoginPage(driver)
        login_page_obj.login_orange("Admin", "admin123")

        driver.close()

    @pytest.mark.skip
    def test_login_invalid(self):
        driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\Drivers"
                                                   "\\geckodriver_0.31.0.exe")

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)

        login_page_obj = LoginPage(driver)
        login_page_obj.login_orange("Admin12345", "admin123")

        driver.close()
