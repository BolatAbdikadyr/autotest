from appium.webdriver.common.mobileby import MobileBy


def locators():
    locator_dict = {
    'login/registration': (MobileBy.ACCESSIBILITY_ID, 'Вход/Регистрация'),
    'login_text_editor': (MobileBy.XPATH, "//android.widget.EditText[@bounds='[48,717][672,813]']"),
    'login_text_editor2': (MobileBy.XPATH, "//android.widget.EditText[@bounds='[48,244][672,340]']"),
    'pass_text_editor': (MobileBy.XPATH, "//android.widget.EditText[@bounds='[48,426][672,522]']"),
    'login_button': (MobileBy.ACCESSIBILITY_ID, "Войти"),
    'open_new_depoz_or_schet': (MobileBy.ACCESSIBILITY_ID, "Открыть новый депозит или счет"),
    'close': (MobileBy.ACCESSIBILITY_ID, "Маска"),
    }
    return locator_dict


#'login_text_editor': (MobileBy.XPATH, "//android.widget.EditText[@elementid='00000000-0000-0454-0000-003500000004']"),
# "//android.widget.EditText[@text='']"
#     'select-subj': (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button[1]"),
#     'select-course': (MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button[2]"),
#     'readnfcdata': (MobileBy.ACCESSIBILITY_ID, "Read NFC Data"),
#     'ok': (MobileBy.ACCESSIBILITY_ID, "OK"),
#     'ped': (MobileBy.ACCESSIBILITY_ID, "Педагогика"),
#     'rmt': (MobileBy.ACCESSIBILITY_ID, "РМТ"),
#     'upr-po': (MobileBy.ACCESSIBILITY_ID, "Управление ПО"),
#     'gis': (MobileBy.ACCESSIBILITY_ID, "GIS"),
#     'block': (MobileBy.ACCESSIBILITY_ID, "BlockChain"),
#     '231': (MobileBy.ACCESSIBILITY_ID, "SE-231M"),
#     '232': (MobileBy.ACCESSIBILITY_ID, "SE-232M"),