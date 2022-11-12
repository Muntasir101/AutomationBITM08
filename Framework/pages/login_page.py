from selenium.webdriver.common.by import By
import time


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def login_orange(self, username, password):
        Username_field = self.driver.find_element(By.NAME, 'username')
        Password_field = self.driver.find_element(By.NAME, 'password')
        Login_btn = self.driver.find_element(By.CSS_SELECTOR, '.orangehrm-login-button')

        # Login Action
        Username_field.send_keys(username)
        time.sleep(3)

        Password_field.send_keys(password)
        time.sleep(3)

        Login_btn.click()
        time.sleep(5)


