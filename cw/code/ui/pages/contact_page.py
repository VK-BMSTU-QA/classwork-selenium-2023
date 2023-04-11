from ui.locators import locators
from ui.pages.base_page import BasePage
from ui.base_case.base_case import BaseCase
from ui.paths import paths


class ContactPage(BasePage):
    auth_locators = locators.AuthorizeLocators
    header_locators = locators.HeaderLocators
    locators = locators.ContactLocators
    PATH = paths.AUTHORIZE

    def authorize(self):
        self.click(self.auth_locators.LOGIN_BUTTON)
        self.send_keys(self.auth_locators.INPUT_EMAIL, BaseCase.EMAIL)
        self.send_keys(self.auth_locators.INPUT_PASSWORD, BaseCase.PASSWORD)
        self.click(self.auth_locators.LOGIN_BUTTON_FORM)
