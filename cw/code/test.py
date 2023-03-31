from contextlib import contextmanager
import allure
import pytest
from _pytest.fixtures import FixtureRequest
import os
import shutil
import sys
import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'https://target-sandbox.my.com/'
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.set_window_size(1920, 1080)

class BasePage(object):
    driver = driver
    def render(self, url):
        self.driver.get(self.url)

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

class Helper(BasePage):
    def __init__(self, url):
        self.url = url
        self.LOGIN = 'vanyabiryukov@yandex.ru'
        self.PASSWD = '123qwe1'
        self.is_logined = False

    def login(self):
        if self.is_logined:
            return

        self.render(self.url)
        btn = self.find((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]'), 10)

        btn.click()
        input_login = self.find((By.NAME, 'email')).send_keys(self.LOGIN)

        input_password = self.find((By.NAME, 'password')).send_keys(self.PASSWD)
        self.find((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[4]/div[1]')).click()

        self.is_logined = True

helper = Helper(url)


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

    def twice_jump_from(self, start, to1, to2):
        self.render(self.url)
        self.find((By.TAG_NAME, 'ul')).find_elements(By.TAG_NAME, 'li')[start].click()
        self.find((By.TAG_NAME, 'ul')).find_elements(By.TAG_NAME, 'li')[to1].click()
        self.find((By.TAG_NAME, 'ul')).find_elements(By.TAG_NAME, 'li')[start].click()
        self.find((By.TAG_NAME, 'ul')).find_elements(By.TAG_NAME, 'li')[to2].click()


    def test_header1(self):
        helper.login()
        self.twice_jump_from(self.COMPANIES, self.STATISTIC, self.AUDIENCE)

    def test_header2(self):
        helper.login()
        self.twice_jump_from(self.BALANCE, self.PROFILE, self.INSTRUMENTS)

class TestChangeProfileData(BasePage):
    url = 'https://target-sandbox.my.com/profile/contacts'

    def get_random_inputs(self):
        return random.randint(1000, 99999), f'+{random.randint(100000, 999999)}{random.randint(10000, 99999)}'

    def change_data(self, name = None, number = None):
        new_name, new_number = self.get_random_inputs()

        if name != None:
            new_name = name
        if number != None:
            new_number = number

        self.render(self.url)
        input_name = self.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[2]/div[1]/div/div/input'))
        input_name.send_keys(Keys.CONTROL + "a")
        input_name.send_keys(Keys.DELETE)
        input_name.send_keys(new_name)

        input_number = self.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[4]/div[1]/div/div/input'))
        input_number.send_keys(Keys.CONTROL + "a")
        input_number.send_keys(Keys.DELETE)
        input_number.send_keys(new_number)

        self.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/button/div')).click()

        return new_name, new_number

    def check_data(self, name = '', number = ''):
        self.render(self.url)
        received_name = self.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[2]/div[1]/div/div/input')).get_attribute("value")
        received_number = self.find((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[4]/div[1]/div/div/input')).get_attribute("value")

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
