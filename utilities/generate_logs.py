import logging

#from utilities.reading_from_config_ini import configReader


#from reading_from_config_ini import configReader
def log_creation():
    log_format = "%(asctime)s [%(levelname)s] - %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"
    logging.basicConfig(filename="/home/devesh-ssd/PycharmProjects/appium_testing/logs/logfile.log",
                        format=log_format, datefmt=date_format,level=logging.INFO)
    logger = logging.getLogger()
    return logger


log_create = log_creation()
print(log_create.error("nidhi"))
# # log_create.info("WWW")
# print(log_create.info("AAAAA"))

# aaa = configReader("basicInfo",'localhost')
# print(aaa)