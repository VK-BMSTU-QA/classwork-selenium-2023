from selenium.webdriver.common.by import By


class BasePageLocators:
    base = ()


class AuthorizeLocators:
    LOGIN_BUTTON = (By.CLASS_NAME, 'responseHead-module-button-2yl51i')
    LOGIN_BUTTON_FORM = (By.CLASS_NAME, 'authForm-module-button-1u2DYF')
    INPUT_EMAIL = (By.CLASS_NAME, 'authForm-module-input-3j70Dv')
    INPUT_PASSWORD = (By.CLASS_NAME, 'authForm-module-inputPassword-3t7Qac')

class HeaderLocators:
    BILLING_BUTTON = (By.XPATH, '//a[@href="/billing"]')
    PROFILE_BUTTON = (By.XPATH, '//a[@href="/profile"]')

class ContactLocators:
    FIO_INPUT = (
            By.XPATH,
            "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[2]/div[1]/div/div/"
            "input"
        )
    SAVE_BUTTON = (
        By.XPATH,
        "/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/button"
    )
