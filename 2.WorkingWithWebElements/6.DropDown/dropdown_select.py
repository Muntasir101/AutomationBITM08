from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Dropdown():
    def select_options(self):
        driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\Drivers"
                                                   "\\geckodriver_0.31.0.exe")

        driver.get("https://the-internet.herokuapp.com/dropdown")
        time.sleep(3)

        # WebElements
        dropdown = driver.find_element(By.CSS_SELECTOR, 'select#dropdown')
        dropdown_options = Select(dropdown)
        #dropdown_options.select_by_index(1)
        #dropdown_options.select_by_value("2")
        dropdown_options.select_by_visible_text('Option 1')
        time.sleep(3)

        driver.close()


test_obj = Dropdown()
test_obj.select_options()
