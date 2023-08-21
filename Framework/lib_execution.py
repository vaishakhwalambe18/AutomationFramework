import shutil
import subprocess
import os
import streamlit as st
import pandas as pd
# from Framework.lib_util import ReadConfig as rc

# Read data from Excel file using pandas
def read_excel(file_path):
    data = pd.read_excel(file_path)
    return data


def create_duplicate(original_file_path):
    # Get the directory and filename of the original file
    directory, filename = os.path.split(original_file_path)

    # Create a path for the duplicate file
    duplicate_file_path = os.path.join(directory, "duplicate_" + filename)

    try:
        # Copy the original file to the duplicate file path
        shutil.copy(original_file_path, duplicate_file_path)
        print(f"Duplicate file created: {duplicate_file_path}")
        return duplicate_file_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def delete_file(file_path):
    try:
        # Delete the file
        os.remove(file_path)
        print(f"File deleted: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

################################################################# RUNNER STARTS HERE ##########################################################################################################

st.title("Test Automation Framework")

# module_path = rc.getValue('common path', 'module_controller')
module_path = 'C:\AutomationFramework\Controller\ModuleController.xlsx'
df = read_excel(module_path)

st.write("Select Modules to execute:")

module_selected = []
for index, row in df.iterrows():
    if st.sidebar.checkbox(row['ModuleName']):
        module_selected.append(row['ModuleName'])

left_column, right_column = st.columns(2)

with left_column:
    current_test_case_selected = []
    for item in module_selected:
        current_module_df = read_excel('C:\AutomationFramework\Controller\Controller_'+item+'.xlsx')
        for curr_index, curr_row in current_module_df.iterrows():
            if st.checkbox(curr_row['TCID']):
                current_test_case_selected.append(curr_row['TCID'])

with right_column:
    # Button to trigger the pytest test
        if st.button("Run Test"):
            st.write("Running the pytest test...")
            st.write(current_test_case_selected)

            # Replace "python_script.py" with the actual name of your Python script
            original_script_path = "C://AutomationFramework//Framework//test_runner.bat"


            script_path = create_duplicate (original_script_path)

            for item in current_test_case_selected:

                # Update bat file
                with open(script_path, "rt") as bat_file:
                    text = bat_file.readlines()

                new_text = []
                for line in text:
                    if "[testcaseid]" in line:
                        new_text.append(line.replace("[testcaseid]", item))
                    else:
                        new_text.append(line)

                with open(script_path, "wt") as bat_file:
                    for line in new_text:
                        bat_file.write(line)

                # Run the batch file using subprocess
                try:
                    subprocess.run(script_path, shell=True, capture_output=True, text=True, check=True)
                    st.write("Tests executed successfully.")

                    # Read and display the test output from the file
                    with open("test_output.txt", "r") as file:
                        test_output = file.read()
                        st.write("Test output:")
                        st.code(test_output)
                except subprocess.CalledProcessError as e:
                    st.error(f"Error running tests: {e.stderr}")

                delete_file(script_path)




























































































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
