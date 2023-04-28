from ui.pages.base_page import BasePage
from ui.locators.profile_locators import ProfilePageLocators


class ProfilePage(BasePage):
    phone_number = '+74957256357'
    name = 'ФИО'

    locators = ProfilePageLocators()

    def get_phone_field(self):
        return self.find(
            self.locators.PHONE_INPUT_PROFILE_PAGE)

    def get_name_field(self):
        return self.find(
            self.locators.NAME_INPUT_PROFILE_PAGE)

    def change_data(self, phone_number, name):
        phone_field = self.get_phone_field()
        name_field = self.get_name_field()

        phone_field.clear()
        name_field.clear()

        phone_field.send_keys(phone_number)
        name_field.send_keys(name)

        self.find(
            self.locators.SUBMIT_UPDATE_PROFILE_PAGE
        ).click()

    def verify_data(self, phone_number, name, doChange):
        if doChange:
            self.change_data(phone_number, name)
        assert phone_number == self.get_phone_field().get_attribute('value')
        assert name == self.get_name_field().get_attribute('value')

    def verify_change_data(self, doChange=True):
        self.verify_data(self.phone_number, self.name, doChange)

    def verify_empty_data(self, doChange=True):
        self.verify_data('', '', doChange)
