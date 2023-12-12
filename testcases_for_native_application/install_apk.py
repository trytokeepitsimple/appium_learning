from pathlib import Path

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService


desired_caps = {}

desired_caps['platformName'] = 'Android'

desired_caps['automationName'] = 'UiAutomator2'

desired_caps['platformVersion'] = '11'

desired_caps['deviceName'] = 'Pixel 6a API 30'

desired_caps['app'] = str(Path().absolute().parent)+'\\app\\Android_Appium_Demo.apk'

desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'

desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

appium_service = AppiumService()
appium_service.start()

print("appium service started succesfully")

appium_server_url = 'http://localhost:4723'

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(desired_caps))

appium_service.stop()