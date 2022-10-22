from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Uplaod():
    def file_uplaod(self):
        driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\Drivers"
                                                   "\\geckodriver_0.31.0.exe")

        driver.get("https://the-internet.herokuapp.com/upload")
        time.sleep(3)

        choose_file_btn = driver.find_element(By.CSS_SELECTOR, "input#file-upload")
        choose_file_btn.send_keys("E:\\Offline_Batch_08\\All Files\\1. Waterfall.pdf")
        time.sleep(3)

        upload_btn = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
        upload_btn.click()
        time.sleep(3)

        upload_success = driver.find_element(By.XPATH, "//div[@id='content']//h3[.='File Uploaded!']")
        message = upload_success.text
        print(message)
        time.sleep(2)

        driver.close()


test_obj = Uplaod()
test_obj.file_uplaod()
