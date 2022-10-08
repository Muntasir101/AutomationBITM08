from selenium import webdriver
import time


class BrowserNavigation():
    def browser_navigate(self):
        driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\Drivers"
                                                   "\\geckodriver_0.31.0.exe")

        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        time.sleep(3)

        driver.get('https://google.com/')
        time.sleep(2)

        # Goes one step backward in the browser history.
        driver.back()
        time.sleep(2)

        # Goes one step forward in the browser history.
        driver.forward()
        time.sleep(2)

        # Refreshes the current page.
        driver.refresh()

        driver.close()


test_obj = BrowserNavigation()
test_obj.browser_navigate()




