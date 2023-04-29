import pytest
from ui.pages.profile_page import ProfilePage
from ui.base_case.base_case import BaseCase


class TestProfile(BaseCase):
    authorize = True

    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = ProfilePage(driver, url_config)   
        
    def test_change_name(self):
        self.name = 'Иванов Иван Иванович'
        self.page.PATH = 'profile/contacts'
        self.page.open()

        self.page.click(self.page.locators.NAME_INPUT)
        self.page.send_keys(self.page.locators.NAME_INPUT, self.name)
        self.page.click(self.page.locators.SAVE_BUTTON)

        self.driver.refresh()
        assert str(self.page.get_content(self.page.locators.NAME_INPUT)) == self.name

    def test_change_phone_number(self):
        self.phone_number = '+74957256357'
        self.page.PATH = 'profile/contacts'
        self.page.open()

        self.page.click(self.page.locators.PHONE_NUMBER_INPUT)
        self.page.send_keys(self.page.locators.PHONE_NUMBER_INPUT, self.phone_number)
        self.page.click(self.page.locators.SAVE_BUTTON)

        self.driver.refresh()
        assert str(self.page.get_content(self.page.locators.PHONE_NUMBER_INPUT)) == self.phone_number
