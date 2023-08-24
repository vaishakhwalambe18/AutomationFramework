##########################################################################################################################################
# import openpyxl as xl
# from Framework.lib_util import *
#
# global dict_testcasedata , moduleTable, ls_testData
# dict_testcasedata= {}
# moduleTable = []
# ls_testData= []
# def execution_driver():
#     # Module Controller Path fron config
#     moduleControllerPath = ReadConfig.getValue('common path', 'module_controller')
#
#     # read module controller path to check which module to run
#     wb_obj = xl.load_workbook(moduleControllerPath,data_only=True)
#     sh = wb_obj["tbl_modules"]
#     for col in sh:
#         # Only run Modules which are set to "Yes"
#         moduleName = col[0].value
#         activeState = col[1].value
#         if activeState.lower() == "yes":
#             print("--------------Module being executed : " + moduleName + "---------------")
#             executionController = col[2].value
#             dataSheet = col[3].value
#             description = col[4].value
#             print("Controller File Name : " + executionController)
#             print("Datasheet Name : "+ dataSheet)
#             print("Description : " + description)
#
#             # Running of current module
#             current_module_Controller_path = ReadConfig.getValue('common path', 'module_path')
#             current_module_TestData_path = ReadConfig.getValue('common path', 'testdata_path')
#
#             current_module_TestData_path = current_module_TestData_path + moduleName + ".xlsx"
#             current_module_Controller_path = current_module_Controller_path + moduleName + ".xlsx"
#
#             # Read Test Cases which is set to yes for execution
#             current_module_Controller_wb = xl.load_workbook(current_module_Controller_path, data_only=True)
#             current_module_sheet = current_module_Controller_wb["tbl_testcases"]
#             for row in current_module_sheet:
#                 curr_testcaseName = row[0].value
#                 curr_TcFileName = row[1].value
#                 curr_description = row[3].value
#                 curr_Active = row[4].value
#                 curr_testDataSet = row[5].value
#
#                 if curr_Active.lower() == 'yes':
#
#                     print("Current Test Cases being executed : " + curr_testcaseName)
#                     print("Total Test Data set selected : " + curr_testDataSet)
#                     if "," in curr_testDataSet:
#                         ls_testData = curr_testDataSet.split(",")
#                         print("Current Test Data being executed: " + ls_testData)
#                     else:
#                         ls_testData = curr_testDataSet
#                         print("Current Test Data being executed: " + ls_testData)
#                         dict_testcasedata = loadDatafromExcel(current_module_TestData_path,curr_TcFileName,ls_testData)
#                         print("Browser : " + dict_testcasedata['Browser'])
#
#
#             print("--------------End of execution for Module : " + moduleName + "---------------")
#
# def selectTestCases():
#     print("Starting selection")