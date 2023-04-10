from selenium.webdriver.common.by import By


class BasePageLocators:
    HEADER_DASHBOARD = (By.XPATH, '//a[@href="/dashboard"]')
    HEADER_SEGMENTS = (By.XPATH, '//a[@href="/segments"]')
    HEADER_BILLING = (By.XPATH, '//a[@href="/billing"]')
    HEADER_STATISTICS = (By.XPATH, '//a[@href="//statistics"]')
    HEADER_PRO = (By.XPATH, '//a[@href="/pro"]')
    HEADER_PROFILE = (By.XPATH, '//a[@href="/profile"]')
    HEADER_TOOLS = (By.XPATH, '//a[@href="/tools"]')
    HEADER_HELP = (By.XPATH, '//a[@href="//target.my.com/help/advertisers/ru"]')


class LoginLocators:
    LOGIN_BUTTON = (By.XPATH, '//div[text() = "Войти"][1]')
    LOGIN_BUTTON_FORM = (By.XPATH, '(//div[text() = "Войти"])[2]')
    EMAIL_INPUT = (By.XPATH, '//input[@name="email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')


class ProfileLocators:
    NAME_INPUT = (By.XPATH, '//div[@class="input" and @data-name = "fio"]/div/input')
    PHONE_NUMBER_INPUT = (By.XPATH, '//div[@data-name="phone"]/div/input')
    SAVE_BUTTON = (By.XPATH, '//div[text() = "Сохранить"]')
