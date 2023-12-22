import time
from pathlib import Path

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {}

desired_caps['platformName'] = 'Android'

desired_caps['automationName'] = 'UiAutomator2'

desired_caps['platformVersion'] = '11'

desired_caps['deviceName'] = 'Pixel 6a API 30'

desired_caps['app'] = str(Path().absolute().parent)+'\\app\\instagram-311-0-0-32-118.apk'

#desired_caps['appPackage'] = 'flipboard.app'

#desired_caps['appActivity'] = 'flipboard.activities.FirstLaunchCoverActivity'

#desired_caps['autoGrantPermissions'] = True

appium_service = AppiumService()
appium_service.start()

print("appium service started succesfully")

appium_server_url = 'http://localhost:4724'

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(desired_caps))

time.sleep(10)
# driver.find_element(AppiumBy.ID,'flipboard.app:id/icon_button_text').click()
#
# for i in range(1,4):
#     time.sleep(1)
#     driver.find_element(AppiumBy.ID , 'flipboard.app:id/topic_picker_topic_row_topic_tag')[i].click()
#
# driver.find_element(AppiumBy.ID , 'flipboard.app:id/icon_button_text').click()

appium_service.stop()