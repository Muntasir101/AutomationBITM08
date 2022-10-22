from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Headless():

    def firefox_headless(self):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.headless = True

        driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\Drivers"
                                                   "\\geckodriver_0.31.0.exe", options=firefox_options)

        driver.get("https://bbc.com/")

        print(driver.title)

        driver.close()

        print("Test Completed")


test_obj = Headless()
test_obj.firefox_headless()
