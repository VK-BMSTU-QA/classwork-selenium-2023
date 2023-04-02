
from base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    url = "https://target-sandbox.my.com/"
    Locators = {
        "BALANCE_BTN": (By.XPATH, '//a[contains(@href, "/billing")]'),
        "DASHBOARD_BTN":  (By.XPATH, '//a[contains(@href, "/dashboard")]'),
        "SEGMENTS_BTN" : (By.XPATH, '//a[contains(@href, "/segments")]'),
        "STATISTICS_BTN" : (By.XPATH, '//a[contains(@href, "/statistics")]'),
        "PRO_BTN":  (By.XPATH, '//a[contains(@href, "/pro")]'),
        "PROFILE_BTN":  (By.XPATH, '//a[contains(@href, "/profile")]')
    }

    def menu_click(self, locator):
        self.find(locator).click()
