import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService

from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {}

desired_caps['platformName'] = 'Android'

desired_caps['automationName'] = 'UiAutomator2'

desired_caps['platformVersion'] = '11'

desired_caps['deviceName'] = 'Pixel 6a API 30'

desired_caps['appPackage'] = 'com.android.contacts'

desired_caps['appActivity'] = '.activities.PeopleActivity'


appium_service = AppiumService()
appium_service.start()

print("appium service started succesfully")

appium_server_url = 'http://localhost:4723'

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(desired_caps))

driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Jeenia").instance(0))').click()
time.sleep(5)
driver.quit()
appium_service.stop()