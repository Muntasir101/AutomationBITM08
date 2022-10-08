from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


class Wdm_Chromium():
    def chromium_wdm(self):
        driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
        # Maximizes the current window that webdriver is using
        driver.maximize_window()

        driver.get("https://google.com/")

        driver.close()


test_obj = Wdm_Chromium()
test_obj.chromium_wdm()
