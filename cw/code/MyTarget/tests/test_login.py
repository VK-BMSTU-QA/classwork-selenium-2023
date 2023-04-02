
import pytest
from MyTarget.pages.login_page import LoginPage
from MyTarget.base_case import BaseCase

# @pytest.mark.skip("SKIP")
def test_login(browser):
    browser.delete_all_cookies()
    browser.refresh()
    login_page = LoginPage(browser)
    login_page.login()