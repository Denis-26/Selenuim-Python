from selenium.webdriver.common.by import By


class AuthPageLocators(object):
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    AUTH_BUTTON = (By.CSS_SELECTOR, 'input.js-submit-btn')


class MainPageLocators(object):
    SETTINGS_BUTTON = (By.LINK_TEXT, "Настройки")
    STATISTICS_BLOCK = (By.CSS_SELECTOR, "div.statistic a")


class SettingsPageLocators(object):
    SETTINGS_BUTTON = (By.LINK_TEXT, "Настройки")
    DATE_INPUT = (By.CSS_SELECTOR, "div.date-input input")
    SAVE_BUTTON = (By.LINK_TEXT, "Сохранить")
    HOME_BUTTON = (By.CSS_SELECTOR, "span.logo")
