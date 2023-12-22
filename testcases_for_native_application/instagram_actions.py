import time
#from pathlib import Path

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['appPackage'] = 'com.instagram.android'
desired_caps['appActivity'] = 'com.instagram.nux.activity.BloksSignedOutFragmentActivity'

appium_service = AppiumService()
appium_service.start()
print("Appium service going up")
appium_server_url = 'http://localhost:4724'
driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(desired_caps))
driver.implicitly_wait(10)
print("App Launched ->Done")
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Username, email or mobile number').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Username, email or mobile number').send_keys('deveshshukla224@outlook.com')
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Password').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Password').send_keys('ShuklaDevesh21@#')
driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Log in"]').click()
time.sleep(5)
appium_service.stop()
print("Appium Service Going Down")