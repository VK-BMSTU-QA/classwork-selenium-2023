from selenium.webdriver.common.by import By


class BasePageLocators:
    locator_billing = (By.XPATH, '//a[@href="/billing"]')
    locator_profile = (By.XPATH, '//a[@href="/profile"]')


class LoginPageLocators:
    email_input = (By.XPATH, '//input[@name="email"]')
    password_input = (By.XPATH, '//input[@name="password"]')
    login_button = (By.CLASS_NAME, 'responseHead-module-button-2yl51i')
    login_button_form = (By.CLASS_NAME, 'authForm-module-button-1u2DYF')


class ProfilePageLocators:
    name_input = (By.XPATH, '//div[@class="input" and @data-name = "fio"]/div/input')
    phone_number_input = (By.XPATH, '//div[@data-name="phone"]/div/input')
    save_button = (By.XPATH, '//div[text() = "Сохранить"]')
