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

sidebar_response = st.sidebar.selectbox('Pick your tool', ('Web Page Scrapper', 'Execute Test Cases'))

if sidebar_response == 'Execute Test Cases':
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
            current_module_df = read_excel('C:\AutomationFramework\Controller\Controller_' + item + '.xlsx')
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

            script_path = create_duplicate(original_script_path)

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

elif sidebar_response == 'Web Page Scrapper':
    st.write(sidebar_response)
