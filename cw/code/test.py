from contextlib import contextmanager
import allure
import pytest
from _pytest.fixtures import FixtureRequest
import os
import shutil
import sys
import time
import random

from BasePage import BasePage
from HelperLogin import HelperLogin

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'https://target-sandbox.my.com/'
helper = HelperLogin(url)


class TestLogin(BasePage):
    url = 'https://target-sandbox.my.com/'

    def test_login(self):
        helper.login()

class TestHeaderLinks(BasePage):
    url = 'https://target-sandbox.my.com/'
    COMPANIES = 0
    AUDIENCE = 1
    BALANCE = 2
    STATISTIC = 3
    PRO = 4
    PROFILE = 5
    INSTRUMENTS = 6
    HELP = 7
    UL = 'ul'
    LI = 'li'

    def twice_jump_from(self, start, to1, to2):
        self.render(self.url)
        self.find((By.TAG_NAME, self.UL)).find_elements(By.TAG_NAME, self.LI)[start].click()
        self.find((By.TAG_NAME, self.UL)).find_elements(By.TAG_NAME, self.LI)[to1].click()
        self.find((By.TAG_NAME, self.UL)).find_elements(By.TAG_NAME, self.LI)[start].click()
        self.find((By.TAG_NAME, self.UL)).find_elements(By.TAG_NAME, self.LI)[to2].click()

    def test_header(self):
        helper.login()
        self.twice_jump_from(self.COMPANIES, self.STATISTIC, self.AUDIENCE)

class TestChangeProfileData(BasePage):
    url = 'https://target-sandbox.my.com/profile/contacts'
    X_INPUT_NAME = '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[2]/div[1]/div/div/input'
    X_INPUT_NUMBER = '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[4]/div[1]/div/div/input'
    X_BUTTON_SEND = '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/button/div'

    def change_data(self, name = None, number = None):
        new_name, new_number = 'Petya', "+72351241221"

        if name != None:
            new_name = name
        if number != None:
            new_number = number

        self.render(self.url)
        input_name = self.find((By.XPATH, self.X_INPUT_NAME))
        input_name.send_keys(Keys.CONTROL + "a")
        input_name.send_keys(Keys.DELETE)
        input_name.send_keys(new_name)

        input_number = self.find((By.XPATH, self.X_INPUT_NUMBER))
        input_number.send_keys(Keys.CONTROL + "a")
        input_number.send_keys(Keys.DELETE)
        input_number.send_keys(new_number)

        self.find((By.XPATH, self.X_BUTTON_SEND)).click()

        return new_name, new_number

    def check_data(self, name = '', number = ''):
        self.render(self.url)
        received_name = self.find((By.XPATH, self.X_INPUT_NAME)).get_attribute("value")
        received_number = self.find((By.XPATH, self.X_INPUT_NUMBER)).get_attribute("value")

        if (received_name != str(name)):
            raise Exception("names does not equal", received_name, str(name))
        if (received_number != str(number)):
            raise Exception("numbers does not equal", received_number, str(number))

    def test_profile_input_both_rand(self):
        helper.login()
        name, number = self.change_data()
        self.check_data(name, number)

    def test_profile_input_real_data(self):
        helper.login()
        self.change_data('IVAN', '+88005553535')
        self.check_data('IVAN', '+88005553535')

    def test_profile_input_clear(self):
        helper.login()
        print(self.change_data('', ''))
        self.check_data('', '')
