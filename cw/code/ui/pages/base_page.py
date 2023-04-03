import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
import urllib.parse as urlparse
from ui.locators import locators


class MyException(Exception):
    pass


class BasePage(object):
    locators = locators.BasePageLocators()
    default_timeout = 90
    path = ""

    def __init__(self, url, driver):
        self.driver = driver
        self.BASE_URL = url
        self.action = ActionChains(driver)

    def get_locator_value(self, locator, timeout=default_timeout) -> WebElement:
        started = time.time()
        while time.time() - started < timeout:
            try:
                content = self.find(locator).get_attribute("value")
                return content
            except StaleElementReferenceException:
                pass
        raise MyException(
            f"{locator} is not clickable, got timeout {timeout} ms, current url {self.driver.current_url}")

    def send_keys(self, locator, keys, timeout=default_timeout) -> WebElement:
        started = time.time()
        while time.time() - started < timeout:
            try:
                elem = self.wait_to_be_clickable(
                    locator, timeout - (time.time() - started))
                elem.clear()
                elem.send_keys(keys)
                return elem
            except StaleElementReferenceException:
                pass
        raise MyException(
            f"{locator} is not clickable, got timeout {timeout} ms, current url {self.driver.current_url}")

    def open(self, timeout=default_timeout):
        url = urlparse.urljoin(self.BASE_URL, self.path)
        self.driver.get(url)
        self.driver.maximize_window()
        self.is_open(url, timeout)

    def is_open(self, url, timeout=default_timeout):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == url:
                return True

        raise MyException(
            f"cant open url {url}, got timeout {timeout} ms, current url: {self.driver.current_url}")

    def wait(self, timeout=default_timeout):
        return WebDriverWait(self.driver, timeout=timeout)

    def wait_to_be_clickable(self, locator, timeout=default_timeout):
        return self.wait(timeout).until(EC.element_to_be_clickable(locator))

    def click(self, locator, timeout=default_timeout) -> WebElement:
        started = time.time()
        while time.time() - started < timeout:
            try:
                elem = self.wait_to_be_clickable(
                    locator, timeout - (time.time() - started))
                elem.click()
                return elem
            except StaleElementReferenceException:
                pass
        raise MyException(
            f"{locator} is not clickable, got timeout {timeout} ms, current url {self.driver.current_url}")

    def find(self, locator, timeout=default_timeout):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))
