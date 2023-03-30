import pytest
from ui.pages.base_page import BasePage


class BaseCase:
    EMAIL = ('79373817765@phone')
    PASSWORD = ('123456789z')

    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = BasePage(driver, url_config)

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.page.open()
