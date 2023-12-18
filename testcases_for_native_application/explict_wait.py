import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {}

desired_caps['platformName'] = 'Android'

desired_caps['automationName'] = 'UiAutomator2'

desired_caps['platformVersion'] = '11'

desired_caps['deviceName'] = 'Pixel 6a API 30'

desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'

desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

appium_service = AppiumService()
appium_service.start()
print("1 : Appium Service Going UP")


appium_server_url = 'http://localhost:4723'

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(desired_caps))
driver.implicitly_wait(10)

print("2 : App Launched Succesfully")

wait = WebDriverWait(driver,5)

element1 = wait.until(EC.element_to_be_clickable((AppiumBy.ID , 'com.skill2lead.appiumdemo:id/LongClick')))
action = TouchAction(driver)
action.long_press(element1).wait(2000).release().perform()
print("3 : Long Press happened - Button Got Clicked")
element2 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"UiSelector().clickable")
#element2 = wait.until(EC.element_to_be_clickable((AppiumBy.ID ,'com.skill2lead.appiumdemo:id/et_email')))
element2.click()
element2.send_keys('admin@gmail.com')
print("4 : Value Entered in Input ")
element3 = driver.find_element(AppiumBy.ID, 'android:id/button1')
element3.click()
print("5 : Submitted Value")
time.sleep(5)
appium_service.stop()
print("6 : Appium Service Going Down")

print("Peace :)")