import pytest
from selenium import webdriver
import time


@pytest.fixture()
def SetUp():
    driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\Drivers"
                                               "\\geckodriver_0.31.0.exe")

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(3)
    yield
    driver.quit()
