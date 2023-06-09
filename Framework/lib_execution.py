import openpyxl as xl
from Framework.lib_util import *

def execution_driver():
    moduleControllerPath = ReadConfig.getValue('common path', 'module_controller')
    print(moduleControllerPath)
    wb_obj = xl.load_workbook(moduleControllerPath,data_only=True)
    sh = wb_obj["tbl_modules"]
    moduleTable = []
    for col in sh:
        moduleName = col[0].value
        activeState = col[1].value
        if activeState.lower() == "yes":
            print("--------------Module being executed : " + moduleName + "---------------")
            executionController = col[2].value
            dataSheet = col[3].value
            description = col[4].value
            print("Controller File Name : " + executionController)
            print("Datasheet Name : "+ dataSheet)
            print("Description : " + description)
            # Running of current module
            current_module_Controller_path = ReadConfig.getValue('common path', 'module_path')
            current_module_TestData_path = ReadConfig.getValue('common path', 'testdata_path')

            current_module_TestData_path = current_module_TestData_path + moduleName + ".xlsx"
            current_module_Controller_path = current_module_Controller_path + moduleName + ".xlsx"
            current_module_Controller_wb = xl.load_workbook(current_module_Controller_path, data_only=True)
            current_module_sheet = current_module_Controller_wb["tbl_testcases"]
            for row in current_module_sheet:
                curr_testcaseName = row[0].value
                curr_TcFileName = row[1].value
                curr_description = row[3].value
                curr_Active = row[4].value
                curr_testDataSet = row[5].value
                ls_testData = []
                if curr_Active.lower() == 'yes':
                    dict_testcasedata = {}
                    print("Current Test Cases being executed : " + curr_testcaseName)
                    print("Total Test Data set selected : " + curr_testDataSet)
                    if "," in curr_testDataSet:
                        ls_testData = curr_testDataSet.split(",")
                        print("Current Test Data being executed: " + ls_testData)
                    else:
                        ls_testData = curr_testDataSet
                        print("Current Test Data being executed: " + ls_testData)
                        dict_testcasedata = loadDatafromExcel(current_module_TestData_path,curr_TcFileName,ls_testData)



            print("--------------End of execution for Module : " + moduleName + "---------------")

def selectTestCases():
    print("Starting selection")