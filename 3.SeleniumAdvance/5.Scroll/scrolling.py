from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Scroll():
    def scroll_page(self):
        driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\Drivers"
                                                   "\\geckodriver_0.31.0.exe")

        driver.get("https://bbc.com/")
        time.sleep(3)

        # Scroll down
        driver.execute_script("window.scrollBy(0,5000);")
        time.sleep(4)

        driver.get_screenshot_as_file(
            'E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\3.SeleniumAdvance\\Screenshot\\footer.png')

        # Scroll up
        driver.execute_script("window.scrollBy(0,-5000);")
        time.sleep(4)

        # Scroll to element
        asia_news = driver.find_element(By.LINK_TEXT, 'Asia News')
        driver.execute_script("arguments[0].scrollIntoView(true);", asia_news)
        time.sleep(4)

        driver.get_screenshot_as_file(
            'E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\3.SeleniumAdvance\\Screenshot\\AsiaNews.png')

        driver.close()


test_obj = Scroll()
test_obj.scroll_page()
