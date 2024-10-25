"""
constants used in the framework
"""
import os

# capabilities = dict(
#     platformName='ios',
#     automationName='xcuitest',
#     deviceName='Android',
#     appPackage="io.appium.android.apis",
#     app="/Users/aparnaprayaga/PycharmProjects/pythonProject2/resources/ApiDemos-debug.apk",
#     appActivity='io.appium.android.apis.ApiDemos',
#     language='en',
#     locale='US'
# )

class constants:
    def get_android_app_path():
        return  os.path.realpath(os.getcwd()+'/resources/ApiDemos-debug.apk')