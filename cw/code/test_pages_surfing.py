import pytest
from ui.pages.base_page import BasePage
from ui.auth import Auth


class TestPagesSurfing(Auth):

    @pytest.mark.parametrize("locator, URL", [
        (BasePage.locators.locator_billing, 'https://target-sandbox.my.com/billing'),
        (BasePage.locators.locator_profile, 'https://target-sandbox.my.com/profile'),
    ], )
    def test_pages_surfing(self, locator, URL):
        self.page.click(locator)
        assert str(self.driver.current_url) == URL
