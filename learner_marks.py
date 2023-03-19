import os
import pandas as pd
import streamlit as st
from openpyxl import load_workbook

# Set the path to the Excel sheet
file_path = os.path.join(os.getcwd(), "data", "student_marks.xlsx")

# Load the Excel sheet using openpyxl engine
book = load_workbook(file_path, read_only=True)
ws = book.active
data = ws.values
columns = next(data)
df = pd.DataFrame(data, columns=columns)

# Convert columns to string type
df["Name"] = df["Name"].astype(str)
df["Password"] = df["Password"].astype(str)

# Convert marks column to numeric type
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce").astype(str)

# Define the Streamlit app
def app():
    # Set the page title
    st.set_page_config(page_title="Student Marks", page_icon=":mortar_board:")

    # Set the app header
    st.header("Technical Sciences Marks: March 2023")

    # Define the input fields
    name = st.text_input("Name")
    password = st.text_input("Password", type="password")

    # Filter the data based on the input fields
    filtered_df = df[(df["Name"].str.strip() == name.strip()) & (df["Password"].str.strip() == password.strip())]

    # Check if there is any data for the input fields
    if filtered_df.empty:
        st.warning("Incorrect name or password. Please try again.")
    else:
        # Get the student's marks
        marks = filtered_df.iloc[0].get("Marks")
        if marks == "nan":
            st.warning("No marks found for this student.")
        else:
            st.success(f"Your marks out of 100 are: {marks}")

# Run the app
if __name__ == "__main__":
    app()
