from global_settings.base_test import BaseTest
from selenium.webdriver.support import expected_conditions as EC


class first_test(BaseTest):
    def test_open_dep(self):
        self.wait.until(EC.element_to_be_clickable(self.all_locators['open_new_depoz_or_schet'])).click()
        self.wait.until(EC.element_to_be_clickable(self.all_locators['close'])).click()
