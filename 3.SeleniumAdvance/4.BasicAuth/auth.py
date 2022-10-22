from selenium import webdriver
import time


class BasicAuth():

    def auth(self):
        driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\Drivers"
                                                   "\\geckodriver_0.31.0.exe")

        # protocol://username:password@url
        driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
        time.sleep(3)

        print(driver.title)

        driver.close()


test_obj = BasicAuth()
test_obj.auth()
