from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

class Wdm_Firefox():
    def firefox_wdm(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get("https://pypi.org/project/webdriver-manager/")


test_obj = Wdm_Firefox()
test_obj.firefox_wdm()
