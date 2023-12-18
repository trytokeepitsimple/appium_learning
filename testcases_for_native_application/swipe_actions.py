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


#value of end y should be less than start y - > because we are moving upword

driver.swipe(333,1800,996,1200,1000)
driver.swipe(333,1800,996,1200,1000)
driver.swipe(333,1800,996,1200,1000)
driver.swipe(333,1800,996,1200,1000)
driver.swipe(333,1800,996,1200,1000)

#value of start y should be less than end y - > because we are moving downword

driver.swipe(333,1200,996,1800,1000)
driver.swipe(333,1200,996,1800,1000)
driver.swipe(333,1200,996,1800,1000)
driver.swipe(333,1200,996,1800,1000)
driver.swipe(333,1200,996,1800,1000)

time.sleep(5)
driver.quit()
appium_service.stop()