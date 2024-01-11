import allure
import pytest
import time

from allure_commons.types import AttachmentType
#from pathlib import Path
#import json
from appium import webdriver
from appium.options.android import UiAutomator2Options
#from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy


def setup_function(function):
    # appium_service
    # global appium_service
    #
    # appium_service = AppiumService()
    # appium_service.start()
    print("1 : Appium Service Going UP")
    appium_server_url = 'http://localhost:4723'

    # capabilities
    desired_caps = {}

    desired_caps['platformName'] = 'Android'

    desired_caps['automationName'] = 'UiAutomator2'

    desired_caps['platformVersion'] = '11'

    desired_caps['deviceName'] = 'Pixel 6a API 30'

    # desired_caps['app'] = str(Path().absolute().parent)+'\\app\\Android_Appium_Demo.apk'

    desired_caps['appPackage'] = 'com.rove.staging'

    desired_caps['appActivity'] = '.MainActivity'

    global driver
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(desired_caps))
    driver.implicitly_wait(10)


def teardown_function(function):
    time.sleep(10)
    driver.quit()
    # appium_service.stop()


def test_app_launched():
    # storage permission screen
    storage_permission = driver.find_element(AppiumBy.ID,
                                             'com.android.permissioncontroller:id/permission_allow_button')
    storage_permission.click()
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(), name='screenshot1',attachment_type=AttachmentType.PNG)

    # login screen - Login with Gmail
    login_by_gmail = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Continue with Google"]')
    login_by_gmail.click()
    time.sleep(7)
    print("3 : Gmail Service Opted")

    # gmail_selection
    opt_gmail_account = driver.find_element(AppiumBy.XPATH,
                                            '(//android.widget.LinearLayout[@resource-id="com.google.android.gms:id/container"])[1]/android.widget.LinearLayout')
    opt_gmail_account.click()
    time.sleep(5)
    print("4 : Gmail Account Login")
    # manual way

    print("5 :Started Getting into Charging flow")
    pairing_via_manual_method = driver.find_element(AppiumBy.XPATH,
                                                    '//android.widget.TextView[@text="Pair your charger manually"]')
    pairing_via_manual_method.click()
    time.sleep(5)
    print("6 : Manual Way Opted successfully")

    # location page
    print("7 : On Location Screen - Opting Location - By Default : Santa Ana")
    santa_ana_location_selection = driver.find_element(AppiumBy.XPATH,
                                                       '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    santa_ana_location_selection.click()
    time.sleep(5)

    # continue button on location button
    print("8 : Opting Continue on location screen")
    continue_on_location_screen = driver.find_element(AppiumBy.XPATH,
                                                      '//android.view.ViewGroup[@content-desc="Continue"]/android.view.ViewGroup')
    continue_on_location_screen.click()
    time.sleep(5)

    # opting charger number
    print("9 : Opt Charger Number")
    charger_number_input = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Charger #"]')
    charger_number_input.click()
    time.sleep(5)
    print("10 : Entering Value in charger number")
    charger_number_input.send_keys("3")
    print("11 : Opting Continue on charger number screen")
    time.sleep(2)
    continue_on_charger_number_screen = driver.find_element(AppiumBy.XPATH,
                                                            '//android.widget.TextView[@text="Continue"]')
    continue_on_charger_number_screen.click()
    time.sleep(10)

    # Payment Page
    # swipe up

    driver.swipe(650, 850, 550, 250, 2000)
    print("12 :Swiped up")
    time.sleep(5)

    # payment method selection
    payment_edit_button = driver.find_element(AppiumBy.XPATH,
                                              '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    payment_edit_button.click()
    time.sleep(2)

    # card_selection
    gpay_option = driver.find_element(AppiumBy.XPATH,
                                      '//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView')
    gpay_option.click()
    time.sleep(1)

    # save button on payment option selection page
    save_button_payment_method_selection = driver.find_element(AppiumBy.XPATH,
                                                               '//android.widget.TextView[@text="Save"]')
    save_button_payment_method_selection.click()
    time.sleep(1)

    # autorize button
    authorize_button_selection = driver.find_element(AppiumBy.XPATH,
                                                     '//android.view.ViewGroup[@content-desc="Authorize"]/android.view.ViewGroup')
    authorize_button_selection.click()
    print("13 : Authorization done")
    time.sleep(5)
    continue_on_payment_screen = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]')
    continue_on_payment_screen.click()
    time.sleep(5)
    print("14 : Payment Done")
    time.sleep(15)

    # charging preview page
    print("15 : On charging page")
    stop_charging_btn = driver.find_element(AppiumBy.XPATH,
                                            '//android.view.ViewGroup[@content-desc="Stop Charging"]/android.view.ViewGroup')
    time.sleep(20)

    stop_charging_btn.click()
    print("16 : charging stopped , wait for receipt")
    time.sleep(12)
    receipt_preview = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Done"]')
    receipt_preview.click()
    time.sleep(2)
    print("17 : Receipt Generated")
    print("18 : Appium service going down")
    print("19 : Peace")