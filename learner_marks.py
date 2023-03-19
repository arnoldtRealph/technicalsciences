import pandas as pd
import streamlit as st

# Load the data
data_folder = "data/"
excel_file = "student_marks.xlsx"
df = pd.read_excel(data_folder + excel_file)

# Set up the Streamlit app
st.title("Technical Sciences March test Results: March 2023")

# Add input fields for name and password
name = st.text_input("Name:")
password = st.text_input("Password:", type="password")

# Add a button to submit the inputs
if st.button("Submit"):
    # Check if the name and password match a row in the dataframe
    result = df[(df["Name"]==name) & (df["Password"]==password)]
    if len(result) > 0:
        # Display the learner's mark
        st.success(f"Your mark is {result.iloc[0]['Marks']} out of 100.")
    else:
        # Display an error message if the name and password don't match
        st.error("Invalid name or password.")
