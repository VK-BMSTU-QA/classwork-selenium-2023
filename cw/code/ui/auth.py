from typing import Union, Any

import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.firefox.webdriver import WebDriver

from ui.pages.base_page import BasePage


class Auth:
    email = 'l2fonat@bk.ru'
    password = 'Qwerty123'

    page: BasePage
    driver: Union[Union[WebDriver, WebDriver], Any]

    authorize = True

    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, url, driver):
        self.driver = driver
        self.page = BasePage(url, driver)

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, request: FixtureRequest):
        self.page.open()

        if self.authorize:
            cookies = request.getfixturevalue('cookies')
            for cookie in cookies:
                self.driver.add_cookie(cookie)

            self.driver.refresh()
