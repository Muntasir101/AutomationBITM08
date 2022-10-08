from selenium import webdriver
import time

class FirefoxConfig():

    def firefox_run(self):
        # Starts a new local session of Firefox.
        driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\Drivers"
                                                   "\\geckodriver_0.31.0.exe")

        """
        Loads a web page in the current browser session.
        """
        driver.get("file:///E:/Offline_Batch_08/17th%20Class/OrangeHRM.html")
        driver.get("https://www.google.com")
        '''
        Delay execution for a given number of seconds.  The argument may be
        a floating point number for sub second precision.
        '''
        time.sleep(5.5)

        # Closes the current window.
        driver.close()

        # Quits the driver and close every associated window.
        #driver.quit()


test_obj = FirefoxConfig()
test_obj.firefox_run()
