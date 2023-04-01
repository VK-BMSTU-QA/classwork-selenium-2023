import pytest
from ui.pages.login_page import LoginPage
from ui.base_case.base_case import BaseCase


class TestLogin(BaseCase):
    authorize = False

    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = LoginPage(driver, url_config)

    def test_login(self):
        self.page.click(self.page.locators.LOGIN_BUTTON)
        self.page.send_keys(self.page.locators.EMAIL_INPUT, BaseCase.EMAIL)
        self.page.send_keys(
            self.page.locators.PASSWORD_INPUT, BaseCase.PASSWORD)
        self.page.click(self.page.locators.LOGIN_BUTTON_FORM)
