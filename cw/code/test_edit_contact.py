import pytest
from ui.pages.contact_page import ContactPage
from ui.base_case.base_case import BaseCase


class TestEditContact(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = ContactPage(driver, url_config)

    def test_edit_contact(self):
        fio = 'Максимова Елизавета Геннадьевна'
        self.page.authorize()
        self.page.click(self.page.header_locators.PROFILE_BUTTON)
        self.page.send_keys(self.page.locators.FIO_INPUT, fio)
        self.page.click(self.page.locators.SAVE_BUTTON)
        assert self.page.find(self.page.locators.FIO_INPUT).get_attribute('value') == fio
