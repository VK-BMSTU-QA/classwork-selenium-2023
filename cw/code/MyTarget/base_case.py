import pytest
from _pytest.fixtures import FixtureRequest
from MyTarget.pages.login_page import LoginPage

class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        self.driver = browser
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.login_page = LoginPage(self.driver)
        self.login_page.login()
