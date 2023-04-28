from ui.fixtures import get_driver
from ui.pages.categories_page import CategoriesPage
from ui.pages.login_page import LoginPage


class TestCategories():
    driver = get_driver('chrome')

    def test_header_categories(self):
        login_page = LoginPage(self.driver)
        login_page.render_page()

        login_page.login()

        categories_page = CategoriesPage(self.driver)
        categories_page.test_navigation()
