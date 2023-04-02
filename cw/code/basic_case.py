import pytest
from pages.login_page import LoginPage


class BasicCase:
    logged_in = False

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.driver = browser

    # Login once per test set
    @pytest.fixture(scope="class", autouse=True)
    def login(self, browser):
        if not self.logged_in:
            browser.delete_all_cookies()
            browser.refresh()
            LoginPage(browser).login()
