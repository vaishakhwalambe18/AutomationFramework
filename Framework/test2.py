import streamlit as st
import pandas as pd
import subprocess


# Function to run pytest in parallel
def run_pytest(test_cases, browser):
    selected_test_cases = " ".join(test_cases)
    pytest_cmd = f"pytest -k {selected_test_cases} -n auto --driver {browser}"  # -n auto for parallel execution
    st.write(pytest_cmd)
    # subprocess.run(pytest_cmd, shell=True)


# Streamlit UI
st.title("Testcase Runner")

# Upload Excel file
excel_file = st.file_uploader("Upload Excel File", type=["xls", "xlsx"])

# Select test cases and browser
if excel_file:
    st.write("### Select Test Cases to Run")
    df = pd.read_excel(excel_file)
    test_cases = st.multiselect("Select Test Cases", df["TCID"].tolist())

    st.write("### Select Browser")
    browser = st.selectbox("Select Browser", ["chrome", "firefox", "edge"])

    if st.button("Run Selected Test Cases"):
        if not test_cases:
            st.warning("Please select at least one test case.")
        else:
            run_pytest(test_cases, browser)
            st.success("Test cases are running in parallel. Check the test reports for results.")
