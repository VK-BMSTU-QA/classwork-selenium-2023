import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

LOGINCLASS = 'responseHead-module-button-2yl51i'
LOGIN = 'authForm-module-button-1u2DYF'
EMAIL = 'email'
PASSWORD = 'password'


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.XPATH, f'//input[@name="{EMAIL}"]')
        self.password_field = (By.XPATH, f'//input[@name="{PASSWORD}"]')
        self.login_button = (By.CLASS_NAME, LOGINCLASS)
        self.login = (By.CLASS_NAME, LOGIN)

    def enter_username(self, username):
        email_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.email_field))
        email_field.send_keys(username)

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.password_field))
        password_field.send_keys(password)

    def click(self, button):
        login_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(button))
        login_button.click()



@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Firefox()
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


class TestLoginPage:
    def test_login(self, browser):
        login_page = LoginPage(browser)
        browser.get("https://target-sandbox.my.com/")

        login_page.click(login_page.login_button)
        login_page.enter_username("ivan.milchenko.92@mail.ru")
        login_page.enter_password("i!N9&vG^TA^v3toD7zUk9D9rpidJ@#v4")
        login_page.click(login_page.login)

        assert browser.current_url == "https://target-sandbox.my.com/dashboard"
