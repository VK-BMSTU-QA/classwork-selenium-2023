from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ProfileContactsLocators:
    FULL_NAME_INPUT = (
        By.CSS_SELECTOR, '.js-contacts-field-name > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
    PHONE_INPUT = (
        By.CSS_SELECTOR, '.js-contacts-field-phone > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
    SAVE_BUTTON = (By.CSS_SELECTOR, '.button')


class ProfileContactsPage(BasePage):
    url = "https://target-sandbox.my.com/profile/contacts"

    def save_input(self):
        self.find(ProfileContactsLocators.SAVE_BUTTON).click()

    def set_full_name(self, full_name):
        full_name_input = self.find(ProfileContactsLocators.FULL_NAME_INPUT)

        full_name_input.send_keys(Keys.CONTROL + "a")
        full_name_input.send_keys(Keys.DELETE)
        full_name_input.send_keys(full_name)

    def check_full_name(self, full_name):
        assert full_name == self.find(ProfileContactsLocators.FULL_NAME_INPUT).get_attribute('value')

    def set_phone(self, phone):
        phone_input = self.find(ProfileContactsLocators.PHONE_INPUT)

        phone_input.send_keys(Keys.CONTROL + "a")
        phone_input.send_keys(Keys.DELETE)
        phone_input.send_keys(phone)

    def check_phone(self, phone):
        assert self.find(ProfileContactsLocators.PHONE_INPUT).get_attribute('value') == phone
