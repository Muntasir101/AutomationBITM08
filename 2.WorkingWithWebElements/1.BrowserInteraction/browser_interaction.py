from selenium import webdriver


class BrowserInteraction():
    def browser_based_command(self):
        driver = webdriver.Firefox(executable_path="E:\\Offline_Batch_08\\Projects\\AutomationBITM08\\Drivers"
                                                   "\\geckodriver_0.31.0.exe")

        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        # Returns the title of the current page.
        title = driver.title
        print(title)

        # Gets the URL of the current page.
        url = driver.current_url
        print(url)

        pageSource = driver.page_source
        #print(pageSource)

        driver.close()


test_obj = BrowserInteraction()
test_obj.browser_based_command()
