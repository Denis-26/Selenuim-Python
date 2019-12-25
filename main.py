import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from date_helper import DateHelper
from page import AuthPage, MainPage, SettingsPage
from utils import Utils
from values import Values


class TestDayShootingCalculation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get(Values.AUTH_URL)

        auth_page = AuthPage(driver)
        auth_page.fill_username(Values.LOGIN)
        auth_page.fill_password(Values.PASSWORD)
        auth_page.submit()

        driver.implicitly_wait(100)

        main_page = MainPage(driver)
        main_page.open_settings()

        settings_page = SettingsPage(driver)
        settings_page.fill_first_date()
        settings_page.fill_second_date()
        settings_page.save()
        settings_page.go_main_page()

        date_helper = DateHelper(Values.DATE_TEMPLATE)
        days_delta = date_helper.two_dates_delta(Values.START_SHOOTING_DAY, Values.END_SHOOTING_DAY)

        shooting_date_str = main_page.get_shooting_dates_str()
        test_string = Utils.build_shooting_date_str(Values.START_SHOOTING_DAY, Values.END_SHOOTING_DAY, days_delta)

        assert shooting_date_str == test_string

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

