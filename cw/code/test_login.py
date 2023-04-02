from pages.login_page import LoginPage


def test_login(browser):
    browser.delete_all_cookies()
    browser.refresh()
    LoginPage(browser).login()
