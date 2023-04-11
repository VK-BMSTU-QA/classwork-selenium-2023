from selenium.webdriver.common.by import By


class BasePageLocators:
    base = ()


class AuthorizeLocators:
    LOGIN_BUTTON = (By.XPATH, '//div[starts-with(@class, "responseHead-module-button")]')
    LOGIN_BUTTON_FORM = (By.XPATH, '//div[starts-with(@class,"authForm-module-button")]')
    INPUT_EMAIL = (By.NAME, 'email')
    INPUT_PASSWORD = (By.NAME, 'password')

class HeaderLocators:
    BILLING_BUTTON = (By.XPATH, '//a[@href="/billing"]')
    PROFILE_BUTTON = (By.XPATH, '//a[@href="/profile"]')

class ContactLocators:
    FIO_INPUT = (
            By.XPATH,
            '//div[starts-with(@class, "js-contacts-field-name")]/div/div/input'
        )
    SAVE_BUTTON = (By.XPATH, '//button[contains(@class, "button_submit")]')
