from basic_case import BasicCase
from pages.profile_page import ProfileContactsPage
import random


class TestProfileContacts(BasicCase):
    def generate_name(self):
        first_names = ["Иван", "Петр", "Алексей", "Андрей", "Дмитрий"]
        last_names = ["Смирнов", "Иванов", "Кузнецов", "Попов", "Лебедев"]
        second_names = ["Александрович", "Сергеевич", "Иванович", "Петрович", "Дмитриевич"]

        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        second_name = random.choice(second_names)

        return f"{second_name} {first_name} {last_name}"

    def generate_phone_number(self):
        phone_number = "+79"
        for i in range(9):
            phone_number += str(random.randint(0, 9))

        return phone_number

    def test_changing_contacts(self):
        page = ProfileContactsPage(self.driver)
        page.render(ProfileContactsPage.url)

        full_name = self.generate_name()
        phone_number = self.generate_phone_number()

        page.set_full_name(full_name)
        page.set_phone(phone_number)

        page.save_input()

        page.render(ProfileContactsPage.url)

        page.check_phone(phone_number)
        page.check_full_name(full_name)
