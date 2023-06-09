import configparser

config = configparser.RawConfigParser()
configFilePath = "C:\\AutomationFramework\\Config\\lib_constants.ini"
config.read(configFilePath)


class ReadConfig:
    @staticmethod
    def getValue(constType, valueToGet):
        value_config = config.get(constType, valueToGet)
        return value_config
