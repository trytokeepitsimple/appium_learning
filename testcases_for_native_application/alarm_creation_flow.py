import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService

from appium.webdriver.common.appiumby import AppiumBy

# capabilities = dict(
#     platformName='Android',
#     automationName='uiautomator2',
#     deviceName='Android',
#     language='en',
#     locale='US',
#     appPackage='com.android.contacts',
#     appActivity='.activities.PeopleActivity'
#
# )

appium_service = AppiumService()
appium_service.start()

print("appium service started succesfully")

appium_server_url = 'http://localhost:4724'

# driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
#
# time.sleep(5)
#
# driver.implicitly_wait(10)
# driver.find_element(AppiumBy.ID, 'com.android.contacts:id/add_contact_button').click()
# print("Add Contact Button got clicked")

capabilities1 = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    language='en',
    locale='US',
    appPackage='com.google.android.deskclock',
    appActivity='com.android.deskclock.DeskClock'

)

driver1 = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities1))

alarm_section = driver1.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.google.android.deskclock:id/navigation_bar_item_icon_view"])[1]')
print(alarm_section)
alarm_section.click()
time.sleep(5)
add_alarm_button = driver1.find_element(AppiumBy.ID , 'com.google.android.deskclock:id/fab')
print(add_alarm_button)
add_alarm_button.click()
time.sleep(5)
print("add alarm button got clicked")
hour_selection = driver1.find_element(AppiumBy.ACCESSIBILITY_ID , "8 o'clock")
print("Hour Button is available", hour_selection)
hour_selection_click=hour_selection.click()
time.sleep(5)
minute_selection = driver1.find_element(AppiumBy.ACCESSIBILITY_ID , '25 minutes')
print("Minute Selection is now availble", minute_selection)
minute_selection.click()
time.sleep(5)
am_button = driver1.find_element(AppiumBy.ID , 'com.google.android.deskclock:id/material_clock_period_am_button')
print("AM button is now available",am_button)
time.sleep(5)
am_button.click()
time.sleep(5)

alarm_creation_btn = driver1.find_element(AppiumBy.ID , 'com.google.android.deskclock:id/material_timepicker_ok_button')
print("Alarm Creation button is also available")
alarm_creation_btn.click()
print("alarm creation button got clicked")
time.sleep(10)
driver1.quit()
appium_service.stop()
print("appium service stopped successfully")

