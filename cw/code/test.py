from basic_case import BasicCase
from main_page import MainPage
from login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class InfoLocators:
    name = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[2]/div[1]/div/div/input')
    PHONE = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[4]/div[1]/div/div/input')
    CONFIRM = (By.CSS_SELECTOR, '.button')


class TestLoginPage:
    def test_login(self, browser):
        login_page = LoginPage(browser)
        browser.get("https://target-sandbox.my.com/")

        login_page.click(login_page.login_button)
        login_page.enter_username("ivan.milchenko.92@mail.ru")
        login_page.enter_password("i!N9&vG^TA^v3toD7zUk9D9rpidJ@#v4")
        login_page.click(login_page.log_in)

        assert browser.current_url == "https://target-sandbox.my.com/dashboard"


class TestInforamtion(BasicCase):
    name = 'Fedorov Vasily Ivanovich'
    phone = '89031231212'

    def test_edit_name(self):
        main_page = MainPage(self.driver)
        main_page.render('https://target.my.com/profile/contacts')

        name_field = main_page.find(InfoLocators.name)
        name_field.send_keys(Keys.CONTROL + "a")
        name_field.send_keys(Keys.DELETE)
        name_field.send_keys(self.name)

        confirm_button = main_page.find(InfoLocators.CONFIRM)
        confirm_button.click()

        self.driver.refresh()
        name_field = main_page.find(InfoLocators.name)
        assert name_field.get_attribute('value') == self.name

    def test_number(self):
        main_page = MainPage(self.driver)
        main_page.render('https://target.my.com/profile/contacts')

        phone_field = main_page.find(InfoLocators.PHONE)
        phone_field.send_keys(Keys.CONTROL + "a")
        phone_field.send_keys(Keys.DELETE)
        phone_field.send_keys(self.phone)

        confirm_button = main_page.find(InfoLocators.CONFIRM)
        confirm_button.click()

        self.driver.refresh()
        phone_field = main_page.find(InfoLocators.PHONE)
        assert phone_field.get_attribute('value') == self.phone.replace('8', '+7')


class TestNavigation(BasicCase):
    cases = [
        {
            "start": {
                "name": "dashboard",
                "class_name": "head-module-logoLink-3VcmqY",
                "url": "https://target.my.com/dashboard",
            },
            "destination": {
                "name": "billing",
                "class_name": ".center-module-billing-1cIfj4",
                "url": "https://target.my.com/billing",
            },
        },
        {
            "start" : {
                "name" : "dashboard",
                "class_name" : "head-module-logoLink-3VcmqY",
                "url" : "https://target.my.com/dashboard",
            },
            "destination" : {
                "name" : "profile",
                "class_name" : ".center-module-profile-1kuUOa",
                "url" : "https://target.my.com/profile/contacts",
            },
        }
    ]

    def test_navigation(self):
        main_page = MainPage(self.driver)

        for value in self.cases:
            start = value["start"]
            destination = value["destination"]
            start_class_name = start["class_name"]
            destination_class_name = destination["class_name"]
            start_url = start["url"]
            destination_url = destination["url"]

            start_button = (By.CLASS_NAME, start_class_name)
            destination_button = (By.CSS_SELECTOR, destination_class_name)

            main_page.click(start_button)
            try:
                assert self.driver.current_url == start_url
            except AssertionError:
                main_page.click(start_button)
                assert self.driver.current_url == start_url

            main_page.click(destination_button)
            try:
                assert self.driver.current_url == destination_url
            except AssertionError:
                main_page.click(destination_button)
                assert self.driver.current_url == destination_url

            self.driver.get(start_url)
