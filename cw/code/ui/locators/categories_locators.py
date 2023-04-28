from selenium.webdriver.common.by import By


class CategoriesPageLocators():
    BALANCE_CATEGORIES_PAGE = (
        By.CLASS_NAME, 'deposit__payment-form__container')

    STATS_CATEGORIES_PAGE = (
        By.CLASS_NAME, 'statistic-page-nt__no-active-campaigns-text')

    PROFILE_CATEGORIES_PAGE = (
        By.CLASS_NAME, 'profile__list')

    NAV_BALANCE_CATEGORIES_PAGE = (By.XPATH, '//a[@href="/billing"]')

    NAV_PROFILE_CATEGORIES_PAGE = (By.XPATH, '//a[@href="/profile"]')

    NAV_STATS_CATEGORIES_PAGE = (By.XPATH, '//a[@href="/statistics"]')
