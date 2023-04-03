from ui.pages.base_page import BasePage
from ui.locators.locators import LoginPageLocators
from ui.auth import Auth


class LoginPage(BasePage):
    locators = LoginPageLocators

    def login(self):
        self.click(self.locators.login_button)
        self.send_keys(self.locators.email_input, Auth.email)
        self.send_keys(self.locators.password_input, Auth.password)
        self.click(self.locators.login_button_form)
