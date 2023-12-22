import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

from testcases_for_native_application.ScrollUtil import ScrollUtil

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['appPackage'] = 'flipboard.app'
desired_caps['appActivity'] = 'flipboard.activities.LaunchActivityAlias'


appium_service = AppiumService()
appium_service.start()
appium_server_url = 'http://localhost:4724'
driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(desired_caps))
driver.implicitly_wait(10)

driver.find_element(AppiumBy.ID,'flipboard.app:id/icon_button_text').click()

driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="flipboard.app:id/topic_picker_topic_row_topic_tag" and @text="# NEWS"]').click()
driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="flipboard.app:id/topic_picker_topic_row_topic_tag" and @text="# SCIENCE"]').click()
driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="flipboard.app:id/topic_picker_topic_row_topic_tag" and @text="# TECHNOLOGY"]').click()
driver.find_element(AppiumBy.ID,'flipboard.app:id/icon_button_text').click()
driver.find_element(AppiumBy.ID,'flipboard.app:id/icon_button_text').click()
time.sleep(2)
ScrollUtil.swipeUp(4, driver)
time.sleep(2)
ScrollUtil.swipeDown(4, driver)
time.sleep(2)
ScrollUtil.swipeLeft(3, driver)
time.sleep(2)
ScrollUtil.swipeRight(3, driver)

time.sleep(2)
driver.quit()