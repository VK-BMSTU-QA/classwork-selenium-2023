from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGINCLASS = 'responseHead-module-button-2yl51i'
LOGIN = 'authForm-module-button-1u2DYF'
EMAIL = 'email'
PASSWORD = 'password'

class LoginLocators:
    LOGIN_BUTTON_MAIN_PAGE = (By.CLASS_NAME, 'responseHead-module-button-2yl51i')
    EMAIL_INPUT = (By.XPATH, '//input[@name="email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
    LOGIN_BUTTON = (By.CLASS_NAME, 'authForm-module-button-1u2DYF')


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_field = (By.XPATH, f'//input[@name="{EMAIL}"]')
        self.password_field = (By.XPATH, f'//input[@name="{PASSWORD}"]')
        self.login_button = (By.CLASS_NAME, LOGINCLASS)
        self.log_in = (By.CLASS_NAME, LOGIN)
        self.url = 'https://target-sandbox.my.com/'

    def enter_username(self, username):
        email_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.email_field))
        email_field.send_keys(username)

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.password_field))
        password_field.send_keys(password)

    def click(self, button):
        login_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(button))
        login_button.click()

    def login(self):
        if not self.is_logged:
            self.render(self.url)

            self.click(self.login_button)
            self.enter_username("ivan.milchenko.92@mail.ru")
            self.enter_password("i!N9&vG^TA^v3toD7zUk9D9rpidJ@#v4")
            self.click(self.log_in)
            
            self.is_logged = True

            self.driver.refresh()

