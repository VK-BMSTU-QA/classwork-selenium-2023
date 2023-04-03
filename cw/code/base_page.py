from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 20
        self.is_logged = False

    def render(self, url):
        self.driver.get(url)

    def wait(self, timeout=None):
        if timeout is None:
            timeout = self.default_timeout
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(expected_conditions.presence_of_element_located(locator))