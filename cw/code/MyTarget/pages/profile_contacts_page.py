from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from _pytest.fixtures import FixtureRequest
import pytest


class ProfileContactsPage(BasePage):
    url = "https://target-sandbox.my.com/profile/contacts"
    class Locators:
        FULL_NAME_FIELD = (By.XPATH, '//div[starts-with(@class, "js-contacts-field-name")]/div/div/input')
        PHONE_FIELD = (By.XPATH, '//div[starts-with(@class, "js-contacts-field-phone")]/div/div/input')
        SAVE_BTN = (By.XPATH, '//button[contains(@class, "button_submit")]')
    
    def open(self):
        self.render(self.url)
    
    def save(self):
        self.find(self.Locators.SAVE_BTN).click()
    
    def check_full_name(self, ref):
        full_name = self.find(self.Locators.FULL_NAME_FIELD).get_attribute('value')
        if (ref != str(full_name)):
            raise Exception("names does not equal", ref, str(full_name))

    def set_full_name(self, full_name):
        inp = self.find(self.Locators.FULL_NAME_FIELD)
        
        inp.send_keys(Keys.CONTROL + "a")
        inp.send_keys(Keys.DELETE)
        inp.send_keys(full_name)

    def check_phone(self, ref):
        phone = self.find(self.Locators.PHONE_FIELD).get_attribute('value')
        if (ref != str(phone)):
            raise Exception("phone does not equal", ref, str(phone))

    def set_phone(self, phone):
        inp = self.find(self.Locators.PHONE_FIELD)
        
        inp.send_keys(Keys.CONTROL + "a")
        inp.send_keys(Keys.DELETE)
        inp.send_keys(phone)