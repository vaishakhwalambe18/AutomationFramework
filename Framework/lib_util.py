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
    def getAPI(self,endpoint, authType,username,password,specificHeaderData,expectedResponseCode):

        if(authType.lower() == 'basic'):
            auth = HTTPBasicAuth('user', 'pass')

        if(specificHeaderData.len > 0):
            print('update_some_thing')

        response = requests.get(endpoint)
        act_response_code = response.status_code()
        act_json_data = response.json()

