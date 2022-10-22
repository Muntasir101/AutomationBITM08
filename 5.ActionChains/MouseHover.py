from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Hover():
    def mouse_hover(self):
        driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\Drivers"
                                                   "\\geckodriver_0.31.0.exe")

        driver.get("https://demo.opencart.com/")
        time.sleep(3)

        actions = ActionChains(driver)

        desktop = driver.find_element(By.LINK_TEXT, "Desktops")
        actions.move_to_element(desktop).perform()
        time.sleep(3)

        mac = driver.find_element(By.LINK_TEXT, "Mac (1)")
        mac.click()

        time.sleep(5)
        
        driver.close()


test_obj = Hover()
test_obj.mouse_hover()

