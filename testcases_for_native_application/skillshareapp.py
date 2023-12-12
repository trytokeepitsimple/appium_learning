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

desired_caps['app'] = str(Path().absolute().parent)+'\\app\\Android_Appium_Demo.apk'

desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'

desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

appium_service = AppiumService()
appium_service.start()
print("1 : Appium Service Going UP")


appium_server_url = 'http://localhost:4723'

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(desired_caps))
driver.implicitly_wait(10)

print("2 : App Launched Succesfully")

#login screen
login_btn = (driver.find_element(AppiumBy.ID, 'com.skill2lead.appiumdemo:id/Login').click())
email_field = (driver.find_element(AppiumBy.ID , 'com.skill2lead.appiumdemo:id/Et4').click())
value_in_email= driver.find_element(AppiumBy.ID , 'com.skill2lead.appiumdemo:id/Et4').send_keys("admin@gmail.com")
password_field = (driver.find_element(AppiumBy.ID , 'com.skill2lead.appiumdemo:id/Et5').click())
password_value = driver.find_element(AppiumBy.ID , 'com.skill2lead.appiumdemo:id/Et5').send_keys('admin123')
sign_in_btn = (driver.find_element(AppiumBy.ID , 'com.skill2lead.appiumdemo:id/Btn3').click())

print("3: Logged In Sucessfully")


#admin name preview panel
admin_name_input_selection = (driver.find_element(AppiumBy.ID , 'com.skill2lead.appiumdemo:id/Edt_admin').click())
admin_name_value = (driver.find_element(AppiumBy.ID , 'com.skill2lead.appiumdemo:id/Edt_admin').send_keys("Devesh Shukla"))
submit_btn = (driver.find_element(AppiumBy.ID , 'com.skill2lead.appiumdemo:id/Btn_admin_sub').click())
print("4 : Name visible on Preview Screen")
time.sleep(5)

appium_service.stop()
print("5 : Appium Service Going Down")

print("Peace :)")
