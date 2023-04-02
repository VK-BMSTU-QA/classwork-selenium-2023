from basic_case import BasicCase
from pages.main_page import MainPage, MainPageLocators


class TestMain(BasicCase):
    MAP_URL = {
        MainPageLocators.CAMPAIGN_BUTTON: MainPage.base_url + 'dashboard',
        MainPageLocators.SEGMENTS_BUTTON: MainPage.base_url + 'segments',
        MainPageLocators.BALANCE_BUTTON: MainPage.base_url + 'billing',
        MainPageLocators.STATISTICS_BUTTON: MainPage.base_url + 'statistics',
        MainPageLocators.PRO_BUTTON: MainPage.base_url + 'pro',
        MainPageLocators.PROFILE_BUTTON: MainPage.base_url + 'profile',
    }

    def test_all_links(self):
        main_page = MainPage(self.driver)
        for locator, url in self.MAP_URL.items():
            main_page.click(locator)
            assert self.driver.current_url == url

    def test_jump_twice(self):
        routes = [
            {
                "start": MainPageLocators.CAMPAIGN_BUTTON,
                "finish_1": MainPageLocators.BALANCE_BUTTON,
                "finish_2": MainPageLocators.SEGMENTS_BUTTON,
            },
            {
                "start": MainPageLocators.PROFILE_BUTTON,
                "finish_1": MainPageLocators.STATISTICS_BUTTON,
                "finish_2": MainPageLocators.PRO_BUTTON,
            }
        ]

        main_page = MainPage(self.driver)

        for route in routes:
            main_page.click(route["start"])
            main_page.click(route["finish_1"])
            main_page.click(route["start"])
            main_page.click(route["finish_2"])
