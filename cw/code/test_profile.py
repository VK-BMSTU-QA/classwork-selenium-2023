import pytest
from ui.pages.profile_page import ProfilePage
from ui.auth import Auth


class TestProfile(Auth):
    authorize = True
    profile_page = 'profile/contacts'
    new_phone = '+79159999999'
    new_name = 'Абракодабра'

    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, url, driver):
        self.driver = driver
        self.page = ProfilePage(url, driver)

    def test_change_name(self):
        self.page.path = self.profile_page
        self.page.open()
        self.page.click(self.page.locators.name_input)
        self.page.send_keys(self.page.locators.name_input, self.new_name)
        self.page.click(self.page.locators.save_button)
        self.driver.refresh()
        assert str(self.page.get_locator_value(self.page.locators.name_input)) == self.new_name

    def test_change_phone(self):
        self.page.path = self.profile_page
        self.page.open()
        self.page.click(self.page.locators.phone_number_input)
        self.page.send_keys(self.page.locators.phone_number_input, self.new_phone)
        self.page.click(self.page.locators.save_button)
        self.driver.refresh()
        assert str(self.page.get_locator_value(self.page.locators.phone_number_input)) == self.new_phone
