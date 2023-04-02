from base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    url = "https://target-sandbox.my.com/"
    email = "shlak.reg@mail.ru"
    passwd = "L4!EZQzrCqa!aRW"

    class Locators:
        SIGNIN_BTN = (By.XPATH, '//div[starts-with(@class, "responseHead-module-button")]')
        EMAIL_FIELD = (By.NAME, 'email')
        PASSWORD_FIELD = (By.NAME, 'password')
        LOGIN_BTN = (By.XPATH, '//div[starts-with(@class,"authForm-module-button")]')
    
    def login(self):
        self.render(self.url)
        
        self.find(self.Locators.SIGNIN_BTN, 10).click()

        self.find(self.Locators.EMAIL_FIELD).send_keys(self.email)
        self.find(self.Locators.PASSWORD_FIELD).send_keys(self.passwd)
        
        self.find(self.Locators.LOGIN_BTN).click()