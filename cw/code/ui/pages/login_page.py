from ui.pages.base_page import BasePage
from ui.locators.login_locators import LoginPageLocators
from ui.locators.categories_locators import CategoriesPageLocators


class LoginPage(BasePage):
    url = 'https://target-sandbox.my.com/'
    email = 'pinvlad00@yandex.com'
    pwd = 'LOL123!'

    locators = LoginPageLocators()
    categoryLocator = CategoriesPageLocators()

    def render_page(self):
        self.render(self.url)
        self.is_opened(self.url)

    def login(self):
        self.find(self.locators.OPEN_BUTTON_LOGIN_PAGE).click()

        email_field = self.find(
            self.locators.EMAIL_INPUT_LOGIN_PAGE)

        email_field.clear()
        email_field.send_keys(self.email)

        pwd_field = self.find(
            self.locators.PASSWORD_INPUT_LOGIN_PAGE)
        pwd_field.clear()
        pwd_field.send_keys(self.pwd)

        self.find(self.locators.SIGN_IN_BUTTON_LOGIN_PAGE).click()

    def check_header_email(self):
        assert self.find(
            self.categoryLocator.NAV_PROFILE_CATEGORIES_PAGE)
