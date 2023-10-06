import streamlit as st
import pandas as pd
import multiprocessing
import time


# Function to simulate running a test case
def run_test_case(test_case_name, test_data):
    # Simulate some test execution (replace with your actual test logic)
    time.sleep(2)
    return f"Test case '{test_case_name}' with data '{test_data}' completed."


# Streamlit app
st.title("Test Case Runner")

# File upload widget
uploaded_file = st.file_uploader("Upload an Excel file", type=["xls", "xlsx"])

if uploaded_file:
    # Read the uploaded Excel file into a Pandas DataFrame
    excel_data = pd.read_excel(uploaded_file)

    # Get the list of test cases and test data columns from the Excel file
    test_case_columns = excel_data.columns
    test_data_columns = test_case_columns[1:]  # Assuming the first column is the test case name

    # Multiselect widget for selecting test cases
    selected_test_cases = st.multiselect("Select Test Cases", test_case_columns)

    # Multiselect widget for selecting test data columns
    selected_test_data = st.multiselect("Select Test Data Columns", test_data_columns)

    # Run the selected test cases in parallel
    if st.button("Run Selected Test Cases"):
        results = []
        processes = []

        # Use multiprocessing to run test cases in parallel
        for test_case in selected_test_cases:
            for test_data in selected_test_data:
                process = multiprocessing.Process(target=run_test_case, args=(test_case, test_data))
                processes.append(process)
                process.start()

        # Wait for all processes to complete
        for process in processes:
            process.join()

        # Collect and display the results
        for process in processes:
            results.append(process.exitcode)

        st.write("Test Case Execution Results:")
        for i, result in enumerate(results):
            st.write(f"Process {i + 1}: {test_case} - {test_data} | Exit Code: {result}")

# Sample Excel file structure:
# | Test Case     | Test Data 1  | Test Data 2  |
# |---------------|--------------|--------------|
# | Test Case 1   | Data 1       | Data 2       |
# | Test Case 2   | Data 3       | Data 4       |
