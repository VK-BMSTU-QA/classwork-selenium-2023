from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginLocators:
    LOGIN_BUTTON_MAIN_PAGE = (By.CLASS_NAME, 'responseHead-module-button-2yl51i')
    EMAIL_INPUT = (By.XPATH, '//input[@name="email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
    LOGIN_BUTTON = (By.CLASS_NAME, 'authForm-module-button-1u2DYF')


class LoginPage(BasePage):
    url = "https://target-sandbox.my.com/"
    # Testing Account
    email = "classwork-selenium-2023@mail.ru"
    password = "PMhG36XHz69wsUr"

    def login(self):
        if not self.logged_in:
            self.render(self.url)

            self.find(LoginLocators.LOGIN_BUTTON_MAIN_PAGE, self.default_timeout).click()

            self.find(LoginLocators.EMAIL_INPUT).send_keys(self.email)
            self.find(LoginLocators.PASSWORD_INPUT).send_keys(self.password)

            self.find(LoginLocators.LOGIN_BUTTON).click()

            self.logged_in = True

            self.driver.refresh()
