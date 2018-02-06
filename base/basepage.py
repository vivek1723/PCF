from config import config


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_browser(self):
        self.driver.get(config.url)
