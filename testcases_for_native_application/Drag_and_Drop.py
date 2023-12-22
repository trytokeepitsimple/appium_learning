import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'

#desired_caps['app']='C:\\Users\\Devesh_SSD\\PycharmProjects\\appium_testing\\app\\Drag-Sort Demos_com.mobeta.android.demodslv.apk'

desired_caps['appPackage'] = 'com.mobeta.android.demodslv'
desired_caps['appActivity'] = '.Launcher'

appium_service = AppiumService()
appium_service.start()

print("appium service started succesfully")

appium_server_url = 'http://localhost:4723'

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(desired_caps))

driver.find_element(AppiumBy.ID , 'com.android.permissioncontroller:id/continue_button').click()
time.sleep(2)
driver.find_element(AppiumBy.ID , 'android:id/button1').click()
time.sleep(2)

elements=driver.find_elements(AppiumBy.ID,'com.mobeta.android.demodslv:id/activity_title')[0].click()
time.sleep(2)

elements2 = driver.find_elements(AppiumBy.XPATH,'(//android.widget.ImageView[@resource-id="com.mobeta.android.demodslv:id/drag_handle"])')

actions = TouchAction(driver)
actions.press(elements2[0]).wait(2000).move_to(elements2[2]).perform().release()

time.sleep(2)
driver.quit()
appium_service.stop()