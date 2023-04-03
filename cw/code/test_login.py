import pytest

from ui.pages.login_page import LoginPage
from ui.auth import Auth


class TestLogin(Auth):
    authorize = False

    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, url, driver):
        self.page = LoginPage(url, driver)
        self.driver = driver

    def test_login(self):
        self.page.click(self.page.locators.login_button)
        self.page.send_keys(self.page.locators.email_input, Auth.email)
        self.page.send_keys(
            self.page.locators.password_input, Auth.password)
        self.page.click(self.page.locators.login_button_form)
