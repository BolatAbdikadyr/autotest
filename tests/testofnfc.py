from global_settings.base_test import BaseTest
from selenium.webdriver.support import expected_conditions as EC
import time

class nfc_check(BaseTest):
    def test_app(self):
        self.wait.until(EC.element_to_be_clickable(self.all_locators['readnfcdata'])).click()
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable(self.all_locators['ok'])).click()
        self.wait.until(EC.element_to_be_clickable(self.all_locators['select-subj'])).click()
        self.wait.until(EC.element_to_be_clickable(self.all_locators['ped'])).click()
        self.wait.until(EC.element_to_be_clickable(self.all_locators['select-subj'])).click()
        self.wait.until(EC.element_to_be_clickable(self.all_locators['rmt'])).click()
        self.wait.until(EC.element_to_be_clickable(self.all_locators['select-subj'])).click()
        self.wait.until(EC.element_to_be_clickable(self.all_locators['upr-po'])).click()
        self.wait.until(EC.element_to_be_clickable(self.all_locators['select-subj'])).click()
        self.wait.until(EC.element_to_be_clickable(self.all_locators['gis'])).click()
        self.wait.until(EC.element_to_be_clickable(self.all_locators['select-subj'])).click()
        self.wait.until(EC.element_to_be_clickable(self.all_locators['block'])).click()
        self.wait.until(EC.element_to_be_clickable(self.all_locators['select-course'])).click()
        self.wait.until(EC.element_to_be_clickable(self.all_locators['231'])).click()
        self.wait.until(EC.element_to_be_clickable(self.all_locators['select-course'])).click()
        self.wait.until(EC.element_to_be_clickable(self.all_locators['232'])).click()
        self.wait.until(EC.element_to_be_clickable(self.all_locators['readnfcdata'])).click()
        self.wait.until(EC.element_to_be_clickable(self.all_locators['ok'])).click()