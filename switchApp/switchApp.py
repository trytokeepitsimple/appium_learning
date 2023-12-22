import json
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy


# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['deviceName'] = 'Pixel 6a API 30'
# desired_caps['automationName'] = 'UiAutomator2'
# desired_caps['platformVersion']='11.0'
# desired_caps['appPackage'] = 'com.android.chrome'
# desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'

print("1 : Loading Device Info")
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
        'appPackage': 'com.android.chrome',
        'appActivity': 'com.google.android.apps.chrome.Main',
        #'browserName': 'Chrome'
        # Add other desired capabilities as needed
    }

    # Now use desired_caps to initialize your Appium driver
    appium_service = AppiumService()
    appium_service.start()

    print("2 : appium service started succesfully")

    appium_server_url = 'http://localhost:4723'

    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(desired_caps))
    driver.implicitly_wait(10)

    print("3: Chrome apps loaded")

    accept_t_c_button = driver.find_element(AppiumBy.ID ,'com.android.chrome:id/terms_accept')
    accept_t_c_button.click()
    time.sleep(2)

    negative_option_for_sync = driver.find_element(AppiumBy.ID,'com.android.chrome:id/negative_button')
    negative_option_for_sync.click()
    time.sleep(2)

    print("4: Loading Chrome")
    driver.get("https://www.google.com")
    time.sleep(2)

    # contexts = driver.contexts
    #
    # for context in contexts:
    #     print(context)

    webview = driver.contexts[1]
    driver.switch_to.context(webview)
    print("5 : Changed View from app to Browser")
    time.sleep(1)


    search_bar=driver.find_element(AppiumBy.XPATH,'//*[@name="q"]')
    search_bar.send_keys("appium")
    #press enter key
    driver.press_keycode(66)
    time.sleep(10)




    print("Done with browser tasks ,now change view from web to native app")
    driver.switch_to.context(driver.contexts[0])
    print("Context Changed from web to native app")

    #package and activity info of second app
    desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'  # Package name of the second app
    desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'  # Activity name of the second app

    driver.activate_app(desired_caps['appPackage'])  # Switch to the second app

    print("2 : Skill Share App Launched Succesfully")
    time.sleep(5)
    # login screen
    login_btn = (driver.find_element(AppiumBy.ID, 'com.skill2lead.appiumdemo:id/Login').click())
    email_field = (driver.find_element(AppiumBy.ID, 'com.skill2lead.appiumdemo:id/Et4').click())
    value_in_email = driver.find_element(AppiumBy.ID, 'com.skill2lead.appiumdemo:id/Et4').send_keys("admin@gmail.com")
    password_field = (driver.find_element(AppiumBy.ID, 'com.skill2lead.appiumdemo:id/Et5').click())
    password_value = driver.find_element(AppiumBy.ID, 'com.skill2lead.appiumdemo:id/Et5').send_keys('admin123')
    sign_in_btn = (driver.find_element(AppiumBy.ID, 'com.skill2lead.appiumdemo:id/Btn3').click())

    print("3: Logged In Sucessfully")

    # admin name preview panel
    admin_name_input_selection = (driver.find_element(AppiumBy.ID, 'com.skill2lead.appiumdemo:id/Edt_admin').click())
    admin_name_value = (
        driver.find_element(AppiumBy.ID, 'com.skill2lead.appiumdemo:id/Edt_admin').send_keys("Devesh Shukla"))
    submit_btn = (driver.find_element(AppiumBy.ID, 'com.skill2lead.appiumdemo:id/Btn_admin_sub').click())
    print("4 : Name visible on Preview Screen")
    driver.quit()

    appium_service.stop()
else:
    print(f"Device '{device_name}' not found in the configuration file.")

