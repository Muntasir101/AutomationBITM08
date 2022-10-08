from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class OrangeHRMLogin():
    def loginTest_001(self):
        driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\Drivers"
                                                   "\\geckodriver_0.31.0.exe")

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)

        # WebElements
        Username_field = driver.find_element(By.NAME, 'username')
        Password_field= driver.find_element(By.NAME, 'password')
        Login_btn = driver.find_element(By.CSS_SELECTOR, '.orangehrm-login-button')

        # Login Action
        Username_field.send_keys('Admin')
        time.sleep(3)
        Password_field.send_keys('admin123')
        time.sleep(3)
        Login_btn.click()
        time.sleep(5)
        
        driver.close()


test_obj = OrangeHRMLogin()
test_obj.loginTest_001()