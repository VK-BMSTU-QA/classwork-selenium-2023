import pytest
from ui.pages.authorize_page import AuthorizePage
from ui.base_case.base_case import BaseCase
from ui.paths import paths


class TestAuthorize(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = AuthorizePage(driver, url_config)

    def test_authorize(self):
        self.page.click(self.page.locators.LOGIN_BUTTON)
        self.page.send_keys(self.page.locators.INPUT_EMAIL, BaseCase.EMAIL)
        self.page.send_keys(self.page.locators.INPUT_PASSWORD, BaseCase.PASSWORD)
        self.page.click(self.page.locators.LOGIN_BUTTON_FORM)
        assert self.page.is_url(paths.DASHBOARD)
