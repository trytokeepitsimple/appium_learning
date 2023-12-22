import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

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

element1 = driver.find_element(AppiumBy.XPATH,'//android.widget.ListView[@resource-id="android:id/list"]/android.view.ViewGroup[11]')
element2=driver.find_element(AppiumBy.XPATH,'//android.widget.ListView[@resource-id="android:id/list"]/android.view.ViewGroup[9]')
#TouchAction class object - action
actions= TouchAction(driver)
#tap is just click
# actions.tap(element1).perform()

actions.long_press(element1).perform()
actions.long_press(element2).perform()

time.sleep(5)
driver.quit()
appium_service.stop()