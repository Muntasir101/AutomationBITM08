from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Screenshot():
    def capture_screenshot(self):
        driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\Drivers"
                                                   "\\geckodriver_0.31.0.exe")

        driver.get("https://google.com/")
        time.sleep(3)

        driver.get_screenshot_as_file('E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\3.SeleniumAdvance\\Screenshot\\Google.png')

        driver.close()


test_obj = Screenshot()
test_obj.capture_screenshot()
