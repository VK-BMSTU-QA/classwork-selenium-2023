from MyTarget.pages.main_page import MainPage
from MyTarget.base_case import BaseCase
import pytest

class TestMainPage(BaseCase):
    
    # @pytest.mark.skip("SKIP")
    def test_all_menu(self):
        main_page = MainPage(self.driver)
        for key, locator in main_page.Locators.items():
            main_page.menu_click(locator)
   
    # @pytest.mark.skip("SKIP")
    def test_menu_double_jumps(self):
        jumps = [
            {
            "from": MainPage.Locators["BALANCE_BTN"],
            "to": [MainPage.Locators["DASHBOARD_BTN"], MainPage.Locators["STATISTICS_BTN"]]
        },
        {
            "from": MainPage.Locators["PROFILE_BTN"],
            "to": [MainPage.Locators["SEGMENTS_BTN"], MainPage.Locators["PRO_BTN"]]
        }
        ]
        main_page = MainPage(self.driver)

        for jump in jumps:
            for to in jump["to"]:
                main_page.menu_click(jump["from"])
                main_page.menu_click(to)
                

