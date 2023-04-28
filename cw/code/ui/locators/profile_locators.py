from selenium.webdriver.common.by import By


class ProfilePageLocators():
    PHONE_INPUT_PROFILE_PAGE = (
        By.XPATH, '//div[@class="js-contacts-field-phone profile__list__row__input"]/div/div/input')

    NAME_INPUT_PROFILE_PAGE = (
        By.XPATH, '//div[@class="input" and @data-name = "fio"]/div/input')

    SUBMIT_UPDATE_PROFILE_PAGE = (
        By.XPATH, '//button[@class="button button_submit" and @data-class-name="Submit"]')
