import unittest
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import AppiumOptions



 # Set the desired capabilities.
desired_caps = {}
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '18.0'
desired_caps['deviceName'] = 'iPhone 16 Pro'
desired_caps['automationName'] = 'XCUITest' # Possible without.
desired_caps['app'] = '/Users/aparnaprayaga/Library/Developer/Xcode/DerivedData/UIKitCatalog-gpkuxewouiinnabhcxppieohcltt/Build/Products/Debug-iphonesimulator/UIKitCatalog.app'


appium_server_url = 'http://localhost:4723'

ios_options = XCUITestOptions()
ios_options.load_capabilities(desired_caps)

class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here

    def setUp(self) -> None:
#         self.driver = webdriver.Remote(appium_server_url, options=ios_options)
        pass

    def test_find_battery(self) -> None:
        driver = webdriver.Remote(appium_server_url, options=ios_options)
        el = webdriver.Remote(appium_server_url, options=ios_options).find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
        el.click()

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()
