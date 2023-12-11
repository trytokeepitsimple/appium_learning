import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import Select

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    language='en',
    locale='US',
    appPackage='com.google.android.dialer',
    appActivity='.extensions.GoogleDialtactsActivity'

)

appium_service = AppiumService()
appium_service.start()

print("appium service started succesfully")

appium_server_url = 'http://localhost:4723'

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

time.sleep(5)
driver.find_element(AppiumBy.ID, 'com.google.android.dialer:id/dialpad_fab').click()
print("1 : DailPad is Visible, Will start keying in value")
driver.find_element(AppiumBy.ID, 'com.google.android.dialer:id/seven').click()
driver.find_element(AppiumBy.ID, 'com.google.android.dialer:id/eight').click()
driver.find_element(AppiumBy.ID, 'com.google.android.dialer:id/nine').click()
driver.find_element(AppiumBy.ID, 'com.google.android.dialer:id/seven').click()
driver.find_element(AppiumBy.ID, 'com.google.android.dialer:id/three').click()
driver.find_element(AppiumBy.ID, 'com.google.android.dialer:id/two').click()
driver.find_element(AppiumBy.ID, 'com.google.android.dialer:id/one').click()
driver.find_element(AppiumBy.ID, 'com.google.android.dialer:id/zero').click()
print("2 : Number keyed In successfully")
driver.find_element(AppiumBy.ID, 'com.google.android.dialer:id/dialpad_voice_call_button').click()
print("3 : Dial Button Clicked Successfully")
time.sleep(5)
driver.quit()
appium_service.stop()
print("appium service stopped successfully")
