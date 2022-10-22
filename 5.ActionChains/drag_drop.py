from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class Dragdrop():
    def drag_and_drop(self):
        driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\Drivers"
                                                   "\\geckodriver_0.31.0.exe")

        driver.get("https://jqueryui.com/droppable/")
        time.sleep(3)

        driver.switch_to.frame(0)

        source = driver.find_element(By.ID, "draggable")
        target = driver.find_element(By.ID, "droppable")

        actions = ActionChains(driver)
        actions.drag_and_drop(source, target).perform()
        time.sleep(5)

        driver.close()


test_obj = Dragdrop()
test_obj.drag_and_drop()