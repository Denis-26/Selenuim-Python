from selenium.webdriver.common.keys import Keys

from base_page import BasePage
from element import BaseFieldElement
from locators import AuthPageLocators, MainPageLocators, SettingsPageLocators
from values import Values


class UsernameField(BaseFieldElement):
    locator = AuthPageLocators.USERNAME_FIELD


class PasswordField(BaseFieldElement):
    locator = AuthPageLocators.PASSWORD_FIELD


class AuthPage(BasePage):

    username_field = UsernameField()
    password_field = PasswordField()

    def submit(self):
        element = self.driver.find_element(*AuthPageLocators.AUTH_BUTTON)
        element.click()

    def fill_username(self, username):
        self.username_field = username

    def fill_password(self, password):
        self.password_field = password


class MainPage(BasePage):

    def open_settings(self):
        self.driver.find_element(*MainPageLocators.SETTINGS_BUTTON).click()

    def get_shooting_dates_str(self):
        shooting_date_str = self.driver.find_elements(*MainPageLocators.STATISTICS_BLOCK)[1]
        return str(shooting_date_str.text)


class SettingsPage(BasePage):

    def fill_first_date(self):
        date_inputs = self.driver.find_elements(*SettingsPageLocators.DATE_INPUT)
        date_inputs[0].send_keys(Keys.BACKSPACE * len(Values.DATE_PLUG))
        date_inputs[0].send_keys(Values.START_SHOOTING_DAY)

    def fill_second_date(self):
        date_inputs = self.driver.find_elements(*SettingsPageLocators.DATE_INPUT)
        date_inputs[1].send_keys(Keys.BACKSPACE * len(Values.DATE_PLUG))
        date_inputs[1].send_keys(Values.END_SHOOTING_DAY)

    def save(self):
        self.driver.find_element(*SettingsPageLocators.SAVE_BUTTON).click()

    def go_main_page(self):
        self.driver.find_element(*SettingsPageLocators.HOME_BUTTON).click()

