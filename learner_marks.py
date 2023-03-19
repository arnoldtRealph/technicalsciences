import openpyxl
import streamlit as st

# Load the data
data_folder = "data/"
excel_file = "learner_marks.xlsx"
workbook = openpyxl.load_workbook(data_folder + excel_file)
sheet = workbook.active

# Set up the Streamlit app
st.title("Learner Marks Lookup")

# Add input fields for name and password
name = st.text_input("Name:")
password = st.text_input("Password:", type="password")

# Add a button to submit the inputs
if st.button("Submit"):
    # Loop through each row in the sheet
    for row in sheet.iter_rows(min_row=2, values_only=True):
        # Check if the name and password match the current row
        if name == row[0] and password == row[1]:
            # Display the learner's mark
            st.success(f"Your mark is {row[2]}.")
            break
    else:
        # Display an error message if the name and password don't match any rows
        st.error("Invalid name or password.")
