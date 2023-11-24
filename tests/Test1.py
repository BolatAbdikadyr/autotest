import time
import os
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open('../creds.conf') as f:
    lines = f.readlines()

login = lines[0].strip()
passwd = lines[1].strip()

desired_cap = {
    "platformName": "Android",
    "appium:platformVersion": "10",
    "appium:appiumdeviceName": "ZTY9TOQG4HLVA6ZD",
    "appium:app": "C:\\Users\\bolata0210\\Downloads\\app.apk",
    "appium:ignoreHiddenApiPolicyError": 'true'
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
wait = WebDriverWait(driver, 30)

wait.until(EC.element_to_be_clickable((MobileBy.ID, "kz.kmf.employee:id/login_et"))).set_value(os.getenv("login"))

wait.until(EC.element_to_be_clickable((MobileBy.ID, "kz.kmf.employee:id/password_et"))).set_value(os.getenv("password"))

wait.until(EC.element_to_be_clickable((MobileBy.ID, "kz.kmf.employee:id/login_btn"))).click()

wait.until(EC.presence_of_element_located((MobileBy.ID, "kz.kmf.employee:id/roles_rv")))

driver.find_elements(MobileBy.ID, "kz.kmf.employee:id/title")[0].click()
driver.find_element(MobileBy.ID, "kz.kmf.employee:id/close_iv").click()

time.sleep(8)

wait.until(EC.presence_of_element_located((MobileBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button"))).click()
wait.until(EC.presence_of_element_located((MobileBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button"))).click()
wait.until(EC.presence_of_element_located((MobileBy.ID, "com.android.permissioncontroller:id/permission_allow_button"))).click()
wait.until(EC.presence_of_element_located((MobileBy.ID, "com.android.permissioncontroller:id/permission_allow_button"))).click()
wait.until(EC.presence_of_element_located((MobileBy.ID, "com.android.permissioncontroller:id/permission_allow_button"))).click()

