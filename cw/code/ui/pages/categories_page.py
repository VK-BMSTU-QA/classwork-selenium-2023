from ui.pages.base_page import BasePage
from ui.locators.categories_locators import CategoriesPageLocators


class CategoriesPage(BasePage):
    locators = CategoriesPageLocators()

    def checkClassName(self, classNameSelector):
        assert self.find(classNameSelector)

    def test_header_categories(self, starting_element,
                               starting_element_className,
                               first_destination_element,
                               first_destination_className,
                               second_destination_element,
                               second_destination_className):

        self.find(starting_element).click()
        self.checkClassName(starting_element_className)

        self.find(first_destination_element).click()
        self.checkClassName(first_destination_className)

        self.find(starting_element).click()
        self.checkClassName(starting_element_className)

        self.find(second_destination_element).click()
        self.checkClassName(second_destination_className)

    def navigateToProfile(self):
        self.find(self.locators.NAV_PROFILE_CATEGORIES_PAGE).click()

    def navigateToBalance(self):
        self.find(self.locators.NAV_BALANCE_CATEGORIES_PAGE).click()

    def test_navigation(self):
        self.test_header_categories(
            self.locators.NAV_BALANCE_CATEGORIES_PAGE,
            self.locators.BALANCE_CATEGORIES_PAGE,
            self.locators.NAV_STATS_CATEGORIES_PAGE,
            self.locators.STATS_CATEGORIES_PAGE,
            self.locators.NAV_PROFILE_CATEGORIES_PAGE,
            self.locators.PROFILE_CATEGORIES_PAGE)
