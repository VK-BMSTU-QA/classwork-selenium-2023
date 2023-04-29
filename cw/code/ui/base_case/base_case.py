import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage


class BaseCase:
    authorize = True
    EMAIL = ('alex-13m@mail.ru')
    PASSWORD = ('123456a')

    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = BasePage(driver, url_config)

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, request: FixtureRequest):
        self.page.open()

        if self.authorize:
                cookies = request.getfixturevalue('cookies')
                for cookie in cookies:
                    self.driver.add_cookie(cookie)

                self.driver.refresh()
