import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from global_settings.locators import locators
from global_settings.login import perform_login


class BaseTest(unittest.TestCase):
    def setUp(self):
        desired_cap = {
            "platformName": "Android",
            "appium:platformVersion": "10",
            "appium:appiumdeviceName": "ZTY9TOQG4HLVA6ZD",
            "appium:app": "C:\\Users\\bolata0210\\Downloads\\app-release.apk",
            "appium:automationName": "UiAutomator2"
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
        self.wait = WebDriverWait(self.driver, 30)
        self.all_locators = locators()
        perform_login(self.driver, self.wait, self.all_locators)

    def tearDown(self):
        pass
