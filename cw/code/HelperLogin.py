from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from contextlib import contextmanager

from BasePage import BasePage

class HelperLogin(BasePage):
    def __init__(self, url):
        self.url = url
        self.LOGIN = 'vanyabiryukov@yandex.ru'
        self.PASSWD = '123qwe1'
        self.is_logined = False

    def login(self):
        X_BUTTON_LOGIN = '/html/body/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]'
        X_BUTTON_AUTH = '/html/body/div[2]/div/div[2]/div/div[4]/div[1]'
        EMAIL = 'email'
        PASSWORD = 'password'


        if self.is_logined:
            return

        self.render(self.url)
        btn = self.find((By.XPATH, X_BUTTON_LOGIN), 10)

        btn.click()
        input_login = self.find((By.NAME, EMAIL)).send_keys(self.LOGIN)

        input_password = self.find((By.NAME, PASSWORD)).send_keys(self.PASSWD)
        self.find((By.XPATH, X_BUTTON_AUTH)).click()

        self.is_logined = True
