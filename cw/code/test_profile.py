from ui.fixtures import get_driver
from ui.pages.login_page import LoginPage
from ui.pages.categories_page import CategoriesPage
from ui.pages.profile_page import ProfilePage


class TestChangeProfile():
    driver = get_driver('chrome')

    def reload(self, categories_page):
        categories_page.navigateToBalance()
        categories_page.navigateToProfile()

    def test_change_profile(self):
        login_page = LoginPage(self.driver)
        login_page.render_page()
        login_page.login()

        categories_page = CategoriesPage(self.driver)
        categories_page.navigateToProfile()

        profile_page = ProfilePage(self.driver)
        profile_page.verify_change_data()

        self.reload(categories_page)

        profile_page.verify_change_data(False)
        profile_page.verify_empty_data()
