from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Attribute():
    def element_attribute(self):
        driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\Drivers"
                                                   "\\geckodriver_0.31.0.exe")

        driver.get("https://demo.opencart.com/index.php?route=account/login&language=en-gb")
        time.sleep(3)

        # WebElements
        email_field = driver.find_element(By.NAME, 'email')
        email_type = email_field.get_attribute("name")
        print('Email field type :' + email_type)

        driver.find_element(By.NAME, email_type).send_keys("asdaddyudgqyu16e47")
        time.sleep(5)

        '''
        Login_btn = driver.find_element(By.CSS_SELECTOR, '.orangehrm-login-button')
        login_bt_type = Login_btn.get_attribute("type")
        print('Login button type :' + login_bt_type)
        '''

        driver.close()


test_obj = Attribute()
test_obj.element_attribute()
