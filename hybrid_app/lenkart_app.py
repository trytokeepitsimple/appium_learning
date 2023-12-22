import time
#from pathlib import Path
import json
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy


#getting device info
conf_file = 'C:\\Users\\Devesh_SSD\\PycharmProjects\\appium_testing\\device_conf\\config.json'
def get_device_config(device_name):
    with open(conf_file, 'r') as config_file:
        config = json.load(config_file)
        for device in config['devices']:
            if device['deviceName'] == device_name:
                print(device)
                return device
        return None

device_name = 'Pixel 6a API 30'  # Set your device name dynamically based on your needs
device_config = get_device_config(device_name)

if device_config:
    desired_caps = {
        'platformName': device_config['platformName'],
        'deviceName': device_config['deviceName'],
        'platformVersion': device_config['platformVersion'],
        'automationName':device_config['automationName'],
        #'app': 'C:\\Users\\Devesh_SSD\\PycharmProjects\\appium_testing\\app\\lenskart-4-0-7.apk',
        'appPackage': 'com.lenskart.app',
        'appActivity': '.home.ui.HomeBottomNavActivity',
        'noReset': True
        # Add other desired capabilities as needed
    }

    # Now use desired_caps to initialize your Appium driver
    # appium_service
    appium_service = AppiumService()
    appium_service.start()
    print("1 : Appium Service Going UP")
    appium_server_url = 'http://localhost:4723'

    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(desired_caps))
    driver.implicitly_wait(10)
    print(desired_caps['noReset'])
    print("App Loaded")
    time.sleep(10)
    driver.quit()
    appium_service.stop()