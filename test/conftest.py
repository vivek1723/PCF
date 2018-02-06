import pytest

from base.getBrowser import GetBrowser
from config import config


@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")

    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = GetBrowser(browser)
    driver = wdf.get_webdriver_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")


@pytest.fixture(scope="session")
def browser(request):
    return config.browser
