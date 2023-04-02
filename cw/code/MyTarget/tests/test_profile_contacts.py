from MyTarget.pages.profile_contacts_page import ProfileContactsPage
from MyTarget.base_case import BaseCase
import pytest


class TestProfileContactsPage(BaseCase):
    # @pytest.mark.skip("SKIP")
    def test_change_data(self):
        contacts_page = ProfileContactsPage(self.driver)
        contacts_page.open()
        contacts_page.set_full_name("George Illar Vladimir")
        contacts_page.set_phone("+79356313456")
        contacts_page.save()

        contacts_page.open()
        contacts_page.check_full_name("George Illar Vladimir")
        contacts_page.check_phone("+79356313456")

        