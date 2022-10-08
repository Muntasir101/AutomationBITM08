from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Wdm_Chrome():
    def chrome_wdm(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # Maximizes the current window that webdriver is using
        driver.maximize_window()

        driver.get("https://google.com/")

        driver.close()


test_obj = Wdm_Chrome()
test_obj.chrome_wdm()
