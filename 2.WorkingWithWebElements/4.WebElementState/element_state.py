from selenium import webdriver
import time
from selenium.webdriver.common.by import By



class WebElementState():
    def state_check(self):
        driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\Drivers"
                                                   "\\geckodriver_0.31.0.exe")

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)

        # Find an element given a By strategy and locator.
        Username = driver.find_element(By.NAME, 'username')

        # Whether the element is visible to a user.If not return False
        Username_display_status = Username.is_displayed()
        print(Username_display_status)

        Username_enable_status = Username.is_enabled()
        print(Username_enable_status)

        driver.close()


test_obj = WebElementState()
test_obj.state_check()


