from configparser import ConfigParser
#from generate_logs import log_creation

# config = ConfigParser()
# config.read("/home/devesh-ssd/PycharmProjects/appium_testing/utilities/config.ini")
# print(config.get("locator","username"))
# print(config.get("basicInfo",'localhost'))


def configReader(section, key):
    config = ConfigParser()
    config.read("/home/devesh-ssd/PycharmProjects/appium_testing/utilities/config.ini")
    return config.get(section,key)

# conf = configReader("locator","username")
# print(conf)

# logger = log_creation()
# logger.info("BBBBB")

