import configparser
import openpyxl as xl
import requests

from requests.auth import HTTPBasicAuth

config = configparser.RawConfigParser()
configFilePath = ".\\Config\\lib_constants.ini"
config.read(configFilePath)


class ReadConfig:
    @staticmethod
    def getValue(constType, valueToGet):
        value_config = config.get(constType, valueToGet)
        return value_config


class ReadExcel:
    def loadDatafromExcel(filepath, tcName, dataset):
        workbook = xl.load_workbook(filepath)
        worksheet = workbook[tcName]

        dictionary = {}

        for row in range(1, worksheet.max_row + 1):
            key = worksheet.cell(row, 1).value
            value = worksheet.cell(row, 2).value
            dictionary[key] = value
        # print(dictionary)
        return dictionary


class kyAPI:
    # >> > import requests
    # >> > r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
    # >> > r.status_code
    # 200
    # >> > r.headers['content-type']
    # 'application/json; charset=utf8'
    # >> > r.encoding
    # 'utf-8'
    # >> > r.text
    # '{"authenticated": true, ...'
    # >> > r.json()
    # {'authenticated': True, ...}
    @staticmethod
    def get_API(endpoint, authType, username, password, specificHeaderData, expectedResponseCode):
        if (authType.lower() == 'basic'):
            auth = HTTPBasicAuth(username, password)

        # if (specificHeaderData.len > 0):
        #     print('update_some_thing')

        response = requests.get(endpoint)
        print(response)
        act_response_code = response.status_code
        assert int(act_response_code) == int(expectedResponseCode)
        pass

        return response
