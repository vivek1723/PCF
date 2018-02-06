from selenium import webdriver
from config import config

Instance = None


def getDriver():
    global Instance
    Instance = webdriver.Chrome(config.chrome_driver_path)
    Instance.implicitly_wait(5)
    Instance.get(config.url)
    return Instance


def closeDriver():
    global Instance
    Instance.quit()
