from selenium import webdriver

from config import config


class GetBrowser:

    def __init__(self, browser):
        self.browser = browser

    # More browser can be supported by adding in this function
    def get_webdriver_instance(self):

        if self.browser == "firefox":
            driver = webdriver.Firefox(executable_path=r'D:\Dropbox\MyDocs\PycharmProjects\pylib\geckodriver.exe')
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome(config.chrome_driver_path)
        else:
            # Set chrome driver
            driver = webdriver.Chrome(config.chrome_driver_path)
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(5)
        # Maximize the window
        # driver.maximize_window()
        driver.set_window_size(900, 700)
        # Loading browser with App URL
        return driver
