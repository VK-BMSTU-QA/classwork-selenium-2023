from ui.fixtures import get_driver
from ui.pages.login_page import LoginPage


class TestLogin():
    driver = get_driver('chrome')

    def test_login(self):
        login_page = LoginPage(self.driver)

        login_page.render_page()
        login_page.login()

        login_page.check_header_email()
