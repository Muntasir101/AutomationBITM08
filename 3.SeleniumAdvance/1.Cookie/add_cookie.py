from selenium import webdriver
import time


class Cookie():
    def add_cookie(self):
        driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\Drivers"
                                                   "\\geckodriver_0.31.0.exe")

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)

        # Delete all cookies from the browser session
        driver.delete_all_cookies()

        # Add the cookie to the driver instance
        driver.add_cookie({
            "name": "orangehrm",
            "value": "be6ff3437e59d9d3dcd29d32cbf8a0b4",
        })

        # View all cookies in the browser session
        print((driver.get_cookies()))
        time.sleep(3)

        driver.refresh()

        print(driver.current_url)
        time.sleep(3)

        driver.close()


test_obj = Cookie()
test_obj.add_cookie()
