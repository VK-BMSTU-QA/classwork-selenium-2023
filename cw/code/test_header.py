import pytest
from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.base_case.base_case import BaseCase


class TestHeaderLinks(BaseCase):
    authorize = True

    @pytest.mark.parametrize("locator, URL", [
        (BasePage.locators.HEADER_BILLING, 'https://target-sandbox.my.com/billing'),
        (BasePage.locators.HEADER_PROFILE, 'https://target-sandbox.my.com/profile'),
    ],)
    def test_header(self, locator, URL):
        self.page.click(locator)
        assert str(self.driver.current_url) == URL
