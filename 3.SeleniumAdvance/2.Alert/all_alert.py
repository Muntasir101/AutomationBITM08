from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Alert():
    def alert_handle(self):
        driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\Drivers"
                                                   "\\geckodriver_0.31.0.exe")

        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(3)

        # Normal alert
        normal_alert = driver.find_element(By.CSS_SELECTOR, 'li:nth-of-type(1) > button')
        normal_alert.click()
        time.sleep(3)
        driver.switch_to.alert.accept()
        time.sleep(3)

        # Confirmation alert
        confirmation_alert = driver.find_element(By.CSS_SELECTOR, 'li:nth-of-type(2) > button')
        confirmation_alert.click()
        time.sleep(3)
        driver.switch_to.alert.dismiss()
        time.sleep(3)

        # Prompt alert
        prompt_alert = driver.find_element(By.CSS_SELECTOR, 'li:nth-of-type(3) > button')
        prompt_alert.click()
        driver.switch_to.alert.send_keys("asdaddyudgqyu16e47")
        time.sleep(3)
        driver.switch_to.alert.accept()
        time.sleep(3)

        driver.close()


test_obj = Alert()
test_obj.alert_handle()
