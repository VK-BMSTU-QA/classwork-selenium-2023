import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from ui.pages.login_page import LoginPage


def get_driver(browser_name):
    if browser_name == "chrome":
        chrome_options = Options()
        Options().set_capability(
            "goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"}
        )
        driver = webdriver.Chrome(
            service=Service(executable_path=ChromeDriverManager().install()),
            options=chrome_options
        )
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
    else:
        raise RuntimeError(f'Cant use browser: "{browser_name}"')

    driver.maximize_window()
    return driver


@pytest.fixture()
def driver(browser):
    driver = get_driver(browser)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def cookies(browser, url):
    driver = get_driver(browser)
    driver.get(url)
    login_page = LoginPage(url, driver)
    login_page.login()

    cookies = driver.get_cookies()
    driver.quit()
    return cookies
