from appium.webdriver.common.appiumby import AppiumBy


class ScrollUtil:

    @staticmethod
    def scrollToTextByAndroidUIAutomator(text, driver):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
        "new UiScrollable(new UiSelector().scrollable(true).instance("
                                                   "0)).scrollIntoView(new UiSelector().textContains(\""+text+"\").instance(0))").click()

    @staticmethod
    def swipeUp(howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(272,1000,272,545,1000)


    @staticmethod
    def swipeDown(howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(272,545,272,1000,1000)

    @staticmethod
    def swipeLeft(howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(1054,912,26,912,1000)


    @staticmethod
    def swipeRight(howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(26,912,1054,912,1000)
