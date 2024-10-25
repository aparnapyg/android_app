"""Created December 29th, 2020 by Alysha Kester-Terry
    This Base Page object locator strategy was gleaned with much gratitude from
    http://elementalselenium.com/tips/9-use-a-base-page-object
"""
from setup_helpers.locators_util import BaseLocators


class BasePageLocators:
    """Initializes the driver for use on all other pages and defines objects that are on almost every page"""

    def __init__(self, driver):
        self.driver = driver


class AndroidPageLocators(BasePageLocators):
    """Android App Page Locators"""

    def app_link(self):
        return BaseLocators.element_by_xpath(self, '//*[@text="App"]')

    def alert_dialog_link(self):
        return BaseLocators.element_by_xpath(self,'//*[@text="Alert Dialogs"]')

    def cancel_dialog_with_message_link(self):
        return BaseLocators.element_by_xpath(self,'//*[@text="OK Cancel dialog with a message"]')

    def get_text_from_modal(self):
        return BaseLocators.element_by_xpath(self, '//android.widget.TextView[@resource-id="android:id/alertTitle"]').text
