from ui.pages.base_page import BasePage
from ui.locators.locators import LoginLocators
from ui.base_case.base_case import BaseCase


class LoginPage(BasePage):
    afterLoginURL = "https://target-sandbox.my.com/dashboard"
    locators = LoginLocators

    def login(self):
        self.click(self.locators.LOGIN_BUTTON)
        self.send_keys(self.locators.EMAIL_INPUT, BaseCase.EMAIL)
        self.send_keys(self.locators.PASSWORD_INPUT, BaseCase.PASSWORD)
        self.click(self.locators.LOGIN_BUTTON_FORM)
