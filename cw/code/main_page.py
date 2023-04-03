from base_page import BasePage
from selenium.webdriver.common.by import By


class MainPageLocators:
    CAMPAIGN_BUTTON = (By.CSS_SELECTOR, '.center-module-campaigns-3KazFg')
    SEGMENTS_BUTTON = (By.CSS_SELECTOR, '.center-module-segments-1MqckW')
    BALANCE_BUTTON = (By.CSS_SELECTOR, '.center-module-billing-1cIfj4')
    STATISTICS_BUTTON = (By.CSS_SELECTOR, '.center-module-statistics-2Wbrwh')
    PRO_BUTTON = (By.CSS_SELECTOR, '.center-module-pro-1lbACy')
    PROFILE_BUTTON = (By.CSS_SELECTOR, '.center-module-profile-1kuUOa')


class MainPage(BasePage):
    base_url = "https://target-sandbox.my.com/"

    def click(self, locator):
        self.find(locator).click()