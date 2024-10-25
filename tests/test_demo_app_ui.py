"""This is the sample test

Through use of the test_click_link function
script demonstrates use of python appium libraries
to print out contents of the dialog box.
"""

import unittest

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import AppiumOptions
from android_objects.android_pages import AndroidAppPage
from android_objects.android_pages import BasePage
from setup_helpers import driver_setup
from setup_helpers.PlatformType import PlatformType
from constants import constants



capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage="io.appium.android.apis",
    app=str(constants.get_android_app_path()),
    appActivity='io.appium.android.apis.ApiDemos',
    language='en',
    locale='US'
)



appium_server_url = 'http://localhost:4723'



appium_options = AppiumOptions()
appium_options.load_capabilities(capabilities)

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=appium_options)
        platform = PlatformType.android
#         desired_caps = driver_setup.get_desired_caps(PlatformType=platform, app_path=capabilities['app'],is_headless='is_headless')
        self.base_page = BasePage(self.driver)
        self.app_page = AndroidAppPage(self.driver)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_click_link(self) -> None:
        modal_text = self.app_page.navigate_app_links_verify_text_displayed_in_modal()
        print(modal_text)


if __name__ == '__main__':
    unittest.main()

