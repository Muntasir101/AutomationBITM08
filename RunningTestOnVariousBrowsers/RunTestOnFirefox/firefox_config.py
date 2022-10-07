from selenium import webdriver

class FirefoxConfig():

    def firefox_run(self):
        driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\Drivers"
                                                   "\\geckodriver_0.31.0.exe")

        driver.get("http://google.com")


test_obj = FirefoxConfig()
test_obj.firefox_run()
