from selenium.webdriver.common.by import By


class BasePageLocators:
    a = ()


class AuthorizeLocators:
    LOGIN_BUTTON = (By.CLASS_NAME, 'responseHead-module-button-2yl51i')
    LOGIN_BUTTON_FORM = (By.CLASS_NAME, 'authForm-module-button-1u2DYF')
    INPUT_EMAIL = (By.CLASS_NAME, 'authForm-module-input-3j70Dv')
    INPUT_PASSWORD = (By.CLASS_NAME, 'authForm-module-inputPassword-3t7Qac')
